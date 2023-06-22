#TESTING EMERGENT WINDOW CREDITS
#PYTHON VERSION : 3.11.2
#SELENIUM VERSION : 4.8.3
#NAVEGADOR : CHROME V 111.0.5563.65 (Build oficial) (64 bits)
#SCRIPT BY DARK MAU
#IMPORTAR LIBRERIAS
import concurrent.futures #CONCURRENCIA Y PARALELISMO
import tkinter as tk #VENTANAS EMERGENTES
import keyboard #MANDAR ACCION DE TECLAS
import time #RETARDOS, FUNCION DE TIME
import os #INTERACCION DE SISTEMAIMP
import unittest #TEST DE PRUEBAS UNITARIAS
#FROMS PARA USAR FUNCIONES
from selenium.webdriver.support import expected_conditions as EC #EXPLICIT WAITS
from selenium.webdriver.support.ui import WebDriverWait #EXPLICIT WAITS
from selenium.common.exceptions import TimeoutException #USO DE TRY EXCEPT
from selenium.webdriver.chrome.options import Options #OPCIONES EXPERIMENTALES Y DE DESARROLLADOR
from selenium.webdriver.common.keys import Keys #USO DE ENVIO DE TECLAS
from selenium.webdriver.common.by import By #FUNCION BY PARA BUSQUEDA
from tkinter import simpledialog #DIALOGOS EN VENTANA EMERGENTE
from selenium import webdriver #IMPORTAR EL DRIVER DEL NAVEGADOR
#FIN DE IMPORTS
#DECLARACION DE VARIABLES
PAUSA = (1)
TIME = (2)
RETARD = (3)
URL = []
#ABRIR TXT CON LA IP EN LA UBICACION ACTUAL
dir_actual = os.path.dirname(os.path.abspath(__file__)) #OBTENER RUTA ACTUAL
ruta_archivo = os.path.join(dir_actual, "IPSIVALE2.txt") #INDICAR NOMBRE DEL TXT CON LA IP
archivo = open(ruta_archivo, "r") #ABRIR TXT
contenido = archivo.readlines() #LEER TXT
ip = " ".join(contenido) #PASAR DE ARREGLO A CADENA LA IP
archivo.close() #CERRAR EL ARCHIVO

###############
#CLASS EMERGENT_WINDOW PARA USAR UNITTEST
class EMERGENT_WINDOW(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
#TEST 1 CORREO ERRONEO        
    def test_login1(self):
        driver = self.driver
        driver.get(ip)
        frame = driver.find_element("xpath","/html/frameset/frame")
        driver.switch_to.frame(frame)
        # BUSQUEDA DE ELEMENTOS USANDO EXPLICIT WAIT Y TRY CATCH
        # EL TRY VEAMOSLO COMO UN IF
        try:
            elementCorreo = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "//*[@id='ContentPlaceHolder1_txtCorreoElectronico']")))
            elementCorreo.send_keys("valadez_consultores@hotmail.com")
        except TimeoutException as  ex:
            print(ex.msg)
            print("El elemento CAMPO CORREO no esta disponible")
        #CONTINUA LA EJECUCION
        try:
            elementContra = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "//*[@id='ContentPlaceHolder1_txtContrasena']")))
            elementContra.send_keys("1")
        except TimeoutException as  ex2:
            print(ex2.msg)
            print("El elemento CONTRASENA no esta disponible")
        elementContra.send_keys(Keys.ENTER)
        time.sleep(TIME)
        try:
            EscorpionLink = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='Image1']")))
            #CorreoLink.send_keys(Keys.ENTER)                                                    
            EscorpionLink.click()
            print("EL BOTON DE CREDITOS CARGÓ EXITOSAMENTE")
            ventana_emergente = WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            ventanas_abiertas = driver.window_handles
            for ventana in ventanas_abiertas:
                if ventana != driver.current_window_handle:
                    driver.switch_to.window(ventana)
                    break
            # Comprueba la URL de la ventana emergente
            url_esperada = "http://www.administracion.ingenieria.unam.mx/"
            if driver.current_url == url_esperada:
                print("La ventana emergente abrió la URL esperada.")
            else:
                print("La ventana emergente no abrió la URL esperada.")

            # Cierra la ventana emergente y vuelve a la ventana principal
            time.sleep(20)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except TimeoutException as  ex3:
            print(ex3.msg)
            print("ERROR AL ENCONTRAR EL LOGO DE ESCORPION")
        
        time.sleep(50)
    def tearDowm(self):
        driver = self.driver
        driver.close()
    
if __name__ == "__main__":
    unittest.main()

######################
time.sleep(PAUSA)
self.driver.close