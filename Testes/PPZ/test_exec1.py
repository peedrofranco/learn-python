# 1) Faça um programa que peça
# dois números inteiros e imprima a soma desses dois números

import unittest
from Exercicios.PPZ.exec01 import SomarNumeros

class_somar = SomarNumeros()


def test_sum_two_numbers():
    assert class_somar.somar(10, 20) == 30
