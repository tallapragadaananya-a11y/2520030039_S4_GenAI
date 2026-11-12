from dotenv import load_dotenv
from google import genai
import time
from google.genai.errors import ServerError
import os

# Step 1: Load API key from .env
load_dotenv(override=True)

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Make first LLM call
for attempt in range(3):
    try:
        response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words."
    )
    # Step 5: Display response
        print("\nLLM Response:")
        print(response.text)
        break
    except ServerError:
        print(f"Server busy (attempt {attempt + 1}/3). Retrying in 5 seconds...")
        time.sleep(5)
