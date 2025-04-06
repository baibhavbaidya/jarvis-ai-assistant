from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Create a chat completion

def ask_jarvis(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )


    return completion.choices[0].message.content.strip()
