# coding: UTF-8
import random
from Tkinter import *
import tkMessageBox


class AddOption(Toplevel):
    def __init__(self,value):
        Toplevel.__init__(self)
        self.value = StringVar()
        self.label = Label(self, text='请输入要增加的选项的名称')
        self.label.pack()
        self.entry = Entry(self, textvariable=self.value)
        self.entry.pack()
        self.button = Button(self,text='enter',command=lambda:self.callback(value))
        self.button.pack()

    def callback(self,value):
        value.append(self.value.get())
        self.destroy()

        
class RomdomGui():
    def __init__(self, root):
        self.lists=[1,3,4,5,5]
        self.root=root
        self.root.geometry('500x600')
        self.create_widgets()

    def create_widgets(self):
        for item in self.lists:
            Checkbutton(self.root, text=item).pack()
 
        self.add_button = Button(self.root, text='增加选项', command=lambda:self.add_option())
        self.add_button.pack()
        #self.select_button = Button(self, text='生成随机选择结果',command=self.select_option)
        #self.select_button.pack()
        #self.del_button = Button(self, text='删除选项', command=self.del_option)

    def add_option(self):
        AddOption(self.lists)


root=Tk()
test = RomdomGui(root)
root.mainloop()       
