# Importaciones necesarias para ejecutar la interfaz gráfica

import gradio as gr
from huggingface_hub import InferenceClient
from huggingface_hub import login


# Autenticación con Hugging Face utilizando un token de API
api_key="Inserte token aqui" # Escribe el token de Hugging Face
login(token=api_key)


# Creación de la InferenceClient para interactuar con el modelo de Hugging Face
cliente = InferenceClient()


# Mensaje inicial del sistema que se enviará a cada usuario al iniciar la conversación
mensaje_sistema = {
    "role": "system",
    "content": """
Bienvenido al Chatbot!
"""}


# Se define la función de chat que maneja las preguntas y respuestas
def funcion_chat(Pregunta,history):
    mensaje = {"role": "user", "content": Pregunta} # Crear un mensaje de usuario basado en la pregunta proporcionada
    respuesta = "" # Variable para acumular la respuesta generada por el modelo
    
    # Generación de la respuesta utilizando el modelo de Hugging Face
    for token in cliente.chat_completion(messages=[mensaje_sistema, mensaje],
                           max_tokens=1000, 
                           stream=True,
                           model="HuggingFaceH4/zephyr-7b-beta"):
        if token.choices[0].finish_reason is not None:
           continue
        respuesta += token.choices[0].delta.content
    return respuesta


# Configuración de la interfaz gráfica utilizando Gradio
with gr.Blocks(title="Chat con IA") as demo:
    gr.Image("S3comLogo.png", height=200, width=100)
    gr.ChatInterface(funcion_chat,clear_btn="Limpiar",submit_btn = "Enviar",retry_btn = None, undo_btn = "Reintentar") # Interfaz de chat

       
# Lanzar la aplicación Gradio cuando se ejecute el script
if __name__ == "__main__":
    demo.launch()