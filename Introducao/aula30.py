"""
CONSTANTE = "Variáveis que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidaded (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60   # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')