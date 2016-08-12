# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoCecred(BoletoData):
    '''Implementa Boleto Cecred

        Gera Dados necessários para criação de boleto para o banco Cecred
    '''

    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 6)
    codigo_beneficiario = CustomProperty('codigo_beneficiario', 7)
    nosso_numero = CustomProperty('nosso_numero', 7)

    carteira = CustomProperty('carteira', 1)

    def __init__(self):
        super(BoletoCecred, self).__init__()

        self.codigo_banco = "756"
        self.logo_image = "logo_cecred.jpg"
        self.especie_documento = 'DM'
        self.label_cedente = 'Coop Contr/Cód Beneficiário'
        self.local_pagamento = 'Pagável Preferencialmente nas Cooperativas ' +\
            'da Rede Sicoob ou Qualquer Banco até o Vencimento.'
