# PDF to QR Scanner API

Este proyecto es una API desarrollada en Python que convierte archivos PDF en imágenes, detecta códigos QR en cada imagen y consulta la URL obtenida a través de scraping web para extraer la información del sitio. El resultado se devuelve en formato JSON. Próximamente, se incluirá vectorización para mejorar el procesamiento.

## Características

- Convierte archivos PDF en imágenes.
- Detecta y decodifica códigos QR en las imágenes generadas.
- Realiza consultas HTTP a las URLs de los códigos QR.
- Extrae información de las páginas web consultadas mediante scraping.
- Retorna la información extraída en formato JSON.

## Requisitos

Para utilizar esta API, necesitas instalar las siguientes dependencias:

```plaintext
PyPDF2
pdf2image
opencv-python
pyzbar
numpy
flask
python-dotenv
selenium

## Instalación
pip install -r requirements.txt

## Uso
python app.py

## Response
## Response del API

El response de la API es un objeto JSON que contiene la información extraída del sitio web asociado a cada código QR detectado en el PDF. Un ejemplo de response es:

```json
{
  "text": "texto del sitio web",
  "urls": [{url del sitio}]
}

## Contribuciones
Las contribuciones son bienvenidas. Para contribuir:

Haz un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva_funcionalidad).
Realiza los cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
Sube tus cambios (git push origin feature/nueva_funcionalidad).
Abre un pull request.

## Futuro desarrollo
Se pretende agregar vectorizacion
