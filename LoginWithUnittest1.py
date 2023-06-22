#TESTING BASE CODE FOR SELENIUM , UNITTEST LOGINS 1
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
from selenium.webdriver.common.keys import Keys #USO DE ENVIO DE TECLAS
from selenium.webdriver.support.ui import WebDriverWait #EXPLICIT WAITS
from selenium.webdriver.support import expected_conditions as EC #EXPLICIT WAITS
from selenium.common.exceptions import TimeoutException #USO DE TRY EXCEPT
from selenium import webdriver #IMPORTAR EL DRIVER DEL NAVEGADOR
from tkinter import simpledialog #DIALOGOS EN VENTANA EMERGENTE
#FIN DE IMPORTS
#DECLARACION DE VARIABLES
PAUSA = (1000)
TIME = (2)
RETARD = (3)
URL = []
#ABRIR TXT CON LA IP EN LA UBICACION ACTUAL
dir_actual = os.path.dirname(os.path.abspath(__file__)) #OBTENER RUTA ACTUAL
ruta_archivo = os.path.join(dir_actual, "IPREAL.txt") #INDICAR NOMBRE DEL TXT CON LA IP
archivo = open(ruta_archivo, "r") #ABRIR TXT
contenido = archivo.readlines() #LEER TXT
ip = " ".join(contenido) #PASAR DE ARREGLO A CADENA LA IP
archivo.close() #CERRAR EL ARCHIVO
#CLASS BASE_TEST PARA USAR UNITTEST
class PruebaLogin(unittest.TestCase):

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
            elementCorreo.send_keys("marco.delgadosafi.unam.mx")
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
        error=driver.find_element("xpath", "//*[@id='ContentPlaceHolder1_ctmMensaje_lblMensaje']")
        time.sleep(TIME)
        error=error.text
        time.sleep(TIME)
        #print(error)
        if(error=="Dirección de Correo Inválida."):
            print("""            
█▀▀ █░░   █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀█   █▀▀ █▀   █ █▄░█ █░█ ▄▀█ █░░ █ █▀▄ █▀█
██▄ █▄▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄█   ██▄ ▄█   █ █░▀█ ▀▄▀ █▀█ █▄▄ █ █▄▀ █▄█

█▀█ █▀█ █░█ █▀▀ █▄▄ ▄▀█   ▄█   █▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▄ ▄▀█
█▀▀ █▀▄ █▄█ ██▄ █▄█ █▀█   ░█   █▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █▄▀ █▀█
            """)
        time.sleep(TIME)
#TEST LOGIN CAMPO CORREO VACIO, CONTRASENA CORRECTA     
    def test_login2(self):
        driver = self.driver
        driver.get(ip)
        frame = driver.find_element("xpath","/html/frameset/frame")
        driver.switch_to.frame(frame)
        # BUSQUEDA DE ELEMENTOS USANDO EXPLICIT WAIT Y TRY CATCH
        # EL TRY VEAMOSLO COMO UN IF
        try:
            elementCorreo = WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath", "//*[@id='ContentPlaceHolder1_txtCorreoElectronico']")))
            elementCorreo.send_keys("")
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
        error=driver.find_element("xpath", "//*[@id='ContentPlaceHolder1_ctmMensaje_lblMensaje']")
        time.sleep(TIME)
        error=error.text
        time.sleep(TIME)
        #print(error)
        if(error=="No ha indicado su Correo Electrónico"):
            print("""           
█▀▀ █░░   █▀▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █▀▄ █▀▀   █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀█   █▀▀ █▀ ▀█▀ ▄▀█   █░█ ▄▀█ █▀▀ █ █▀█
██▄ █▄▄   █▄▄ █▀█ █░▀░█ █▀▀ █▄█ █▄▀ ██▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄█   ██▄ ▄█ ░█░ █▀█   ▀▄▀ █▀█ █▄▄ █ █▄█

█▀█ █▀█ █░█ █▀▀ █▄▄ ▄▀█   ▀█   █▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▄ ▄▀█
█▀▀ █▀▄ █▄█ ██▄ █▄█ █▀█   █▄   █▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █▄▀ █▀█
            """)
        time.sleep(TIME)
#TEST LOGIN CAMPO SIN CONTRASENA, CORREO CORRECTO     
    def test_login3(self):
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
            elementContra.send_keys("")
        except TimeoutException as  ex2:
            print(ex2.msg)
            print("El elemento CONTRASENA no esta disponible")
        elementContra.send_keys(Keys.ENTER)
        time.sleep(TIME)
        error=driver.find_element("xpath", "//*[@id='ContentPlaceHolder1_ctmMensaje_lblMensaje']")
        time.sleep(TIME)
        error=error.text
        time.sleep(TIME)
        #print(error)
        if(error=="No ha indicado su Contraseña"):
            print("""           
█▀▀ ▄▀█ █▀▄▀█ █▀█ █▀█   █▀ █ █▄░█   █▀▀ █▀█ █▄░█ ▀█▀ █▀█ ▄▀█ █▀ █▀▀ █▄░█ ▄▀█
█▄▄ █▀█ █░▀░█ █▀▀ █▄█   ▄█ █ █░▀█   █▄▄ █▄█ █░▀█ ░█░ █▀▄ █▀█ ▄█ ██▄ █░▀█ █▀█

                          ▀█
█▀█ █▀█ █░█ █▀▀ █▄▄ ▄▀█   ▀█  █▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▄ ▄▀█
█▀▀ █▀▄ █▄█ ██▄ █▄█ █▀█   ▄█  █▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █▄▀ █▀█
            """)
        time.sleep(TIME)
#TEST LOGIN CONTRASENA INCORRECTA,CORREO CORRECTO      
    def test_login4(self):
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
            elementContra.send_keys("85204520")
        except TimeoutException as  ex2:
            print(ex2.msg)
            print("El elemento CONTRASENA no esta disponible")
        elementContra.send_keys(Keys.ENTER)
        time.sleep(TIME)
        error=driver.find_element("xpath", "//*[@id='ContentPlaceHolder1_ctmMensaje_lblMensaje']")
        time.sleep(TIME)
        error=error.text
        time.sleep(TIME)
        #print(error)
        if(error=="Contraseña incorrecta.\nEste campo es sensible a mayúsculas."):
            print("""           

█▀▀ █░░ ▄▀█ █░█ █▀▀   █ █▄░█ █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀▀ ▀█▀ ▄▀█
█▄▄ █▄▄ █▀█ ▀▄▀ ██▄   █ █░▀█ █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▄ ░█░ █▀█

█▀█ █▀█ █░█ █▀▀ █▄▄ ▄▀█   █░█   █▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▄ ▄▀█
█▀▀ █▀▄ █▄█ ██▄ █▄█ █▀█   ▀▀█   █▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █▄▀ █▀█
            """)
        time.sleep(TIME)
#TEST LOGIN CORRECTO       
    def test_login5(self):
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
        try:
            welcometxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//*[@id='lblFooter']")))
        except TimeoutException as  ex2:
            print(ex2.msg)
            print("El elemento no esta disponible")
        time.sleep(3)
        welcometxt=driver.find_element("xpath", "//*[@id='lblFooter']")
        welcometxt=welcometxt.text
        time.sleep(TIME)
        #print(error)
        if(welcometxt=="©2011 - Departamento de Sistemas - Secretaría Administrativa - F. I. - UNAM"):
            print("""           

█░░ █▀█ █▀▀ █ █▄░█   █▀▀ ▀▄▀ █ ▀█▀ █▀█ █▀ █▀█
█▄▄ █▄█ █▄█ █ █░▀█   ██▄ █░█ █ ░█░ █▄█ ▄█ █▄█

█▀█ █▀█ █░█ █▀▀ █▄▄ ▄▀█   █▀   █▀▀ █ █▄░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▄ ▄▀█
█▀▀ █▀▄ █▄█ ██▄ █▄█ █▀█   ▄█   █▀░ █ █░▀█ █▀█ █▄▄ █ █▄ █▀█ █▄▀ █▀█
            """)
        time.sleep(TIME)        
    def tearDowm(self):
        driver = self.driver
        driver.close()
    
if __name__ == "__main__":
    unittest.main()

time.sleep(PAUSA)
driver.close