from openai import OpenAI
import os

# Ensure the API key is set as an environment variable
api_key = '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'


# Initialize the OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Create a chat completion request
completion = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say me song for babies",
        },
    ],
)

# Print the response
print(completion.choices[0].message.content)
