# Convertidor numérico en Python (Proyecto de compiladores)

## ¿Cómo inicializar el proyecto?

1. Crear un entorno virtual en pyton con pyenv (pyenv-win en caso de windows)

```
    python -m venv conversor_venv
```

2. Activar el entorno virtual

```
    ./conversor_venv\Scripts\activate
```
3. Instalar las dependencias

```
    pip install -r requirements.txt 
```

4. Iniciar el proyecto
```
    python app.py
```
O simplemente darle a el botón play de VSCode

## Estructura del proyecto

```
proyecto/
│
├── app.py                # Archivo principal Flask
├── logic/                # Módulos de lógica (analizador, parser, etc.)
│   ├── lexer.py
│   ├── parser.py
│   └── ...
├── templates/            # HTML para Flask
│   └── index.html
├── static/               # Archivos CSS/JS
├── requirements.txt
└── README.md
```