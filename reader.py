import os
from dotenv import load_dotenv
from pdf2image import convert_from_path
import uuid
from qrreader import QrReader
import getpass

class ReaderClass:
    load_dotenv()
    output_folder = os.getenv('IMAGE_PATH')
    poppler_path = os.getenv('PLOOPER_PATH')
    pdf_path = os.getenv('PDF_PATH')
    usuario_actual = getpass.getuser()
    def __init__(self, file):
        if not self.output_folder:
            raise ValueError("La variable de entorno IMAGE_PATH no está configurada")
        
        if not self.poppler_path:
            raise ValueError("La variable de entorno PLOOPER_PATH no está configurada")
        
        if not self.pdf_path:
            raise ValueError("La variable de entorno PDF_PATH no está configurada")
        
        self.file = file
        self.unique_id = uuid.uuid4()
        
    def isPdf(self):
        return (
            self.file.filename.split('.')[-1].lower() == 'pdf' and
            self.file.content_type == 'application/pdf'
        )
        
    def proccess(self):
        qrs_uris = set()
        
        if not os.path.exists(self.output_folder):
            raise ValueError("La ruta establecida en la variable de entorno IMAGE PATH no existe")
        
        if not os.path.exists(self.pdf_path):
            raise ValueError("La ruta establecida en la variable de entorno PDF PATH no existe")
        
                
        temp_pdf_path = os.path.join(self.pdf_path, f'{self.unique_id}.pdf')
        self.file.save(temp_pdf_path)
        
        try:
            pages = convert_from_path(temp_pdf_path, 300, poppler_path=r'C:\poppler-24.08.0\Library\bin')
        except Exception as e:
            raise ValueError(f"Error al convertir el PDF: {str(e)}. Asegúrese de que Poppler esté instalado y que la ruta en PLOOPER_PATH sea correcta.")        
       
        os.remove(temp_pdf_path)
        for i, page in enumerate(pages):
            output_path = os.path.join(self.output_folder, f'{self.unique_id}_pagina_{i + 1}.jpg')
            page.save(output_path, 'JPEG')
            qr_reader = QrReader(output_path)
            qr_data = qr_reader.get_data()
            if qr_data:
                qrs_uris.add(qr_data)
                os.remove(output_path)
            
        return list(qrs_uris)
            

