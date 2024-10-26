# API de Escáner de PDF a QR

Este proyecto es una API desarrollada en Python que convierte archivos PDF en imágenes, detecta códigos QR en cada imagen y consulta la URL obtenida a través de web scraping para extraer la información del sitio. El resultado se devuelve en formato JSON. Próximamente, se incluirá vectorización para mejorar el procesamiento.

## Características

- Convierte archivos PDF en imágenes.
- Detecta y decodifica códigos QR en las imágenes generadas.
- Realiza consultas HTTP a las URLs de los códigos QR.
- Extrae información de las páginas web consultadas mediante web scraping.
- Retorna la información extraída en formato JSON.

## Requisitos

Para utilizar esta API, necesitas instalar las siguientes dependencias:

- Python 3.x
- Flask
- PyPDF2
- pdf2image
- opencv-python
- pyzbar
- numpy
- python-dotenv
- selenium

Puedes instalar todas las dependencias utilizando el archivo `requirements.txt` incluido en el proyecto:
```console
pip install -r requirements.txt
```

## Response del API

El response de la API es un objeto JSON que contiene la información extraída del sitio web asociado a cada código QR detectado en el PDF. Un ejemplo de response es:

```json
{
  "text": "texto del sitio web",
  "urls": [url]
}
```


