#TESTING SIVALE MULTIPLE WINDOWS CHROME LOGIN STRESS TEST 
#PYTHON VERSION : 3.11.2
#SELENIUM VERSION : 4.8.3
#NAVEGADOR : CHROME V 111.0.5563.65 (Build oficial) (64 bits)
#SCRIPT BY DARK MAU
from selenium import webdriver
from tkinter import simpledialog
from selenium.webdriver.common.keys import Keys
import concurrent.futures
#USO DE VENTANAS EMERGENTES
import tkinter as tk
#Eventos de teclado
import keyboard
#FUNCION DE TIME
import time
#INTERACCION DE SISTEMA PARA MANEJO DE ARCHIVOS LOCALES
import os
#PARA USAR EXPLICIT WAITS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#USO DE TRY EXCEPT
from selenium.common.exceptions import TimeoutException

PAUSA = (0.13)
# Configura las opciones de Chrome para iniciar cada instancia con un puerto de depuración diferente
options = webdriver.ChromeOptions()
    # Imprime el texto ingresado por el usuario
print("""
 
    ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗  ░██████╗████████╗██████╗░███████╗░██████╗░██████╗
    ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║  ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔════╝
    ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║  ╚█████╗░░░░██║░░░██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║  ░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║  ██████╔╝░░░██║░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    
    ████████╗███████╗░██████╗████████╗    ─────█─▄▀█──█▀▄─█─────      
    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ────▐▌──────────▐▌──── 
    ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░    ────█▌▀▄──▄▄──▄▀▐█──── 
    ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░    ───▐██──▀▀──▀▀──██▌───  
    ░░░██║░░░███████╗██████╔╝░░░██║░░░    ──▄████▄──▐▌──▄████▄──
    ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░   
    
    ██████╗░██╗░░░██╗
    ██╔══██╗╚██╗░██╔╝
    ██████╦╝░╚████╔╝░
    ██╔══██╗░░╚██╔╝░░
    ██████╦╝░░░██║░░░
    ╚═════╝░░░░╚═╝░░░

    ██████╗░░█████╗░██████╗░██╗░░██╗░░░███╗░░░███╗░█████╗░██╗░░░██╗░
    ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░████╗░░███║██╔══██╗██║░░░██║░
    ██║░░██║███████║██████╔╝█████═╝░░░░██╔████╔██║███████║██║░░░██║░
    ██║░░██║██╔══██║██╔══██╗██╔═██╗░░░░██║╚██╔╝██║██╔══██║██║░░░██║░
    ██████╔╝██║░░██║██║░░██║██║░╚██╗░░░██║░╚═╝░██║██║░░██║╚██████╔╝░
    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░░
    
""")   
# Pedir al usuario que llene la casilla de pruebas.
def get_user_input():
    # Crea una ventana emergente utilizando tkinter
    root = tk.Tk()
    root.withdraw()
    # Muestra una ventana de diálogo para que el usuario ingrese un texto
    user_input = simpledialog.askinteger(title="WINDOWS CHROME LOGIN STRESS TEST by DARK MAU", prompt="NUMERO DE VENTANAS?")
    return user_input
# Llama a la función para obtener la entrada del usuario y guardarla en una variable
windowsStressNum = get_user_input()

# Imprime la variable para verificar que se haya guardado correctamente
print(f"EL NUMERO DE PRUEBAS ES: {windowsStressNum}")
##################################################################
# ABRIR TXT CON LA IP EN LA UBICACION ACTUAL
dir_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(dir_actual, "IPSIVALE.txt")
archivo = open(ruta_archivo, "r")
contenido = archivo.readlines()
archivo.close()

urls = []

for linea in contenido:
    urls.append(str(linea.strip()))
print("LA IP ES : ")
print(urls)

# NUMERO DE VENTANAS
for i in range(windowsStressNum):
    urls += contenido
# Inicia una única instancia de Chrome y abre la primera URL
#options.add_experimental_option('debuggerAddress', 'localhost:9010')
driver = webdriver.Chrome(options=options)
#driver.maximize_window()
###IMPLICITLY WAIT
#driver.implicitly_wait(2)
#EXPLICITLY WAIT


driver.get(urls[0])
#variable de control
detener = False
# Abre cada URL restante en una nueva pestaña de la misma ventana
for i, url in enumerate(urls[1:]):
    # Revisa si alguna de las teclas S, P o D fue presionada
    if keyboard.is_pressed('s'):
        print("Ciclo detenido")
        while True:
            # Espera hasta que la tecla R sea presionada para reanudar el ciclo
            if keyboard.is_pressed('r'):
                print("Ciclo reanudado")
                break
    elif keyboard.is_pressed('p'):
        print("""
█████████████████████████████████████████████████████████████████████████████
█─▄▄▄─█▄─▄█─▄▄▄─█▄─▄███─▄▄─███▄─▄▄▀█▄─▄▄─█─▄─▄─█▄─▄▄─█▄─▀█▄─▄█▄─▄█▄─▄▄▀█─▄▄─█
█─███▀██─██─███▀██─██▀█─██─████─██─██─▄█▀███─████─▄█▀██─█▄▀─███─███─██─█─██─█
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀""")
        while True:
            # Espera hasta que la tecla R sea presionada para reanudar el ciclo
            if keyboard.is_pressed('r'):
                print("""
██████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─█▄─▄█─▄▄▄─█▄─▄███─▄▄─███▄─▄▄▀█▄─▄▄─██▀▄─██▄─▀█▄─▄█▄─██─▄█▄─▄▄▀██▀▄─██▄─▄▄▀█─▄▄─█
█─███▀██─██─███▀██─██▀█─██─████─▄─▄██─▄█▀██─▀─███─█▄▀─███─██─███─██─██─▀─███─██─█─██─█
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀
                """)
                break
    elif keyboard.is_pressed('d'):
        print("""
██████████████████████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄─█▄─▄█─▄▄▄─█▄─▄███─▄▄─███▄─▄█▄─▀█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▄▄▀█▄─██─▄█▄─▀█▀─▄█▄─▄▄─█▄─▄█▄─▄▄▀█─▄▄─█
█─███▀██─██─███▀██─██▀█─██─████─███─█▄▀─████─████─▄█▀██─▄─▄██─▄─▄██─██─███─█▄█─███─▄▄▄██─███─██─█─██─█
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀""")
        break
    
    driver.execute_script(f"window.open('{url}', '_blank');")
    # Cambia a la nueva pestaña
    driver.switch_to.window(driver.window_handles[-1])
    # cambiar al frame de la pagina
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
    
    #CONTADOR EN CONSOLA DE PESTAÑAS ABIERTAS
    print(f"PESTAÑA: {i+1} ABIERTA CON EXITO")
    #INTERRUPT THE TEST

print("""

██████╗░██████╗░██╗░░░██╗███████╗██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔══██╗
██████╔╝██████╔╝██║░░░██║█████╗░░██████╦╝███████║
██╔═══╝░██╔══██╗██║░░░██║██╔══╝░░██╔══██╗██╔══██║
██║░░░░░██║░░██║╚██████╔╝███████╗██████╦╝██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝

███████╗██╗███╗░░██╗░█████╗░██╗░░░░░██╗███████╗░█████╗░██████╗░░█████╗░
██╔════╝██║████╗░██║██╔══██╗██║░░░░░██║╚════██║██╔══██╗██╔══██╗██╔══██╗
█████╗░░██║██╔██╗██║███████║██║░░░░░██║░░███╔═╝███████║██║░░██║███████║
██╔══╝░░██║██║╚████║██╔══██║██║░░░░░██║██╔══╝░░██╔══██║██║░░██║██╔══██║
██║░░░░░██║██║░╚███║██║░░██║███████╗██║███████╗██║░░██║██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
""")
time.sleep(200)
# Cierra la ventana al finalizar
driver.quit()