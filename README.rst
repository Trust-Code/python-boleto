========
python-boleto - Fork mantido por Trustcode
========

.. image:: https://travis-ci.org/Trust-Code/python-boleto.svg?branch=master3
    :target: https://travis-ci.org/Trust-Code/python-boleto

.. image:: https://coveralls.io/repos/github/Trust-Code/python-boleto/badge.svg?branch=master3
    :target: https://coveralls.io/github/Trust-Code/python-boleto?branch=master3

.. image:: https://landscape.io/github/Trust-Code/python-boleto/master3/landscape.svg?style=flat
   :target: https://landscape.io/github/Trust-Code/python-boleto/master3
   :alt: Code Health

.. image:: https://badge.fury.io/py/python3-boleto.svg
  :target: https://badge.fury.io/py/python3-boleto


.. _pyboleto-synopsis:

python-boleto é um projeto python para gerar boletos de cobrança.

O projeto original pode ser encontrado aqui:
https://github.com/eduardocereto/pyboleto


.. contents::
    :local:

.. _pyboleto-implemented-bank:

Bancos implementados
=================

Você pode ajudar criando códigos para mais bancos ou imprimir e testar as implementações já existentes.

Por enquanto, são essas que temos.

 +----------------------+----------------+-----------------+------------+
 | **Banco**            | **Carteira /** | **Implementado**| **Testado**|
 |                      | **Convenio**   |                 |            |
 +======================+================+=================+============+
 | **Banco do Brasil**  | 18             | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Banrisul**         | x              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Bradesco**         | 06, 03         | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Caixa Economica**  | SR             | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **HSBC**             | CNR, CSB       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 157            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 175, 174, 178, | Yes             | No         |
 |                      | 104, 109       |                 |            |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 102            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 101, 201       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Sicoob**           | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Sicredi**          | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Cecred**           | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+

.. _pyboleto-docs:

Documentation
=============


.. _pyboleto-installation:

Installation
============

Você pode instalar o pyboleto através do Python Package Index (PyPI)
ou instalando diretamente da fonte.

Para instalar usando o pip,::

    $ pip3 install python3-boleto


.. _pyboleto-installing-from-source:

Baixando e instalando da fonte
--------------------------------------

Baixe a última versão do pyboleto em
http://pypi.python.org/pypi/python-boleto/

Você pode instalar utilizando os seguintes passos,::

    $ tar xvfz python-boleto-0.0.0.tar.gz
    $ cd python-boleto-0.0.0
    $ python setup.py build
    # python setup.py install # as root

.. _pyboleto-installing-from-hg:

Utilizando a versão de desenvolvimento
-----------------------------

Você pode clonar o repositório usando o seguinte comando::

    $ git clone https://github.com/Trust-Code/python-boleto.git

.. _pyboleto-unittests:

Executando unittests
===================
Você irá precisar do setuptools ou do distribute para executar os testes. Provavelmente já deve ter instalado um ou o outro. Irá precisar também do `pdftohtml`_.::

    $ cd pyboleto
    $ python setup.py test


.. _pdftohtml: http://poppler.freedesktop.org/

.. _pyboleto-license:

License
=======

Este software é licenciado sob a `New BSD License`. Veja o arquivo 
``LICENSE`` na raiz do projeto para ler o texto completo.
.. vim:tw=0:sw=4:et
