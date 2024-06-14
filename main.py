import google.generativeai as genai
import os

# Get API key from https://aistudio.google.com/
genai.configure(api_key=os.environ['GENAI_API'])

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1048576,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

def generate_readme(prompt):
  model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
  
  prompt_parts = [
    "Your job is to generate README Files for coding projects.",
    f"input: {prompt}",
    "output: ",
  ]
  
  response = model.generate_content(prompt_parts)
  return response.text

# Example usage
print(generate_readme("""Write a README file for this code..."""))
