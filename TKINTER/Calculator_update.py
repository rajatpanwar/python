import tkinter as tk
from tkinter import ttk   #import the tkinter

expr=" "          # create global variable

def press(num):        #create function press
    global expr
    expr=expr+str(num)             #converting string
    eq.set(expr)    #update expression using set method

