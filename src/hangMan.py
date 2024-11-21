from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

word = ''
guessed = ''
numWrong = 0

def run_hangman():
  # Create New Window
  top = Toplevel()
  top.title("HangMan")
  top.geometry("800x600")
  top.resizable(width=False, height=False)
  frame = create_frame(top)
  frame.pack()

def reset_all(frame, master):
  frame.destroy()
  frame = create_frame(master)
  frame.pack()

def create_frame(master):
  top = LabelFrame(master)
  # Create Frames for display and text buttons
  display = LabelFrame(top)
  display.pack()
  game = LabelFrame(top)
  game.pack()

  # Options buttons
  options = LabelFrame(top)
  options.pack()

  global guessed, word, numWrong
  guessed = ''
  word = ''
  numWrong = 0
  # Get random word from list
  fp = open(r"assets/files/hangman/wordlist.txt", 'r')
  lines = fp.readlines()
  line = random.randint(0, len(lines))
  word = lines[line]
  fp.close()
  # Create variable to store and display letters guessed
  for x in range(1, len(word)):
    if x == len(word) - 1:
      guessed += '_'
    else:
      guessed += '_  '

  # Increment numWrong counter and update image, end gameDriver if 7 wrong guesses
  def incorrect():
    global numWrong
    numWrong += 1
    img1 = ImageTk.PhotoImage(Image.open("assets/images/hangman/" + str(numWrong) + ".png"))
    render_image.config(image=img1)
    render_image.image = img1
    if numWrong == 7:
      end_game(False)

  def end_game(win):
    game.destroy()
    word_display.config(text=word)
    reset_btn.config(text='Play Again')
    if win: message = "YOU WIN"
    else: message = "YOU LOSE"
    messagebox.showinfo(message, message)

  # Check if guessed letter is in word, add it to the guessed string if it is
  def guess_letter(c, btn):
    global word, guessed
    btn.config(state='disabled')
    if word.count(c) == 0:
      incorrect()
    else:
      lst = list(guessed)
      count = 0
      for i in range(0, len(word)):
        if word[i] == c:
          lst[count] = c
        count += 3
        guessed = ''.join(lst)
      word_display.config(text=guessed)
      word_display.text = guessed
      if guessed.count('_') == 0:
        end_game(True)

  # Display Default HangMan image
  img0 = ImageTk.PhotoImage(Image.open("assets/images/hangman/0.png"))
  render_image = Label(display, image=img0)
  render_image.image = img0
  render_image.grid(row=0, column=0)

  # Display Empty word to guess
  global word_display
  word_display = Label(display, text=guessed, font=('Arial', 20, 'bold'), padx=10, pady=10)
  word_display.grid(row=1, column=0)

  # Reset the gameDriver
  reset_btn = Button(options, text="Reset", command=lambda: reset_all(top, master))
  reset_btn.pack()

  # Keyboard
  Q = Button(game, text='Q', padx=10, pady=5, foreground='black', command=lambda: guess_letter('q', Q))
  W = Button(game, text='W', padx=10, pady=5, foreground='black', command=lambda: guess_letter('w', W))
  E = Button(game, text='E', padx=10, pady=5, foreground='black', command=lambda: guess_letter('e', E))
  R = Button(game, text='R', padx=10, pady=5, foreground='black', command=lambda: guess_letter('r', R))
  T = Button(game, text='T', padx=10, pady=5, foreground='black', command=lambda: guess_letter('t', T))
  Y = Button(game, text='Y', padx=10, pady=5, foreground='black', command=lambda: guess_letter('y', Y))
  U = Button(game, text='U', padx=10, pady=5, foreground='black', command=lambda: guess_letter('u', U))
  I = Button(game, text='I', padx=12, pady=5, foreground='black', command=lambda: guess_letter('i', I))
  O = Button(game, text='O', padx=10, pady=5, foreground='black', command=lambda: guess_letter('o', O))
  P = Button(game, text='P', padx=10, pady=5, foreground='black', command=lambda: guess_letter('p', P))

  A = Button(game, text='A', padx=10, pady=5, foreground='black', command=lambda: guess_letter('a', A))
  S = Button(game, text='S', padx=10, pady=5, foreground='black', command=lambda: guess_letter('s', S))
  D = Button(game, text='D', padx=10, pady=5, foreground='black', command=lambda: guess_letter('d', D))
  F = Button(game, text='F', padx=10, pady=5, foreground='black', command=lambda: guess_letter('f', F))
  G = Button(game, text='G', padx=10, pady=5, foreground='black', command=lambda: guess_letter('g', G))
  H = Button(game, text='H', padx=10, pady=5, foreground='black', command=lambda: guess_letter('h', H))
  J = Button(game, text='J', padx=11, pady=5, foreground='black', command=lambda: guess_letter('j', J))
  K = Button(game, text='K', padx=10, pady=5, foreground='black', command=lambda: guess_letter('k', K))
  L = Button(game, text='L', padx=10, pady=5, foreground='black', command=lambda: guess_letter('l', L))

  Z = Button(game, text='Z', padx=10, pady=5, foreground='black', command=lambda: guess_letter('z', Z))
  X = Button(game, text='X', padx=10, pady=5, foreground='black', command=lambda: guess_letter('x', X))
  C = Button(game, text='C', padx=10, pady=5, foreground='black', command=lambda: guess_letter('c', C))
  V = Button(game, text='V', padx=10, pady=5, foreground='black', command=lambda: guess_letter('v', V))
  B = Button(game, text='B', padx=10, pady=5, foreground='black', command=lambda: guess_letter('b', B))
  N = Button(game, text='N', padx=10, pady=5, foreground='black', command=lambda: guess_letter('n', N))
  M = Button(game, text='M', padx=10, pady=5, foreground='black', command=lambda: guess_letter('m', M))

  Q.grid(row=0, column=0, columnspan=2)
  W.grid(row=0, column=2, columnspan=2)
  E.grid(row=0, column=4, columnspan=2)
  R.grid(row=0, column=6, columnspan=2)
  T.grid(row=0, column=8, columnspan=2)
  Y.grid(row=0, column=10, columnspan=2)
  U.grid(row=0, column=12, columnspan=2)
  I.grid(row=0, column=14, columnspan=2)
  O.grid(row=0, column=16, columnspan=2)
  P.grid(row=0, column=18, columnspan=2)

  A.grid(row=1, column=1, columnspan=2)
  S.grid(row=1, column=3, columnspan=2)
  D.grid(row=1, column=5, columnspan=2)
  F.grid(row=1, column=7, columnspan=2)
  G.grid(row=1, column=9, columnspan=2)
  H.grid(row=1, column=11, columnspan=2)
  J.grid(row=1, column=13, columnspan=2)
  K.grid(row=1, column=15, columnspan=2)
  L.grid(row=1, column=17, columnspan=2)

  Z.grid(row=2, column=2, columnspan=2)
  X.grid(row=2, column=4, columnspan=2)
  C.grid(row=2, column=6, columnspan=2)
  V.grid(row=2, column=8, columnspan=2)
  B.grid(row=2, column=10, columnspan=2)
  N.grid(row=2, column=12, columnspan=2)
  M.grid(row=2, column=14, columnspan=2)

  return top
