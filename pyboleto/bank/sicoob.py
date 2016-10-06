# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoSicoob(BoletoData):
    '''Implementa Boleto Sicoob

        Gera Dados necessários para criação de boleto para o banco Sicoob
    '''

    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 6)
    codigo_beneficiario = CustomProperty('codigo_beneficiario', 7)
    nosso_numero = CustomProperty('nosso_numero', 7)

    carteira = CustomProperty('carteira', 1)

    def __init__(self):
        super(BoletoSicoob, self).__init__()

        self.codigo_banco = "756"
        self.logo_image = "logo_sicoob.jpg"
        self.especie_documento = 'DM'
        self.label_cedente = 'Coop Contr/Cód Beneficiário'
        self.local_pagamento = 'Pagável Preferencialmente nas Cooperativas ' +\
            'da Rede Sicoob ou Qualquer Banco até o Vencimento.'

    @property
    def modalidade(self):
        return '01' if self.carteira == '1' else '03'

    @property
    def dv_nosso_numero(self):
        composto = "%4s%10s%7s" % (self.agencia_cedente,
                                   self.codigo_beneficiario.zfill(10),
                                   self.nosso_numero)
        constante = '319731973197319731973'
        soma = 0
        for i in range(21):
            soma += int(composto[i]) * int(constante[i])
        resto = soma % 11
        return '0' if (resto == 1 or resto == 0) else 11 - resto

    @property
    def agencia_conta_cedente(self):
        return "%s/%s" % (self.agencia_cedente, self.codigo_beneficiario)

    def format_nosso_numero(self):
        return "%8s-%1s" % (self.nosso_numero,
                            self.dv_nosso_numero)

    @property
    def codigo_dv_banco(self):
        return self.codigo_banco

    @property
    def campo_livre(self):
        content = "%1s%4s%2s%7s%7s%1s%3s" % (self.carteira,
                                             self.agencia_cedente.strip(),
                                             self.modalidade,
                                             self.codigo_beneficiario,
                                             self.nosso_numero[:7],
                                             self.dv_nosso_numero,
                                             '001')
        return content
