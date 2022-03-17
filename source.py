import tkinter as tk
from tkinter import filedialog
from PIL import Image
import requests
import glob

root = tk.Tk()
root.geometry('850x150')
root.title(string='ResourcePy')
enter = tk.Label(root,text='Enter Name:',font=('Minecraft',16)).grid(row=0,column=0)
entry = tk.Entry(root, width=40,font=('Minecraft',12))
entry.grid(row=0,column=1)
enter2 = tk.Label(root,text='Enter Pack Type:',font=('Minecraft',16)).grid(row=1,column=0)
entry2 = tk.Entry(root, width=40,font=('Minecraft',12))
entry2.grid(row=1,column=1)
def opendir():
    global entry2
    global entry
    pack_type = entry2.get()
    name = entry.get()
    filenamusda = filedialog.askdirectory()
    path = filenamusda + "/*.png"
    r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    rdata = r.json()
    uuid = rdata["id"]
    names = rdata["name"]
    req = requests.get(f"https://crafatar.com/avatars/{uuid}?size={pack_type}&overlay")
    with open("face.png", "wb") as f:
        f.write(req.content)
    for file in glob.glob(path):
        img = Image.open(file)
        img2 = Image.open('face.png')
        img2.paste(img, (0, 0))
        img2.save(file)
openfile = tk.Button(root,text='Open Path of blocks/items',font=('Minecraft',13),command=opendir).grid(row=0,column=2)
root.mainloop()

