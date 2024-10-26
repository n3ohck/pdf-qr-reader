from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class AnonymousScraper:
    def __init__(self):
        # Configurar opciones para navegador anónimo
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--headless")  # Ejecuta el navegador sin abrir ventana
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Inicializar el controlador de Chrome con opciones
        self.driver = webdriver.Chrome(options=options)

    def get_text(self, url):
        # Acceder a la URL y obtener el texto
        self.driver.get(url)
        time.sleep(3)  # Espera a que se cargue la página (ajusta según sea necesario)
        
        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        return page_text

    def close(self):
        # Cerrar el navegador
        self.driver.quit()