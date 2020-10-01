from time import sleep
from colorama import Cursor, init, Fore, Back
import emoji


ok = "Ok Google"
find = "Je veux trouver le meilleur alternant en Web Dev à Paris"
string_one = """{
 "about": {
     "name": "Luis Felipe Henao",
     "title: "Développeur Web Fullstack - Alternance",
     "email": "felipe@henao.me",
     "phone": "+33760777810",
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
 }"""
signature = """
+++++++++++++++++++++++++++++++++++++++++
+ Alternance 3 semaines x 1 semaine     +
+ Région parisienne                     +
+ À partir du 09/11/2020                +
+ Téléchargez mon CV depuis le          +
+ lien présent dans le post.            +
+ ( https://bit.ly/3idwFOz )            +
+ N'hésitez pas à visiter mon           +
+ profil LinkedIn:                      +
+ https://www.linkedin.com/in/lf-henao/ +
+ Email: felipe@henao.me                +
+++++++++++++++++++++++++++++++++++++++++"""

init()

for char in ok:
    print(Fore.YELLOW+Back.BLUE + char + Back.RESET, end="", flush=True)
    sleep(0.07)

print(Cursor.UP(1)+"\n")

for char in find:
    print(Fore.YELLOW+Back.BLUE + char, end="", flush=True)
    sleep(0.07)

print(Back.RESET,Cursor.UP(1)+'\n')
print(Fore.BLUE+Back.WHITE+
        "Searching: \"le meilleur alternant en Web Dev à Paris\"",
        emoji.emojize(':detective:')
    )

for i in range(12):
    sleep(0.3)
    print(Cursor.UP(1)+Cursor.FORWARD(55)+"."*i)

print("One Web Dev found!" + emoji.emojize(':man_technologist:'))
sleep(2)
print("Loading data....")
sleep(2)
print("Importing email: \"felipe@henao.me\" " ,emoji.emojize(':e-mail:'), emoji.emojize(
        ':open_file_folder:')+'\n')
sleep(0.7)

for char in string_one:
    print(Fore.LIGHTGREEN_EX+Back.RESET + char, end="", flush=True)
    sleep(0.01)

sleep(2)
print("\nData loaded successfully!")
sleep(1)
for char in signature:
    print(Fore.BLUE+Back.WHITE + char, end="", flush=True)
    sleep(0.02)
print(Cursor.DOWN(1))
sleep(30)
