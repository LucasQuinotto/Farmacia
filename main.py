from farmaceutica import Farmaceutica
from paciente import Paciente


def executar():
    paciente_teste = Paciente(dict(medicamento="Remédio pra dor", quantidade="1", validade="18/04/21", cpf="01234"),
                              dict(nome="Maria", cpf="01234"))

    farmaceutica_teste = Farmaceutica()
    farmaceutica_teste.receber_receita(paciente_teste.receita)

    if farmaceutica_teste.validar_receita(paciente_teste.documento):
        print("Sua receita foi validada, checando o estoque ...")
        if farmaceutica_teste.verificar_estoque():
            farmaceutica_teste.retirar_estoque()
            farmaceutica_teste.entregar_medicamento()
        else:
            print("Infelizmente não há estoque de medicamento o suficiente para a sua receita ...")
    else:
        print("Sua receita foi invalidada ...")

executar()