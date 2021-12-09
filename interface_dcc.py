
import abc

class InterfaceDcc(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def Create_Sphere(self):
        pass

    @abc.abstractmethod
    def Create_Cube(self):
        pass
    
    @abc.abstractmethod
    def Save_Scene(self):
        pass

    #@abc.abstractmethod
    #def Save_Metadata(self):
    #    pass

    pass
