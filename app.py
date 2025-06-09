import tkinter as tk
from tkinter import messagebox, ttk
import estoque_crud

def abrir_janela_adicionar():
    def salvar():
        codigo = entry_codigo.get()
        descricao = entry_descricao.get()
        fabricante = entry_fabricante.get()
        preco = entry_preco.get()

        msg = estoque_crud.adicionar_item_gui(codigo, descricao, fabricante, preco)
        messagebox.showinfo("Resultado", msg)
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Adicionar Item")

    tk.Label(janela, text="Código").grid(row=0, column=0)
    tk.Label(janela, text="Descrição").grid(row=1, column=0)
    tk.Label(janela, text="Fabricante").grid(row=2, column=0)
    tk.Label(janela, text="Preço").grid(row=3, column=0)

    entry_codigo = tk.Entry(janela)
    entry_descricao = tk.Entry(janela)
    entry_fabricante = tk.Entry(janela)
    entry_preco = tk.Entry(janela)

    entry_codigo.grid(row=0, column=1)
    entry_descricao.grid(row=1, column=1)
    entry_fabricante.grid(row=2, column=1)
    entry_preco.grid(row=3, column=1)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=0, columnspan=2, pady=5)

def abrir_janela_listar():
    janela = tk.Toplevel(root)
    janela.title("Estoque Atual")

    tree = ttk.Treeview(janela, columns=("codigo", "descricao", "fabricante", "preco"), show="headings")
    tree.heading("codigo", text="Código")
    tree.heading("descricao", text="Descrição")
    tree.heading("fabricante", text="Fabricante")
    tree.heading("preco", text="Preço")

    for item in estoque_crud.listar_estoque_gui():
        tree.insert("", tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)

def abrir_janela_excluir():
    def excluir():
        codigo = entry_codigo.get()
        msg = estoque_crud.excluir_item_gui(codigo)
        messagebox.showinfo("Resultado", msg)
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Excluir Item")
    tk.Label(janela, text="Código do item a excluir:").pack()
    entry_codigo = tk.Entry(janela)
    entry_codigo.pack()
    tk.Button(janela, text="Excluir", command=excluir).pack(pady=5)

def abrir_janela_alterar():
    def alterar():
        codigo = entry_codigo.get()
        novo_codigo = entry_novo_codigo.get()
        nova_descricao = entry_descricao.get()
        novo_fabricante = entry_fabricante.get()
        novo_preco = entry_preco.get()

        msg = estoque_crud.alterar_item_gui(codigo, novo_codigo, nova_descricao, novo_fabricante, novo_preco)
        messagebox.showinfo("Resultado", msg)
        janela.destroy()

    janela = tk.Toplevel(root)
    janela.title("Alterar Item")

    tk.Label(janela, text="Código do item a alterar").grid(row=0, column=0)
    entry_codigo = tk.Entry(janela)
    entry_codigo.grid(row=0, column=1)

    tk.Label(janela, text="Novo Código").grid(row=1, column=0)
    tk.Label(janela, text="Nova Descrição").grid(row=2, column=0)
    tk.Label(janela, text="Novo Fabricante").grid(row=3, column=0)
    tk.Label(janela, text="Novo Preço").grid(row=4, column=0)

    entry_novo_codigo = tk.Entry(janela)
    entry_descricao = tk.Entry(janela)
    entry_fabricante = tk.Entry(janela)
    entry_preco = tk.Entry(janela)

    entry_novo_codigo.grid(row=1, column=1)
    entry_descricao.grid(row=2, column=1)
    entry_fabricante.grid(row=3, column=1)
    entry_preco.grid(row=4, column=1)

    tk.Button(janela, text="Alterar", command=alterar).grid(row=5, column=0, columnspan=2, pady=5)

# ----- JANELA PRINCIPAL -----
root = tk.Tk()
root.title("Sistema de Estoque")
root.geometry("300x300")

tk.Button(root, text="Adicionar Item", command=abrir_janela_adicionar).pack(pady=10)
tk.Button(root, text="Listar Estoque", command=abrir_janela_listar).pack(pady=10)
tk.Button(root, text="Alterar Item", command=abrir_janela_alterar).pack(pady=10)
tk.Button(root, text="Excluir Item", command=abrir_janela_excluir).pack(pady=10)
tk.Button(root, text="Sair", command=root.destroy).pack(pady=10)

root.mainloop()
