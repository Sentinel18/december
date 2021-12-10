from easygui import *
"""
user_response = msgbox("Hello There!", title = "General Kenobi", ok_button="I have the high ground!",image="python_logo.png")

print(user_response)

flavor = buttonbox("Melyik a kedvenc fagylaltod?", title = "fagylalt", choices=["csoki","eper", "torta"],
                    images="python_logo.png", default_choice="csoki")
"""

flavor = choicebox("Melyik a kedvenc fagylaltod?", title = "fagylalt", choices=["csoki","eper", "torta"], preselect=1)

print(flavor)
