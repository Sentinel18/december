import easygui

try:
    ev =  int(easygui.enterbox("Évszám: ",title="Adatbekérés"))
    if ev % 4 ==0:
        if ev%100==0:
            easygui.msgbox("Szökőév",title="Eredmény")
        else:
            easygui.msgbox("Szökőév",title="Eredmény")
    else:
         easygui.msgbox("Szökőév",title="Eredmény")
except:
    easygui.msgbox("Nem megfelelő érték",title="Hiba")