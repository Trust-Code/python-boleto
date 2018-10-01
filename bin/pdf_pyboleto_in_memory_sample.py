import pyboleto
from pyboleto.bank.sicredi import BoletoSicredi
from pyboleto.pdf import BoletoPDF
import datetime

d = BoletoSicredi()
d.aceite = 'Sim'
d.especie_documento = 'DI'
d.carteira = '1'
d.posto = '08'

d.cedente = 'Empresa ACME LTDA'
d.cedente_documento = "102.323.777-01"
d.cedente_endereco = ("Rua Acme, 123 - " +
                      "Centro - Sao Paulo/SP - " +
                      "CEP: 12345-678")
d.agencia_cedente = '9999'
d.conta_cedente = '99999'

# buscar dados do wk
d.data_vencimento = datetime.date(2018, 1, 25)
d.data_documento = datetime.date(2017, 11, 24)
d.data_processamento = datetime.date(2017, 11, 24)
d.valor_documento = 90.75
d.nosso_numero = '18324121'
d.numero_documento = '33287-1/12'

d.instrucoes = [
    "- Linha 1",
    "- Sr Caixa, cobrar multa de 2% apos o vencimento",
    "- Receber ate 10 dias apos o vencimento",
    ]

d.demonstrativo = [
    "- Servico Teste R$ 5,00",
    "- Total R$ 5,00",
    ]

d.valor_documento = 255.00

d.sacado = [
    "Cliente Teste",
    "Rua Desconhecida, 00/0000 - Nao Sei - Cidade - Cep. 00000-000",
    ""
    ]

import io
buf = io.BytesIO()

boleto = BoletoPDF(buf)
boleto.drawBoleto(d)
boleto.nextPage()
boleto.save()

pdf_buffer = buf.getbuffer()
file = open("boleto_buffer.pdf", "wb")
file.write(pdf_buffer)

