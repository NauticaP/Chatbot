# Chatbot con Inteligencia Artificial

Este repositorio contiene el código para un chatbot que utiliza inteligencia artificial. El chatbot está construido con `gradio` para la interfaz de usuario y la API de Hugging Face para las respuestas de IA.

## Descripción

El chatbot está diseñado para responder a preguntas y mantener una conversación básica utilizando un modelo de IA proporcionado por Hugging Face. La interfaz gráfica está creada con `gradio`, lo que permite una interacción fácil y directa con el chatbot.

## Requisitos

- Python 3.7 o superior
- `gradio`
- `huggingface_hub`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/NauticaP/Chatbot.git
    cd Chatbot
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install gradio huggingface_hub
    ```

4. Obtén tu token de API de Hugging Face en [Hugging Face Tokens](https://huggingface.co/settings/tokens) y configúralo en el código:
    ```python
    api_key="..." #Escribe el token de Hugging Face
    ```

## Uso

1. Asegúrate de haber iniciado sesión en Hugging Face:
    ```python
    from huggingface_hub import login
    login(token=api_key)
    ```

2. Ejecuta el script principal:
    ```bash
    python nombre_del_script.py
    ```

3. Abre tu navegador web e ingresa a la dirección que proporciona `gradio` (por defecto `http://127.0.0.1:7860`).

## Estructura del Código

- `funcion_chat`: Función que maneja la lógica de conversación del chatbot.
- `gr.Blocks`: Interfaz gráfica creada con `gradio`.
- `mensaje_sistema`: Mensaje de bienvenida del sistema.

## Ejemplo de Uso

1. Abre la aplicación.
2. Ingresa tu pregunta en el campo de texto.
3. Haz clic en "Enviar" para recibir una respuesta.
