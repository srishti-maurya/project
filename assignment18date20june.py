from tkinter import *
r = Frame ()
r.pack ()
dict = {"noah": 9876542155, "liam": 8545662483, "william": 7485633527, "benjamin": 7589846527, "jacob": 9961744778,
        "alexander": 9862347429, "daniel": 8562788587,"matthew": 8745262345}
label1 = Label (r, text="DISPLAYING NAME...")
label1.pack (side="top")
label2 = Label (r, text="DISPLAYING NUMBER...")
label2.pack (side="bottom")
def fun(event):
    label = lst.get (ACTIVE)
    print(label)
    ph = dict.get (label)
    global label1, label2
    label1.config (text=label)
    label2.config (text=ph)
lst = Listbox (r)
sbar = Scrollbar (r)
sbar.config (command=lst.yview)
lst.config (yscrollcommand=sbar.set)
sbar.pack (side=RIGHT, fill=Y)
lst.pack (side=LEFT, expand=YES, fill=BOTH)
lst.bind ('<Double-1>',fun)
for k, v in dict.items ():
    lst.insert ('end', k)
T = Text(r, height=20, width=30)
T.pack()
T.insert(END, dict)
r.mainloop ()















