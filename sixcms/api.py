#!/usr/bin/env python
#coding:utf-8

from SOAPpy.WSDL import Proxy


class Connection(object):

    def __init__(self, wsdlsource, username, password, server=Proxy):
        self.server = server(wsdlsource)
        self.username = username
        self.password = password

    def hello(self, string):
        return self.server.CMSSOAP_Hello(string=string)

    def info(self):
        return self.server.CMSSOAP_Info(user=self.username,
                                        passwd=self.password)

    def record_get(self, data, mode='get', return_='all', **kwargs):
        kwargs['mode'] = mode
        kwargs['return'] = return_
        return self.server.CMSSOAP_RecordGet(user=self.username,
                                             passwd=self.password,
                                             data=data,
                                             options=kwargs)

    def record_save(self, data, **kwargs):
        return self.server.CMSSOAP_RecordSave(user=self.username,
                                              passwd=self.password,
                                              data=data,
                                              options=kwargs)
