# -*- coding: utf-8 -*-
from __future__ import with_statement

import difflib
import fnmatch
import os
import re
import subprocess
import tempfile
import unittest

from xml.etree.ElementTree import fromstring, tostring

import pyboleto
from pyboleto.pdf import BoletoPDF
from pyboleto.html import BoletoHTML


def list_recursively(directory, pattern):
    """Returns files recursively from directory matching pattern
    :param directory: directory to list
    :param pattern: glob mattern to match
    """
    matches = []
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            # skip backup files
            if (filename.startswith('.#') or
                    filename.endswith('~')):
                continue
            matches.append(os.path.join(root, filename))
    return matches


def get_sources(root):
    for dirpath in ['pyboleto', 'tests']:
        path = os.path.join(root, dirpath)
        for fname in list_recursively(path, '*.py'):
            if fname.endswith('__init__.py'):
                continue
            yield fname

        # yield os.path.join(root, 'setup.py')


def _diff(orig, new, short, verbose):
    lines = difflib.unified_diff(orig, new)
    if not lines:
        return ''

    return ''.join('%s: %s' % (short, line) for line in lines)


def diff_files(orig, new, verbose=False):
    with open(orig) as f_orig:
        with open(new) as f_new:
            return _diff(f_orig.readlines(),
                         f_new.readlines(),
                         short=os.path.basename(orig),
                         verbose=verbose)


def diff_pdf_htmls(original_filename, filename):
    # REPLACE all generated dates with %%DATE%%
    for fname in [original_filename, filename]:
        with open(fname) as f:
            data = f.read()
            data = re.sub(r'name="date" content="(.*)"',
                          r'name="date" content="%%DATE%%"', data)
            data = re.sub(r'<pdf2xml[^>]+>', r'<pdf2xml>', data)
        with open(fname, 'w') as f:
            f.write(data)

    return diff_files(original_filename, filename)


class ClassInittableMetaType(type):
    # pylint fails to understand this is a metaclass
    def __init__(self, name, bases, namespace):
        type.__init__(self, name, bases, namespace)
        self.__class_init__(namespace)


class SourceTest(object):
    __metaclass__ = ClassInittableMetaType

    @classmethod
    def __class_init__(cls, namespace):
        root = os.path.dirname(os.path.dirname(pyboleto.__file__))
        cls.root = root
        for filename in get_sources(root):
            testname = filename[len(root):]
            if not cls.filename_filter(testname):
                continue
            testname = testname[:-3].replace('/', '_')
            name = 'test_%s' % (testname, )
            # func = lambda self, r=root, f=filename: self.check_filename(r, f)

            def func(self, r=root, f=filename):
                self.check_filename(r, f)
            func.__name__ = name
            setattr(cls, name, func)

    def check_filename(self, root, filename):
        pass

    @classmethod
    def filename_filter(cls, filename):
        if cls.__name__ == 'SourceTest':
            return False
        else:
            return True


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def pdftoxml(filename, output):
    p = subprocess.Popen(['pdftohtml',
                          '-stdout',
                          '-xml',
                          '-noframes',
                          '-i',
                          '-q',
                          filename],
                         stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stderr:
        raise SystemExit("Error while runnig pdftohtml: %s" % (stderr, ))

    root = fromstring(stdout)
    indent(root)
    with open(output, 'wb') as f:
        f.write(tostring(root))


class BoletoTestCase(unittest.TestCase):
    def _get_expected(self, bank, generated, f_type='xml'):
        fname = os.path.join(
            os.path.dirname(pyboleto.__file__),
            "..", "tests", f_type, bank + '-expected.' + f_type)
        if not os.path.exists(fname):
            with open(fname, 'wb') as f:
                with open(generated) as g:
                    f.write(g.read())
        return fname

    def test_pdf_triplo_rendering(self):
        if "dados" not in dir(self):
            return
        bank = type(self.dados[0]).__name__
        filename = tempfile.mktemp(prefix="pyboleto-triplo-",
                                   suffix=".pdf")
        boleto = BoletoPDF(filename, True)
        for d in self.dados:
            boleto.drawBoleto(d)
            boleto.nextPage()
        boleto.save()

        generated = filename + '.xml'
        pdftoxml(filename, generated)
        expected = self._get_expected('Triplo-' + bank, generated)
        diff = diff_pdf_htmls(expected, generated)
        os.unlink(generated)

        os.unlink(filename)
        if diff:
            self.fail("Error while checking xml for %r:\n%s" % (
                bank, diff))

    def test_pdf_rendering(self):
        if "dados" not in dir(self):
            return
        dados = self.dados[0]
        bank = type(dados).__name__
        filename = tempfile.mktemp(prefix="pyboleto-",
                                   suffix=".pdf")
        boleto = BoletoPDF(filename, True)
        boleto.drawBoleto(dados)
        boleto.nextPage()
        boleto.save()

        generated = filename + '.xml'
        pdftoxml(filename, generated)
        expected = self._get_expected(bank, generated)
        diff = diff_pdf_htmls(expected, generated)
        os.unlink(generated)
        os.unlink(filename)
        if diff:
            self.fail("Error while checking xml for %r:\n%s" % (
                bank, diff))

    def test_html_rendering(self):
        if "dados" not in dir(self):
            return
        dados = self.dados[0]
        bank = type(dados).__name__
        filename = tempfile.mktemp(prefix="pyboleto-",
                                   suffix=".html")
        boleto = BoletoHTML(filename, False)
        boleto.drawBoleto(dados)
        boleto.nextPage()
        boleto.save()

        generated = filename
        expected = self._get_expected(bank, generated, f_type='html')
        diff = diff_files(expected, generated)
        os.unlink(generated)

        if diff:
            self.fail("Error while checking xml for %r:\n%s" % (
                bank, diff))
