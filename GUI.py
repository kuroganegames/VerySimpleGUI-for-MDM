#coding:utf-8

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random
import subprocess as sp


def btn_click():
    print(
    ent_model.get(),
    ent_prompt.get(),
    bln_seed.get(),
    var_seed.get(),
    var_length.get(),
    var_rep.get(),
    )
    
    if bln_seed.get():
        i_seed = random.randint(0, 4294967296-1)
    else:
        i_seed = var_seed.get()
    
    sp.run([
        "python", "-m", "sample",
        "--model_path",ent_model.get(),
        "--text_prompt",ent_prompt.get(),
        "--seed",str(i_seed),
        "--motion_length",str(var_length.get()),
        "--num_repetitions",str(var_rep.get()),
        ])

    



def file_select():
  dir_init = "./save/humanml_trans_enc_512"
  type_ext = [("pre-trained model","*.pt"), ("all","*")] 
  dir_model = tk.filedialog.askopenfilename(filetypes = type_ext, initialdir = dir_init)
  ent_model.delete(0, tk.END)
  ent_model.insert(tk.END, dir_model) #結果を表示


root = tk.Tk()
root.title("Python GUI")
root.geometry("640x400")


lbl_model = tk.Label(root, text="directory of pre-trained model")
lbl_model.pack()


ent_model = tk.Entry(root, width=120)
ent_model.insert(0, r"./save/humanml_trans_enc_512/model000200000.pt")
ent_model.pack()


btn_model = tk.Button(root, text="ref",command=file_select)
btn_model.pack()


lbl_prompt = tk.Label(root, text="prompt")
lbl_prompt.pack()
ent_prompt = tk.Entry(root, width=120)
ent_prompt.pack()


#seed
bln_seed = tk.BooleanVar()
bln_seed.set(True)
chk_seed = tk.Checkbutton(root, variable=bln_seed, text='random seed?')
chk_seed.pack()

var_seed = tk.IntVar(root)
var_seed.set(-1)

spb_seed = tk.Spinbox(
    root,
    textvariable=var_seed,
    from_=-1,
    to=4294967296-1,
    increment=1,
    )
spb_seed.pack()





#motion_length 
lbl_length = tk.Label(root, text="motion_length in seconds (maximum is 9.8[sec] for HumanML3D (text-to-motion)")
lbl_length.pack()
var_length = tk.IntVar()
var_length.set(6)
sc_length = tk.Scale(root, variable=var_length, orient='horizontal', length=510, from_=0, to=9.8,resolution=0.1,tickinterval=1)
sc_length.pack()




#num_repetitions
lbl_rep = tk.Label(root, text="Number of repetitions, per sample (text prompt/action)")
lbl_rep.pack()
var_rep = tk.IntVar(root)
var_rep.set(1)

spb_rep = tk.Spinbox(
    root,
    textvariable=var_rep, 
    from_=1,
    to=15, 
    increment=1,
    )
spb_rep.pack()

btn_run = tk.Button(root, text='run', command=btn_click)
btn_run.pack()


root.mainloop()

