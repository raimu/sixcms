#!/usr/bin/env python
#coding:utf-8

import unittest
import mock
from sixcms.api import Connection


class TestCase(unittest.TestCase):

    def setUp(self):
        wsdlsource = 'http://example.com/sixcms/soap.php?wsdl'
        server = mock.Mock()
        self.six = Connection(wsdlsource, 'user', 'password', server=server)
        server.assert_called_once_with(wsdlsource)
        self.server = server.return_value

    def test_hello(self):
        return_value = self.six.hello('world')
        self.server.CMSSOAP_Hello.assert_called_once_with(string='world')
        self.assertEqual(self.server.CMSSOAP_Hello.return_value, return_value)

    def test_info(self):
        return_value = self.six.info()
        self.server.CMSSOAP_Info.assert_called_once_with(
            user='user',
            passwd='password'
        )
        self.assertEqual(self.server.CMSSOAP_Info.return_value, return_value)

    def test_record_get(self):
        return_value = self.six.record_get({'title': 'hallo'})
        self.server.CMSSOAP_RecordGet.assert_called_once_with(
            user='user',
            passwd='password',
            data={'title': 'hallo'},
            options={'mode': 'get', 'return': 'all'}
        )
        self.assertEqual(self.server.CMSSOAP_RecordGet.return_value,
                         return_value)

    def test_record_save(self):
        return_value = self.six.record_save({'foo': 'bar'}, mode='insert')
        self.server.CMSSOAP_RecordSave.assert_called_once_with(
            user='user',
            passwd='password',
            data={'foo': 'bar'},
            options={'mode': 'insert'}
        )
        self.assertEqual(self.server.CMSSOAP_RecordSave.return_value,
                         return_value)


if __name__ == '__main__':
    unittest.main()
