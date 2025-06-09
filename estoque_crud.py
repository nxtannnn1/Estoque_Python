from validacoes import Validador

def adicionar_item_gui(codigo, descricao, fabricante, preco):
    if not Validador.validar_codigo(codigo):
        return "Código inválido!"
    if not Validador.validar_descricao(descricao):
        return "Descrição inválida!"
    if not Validador.validar_fabricante(fabricante):
        return "Fabricante inválido!"
    if not Validador.validar_preco(preco):
        return "Preço inválido!"

    with open("estoque.txt", "a", encoding="utf-8") as f:
        f.write(f"{codigo},{descricao},{fabricante},{preco}\n")
    return "Item adicionado com sucesso!"

def listar_estoque_gui():
    try:
        with open("estoque.txt", "r", encoding="utf-8") as f:
            return [linha.strip().split(",") for linha in f if linha.strip()]
    except FileNotFoundError:
        return []

def excluir_item_gui(codigo):
    removido = False
    with open("estoque.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    with open("estoque.txt", "w", encoding="utf-8") as f:
        for linha in linhas:
            if not linha.startswith(f"{codigo},"):
                f.write(linha)
            else:
                removido = True

    return "Item removido com sucesso!" if removido else "Código não encontrado."

def alterar_item_gui(codigo, novo_codigo, nova_descricao, novo_fabricante, novo_preco):
    atualizado = False
    with open("estoque.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    with open("estoque.txt", "w", encoding="utf-8") as f:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == codigo:
                f.write(f"{novo_codigo},{nova_descricao},{novo_fabricante},{novo_preco}\n")
                atualizado = True
            else:
                f.write(linha)

    return "Item alterado com sucesso!" if atualizado else "Código não encontrado."
