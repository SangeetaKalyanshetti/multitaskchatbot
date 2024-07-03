import os

from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
print(GOOGLE_API_KEY)

working_dir = os.path.dirname(os.path.abspath(__file__))


# Configuring google generative with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load Gemini-Pro model for chatBot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("models/gemini-pro")
    return gemini_pro_model

# Function to load Vision model for Image Captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("models/gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

# Function to get a response from gemini pro 

def gemini_pro_response(user_prompt):
    
    gemini_pro_model = genai.GenerativeModel("models/gemini-pro")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result