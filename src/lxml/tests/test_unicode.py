# -*- coding: UTF-8 -*-
import unittest, doctest

from StringIO import StringIO
from lxml import etree

ascii_uni = u'a'

uni = u'á'

class UnicodeTestCase(unittest.TestCase):
    def test_unicode_xml(self):
        tree = etree.XML(u'<p>%s</p>' % uni)
        self.assertEquals(uni, tree.text)

    def test_unicode_tag(self):
        el = etree.Element(uni)
        self.assertEquals(uni, el.tag)

    def test_unicode_attr(self):
        el = etree.Element('foo', {'bar': uni})
        self.assertEquals(uni, el.attrib['bar'])

    def test_unicode_comment(self):
        el = etree.Comment(uni)
        self.assertEquals(' %s ' % uni, el.text)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(UnicodeTestCase)])
    return suite
