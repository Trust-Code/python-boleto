# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoCaixa(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal

    '''
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 6)
    codigo_beneficiario = CustomProperty('codigo_beneficiario', 6)
    '''
        Este numero tem o inicio fixo
        Carteira SR: 80, 81 ou 82
        Carteira CR: 90 (Confirmar com gerente qual usar)

    '''
    nosso_numero = CustomProperty('nosso_numero', 10)

    def __init__(self):
        super(BoletoCaixa, self).__init__()

        self.codigo_banco = "104"
        self.local_pagamento = "Preferencialmente nas Casas Lotéricas e \
Agências da Caixa"
        self.logo_image = "logo_bancocaixa.jpg"

    @property
    def agencia_conta_cedente(self):
        return "%s/%s-%s" % (self.agencia_cedente, self.codigo_beneficiario,
                             self.modulo11(self.codigo_beneficiario))

    @property
    def dv_nosso_numero(self):
        numero = "%1s4%15s" % (self.carteira, self.nosso_numero.zfill(15))
        return self.modulo11(numero)

    @property
    def campo_livre(self):
        nosso_numero_completo = self.format_nosso_numero()
        content = "%6s%1s%3s%1s%3s%1s%9s" % (
            self.codigo_beneficiario,
            self.modulo11(self.codigo_beneficiario),
            nosso_numero_completo[2:5],
            self.carteira,
            nosso_numero_completo[5:8],
            '4',  # Beneficiário emite,
            nosso_numero_completo[8:17],
            )
        return "%s%s" % (content, self.modulo11(content))

    def format_nosso_numero(self):
        content = "%1s4%15s-%1s" % (
            self.carteira,
            self.nosso_numero.zfill(15),
            self.dv_nosso_numero,
        )
        return content
