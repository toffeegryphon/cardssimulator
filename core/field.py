from .holder import Holder

class Field(Holder):
    _type = 'field'
    def __init__(self):
        super(Holder, self).__init__()
