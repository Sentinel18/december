import easygui
import math

try:
    diameter_str = easygui.enterbox("A kör átmérője cm-ben",title="Adatbekérés")
    diameter = float(diameter_str)
    if diameter> 0:
        radius = diameter/2
        kerulet = 2*radius * math.pi
        terulet = radius**2*math.pi
        easygui.msgbox("A {} cm átmérőjű kör kerülete {:.3f} cm, területe pedig: {:.3f} cm^2".format(diameter,kerulet,terulet))

    else:
        easygui.msgbox("Nem megfelelő az érték",title="hiba")
except:
    easygui.msgbox("Nem megflelő az érték:", title="Hiba")

