# -*- coding: utf-8 -*-
import google.generativeai as genai
import os
import speech_recognition as sr

# আপনার API Key
API_KEY = "AIzaSyDXwM8x5s6owxdUAwg9GXzhQr4LmXQzzWs"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_voice_input(prompt_text):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\n🎤 {prompt_text}...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return None

def build_voice_app():
    task = get_voice_input("আপনি কি সফটওয়্যার বানাতে চান তা বলুন")
    app_pass = get_voice_input("সফটওয়্যারের জন্য একটি সিক্রেট পাসওয়ার্ড বলুন")
    
    if not task or not app_pass:
        return

    system_prompt = f"Create a complete Python Streamlit application for: {task}. The valid password is: '{app_pass}'."
    response = model.generate_content(system_prompt)
    
    with open("main_app.py", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    build_voice_app()
