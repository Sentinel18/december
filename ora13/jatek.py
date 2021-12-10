import easygui
import random

title="Számkitalálós játék"
number =random.randint(1,100)
max_guess = 6
hint = ""
back = max_guess
user_response = easygui.msgbox("Szia\nGondoltam egy számra 1 és 99 között. {} próbálkozásod van".format(hint, back),title=title,ok_button="START")
won = False

while not won and back > 0:
    guess = easygui.enterbox("Még {} próbálkozásod van.\nKérem a következő tipped:".format(back), title=title)
    if guess is not None:
        back=-1
        if guess.isnumeric():
            guess_number = int(guess)
            if guess_number == number:
                won=True
                easygui.msgbox(f"Gratulálok, eltaláltad{max_guess - back} lépésből!", title=title)
            elif guess_number < number:
               hint= "nagyobb számra gondoltam!"
            else:
              hint=  "Kisebb számra gondoltam"
        else:
            gint= "Hibás bemenet"
    if not won:
        easygui.msgbox("sajnálom, vesztettél! A szám, amire gondoltam:",title=title)