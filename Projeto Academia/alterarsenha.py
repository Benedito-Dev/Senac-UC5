import tkinter as tk
from tkinter import messagebox
from tkinter import font

def alterar_senha():
    senha_antiga = entry_senha_antiga.get()
    nova_senha = entry_nova_senha.get()
    
    if senha_antiga and nova_senha:
        # Aqui você pode adicionar lógica para alterar a senha, se necessário.
        messagebox.showinfo("", "Senha alterada com sucesso!")
        # Limpar os campos após a alteração
        entry_senha_antiga.delete(0, tk.END)
        entry_nova_senha.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

janela = tk.Tk()
janela.title("")
janela.geometry("300x300")

# Definindo o fundo da janela como verde
janela.config(bg="#609746")

# Criando a fonte Nunito
nunito_font = font.Font(family="Nunito", size=10)
titulo_font = font.Font(family="Nunito", size=14, weight="bold")  # Fonte do título em negrito
botao_font = font.Font(family="Nunito", size=10, weight="bold")  # Fonte do botão em negrito

# Label para o título com fonte Nunito
titulo_label = tk.Label(janela, text="Alterar senha", bg="#609746", fg="#ffffff", font=titulo_font)
titulo_label.grid(row=0, columnspan=2, pady=10)

# Labels com texto branco e fonte Nunito
label_senha_antiga = tk.Label(janela, text="Senha antiga:", bg="#609746", fg="#ffffff", font=nunito_font)
label_senha_antiga.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_senha_antiga = tk.Entry(janela, show='*', bg="#efefef", fg="#000000", font=nunito_font)  # Adicionado show='*'
entry_senha_antiga.grid(row=1, column=1, padx=10, pady=5)

label_nova_senha = tk.Label(janela, text="Nova senha:", bg="#609746", fg="#ffffff", font=nunito_font)
label_nova_senha.grid(row=2, column=0, padx=10, pady=5, sticky='e')

entry_nova_senha = tk.Entry(janela, show='*', bg="#efefef", fg="#000000", font=nunito_font)  # Adicionado show='*'
entry_nova_senha.grid(row=2, column=1, padx=10, pady=5)

# Botão com fundo preto, letra verde e fonte em negrito
botao_salvar = tk.Button(janela, text="Salvar nova senha", command=alterar_senha, bg="#000000", fg="#d0fd1b", font=botao_font)
botao_salvar.grid(row=6, columnspan=2, pady=10)

# Ajustando o alinhamento e preenchimento
for i in range(7):
    janela.grid_rowconfigure(i, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=1)

janela.mainloop()