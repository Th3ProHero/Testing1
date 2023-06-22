#TESTING GENERAR VALE MENU ALL FULL CHARGE ELEMENTS
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
from selenium.common.exceptions import NoSuchElementException #EXCEPTION para falla de encontrar elementos
from selenium.webdriver.support.ui import WebDriverWait #EXPLICIT WAITS
from selenium.common.exceptions import TimeoutException #USO DE TRY EXCEPT
from selenium.webdriver.chrome.options import Options #OPCIONES EXPERIMENTALES Y DE DESARROLLADOR
from selenium.webdriver.common.keys import Keys #USO DE ENVIO DE TECLAS
from selenium.webdriver.common.by import By #FUNCION BY PARA BUSQUEDA
from tkinter import simpledialog #DIALOGOS EN VENTANA EMERGENTE
from selenium import webdriver #IMPORTAR EL DRIVER DEL NAVEGADOR
#FIN DE IMPORTS
#DECLARACION DE VARIABLES
PAUSA = (10)
TIME = (1)
RETARD = (3)
URL = []
#ABRIR TXT CON LA IP EN LA UBICACION ACTUAL
dir_actual = os.path.dirname(os.path.abspath(__file__)) #OBTENER RUTA ACTUAL
ruta_archivo = os.path.join(dir_actual, "IPSIVALE2.txt") #INDICAR NOMBRE DEL TXT CON LA IP
archivo = open(ruta_archivo, "r") #ABRIR TXT
contenido = archivo.readlines() #LEER TXT
ip = " ".join(contenido) #PASAR DE ARREGLO A CADENA LA IP
archivo.close() #CERRAR EL ARCHIVO

# ARREGLO PARA FUNCION DE COMPROBACION DE ELEMENTOS EN XPATH DEL MENU DE GENERAR VALE
elementos = {
    "Barra de  búsqueda": "/html/body/form/div[3]/center/div[1]/table/tbody/tr/td[1]/input",
    "Busqueda Click": "/html/body/form/div[3]/center/div[1]/table/tbody/tr/td[3]/a",
    "Texto Generar Vale": "/html/body/form/div[3]/center/div[1]/table/tbody/tr/td[3]/a",
    "Añadir articulos": "/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr/td/input",
    "Columna de Cantidad": "/html/body/form/div[3]/center/div[2]/div/table/tbody/tr[1]/th[1]",
    "Columna de Unidad": "/html/body/form/div[3]/center/div[2]/div/table/tbody/tr[1]/th[2]",
    "Columna de Articulo": "/html/body/form/div[3]/center/div[2]/div/table/tbody/tr[1]/th[3]",
    "Columna de Precio Unitario": "/html/body/form/div[3]/center/div[2]/div/table/tbody/tr[1]/th[4]"
}
###############
#CLASS EMERGENT_WINDOW PARA USAR UNITTEST
class menu1(unittest.TestCase):

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
            elementCorreo.send_keys("marco.delgado@safi.unam.mx")
        except TimeoutException as  ex:
            print(ex.msg)
            print("El elemento CAMPO CORREO no esta disponible")
        #CONTINUA LA EJECUCION
        try:
            elementContra = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "//*[@id='ContentPlaceHolder1_txtContrasena']")))
            elementContra.send_keys("897047")
        except TimeoutException as  ex2:
            print(ex2.msg)
            print("El elemento CONTRASENA no esta disponible")
        elementContra.send_keys(Keys.ENTER)
        time.sleep(TIME)
        try:
            elementGenerarVale = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "//*[@id='ContentPlaceHolder1_trvMenut2']")))
            elementGenerarVale.click()
        except TimeoutException as  ex3:
            print(ex3.msg)
            print("El elemento MENU GENERAR VALE no esta disponible")
        time.sleep(TIME)
        ############CONFIRMACION DE GENERAR VALE entrar en el frame 1
        try:
            elementTextGenerarVale = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "//*[@id='ContentPlaceHolder1_trvMenut2']")))
            elementTextGenerarVale.click()
        except TimeoutException as  ex4:
            print(ex4.msg)
            print("ERROR AL INGRESAR A LA PESTAÑA DE GENERAR VALE")
        time.sleep(TIME)    
#####################################        
        try:
            elementTextGenerarVale = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "/html/body/div[1]/div[2]/div/div/form/div[5]/iframe")))
            frame2 = driver.find_element("xpath","/html/body/div[1]/div[2]/div/div/form/div[5]/iframe")
            driver.switch_to.frame(frame2)
            print("Acceso a iFrame Correcto")
        except TimeoutException as  ex5:
            print(ex5.msg)
            print("ERROR AL INGRESAR AL FRAME")
        time.sleep(TIME)       
#CARGA DE ELEMENTOS CORRECTA
        for nombre, xpath in elementos.items():
            try:
                elemento = driver.find_element("xpath",xpath)
                print(f"Elemento cargado correctamente: {nombre}")
            except NoSuchElementException:
                print(f"Elemento no encontrado: {nombre}")

    def tearDowm(self):
        driver = self.driver
        driver.close()
    
if __name__ == "__main__":
    unittest.main()

######################
time.sleep(50)
self.driver.close