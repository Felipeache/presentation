from time import sleep
from os import system
from colorama import Cursor, init, Fore, Back
import emoji, sys

ok = "Ok Google"
find = "Je veux trouver le meilleur alternant en Web Dev à Paris"
init()
for char in ok:
    print(Fore.WHITE+Back.BLUE+char, end="", flush=True)
    sleep(0.1)
print(Cursor.UP(1)+"\n")
for char in find:
    print(char, end="", flush=True)
    sleep(0.1)
print(Cursor.UP(1)+'\n')
print("Searching: \"le meilleur alternant en Web Dev à Paris\"", emoji.emojize(':detective:'))
for i in range(12):
     sleep(0.5)
     print(Cursor.UP(1)+Cursor.FORWARD(55)+Fore.WHITE+Back.BLUE+"."*i+Back.RESET)

print("One " + emoji.emojize(':man_technologist:') + " found!")
sleep(3)
print("Importing email: \"felipe@henao.me\" " + emoji.emojize(':open_file_folder:')+'\n')
sleep(3)
print("""{
"about": {
    "name": "Luis Felipe Henao",
    "title: "Développeur Web Fullstack - Alternance",
    "email": "felipe@henao.me",
    "phone": "+33760777810",""")
sleep(3)
print(Cursor.UP(1)+"""
    "bio": "Hello!"""+emoji.emojize(':waving_hand:')+"""
    Je suis Felipe, j'adore les """+emoji.emojize(':french_fries:')+""" et coder.
    Je suis autonome, sérieux et rigoureux.
    J'ai de l'experience sur Python, Django, Angular, JS, Ionic.
    Je souhaite intégrer une équipe me permetant évouluer
    en alternance pendant 12 mois. 3semaines x 1 semaine",
"location": {
  "city": "Courbevoie"
  "country": "France",
  }
},""")
sleep(2)
print("Data loaded successfully!")
sleep(2)
print(Fore.BLACK+Back.WHITE+"""
    Alternance 3 semaines x 1 semaines
    A partir du 09/11/2020
    N'hesitez pas à venir vers moi sur:
    LinkedIn: https://www.linkedin.com/in/lf-henao/
    Email: felipe@henao.me
    """)
