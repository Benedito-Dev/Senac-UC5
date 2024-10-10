import customtkinter as ctk
import tkinter as tk

class Aplication(tk.Tk):
    def __init__(self):
        self.title('4 FITNESS')
        self.geometry('800x600')
        self.menu_inicial

    def menu_inicial(self):
        for widget in self.winfo_children():
            widget.destroy()

        background_frame = ctk.CTkFrame(self, bg_color="#313131", corner_radius=0)
        background_frame.pack(fill='both', expand=True)

        self.entry_nome = ctk.CTkEntry(background_frame)
        self.entry_nome.grid(row=0,column=0, pady=10)

        self.entry_senha = ctk.CTkEntry(background_frame)
        self.entry_senha.grid(row=0,column=0, pady=10)