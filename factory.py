from .dccMaya import Maya
from .dccHoudini import Houdini
from .dccMayaPython import dccMayaPython
from .dccNuke import Nuke

class Factory:

    def __init__(self):
        self.__factory = {
            'maya': Maya,
            'houdini': Houdini,
            'nuke': Nuke,
            'python': dccMayaPython
        }

    def GetInstance(self, name):
        if ('happrentice' in name) or ('houdini' in name) :
            name = 'houdini'
        if ('Nuke' in name) or ('nuke' in name) :
            name = 'nuke'
        return self.__factory.get(name, None)