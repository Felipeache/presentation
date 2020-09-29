from time import sleep
from colorama import Cursor, init, Fore, Back
import emoji


ok = "Ok Google"
find = "Je veux trouver le meilleur alternant en Web Dev à Paris"
init()

for char in ok:
    print(Fore.YELLOW+Back.BLUE+char+Back.RESET, end="", flush=True)
    sleep(0.1)

print(Cursor.UP(1)+"\n")

for char in find:
    print(Fore.YELLOW+Back.BLUE+char, end="", flush=True)
    sleep(0.1)

print(Back.RESET,Cursor.UP(1)+'\n')
print(Fore.BLUE+Back.WHITE+
        "Searching: \"le meilleur alternant en Web Dev à Paris\"",
        emoji.emojize(':detective:')
    )

for i in range(12):
    sleep(0.5)
    print(Cursor.UP(1)+Cursor.FORWARD(55)+"."*i)

print("One Web Dev found!" + emoji.emojize(':man_technologist:'))
sleep(2)
print("Loading data....")
sleep(2)
print("Importing email: \"felipe@henao.me\" " + emoji.emojize(
        ':open_file_folder:')+'\n')
sleep(1.5)

print(Fore.LIGHTGREEN_EX+Back.RESET+"""{
"about": {
    "name": "Luis Felipe Henao",
    "title: "Développeur Web Fullstack - Alternance",
    "email": "felipe@henao.me",
    "phone": "+33760777810",""")
sleep(1.5)
print(Cursor.UP(1)+"""
"bio": "Hello!"""+emoji.emojize(':waving_hand:')+"""
        Je suis Felipe, j'adore les """+emoji.emojize(':french_fries:')+""" et coder.
        Je suis autonome, sérieux et rigoureux.
        J'ai de l'expérience sur Python, Django, Angular, JS, Ionic.
        Je souhaite intégrer une équipe me permettant d'évoluer
        en alternance pendant 12 mois.",
"location": {
    "city": "Courbevoie" 
    "country": "France", 
  }
},""")
sleep(2)

print("Data loaded successfully!")
sleep(2)

print(Fore.BLUE+Back.WHITE+"""
Alternance 3 semaines x 1 semaine
Région parisienne
À partir du 09/11/2020
N'hésitez pas à venir consulter mon 
CV sur LinkedIn: 
https://www.linkedin.com/in/lf-henao/
"""+emoji.emojize(':e-mail:')+""" Email: felipe@henao.me
""")
print(Cursor.UP(1),"")

