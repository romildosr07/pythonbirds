"""
Você deve criar uma classe Carro que vai possuir dois atributos compostos por outras duas classes: 1 Motor, 2 Direcao
o motor terar a responsabilidade de controlar a velocidade ele oferece os seguintes atributos: 1 atributo de dado
velocidade, 2 metodo acelerar que deverar incrementar a velocidade em uma unidade, 3 metodo frear que deverar
decrementar a velocidade em duas unidades
a direção terar a responsabilidade de  controlar a direçao ela oferece os sequintes atributos: 1 valore de direçao com
valores possiveis: Norte, Sul, Leste, Oeste, 2 metodo girar a direita,  metodo girar a esquerda

  N
O   l
  s
Exemplo:
>>> # testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # testando direcao
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_direita()
>>> carro.calcular_direcao()
'Leste'
>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_direita(self):
        return self.direcao.girar_a_direita()

    def girar_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.valor


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE
    }
    rotacao_a_esquerda = {
        NORTE: OESTE,
        OESTE: SUL,
        SUL: LESTE,
        LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
