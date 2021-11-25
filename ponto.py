from datetime import timedelta
from data_hora import DataHora

class Ponto:
    def __init__(self, data, entrada, saida_almoco, entrada_almoço, saida):
        self.__data = data
        self.__entrada = entrada
        self.__saida_almoco = saida_almoco
        self.__entrada_almoco = entrada_almoço
        self.__saida = saida
        self.__total_almoco = self.__calc_almoco()
        self.__total_dia = self.__calc_total()
        self.__extra = self.__calc_extra()

## Properties
    @property
    def data(self):
        return self.__data

    @property
    def entrada(self):
        return self.__entrada

    @property
    def entrada_almoco(self):
        return self.__entrada_almoco

    @property
    def saida(self):
        return self.__saida

    @property
    def saida_almoco(self):
        return self.__saida_almoco

    @property
    def total_dia(self):
        return self.__total_dia

    @property
    def total_almoco(self):
        return self.__total_almoco

    @property
    def extra(self):
        return self.__extra

## Methods
    def formatado(self):
        txt = "{} - {} - {} - {} - {} - {} - {}".format(self.data.formatedData, self.entrada.formatedHora, self.saida_almoco.formatedHora, self.entrada_almoco.formatedHora, self.saida.formatedHora, self.__calc_almoco(), self.__calc_total())
        return txt
    
    def __calc_almoco(self):
        almoco = self.entrada_almoco.diff_tempo(self.saida_almoco)
        self.__total_almoco = almoco
        return self.total_almoco
    
    def __calc_total(self):
        total = self.saida.diff_tempo(self.entrada) - self.total_almoco
        self.__total_dia = total
        return self.total_dia

    def __calc_extra(self):
        extra = self.total_dia - timedelta(hours=8, minutes=48)
        self.__extra = extra
        return self.extra

    def cria_dict(self, key1, key2, key3, key4):
        dicio = {}
        dicio[self.data.formatedData]={}
        dicio[self.data.formatedData][key1] = self.entrada.formatedHora
        dicio[self.data.formatedData][key2] = self.saida_almoco.formatedHora
        dicio[self.data.formatedData][key3] = self.entrada_almoco.formatedHora
        dicio[self.data.formatedData][key4] = self.saida.formatedHora
        return dicio


