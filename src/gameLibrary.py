from tkinter import *
from hangMan import *
from sudoku import *

root = Tk()
root.title("Home")
root.geometry("400x400")
root.resizable(width=False, height=False)

main_frame = LabelFrame(root, pady=40, padx=40)
main_frame.pack()
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
home_title = Label(main_frame, text="Select Game", font=('Arial', 40, 'bold'))
home_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
hangMan_btn = Button(main_frame, text="HangMan", font=('Arial', 20, 'bold'), command=run_hangman)
hangMan_btn.grid(row=1, column=0, pady=10, ipadx=6, ipady=5)
sudoku_btn = Button(main_frame, text="Sudoku", font=('Arial', 20, 'bold'), command=run_sudoku)
sudoku_btn.grid(row=1, column=1, pady=10, ipadx=10, ipady=5)

root.mainloop()
