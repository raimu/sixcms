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
        data = self.server.CMSSOAP_RecordGet(user=self.username,
                                             passwd=self.password,
                                             data=data,
                                             options=kwargs)
        return self._to_python(data)

    def record_save(self, data, **kwargs):
        return self.server.CMSSOAP_RecordSave(user=self.username,
                                              passwd=self.password,
                                              data=data,
                                              options=kwargs)

    def _to_python(self, data):
        if hasattr(data, 'item'):
            record = {}
            for item in data.item:
                for i in self._to_python(item):
                    if isinstance(i, dict):
                        yield i
                    else:
                        record[i.key] = i.value
            if record:
                yield record
        elif hasattr(data, 'value'):
            if isinstance(data.value, str) or isinstance(data.value, unicode):
                yield data
            else:
                for row in data.value:
                    new_row = {}
                    for key, value in row:
                        if isinstance(value, str) or isinstance(value, unicode):
                            new_row[key] = value
                        else:
                            new_row[key] = [i for i in self._to_python(value)]
                    yield new_row
        elif len(data) == 0:
            yield {}
        elif isinstance(data, str) and data.startswith('id-'):
            pass
        else:
            raise KeyError("cannot convert structure to python")