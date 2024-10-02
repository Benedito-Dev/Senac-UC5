import tkinter as tk
from tkinter import messagebox
from tkinter import font

def editar_pref():
    notificacoes = selected_notificacoes.get()
    idioma = selected_idioma.get()
    und_de_medida = entry_und_de_medida.get()
    freq_de_treino = entry_freq_de_treino.get()
    metas_pessoais = entry_metas_pessoais.get()
    
    if notificacoes and idioma and und_de_medida and freq_de_treino and metas_pessoais:
        messagebox.showinfo("", "Alterações realizadas!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

janela = tk.Tk()
janela.title("")
janela.geometry("400x400")
janela.config(bg="#609746")

nunito_font = font.Font(family="Nunito", size=10)
titulo_font = font.Font(family="Nunito", size=14, weight="bold")
botao_font = font.Font(family="Nunito", size=10, weight="bold")

titulo_label = tk.Label(janela, text="Editar Preferências", bg="#609746", fg="#ffffff", font=titulo_font)
titulo_label.grid(row=0, columnspan=2, pady=10)

label_notificacoes = tk.Label(janela, text="Notificações:", bg="#609746", fg="#ffffff", font=nunito_font)
label_notificacoes.grid(row=1, column=0, padx=10, pady=5, sticky='e')

selected_notificacoes = tk.StringVar(value="Exibir")
opcoes_notificacoes = ["Exibir", "Não exibir"]
menu_notificacoes = tk.OptionMenu(janela, selected_notificacoes, *opcoes_notificacoes)
menu_notificacoes.grid(row=1, column=1, padx=10, pady=5)

label_idioma = tk.Label(janela, text="Idioma:", bg="#609746", fg="#ffffff", font=nunito_font)
label_idioma.grid(row=2, column=0, padx=10, pady=5, sticky='e')

selected_idioma = tk.StringVar(value="Português")
opcoes_idioma = ["Português"]
menu_idioma = tk.OptionMenu(janela, selected_idioma, *opcoes_idioma)
menu_idioma.grid(row=2, column=1, padx=10, pady=5)

label_und_de_medida = tk.Label(janela, text="Unidade de medida:", bg="#609746", fg="#ffffff", font=nunito_font)
label_und_de_medida.grid(row=3, column=0, padx=10, pady=5, sticky='e')

entry_und_de_medida = tk.Entry(janela, bg="#efefef", fg="#000000", font=nunito_font)
entry_und_de_medida.grid(row=3, column=1, padx=10, pady=5)

label_freq_de_treino = tk.Label(janela, text="Frequência de treino:", bg="#609746", fg="#ffffff", font=nunito_font)
label_freq_de_treino.grid(row=4, column=0, padx=10, pady=5, sticky='e')

entry_freq_de_treino = tk.Entry(janela, bg="#efefef", fg="#000000", font=nunito_font)
entry_freq_de_treino.grid(row=4, column=1, padx=10, pady=5)

label_metas_pessoais = tk.Label(janela, text="Metas pessoais:", bg="#609746", fg="#ffffff", font=nunito_font)
label_metas_pessoais.grid(row=5, column=0, padx=10, pady=5, sticky='e')

entry_metas_pessoais = tk.Entry(janela, bg="#efefef", fg="#000000", font=nunito_font)
entry_metas_pessoais.grid(row=5, column=1, padx=10, pady=5)

botao_salvar = tk.Button(janela, text="Salvar alterações", command=editar_pref, bg="#000000", fg="#d0fd1b", font=botao_font)
botao_salvar.grid(row=6, columnspan=2, pady=10)

for i in range(7):
    janela.grid_rowconfigure(i, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=1)

janela.mainloop()