# Gestor de Gastos

Programa simple en Python para llevar un control de gastos personales.

## Descripción

Este programa permite registrar, visualizar y eliminar gastos de manera fácil y rápida. Los datos se almacenan en formato JSON para persistencia entre sesiones.

## Funcionalidades

- Agregar nuevos gastos con descripción, monto y categoría
- Ver lista completa de todos los gastos registrados
- Calcular el total de gastos acumulados
- Ver resumen de gastos agrupados por categoría
- Eliminar gastos existentes

## Requisitos

- Python 3.7 o superior
- Módulos externos:
  - `colorama`
  - `tabulate`

## Instalación

1. Clonar o descargar este repositorio

2. Crear un entorno virtual:
```bash
python -m venv venv
```

3. Activar el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate


4. Instalar dependencias:
pip install -r requirements.txt


## Uso

Ejecutar el programa:
python main.py


El programa mostrará un menú interactivo con las siguientes opciones:

1. **Agregar gasto**: Ingresar descripción, monto y categoría
2. **Ver todos los gastos**: Listar todos los gastos registrados
3. **Ver total gastado**: Mostrar la suma total de gastos
4. **Ver gastos por categoría**: Resumen agrupado por categorías
5. **Eliminar gasto**: Seleccionar y eliminar un gasto existente
6. **Salir**: Cerrar el programa

## Estructura del Proyecto
```
Gestor de Gastos/
├── venv/                 # Entorno virtual
├── main.py               # Programa principal
├── task_manager.py       # Módulo de gestión de gastos
├── storage.py            # Módulo de almacenamiento
├── gastos.json           # Archivo de datos (se crea automáticamente)
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo


## Buenas Prácticas Aplicadas

- Uso de docstrings (PEP 257)
- Código formateado según PEP 8
- Modularización del código
- Uso de entorno virtual
- Documentación clara