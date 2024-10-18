import random
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def run_sudoku():
  # Create New Window
  top = Toplevel()
  top.title("Sudoku")
  top.geometry("550x550")
  top.resizable(width=False, height=False)
  frame = create_frame(top)
  frame.pack()

def reset_all(frame, master):
  frame.destroy()
  frame = create_frame(master)
  frame.pack()

def create_frame(master):
  top = LabelFrame(master)
  game = LabelFrame(top)
  game.pack()

  # Options buttons
  errLabel = Label(game, text='', fg='red')
  errLabel.grid(row=15, column=1, columnspan=10, pady=5)

  solvedLabel = Label(game, text='', fg='green')
  solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

  cells = {}

  return top
