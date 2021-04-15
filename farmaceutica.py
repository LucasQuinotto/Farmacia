from datetime import datetime


class Farmaceutica:

    def receber_receita(self, receita: dict):
        self.receita = receita

    def validar_receita(self, documento: dict):
        if datetime.strptime(self.receita["validade"], "%d/%m/%y") >= datetime.today() and self.receita["cpf"] == documento["cpf"]:
            return True
        else:
            return False

    def verificar_estoque(self):
        with open("estoque.txt", "r", encoding="utf-8") as file:
            self.estoque_medicamento = file.readlines()

        for i in range(len(self.estoque_medicamento)):
            linha_estoque = self.estoque_medicamento[i].strip().split(";")
            if linha_estoque[0] == self.receita["medicamento"] and int(linha_estoque[1]) >= int(self.receita["quantidade"]):
                return True
        return False


    def entregar_medicamento(self):
        return print("Aqui está o seu medicamento !!  Tenha um bom dia !!")


    def retirar_estoque(self):
        with open("estoque.txt", "w", encoding="utf-8") as file:
            for i in range(len(self.estoque_medicamento)):
                linha_estoque = self.estoque_medicamento[i].strip().split(";")
                if linha_estoque[0] == self.receita["medicamento"]:
                    novo_estoque_medicamento = int(linha_estoque[1]) - int(self.receita["quantidade"])
                    linha_estoque[1] = str(novo_estoque_medicamento) + "\n"
                    self.estoque_medicamento[i] = ";".join(linha_estoque)
            file.write("".join(self.estoque_medicamento))