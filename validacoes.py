class Validador:
    @staticmethod
    def validar_codigo(codigo):
        return codigo.isdigit() 

    @staticmethod
    def validar_descricao(descricao):
        return len(descricao.strip()) > 2

    @staticmethod
    def validar_fabricante(fabricante):
        return len(fabricante.strip()) > 2

    @staticmethod
    def validar_preco(preco):
        try:
            return float(preco) > 0
        except ValueError:
            return False
