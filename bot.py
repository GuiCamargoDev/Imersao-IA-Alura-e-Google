import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyBbccPzTef3WvoZu9ZYPEC5jMF5BKSax-w"
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}   

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

response = model.generate_content("Vamos aprender conteúdo sobre IA. Me dê sugestões.")
print(response.text)

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta: ", response.text,"\n")
  prompt = input("Esperando prompt: ")

#Melhorando a visualização
#Código disponível em https://ai.google.dev/tutorials/python_quickstart#import_packages
import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#Imprimindo o histórico
for message in chat.history:
  display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
  print('-------------------------------------------')