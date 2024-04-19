import requests
import json

openai_api_key = ""
if openai_api_key is None:
    raise ValueError("El API key no va bien.")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "Eres un asistente tecnológico especializado en explicar conceptos con claridad a desarrolladores de software"
        },
        {
            "role": "user",
            "content": "Resume los pasos necesarios para utilizar la API de ChatGPT"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    # print("Response from OpenAI:", response_data)

    # Extract and print the completion message
    completion_message = response_data['choices'][0]['message']['content']
    print("Respuesta de ChatGPT:", completion_message)
else:
    print("Error:", response.status_code, response.text)
