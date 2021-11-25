from ponto import Ponto
from data_hora import DataHora
import file_manipulation as f

def set_data():
    print("###  Primeiro informe a data do registro ###")
    dia = input("Dia: ")
    mes = input("Mês: ")
    ano = input("Ano: ")

    data = DataHora(dia=dia, mes=mes, ano=ano)
    data.set_data()
    return data

def set_horas(key):
    print("### Agora informe os horários ###")
    horario = {}
    for i in key:
        print(i.capitalize())
        hora = input("Hora: ")
        minuto = input("Minuto: ")
        print("---")
        hora_i = DataHora(hora=hora, minuto=minuto)
        hora_i.set_hora()
        horario[i] = hora_i
    return horario

def registro_ponto():
    keys = ("entrada", "saida_almoco", "entrada_almoco", "saida")
    data = set_data()
    horas = set_horas(keys)
    ponto = Ponto(data, horas[keys[0]], horas[keys[1]], horas[keys[2]], horas[keys[3]])
    dicio = ponto.cria_dict(keys[0], keys[1], keys[2], keys[3])
    return dicio

def initialize():
    f.createFile()
    jsondb = f.readJsonFile()
    pontoDict = registro_ponto()
    pontoJson = f.createJson(jsondb, pontoDict)
    f.saveJsonFile(pontoJson)


if __name__ == "__main__":
    initialize()
