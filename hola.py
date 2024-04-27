import mysql.connector  # Importa el modulo para interactuar con MySQL (se necesita descargar modulo pip desde la terminal)
import time # Importa el modulo para trabajar con fechas y horas

# Importa la clase SDS011 del modulo sds011 para interactuar con el sensor de calidad del aire SDS011 
# --> from sds011 import SDS011 #(se necesita descargar modulo pip desde la terminal) || este tambien pero no me salia disponible en la termina

# Importa el modulo mqtt del paquete paho para utilizar el cliente MQTT y suscribirte a los datos del sensor
import paho.mqtt.client as mqtt #(se necesita descargar modulo pip desde la terminal)

# Importa el modulo smbus para trabajar con el protocolo I2C y comunicarte con dispositivos conectados a la Raspberry Pi
import smbus2 #(se necesita descargar modulo pip desde la terminal)

# Importa el modulo serial para trabajar con la comunicacion serial, que puede ser util para algunos sensores de calidad del aire
import serial #(se necesita descargar modulo pip desde la terminal)

# Importa las clases CPUTemperature y MCP3008 del modulo gpiozero para trabajar con la temperatura de la CPU y el convertidor analogico a digital (ADC)
from gpiozero import CPUTemperature, MCP3008 #(se necesita descargar modulo pip desde la terminal)

import RPi.GPIO as GPIO  # RPi.GPIO es especifico de Raspberry Pi, mediante la instalacion de paquetes del sistema operativo de Raspberry Pi
#sudo apt update
#sudo apt install python3-rpi.gpio



# Funcion para crear la tabla en la base de datos MySQL
def crear_tabla():
    try:
        # Conecta con la base de datos MySQL
        conn = mysql.connector.connect(
            host="tu_host_mysql",
            user="tu_usuario_mysql",
            password="", # Sin contraseña segun tu indicacion
            database="tu_base_de_datos_mysql"
        )
        # Crea un cursor para ejecutar comandos SQL
        c = conn.cursor()
        # Ejecuta un comando SQL para crear la tabla si no existe
        c.execute('''CREATE TABLE IF NOT EXISTS datos (
                    fecha_hora DATETIME,
                    temperatura FLOAT,
                    humedad FLOAT,
                    co2 FLOAT,
                    ch4 FLOAT,
                    no2 FLOAT,
                    hfc FLOAT,
                    so2 FLOAT,
                    pm10 FLOAT
                    )''')
        # Guarda los cambios en la base de datos
        conn.commit()
    except mysql.connector.Error as e:
        # Captura y maneja errores de MySQL
        print("Error al crear la tabla:", e)
    finally:
        # Cierra la conexion con la base de datos
        conn.close()

# Funcion para insertar datos en la tabla MySQL
def insertar_datos(temperatura, humedad, co2, ch4, no2, hfc, so2, pm10):
    try:
        # Conecta con la base de datos MySQL
        conn = mysql.connector.connect(
            host="tu_host_mysql",
            user="tu_usuario_mysql",
            password="",
            database="tu_base_de_datos_mysql"
        )
        # Crea un cursor para ejecutar comandos SQL
        c = conn.cursor()
        # Obtiene la fecha y hora actual
        fecha_hora = time.strftime('%Y-%m-%d %H:%M:%S')
        # Ejecuta un comando SQL para insertar los datos en la tabla
        c.execute("INSERT INTO datos (fecha_hora, temperatura, humedad, co2, ch4, no2, hfc, so2, pm10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                  (fecha_hora, temperatura, humedad, co2, ch4, no2, hfc, so2, pm10))
        # Guarda los cambios en la base de datos
        conn.commit()
    except mysql.connector.Error as e:
        # Captura y maneja errores de MySQL
        print("Error al insertar datos:", e)
    finally:
        # Cierra la conexion con la base de datos
        conn.close()

# Funcion para obtener los valores de los sensores (simulacion)
def obtener_valores_sensores():
    # Simula la lectura de la temperatura utilizando la CPU de la Raspberry Pi
    cpu_temp = CPUTemperature().temperature
    # Simula la lectura de la humedad (supongamos que es fija)
    humedad = 60.0
    # Simula la lectura de los contaminantes utilizando un convertidor analogico-digital (MCP3008)
    adc = MCP3008(channel=0)
    co2 = adc.value * 1023.0  # Simula el valor de CO2 (escala de 0 a 1023)
    adc = MCP3008(channel=1)
    ch4 = adc.value * 1023.0  # Simula el valor de CH4 (escala de 0 a 1023)
    adc = MCP3008(channel=2)
    no2 = adc.value * 1023.0  # Simula el valor de NO2 (escala de 0 a 1023)
    adc = MCP3008(channel=3)
    hfc = adc.value * 1023.0  # Simula el valor de HFC (escala de 0 a 1023)
    adc = MCP3008(channel=4)
    so2 = adc.value * 1023.0  # Simula el valor de SO2 (escala de 0 a 1023)
    adc = MCP3008(channel=5)
    pm10 = adc.value * 1023.0  # Simula el valor de PM10 (escala de 0 a 1023)
    return cpu_temp, humedad, co2, ch4, no2, hfc, so2, pm10

# Funcion para recolectar datos y almacenarlos en la base de datos MySQL
def recolectar_datos():
    while True:
        # Obtener valores de los sensores
        temperatura, humedad, co2, ch4, no2, hfc, so2, pm10 = obtener_valores_sensores()
        # Insertar datos en la base de datos
        insertar_datos(temperatura, humedad, co2, ch4, no2, hfc, so2, pm10)
        # Esperar 1 segundo antes de recopilar nuevos datos
        time.sleep(1)

# Funcion para configurar los pines GPIO
def configurar_pines():
    GPIO.setmode(GPIO.BOARD)  # Configura los pines GPIO usando el esquema de numeracion de pines fisicos
    # Configura los pines GPIO segun sea necesario para la entrada/salida de los sensores
    # Por ejemplo, si se necesita configurar el pin 17 como entrada
    GPIO.setup(17, GPIO.IN)
    # O si se necesita configurar el pin 18 como salida
    GPIO.setup(18, GPIO.OUT)
    # Se debe asegurar los numeros de los pines y sus configuraciones.
configurar_pines()

# Si quiere ejecutar el bucle de recoleccion de datos, descomente la siguiente linea:
# recolectar_datos()