# -*- coding: utf-8 -*-
from ..data import BoletoException
BANCOS_IMPLEMENTADOS = {
    '001': 'bancodobrasil.BoletoBB',
    '041': 'banrisul.BoletoBanrisul',
    '237': 'bradesco.BoletoBradesco',
    '104': 'caixa.BoletoCaixa',
    '399': 'hsbc.BoletoHsbc',
    '341': 'itau.BoletoItau',
    '356': 'real.BoletoReal',
    '033': 'santander.BoletoSantander',
    '748': 'sicredi.BoletoSicredi',
    '756': 'sicoob.BoletoSicoob',
    '0851': 'cecred.BoletoCecred',
}


def get_class_for_codigo(banco_codigo):
    """Retorna a classe que implementa o banco

    :param banco_codigo:
    :type banco_codigo: string
    :return: Classo do Banco subclasse de :class:`pyboleto.data.BoletoData`
    :rtype: :class:`pyboleto.data.BoletoData`
    """
    try:
        banco = BANCOS_IMPLEMENTADOS[banco_codigo].split('.')
    except KeyError:
        raise BoletoException

    mod = __import__('pyboleto.bank.' + banco[0],
                     globals(), locals(), [banco[1]])

    return getattr(mod, banco[1])
