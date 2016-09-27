# -*- coding: utf-8 -*-
import unittest
import datetime

from pyboleto.bank.sicoob import BoletoSicoob

from .testutils import BoletoTestCase


class TestBancoSicoob(BoletoTestCase):
    def setUp(self):
        self.dados = []
        d = BoletoSicoob()
        d.carteira = '1'
        d.agencia_cedente = '3069'
        d.conta_cedente = '84725'
        d.codigo_beneficiario = '225'
        d.data_vencimento = datetime.date(2016, 05, 6)
        d.data_documento = datetime.date(2016, 04, 8)
        d.data_processamento = datetime.date(2016, 04, 8)
        d.valor_documento = 97.50
        d.nosso_numero = '3'
        d.numero_documento = '1212/1'
        self.dados.append(d)

    @unittest.skip("Não Implementado")
    def test_linha_digitavel(self):
        self.assertEqual(
            self.dados[0].linha_digitavel,
            '75693.30694 03000.022503 00000.350017 3 67860000009750'
        )

    def test_agencia(self):
        self.assertEqual(self.dados[0].agencia_cedente, '3069')

    def test_conta(self):
        self.assertEqual(self.dados[0].conta_cedente, '84725'.zfill(6))

    def test_dv_nosso_numero(self):
        self.assertEqual(self.dados[0].dv_nosso_numero, 5)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBancoSicoob)

if __name__ == '__main__':
    unittest.main()
