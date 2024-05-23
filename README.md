# Instrucciones para Configurar y Usar la Aplicación en Linux Mint

Este documento proporciona instrucciones detalladas para configurar y usar la aplicación en una computadora con Linux Mint.

## Requisitos Previos

Asegúrate de tener instaladas las siguientes dependencias:

- Python 3
- pip (gestor de paquetes de Python)
- Tkinter (paquete GUI para Python)
- pymongo (cliente de MongoDB para Python)
- MongoDB

## Paso 1: Actualizar e Instalar Dependencias

Actualiza tu sistema e instala las dependencias necesarias.

```sh
sudo apt update
sudo apt install python3-pip python3-tk
pip3 install pymongo

## Paso 2: Instalar y Configurar MongoDB

## 2.1. Importar la clave pública de MongoDB

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

## 2.2. Crear el archivo de lista para MongoDB

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

## 2.3. Actualizar paquetes e instalar MongoDB

sudo apt update
sudo apt install -y mongodb-org

## 2.4. Iniciar el servicio de MongoDB

sudo systemctl start mongod

## 2.5. Habilitar el servicio de MongoDB para que arranque al iniciar el sistema

sudo systemctl enable mongod

## 3. Descargar y ejecutar el script AgendaMono.py

## 4. username: usuario, password: password_seguro y authSource: agenda

## Puerto del contenedor: 27017
