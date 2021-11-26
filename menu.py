import json
import os
from ponto import Ponto
from data_hora import DataHora
import file_manipulation as f

class Menu():
    def __init__(self) -> None:
        self.__exist = True

    def direcionamento(self, opcao, db):
        clear_console()
        if opcao == "1":
            self.one(db)
            return
        if opcao == "2":
            self.two(opcao, db)
            return
        if opcao == "3":
            self.three(opcao)
            return
        if opcao == "0":
            self.__exist = False
            return
        if opcao == "":
            print("Escolha novamente!")
        else:
            print("[WARNING] - Essa opção não é existe. Escolha outra.\n")

    def run(self):
        while self.__exist:
            jsondb = f.readJsonFile()
            opcao = cabecalho()
            self.direcionamento(opcao, jsondb)
    
    def one(self, db):
        item = opcao_registro()
        if item == None:
            return
        ponto = registro_ponto(item)
        pontoJson = f.createJson(db, ponto)
        f.saveJsonFile(pontoJson)
        clear_console()

    def two(self, opcao):
        print("Você escolheu a opção {}.\n".format(opcao))

    def three(self, opcao):
        print("Você escolheu a opção {}.\n".format(opcao))

def clear_console():
    command = "clear"
    if os.name in ('nt', 'dos'):
        command = "cls"
    os.system(command)

def cabecalho():
    print("###")
    print('Seja bem vindo ao controle de pontos')
    print("###")
    print("1 - Registrar Hora")
    print("2 - Verificar os pontos")
    print("3 - Corrigir uma marcação")
    print("0 - Sair")
    print("###")
    opcao = input("Escolha uma opção: ")
    return(opcao)

def opcao_registro():
    print("###")
    print("1 - Entrada")
    print("2 - Saída Almoço")
    print("3 - Entrada Almoço")
    print("4 - Saída")
    print("0 - Sair")
    print("###")
    try:
        item = int(input("Qual você deseja registrar: "))
    except:
        clear_console()
        print("[WARNING] - Essa opção não é existe. Cancelando... \n")
        return
    else:
        if item - 1 in range(4):
            clear_console()
            return item - 1
        else:
            clear_console()
            print("Saindo... \n")
            return

def set_data():
    print("###  Primeiro informe a data do registro ###")
    dia = input("Dia: ")
    mes = input("Mês: ")
    ano = input("Ano: ")

    data = DataHora(dia=dia, mes=mes, ano=ano)
    data.set_data()
    return data

def set_horas(key):
    print("### Informe o horário ###")
    horario = {}
    print(key.capitalize())
    hora = input("Hora: ")
    minuto = input("Minuto: ")
    print("---")
    hora_i = DataHora(hora=hora, minuto=minuto)
    hora_i.set_hora()
    horario[key] = hora_i
    return horario

def registro_ponto(item):
    keys = ("entrada", "saida_almoco", "entrada_almoco", "saida")
    data = set_data()
    hora = set_horas(keys[item])
    if item == 0:
        ponto = Ponto(data, entrada=hora[keys[item]])
    if item == 1:
        ponto = Ponto(data, saida_almoco=hora[keys[item]])
    if item == 2:
        ponto = Ponto(data, entrada_almoco=hora[keys[item]])
    if item == 3:
        ponto = Ponto(data, saida=hora[keys[item]]) 
    dicio = ponto.cria_dict(keys, item)
    return dicio