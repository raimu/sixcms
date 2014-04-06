
class Objects(object):

    def create(self, **kwargs):
        pass

    def get(self, **kwargs):
        o = Model()
        o.first_name = "Donald"
        return o


class Model(object):

    objects = Objects()

    def save(self):
        pass


class CharField(object):

    def __init__(self, **kwargs):
        pass
