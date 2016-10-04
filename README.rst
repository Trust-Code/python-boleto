========
python-boleto - Fork mantido por Trustcode
========

.. image:: https://travis-ci.org/Trust-Code/python-boleto.svg?branch=master
    :target: https://travis-ci.org/Trust-Code/python-boleto

.. image:: https://coveralls.io/repos/github/Trust-Code/python-boleto/badge.svg?branch=master
    :target: https://coveralls.io/github/Trust-Code/python-boleto?branch=master

.. image:: https://landscape.io/github/Trust-Code/python-boleto/master/landscape.svg?style=flat
   :target: https://landscape.io/github/Trust-Code/python-boleto/master
   :alt: Code Health


.. _pyboleto-synopsis:

python-boleto é um projeto python para gerar boletos de cobrança.

O projeto original pode ser encontrado aqui:
https://github.com/eduardocereto/pyboleto


.. contents::
    :local:

.. _pyboleto-implemented-bank:

Bancos implementados
=================

You can help writing code for more banks or printing and testing current
implementations.

For now here's where we are.

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
 | **Cecred**           | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+

.. _pyboleto-docs:

Documentation
=============


.. _pyboleto-installation:

Installation
============

You can install pyboleto either via the Python Package Index (PyPI)
or from source.

To install using pip,::

    $ pip install python-boleto


.. _pyboleto-installing-from-source:

Downloading and installing from source
--------------------------------------

Download the latest version of pyboleto from
http://pypi.python.org/pypi/python-boleto/

You can install it by doing the following,::

    $ tar xvfz python-boleto-0.0.0.tar.gz
    $ cd python-boleto-0.0.0
    $ python setup.py build
    # python setup.py install # as root

.. _pyboleto-installing-from-hg:

Using the development version
-----------------------------

You can clone the repository by doing the following::

    $ git clone https://github.com/Trust-Code/python-boleto.git

.. _pyboleto-unittests:

Executing unittests
===================

You need either setuptools or distribute in order to execute the tests. Chances are you already have one or another. You also need `pdftohtml`_.::

    $ cd pyboleto
    $ python setup.py test


.. _pdftohtml: http://poppler.freedesktop.org/

.. _pyboleto-license:

License
=======

This software is licensed under the `New BSD License`. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. vim:tw=0:sw=4:et
