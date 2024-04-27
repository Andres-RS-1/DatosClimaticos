# Sistema de Monitoreo Ambiental para Raspberry Pi
Este proyecto consiste en un sistema de monitoreo ambiental que utiliza una Raspberry Pi para recolectar datos de sensores de calidad del aire y temperatura/humedad, y los almacena en una base de datos MySQL.

## Requisitos
Python 3
Bibliotecas Python: mysql.connector, paho-mqtt, smbus2, gpiozero, RPi.GPIO
Raspberry Pi con acceso a internet
Sensores compatibles (por ejemplo, SDS011 para la calidad del aire, DHT11 para temperatura/humedad)
## Instalación
Clona este repositorio en tu Raspberry Pi.
Instala las bibliotecas Python requeridas utilizando pip:
bash
Copy code
pip install mysql-connector-python paho-mqtt smbus2 gpiozero RPi.GPIO
Conecta los sensores compatibles a los pines GPIO de la Raspberry Pi según sea necesario.
Asegúrate de tener una base de datos MySQL configurada y actualiza las credenciales de conexión en el código.
Uso
Ejecuta el script principal para comenzar a recolectar datos:
bash
Copy code
python main.py
Esto comenzará a recolectar datos de los sensores y almacenarlos en la base de datos MySQL.
### Configuración de Pines GPIO
Si estás utilizando sensores que se conectan a los pines GPIO del Raspberry Pi, asegúrate de que el código configure correctamente los pines GPIO para la entrada/salida de los sensores. Esto puede requerir el uso de funciones específicas de bibliotecas como RPi.GPIO para Python.

### Interfaz I2C
Si estás utilizando sensores que se comunican a través del protocolo I2C, como el ADC MCP3008, necesitarás habilitar la interfaz I2C en tu Raspberry Pi. Puedes hacerlo a través de la configuración del sistema o utilizando el comando raspi-config en la terminal.

### Direcciones de los dispositivos I2C
Si estás utilizando dispositivos I2C, asegúrate de conocer las direcciones correctas de los dispositivos conectados. Esto puede requerir la búsqueda de documentación específica para los sensores que estás utilizando.

### Permisos de Acceso
Dependiendo de los sensores y de cómo estén conectados (por ejemplo, a través de UART o USB), es posible que necesites permisos especiales para acceder a los puertos seriales en tu Raspberry Pi. Esto puede implicar agregar tu usuario al grupo dialout o gpio según sea necesario.

## Contribución
Las contribuciones son bienvenidas. Si encuentras algún error o tienes sugerencias para mejorar el código, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.
