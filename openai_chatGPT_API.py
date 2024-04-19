from openai import OpenAI

client = OpenAI(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Resúmeme los pasos para acceder a la API de ChatGPT usando Python",
        }
    ],
    temperature=0.7,  # Ajusta la creatividad de las respuestas. 1.0 es el más creativo, 0 es determinista.
    max_tokens=1000,   # Limita la longitud de la respuesta generada.
    top_p=1.0,        # Controla la diversidad mediante nucleo de sampling. Un valor más alto significa más diversidad.
    frequency_penalty=0.5,  # Reduce la repetición de palabras y frases en la generación.
    presence_penalty=0.0,   # Incentiva la aparición de nuevos temas y conceptos en la generación.
)

# Usar la notación de punto para acceder al contenido de la respuesta.
print(chat_completion.choices[0].message.content)

