from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__ (self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes (cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação"} {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media).ljust(25)} {restaurante._ativo}')

    @property
    def ativo (self):
        return '⌧' if self.ativo else '☐'
    
    def ativar_restaurante(self):
        self._ativo = not self.ativo
        nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado :")
        restaurante_encontrado = False

    def receber_avaliação (self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self.avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao (self):
        if not self._avaliacao:
            return 0 
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media