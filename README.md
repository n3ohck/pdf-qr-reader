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
