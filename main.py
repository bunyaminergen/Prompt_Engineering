import openai
from docx import Document
from config import api_key

openai.api_key = api_key

prompt = "remote work"
selectedLanguage = "Türkçe"

messages = [
    {"role": "system", "content": "You are a article generator."},
    {"role": "user", "content": f"Generate a article about {prompt} topic in {selectedLanguage} Language"}
]

response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages,
                                        max_tokens=3000,
                                        temperature=0.5)
article = response['choices'][0]['message']['content']

doc = Document()
doc.add_paragraph(article)
doc.save('article.docx')
