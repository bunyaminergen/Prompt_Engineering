from docx import Document
import openai
from config import api_key


def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


openai.api_key = api_key
knowledge_base = read_docx("article.docx")

user_question = "Metin ne hakkindadir?"

messages = [
    {"role": "system", "content":
        "You are a helpful assistant that can answer questions based on the provided knowledge base."},
    {"role": "assistant", "content": knowledge_base},
    {"role": "user", "content": user_question}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=500,
    temperature=0.1,
)

answer = response['choices'][0]['message']['content']
print(f"Q: {user_question}\nA: {answer}")
