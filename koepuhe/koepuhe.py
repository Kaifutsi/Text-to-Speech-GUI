#Kirjastojen tuonti
from tkinter import *
from gtts import gTTS
from playsound import playsound
language = "fi"
from PIL import Image, ImageTk


#Toiminnon luominen painikkeelle tekstin muuntamiseksi puheeksi
#get : Saadaksesi syöttöruutuun syötetyn tekstin ja tallentaaksesi sen muuttujaan
#gTTS : Muunna funktiolle välitetty viesti puheeksi
#save: Puheen tallentaminen mp3-muodossa
#playsound : Toistaa edellisessä vaiheessa tallennetun puheen

def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text = message, lang = language)
    speech.save('koepuhe.mp3')
    playsound('koepuhe.mp3')
 
def exit():
    window.destroy()
 
def reset():
    Msg.set("")



#Alkuperäisen Tkinter-ikkunan luominen
 
window = Tk()
window.geometry("400x700") 
window.configure(bg='darkred')
window.title("TEKSTI PUHEEKSI")



#Widgetien lisääminen ikkunaan

Label(window, text = "        TEKSTI PUHEEKSI        ", font = "arial 20 bold", bg='white',fg="darkred").pack(pady=40)
Msg = StringVar()
Label(window,text ="Kirjoita tekstisi tähän: ", font = 'arial 20 bold', fg ='white', bg = 'darkred').pack(padx=10, pady=10)
 
entry_field = Entry(window, textvariable = Msg ,width ='30',font = 'arial 15 bold',bg="white")
entry_field.pack(padx=10, pady=10)
 
Button(window, text = "TOISTA TEKSTI", font = 'arial 15 bold' , command = text_to_speech ,width = '20',bg = 'white',fg="darkred").pack(padx=10, pady=10)
Button(window, font = 'arial 15 bold',text = 'reset APPLICATION', width = '20' , command = reset,bg = 'white',fg="darkred").pack(padx=10, pady=10)
Button(window, font = 'arial 15 bold',text = 'exit APPLICATION', width = '20' , command = exit, bg = 'white',fg="darkred").pack(padx=10, pady=10)


img = ImageTk.PhotoImage(Image.open("picpuhe.png"))
panel = Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

window.mainloop()