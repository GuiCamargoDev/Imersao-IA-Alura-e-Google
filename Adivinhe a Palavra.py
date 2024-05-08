import requests
import random

#url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
#resposta = requests.get(url)
#data = resposta.json()
#print(data)

valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']
print(f'A palavra secreta tem {len(palavra_secreta)} letras')
print(f'A dica é -> {dica}')
chute = input('O que você acha que é')
if chute == palavra_secreta:
  print('Acertou')
else:
  print(f'Errou... a palavra secreta era {palavra_secreta}')
