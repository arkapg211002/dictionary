'''ARKAPRATIM GHOSH' TECHNO MAIN SALTLAKE'''
from tkinter import *
from PyDictionary import PyDictionary
#object
dictionary=PyDictionary()
root=Tk()
root.geometry("400x500")
root.title("Pocket Dictionary")
root.maxsize(400,500)
root.minsize(400,500)
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

Label(root,text="DICTIONARY",font=("ComicSansMS 20 bold"),fg="white",bg="grey",borderwidth=3,relief=SUNKEN).pack(pady=10,fill=X)

frame=Frame(root)
Label(frame,text="TYPE WORD",font=("comicsansms 15"),fg="white",bg="grey",borderwidth=3,relief=SUNKEN).pack(side=LEFT,fill=X,padx=2,pady=2)
word=Entry(frame,font=("comicsansms 15 bold italic"))
word.pack()
frame.pack(pady=10)

frame2=Frame(root)
Label(frame2,text="MEANING",font=("comicsansms 15"),fg="white",bg="grey",borderwidth=3,relief=SUNKEN).pack(side=LEFT)
meaning=Label(frame2,text="",font=("comicsansms 15"))
meaning.pack()
frame2.pack(pady=10)

frame3=Frame(root)
Label(frame3,text="SYNONYM",fg="white",bg="grey",font=("comicsansms 15"),borderwidth=3,relief=SUNKEN).pack(side=LEFT)
synonym=Label(frame3,text="",font=("comicsnasms 15"))
synonym.pack()
frame3.pack(pady=10)

frame4=Frame(root)
Label(frame4,text="ANTONYM",fg="white",bg="grey",font=("comicsansms 15"),borderwidth=3,relief=SUNKEN).pack(side=LEFT)
antonym=Label(frame4,text="",font=("comicsansms 15"))
antonym.pack()
frame4.pack(pady=10)

Button(root,text="SEARCH",font=("comicsnasms 15 italic"),command=dict()).pack()
root.mainloop()
