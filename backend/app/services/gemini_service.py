import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
print("API KEY FOUND:", os.getenv("GEMINI_API_KEY"))

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def analyze_repository(repo_name: str):
    print("FUNCTION STARTED")

    prompt = f"""
    Analyze the software project named {repo_name}.

    Return:
    1. Project summary
    2. Possible technologies
    3. Estimated complexity
    """

    print("SENDING TO GEMINI")

    response = model.generate_content(prompt)

    print("RESPONSE RECEIVED")

    return response.text