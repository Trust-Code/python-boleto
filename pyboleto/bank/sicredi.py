# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoSicredi(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o Banco Sicredi
    '''
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 5)
    posto = CustomProperty('posto', 2)
    carteira = CustomProperty('carteira', 1)
    # Nosso numero (sem dv) com 8 digitos
    # AA/BXXXXX-DV 
    # Pag. 6 manual cnab 400
    nosso_numero = CustomProperty('nosso_numero', 8)

    def __init__(self):
        '''
            Construtor para boleto do Banco Sicredi

            Args:
                format_convenio Formato do convenio 6, 7 ou 8
                format_nnumero Formato nosso numero 1 ou 2
        '''
        super(BoletoSicredi, self).__init__()

        self.codigo_banco = "748"
        self.local_pagamento = u'Pagável prefencialmente nas Coop. de Crédito Sicredi'
        self.logo_image = "logo_sicredi.png"

    def format_ano(self):
        ano = str(self.data_vencimento.strftime('%y'))
        ano = ano.zfill(2)
        return ano

    @property
    def dv_nosso_numero(self):
        composto = "%s%s%s%s" % (self.agencia_cedente, self.posto, self.conta_cedente,
                                     self.nosso_numero)
        composto = self.modulo11(composto)
        return composto

    def format_nosso_numero(self):
        return "%s/%s-%s" % (self.nosso_numero[:2], self.nosso_numero[2:],
                                self.dv_nosso_numero)
    @property
    def campo_livre(self):
        content = "1%s%s%s%s%s%s%s" % (self.carteira,
                                             self.nosso_numero,
                                             self.dv_nosso_numero,
                                             self.agencia_cedente,
                                             self.posto,
                                             self.conta_cedente,
                                             '10'
                                             )
        content += str(self.modulo11(content))
        return content

