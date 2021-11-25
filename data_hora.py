from datetime import datetime

class DataHora:
    def __init__(self, dia=1, mes=1, ano=1, hora=0, minuto=0,var=""):
        self.__dia = int(dia)
        self.__mes = int(mes)
        self.__ano = int(ano)
        self.__hora = int(hora)
        self.__minuto = int(minuto)
        self.__formatedData = var
        self.__formatedHora = var

## Códigos das Datas

    def set_data(self):
        self.formatedData = datetime(self.__ano, self.__mes, self.__dia).strftime("%d-%m-%Y")
        
    @property
    def formatedData(self):
        return self.__formatedData

    @formatedData.setter
    def formatedData(self, valor):
        self.__formatedData = valor

## Códigos das Horas

    def set_hora(self):
        formatado = self.set_time()
        self.formatedHora = formatado.strftime("%H:%M")

    def set_time(self):
        time_obj = datetime(self.__dia, self.__mes, self.__ano, self.__hora, self.__minuto)
        return time_obj
        
    @property
    def formatedHora(self):
        return self.__formatedHora
    
    @formatedHora.setter
    def formatedHora(self, valor):
        self.__formatedHora = valor
    
    def diff_tempo(self, hora):
        diff = self.set_time() - hora.set_time()
        return diff
