# -*- coding: utf-8 -*-
import unittest
import datetime

from pyboleto.bank.sicredi import BoletoSicredi

from .testutils import BoletoTestCase


class TestBancoSicredi(BoletoTestCase):
    def setUp(self):
        self.dados = []
        for i in range(3):
            d = BoletoSicredi()
            d.carteira = '1'
            d.posto = '08'
            d.aceite = 'Sim'
            d.especie_documento = 'DI'
            d.agencia_cedente = '0434'
            d.conta_cedente = '36699'
            d.data_vencimento = datetime.date(2018, 1, 25)
            d.data_documento = datetime.date(2017, 11, 24)
            d.data_processamento = datetime.date(2017, 11, 24)
            d.valor_documento = 90.75
            d.nosso_numero = '18324121'
            d.numero_documento = '33287-1/12'
            self.dados.append(d)

    def test_linha_digitavel(self):
        self.assertEqual(
            self.dados[0].linha_digitavel,
            '74891.11836 24121.904346 08366.991068 1 74150000009075'
        )

    def test_codigo_de_barras(self):
        self.assertEqual(
            self.dados[0].barcode,
            '74891741500000090751118324121904340836699106'
        )

    def test_agencia(self):
        self.assertEqual(self.dados[0].agencia_cedente, '0434')

    def test_conta(self):
        self.assertEqual(self.dados[0].conta_cedente, '36699')

    def test_dv_nosso_numero(self):
        self.assertEqual(self.dados[0].dv_nosso_numero, 9)


suite = unittest.TestLoader().loadTestsFromTestCase(TestBancoSicredi)

if __name__ == '__main__':
    unittest.main()
