# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoItau(BoletoData):
    '''Implementa Boleto Itaú

        Gera Dados necessários para criação de boleto para o banco Itau
        Todas as carteiras com excessão das que utilizam 15 dígitos: (106,107,
        195,196,198)
    '''

    # Nosso numero (sem dv) com 8 digitos
    nosso_numero = CustomProperty('nosso_numero', 8)
    # Conta (sem dv) com 5 digitos
    conta_cedente = CustomProperty('conta_cedente', 5)
    #  Agência (sem dv) com 4 digitos
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    carteira = CustomProperty('carteira', 3)

    def __init__(self):
        super(BoletoItau, self).__init__()

        self.codigo_banco = "341"
        self.logo_image = "logo_itau.jpg"
        self.especie_documento = 'DM'
        self.local_pagamento = 'Até o vencimento, preferencialmente no Itaú. ' +\
                'Após o vencimento, somente no Itaú '

    @property
    def dv_nosso_numero(self):
        composto = "%4s%5s%3s%8s" % (self.agencia_cedente, self.conta_cedente,
                                     self.carteira, self.nosso_numero)
        return self.modulo10(composto)

    @property
    def dv_agencia_conta_cedente(self):
        agencia_conta = "%s%s" % (self.agencia_cedente, self.conta_cedente)
        return self.modulo10(agencia_conta)

    @property
    def agencia_conta_cedente(self):
        return "%s/%s-%s" % (self.agencia_cedente, self.conta_cedente,
                             self.conta_cedente_dv)

    def format_nosso_numero(self):
        return "%3s/%8s-%1s" % (self.carteira, self.nosso_numero,
                                self.dv_nosso_numero)

    @property
    def campo_livre(self):
        content = "%3s%8s%1s%4s%5s%1s%3s" % (self.carteira,
                                             self.nosso_numero,
                                             self.dv_nosso_numero,
                                             self.agencia_cedente,
                                             self.conta_cedente,
                                             self.conta_cedente_dv,
                                             '000'
                                             )
        return content
