import pprint


class DummyClass():
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    @staticmethod
    def dummy_staticmethod(arg):
        pass

    @classmethod
    def dummy_classmethod(cls, arg):
        pass

    def __repr__(self,
                 compact=True,
                 pprint_objs=[dict, list, tuple],
                 ):
        txt = f'{self.__class__.__name__}' + ('(' if compact else '(\n')
        txts = []
        for k, v in self.__dict__.items():
            if k.startswith('__'):
                continue
            elif type(v) in pprint_objs:
                vstr = pprint.pformat(v)
            elif type(v) == str:
                vstr = f"'{v}'"
            else:
                vstr = str(v)
            vstr = vstr[:-1] if vstr[-1] == '\n' else vstr
            txts += [f'{k}={vstr}']
        txt += ('; ' if compact else ';\n').join(txts)
        txt += ')' if compact else '\n)'
        return txt
