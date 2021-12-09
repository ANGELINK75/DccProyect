from .maya import Maya
from .houdini import Houdini

class Factory:

    def __init__(self):
        self.__factory = {
            'maya': Maya,
            'houdini': Houdini,
            'nuke': None
        }

    def GetInstance(self, name):
        if 'houdini' in name:
            name = 'houdini'
        return self.__factory.get(name, None)