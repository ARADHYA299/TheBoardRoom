import google.generativeai as genai  # type: ignore

class GeminiLLM:
    def __init__(self,api_key :str): 
      genai.configure(api_key=api_key)
      self.model = genai.GenerativeModel("gemini-1.5-flash")
      
    def call(self , prompt : str):
      response = self.model.generate_content(prompt)
      return response.text