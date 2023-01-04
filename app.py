import streamlit as st
import openai
import os

# Inicializa el modelo GPT-3
openai.api_key = os.environ.get("OPENAI_API_KEY")
model_engine = "text-davinci-003"

def generate_arguments(prompt):
  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()

# Define la interfaz de usuario con streamlit
st.title("Generador de argumentos")

st.caption("Por Moris Polanco")

# Solicita al usuario que introduzca un tema
topic = st.text_input("Introduce el tema sobre el que quieres elaborar un argumento:")

if st.button("Generar argumento"):
  # Genera el argumento con GPT-3
  argument = generate_arguments(f"Elaborar un argumento sobre el tema: '{topic}'. 1. Se enuncia el problema en forma de pregunta y se plantea o propone una tesis o conclusión. 2. Principales razones para sostener la tesis; datos, si es un problema descriptivo. 3. Objeciones a las razones. 4. Respuesta a esas objeciones. 5. Conclusión y consecuencias que se derivan de aceptar la tesis.")

  # Muestra el argumento generado en pantalla
  st.markdown(argument)
