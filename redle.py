from tkinter import *
import tkinter.scrolledtext as st
from tkinter import filedialog
from tkinter import messagebox
from subprocess import Popen, PIPE, STDOUT
import re
import os
import sys

root=Tk() 
root.title("Mars")
root.geometry("532x550")
s=0
fname=""

def run():
    global s
    if(s==1):
        script_path = fname
        p = Popen([sys.executable, '-u', script_path],stdout=PIPE, stderr=STDOUT)
        with p.stdout:
            for line in iter(p.stdout.readline, b''):
                output_area.insert("1.0",line)
        p.wait()
    else:
        savefile()
        script_path = fname
        p = Popen([sys.executable, '-u', script_path],stdout=PIPE, stderr=STDOUT)
        with p.stdout:
            for line in iter(p.stdout.readline, b''):
                output_area.insert("1.0",line)
        p.wait()


code_area = st.ScrolledText(root,width = 100,height = 20,font = ("Times New Roman",15)) 
testcase_area = st.ScrolledText(root,width = 10,height = 10,font = ("Times New Roman",15))
output_area = st.ScrolledText(root,width = 10,height = 10,font = ("Times New Roman",15))
code_area.pack(fill=BOTH,side=LEFT)
testcase_area.pack(fill=BOTH,side=TOP,expand=TRUE)
output_area.pack(fill=BOTH,side=BOTTOM,expand=TRUE)

run=Button(root,text="Run",padx=100,pady=5,command=run)
run.pack(fill=BOTH,side=TOP)

def openfile():
    global fname
    file1 = filedialog.askopenfile(parent=root,mode='rb',title="Select a Python file",filetypes=[("Data file","*.py"),("All files","*.*")],)
    if file1 != None:
        contents=file1.read()
        code_area.insert("1.0",contents)
        testcase_area.delete("1.0",END)
        output_area.delete("1.0",END)
        file1.close()
        fname=file1.name
        
def savefile():
    global s
    file1 = filedialog.asksaveasfile(mode ="w",defaultextension="*.py",confirmoverwrite=True)
    if file1 != None:
        s=1
        data = code_area.get("1.0",END+'-1c')
        file1.write(data)
        file1.close()

def exitfile():
    reply = messagebox.askyesnocancel(title="EXIT", message="Do you want to save and exit")
    if(reply == True):
        savefile()
    elif(reply == False):
        root.destroy()
    else:
        pass
    
def newfile():
    if len(code_area.get("1.0",END+'-1c'))>0:
        if messagebox.askyesno("Save?","Do you wish to save?"):
            savefile()
        else: 
            code_area.delete("1.0",END)
            testcase_area.delete("1.0",END)
            output_area.delete("1.0",END)
    code_area.delete("1.0",END)
    testcase_area.delete("1.0",END)
    output_area.delete("1.0",END)
    
def about():
    label = messagebox.showinfo("About","A Python Code Evaluator")

    
    
def cut():
    pass

def copy():
    pass

def paste():
    pass

def Select_All():
    pass



    
menubar = Menu(root) 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File',command = newfile,accelerator="Ctrl+N") 
file.add_command(label ='Open...', command = openfile,accelerator="Ctrl+O") 
file.add_command(label ='Save', command = savefile,accelerator="Ctrl+S")
file.add_separator() 
file.add_command(label ='Exit', command = exitfile,accelerator="Alt+F4")

edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None,accelerator="Ctrl+X") 
edit.add_command(label ='Copy', command = None,accelerator="Ctrl+C") 
edit.add_command(label ='Paste', command = None,accelerator="Ctrl+V") 
edit.add_command(label ='Select All', command = None,accelerator="Ctrl+A") 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None)

help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = about)


root.config(menu = menubar) 
root.mainloop()
