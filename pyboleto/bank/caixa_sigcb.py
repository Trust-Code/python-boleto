# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoCaixaSigcb(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal
    '''

    agencia_cedente = CustomProperty('agencia_cedente', 4)
    convenio = CustomProperty('convenio', 6)
    nosso_numero = CustomProperty('nosso_numero', 17)

    def __init__(self):
        super(BoletoCaixaSigcb, self).__init__()

        self.codigo_banco = "104"
        self.local_pagamento = ("Preferencialmente nas Casas Lotéricas e "
                                "Agências da Caixa")
        self.logo_image = "logo_bancocaixa.jpg"

    @property
    def campo_livre(self):  # 24 digits
        content = "%6s%1s%3s%1s%3s%1s%9s" % (
            self.convenio.split('-')[0],
            self.modulo11(self.convenio.split('-')[0]),
            self.nosso_numero[2:5],
            self.nosso_numero[0:1],
            self.nosso_numero[5:8],
            self.nosso_numero[1:2],
            self.nosso_numero[8:17]
        )
        dv_content = self.modulo11(content)

        return "%24s%1s" % (content, dv_content)

    def format_nosso_numero(self):
        return self.nosso_numero
