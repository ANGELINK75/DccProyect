
import os
import sys

from . import factory

class ProyectoDDCError(Exception):
  pass

class Main:
  def __init__(self):
    self.__path = None
    self.__interpreter = None
    self.__factory = factory.Factory()
    self.__dccInstance = self.GetDdcInstance()()

    #self.__dccInstance.HelloWorld()

  def GetDdcInstance(self):
    path_Interpreter = sys.executable
    interpreter = os.path.basename(path_Interpreter).split('.')[0]
    instance = self.__factory.GetInstance(interpreter)

    if not instance:
      raise ProyectoDDCError(f'El  DCC {interpreter} no esta soportado')

    return instance

  def HelloWorld(self):
    print('Hello World')

  def CreatePoly(self, poly, name):
    poly = self.__dccInstance.CreatePoly(poly, name)

  def SaveScene(self, path, name):
    self.__path = self.__dccInstance.SaveScene(path, name)
    self.__sg.CreateShot( str(self.__shotNumber) )

  def SaveMetadata(self):
    data = {
        'escena': self.path,
        'dcc': self.interpreter,
    }
    metadata = self.getMetadata()

  def ExportAlembic(self, name):
    try:
      self.__dccInstance.ExportAlembic(self.path, name)
    except AttributeError:
      print("La intancia no tiene este metodo")