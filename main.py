
import os
import sys
import json
import random

from . import factory

class ProyectoDDCError(Exception):
  pass

class Main:

  #Dentro de un estudio el path seria a 'C\\JobName\\ProyectName\\Secuences\\Shots'
    #Cambiar path antes de ejecutar
  MAIN_FOLDER = "D:\\Desktop\\Trabajos\\UP\\9no Semestre\\Pipeline\\Dcc Scenes"

  def __init__(self):

    self.__scenePath = None;
    self.__sceneName = None;
    self.__interpreter = None;

    self.__factory = factory.Factory()
    self.__dccInstance = self.GetDdcInstance()()

    self.__shotNumber = "014" # str(random.randrange(100,900))
    self.__shotPath = os.path.join( self.MAIN_FOLDER, self.__shotNumber )


  def GetDdcInstance(self):
    path_Interpreter = sys.executable
    self.__interpreter = os.path.basename(path_Interpreter).split('.')[0]
    instance = self.__factory.GetInstance(self.__interpreter)

    if not instance:
      raise ProyectoDDCError(f'The  DCC {self.__interpreter} is not supported')

    return instance

  def Create_Sphere(self, name):
    sphere = self.__dccInstance.Create_Sphere(name)
  
  def Create_Cube(self, name):
    cube = self.__dccInstance.Create_Cube(name)

  def Save_Scene(self, path, name):
    print(path)
    self.__sceneName = name
    if path == "": path = self.__shotPath
    self.__scenePath = self.__dccInstance.Save_Scene(path, name)

    #elf.__path = self.__dccInstance.SaveScene(name)
    #self.__sg.CreateShot( str(self.__shotNumber) )

  def Save_Metadata(self):
    if not self.__scenePath:
      raise ValueError("The scene has not been saved. Cannot save metadata.")
    else:  
      metadata = self.__Get_Metadata()
      metaDir = os.path.dirname(self.__scenePath)
      metaName = self.__sceneName+'_metadata.json'
      metaFile = os.path.join( metaDir, metaName )

      fileData = {}
      if os.path.exists(metaFile):
        with open(metaFile, 'r') as File:
          fileData = json.load(File)
      
      for key, value in metadata.items():
        fileData[key] = value
      
      with open(metaFile, 'w+') as File:
        json.dump(fileData, File)
      print('"{metaFile}" - Metadata File Saved')

  def __Get_Metadata(self):
    data = {
        'scene': self.__scenePath,
        'dcc': self.__interpreter,
        'user': os.getenv('USERNAME', ''),
        'shot': self.__shotNumber,
        'os': os.getenv('OS','')
    }
    return data

  def Export_Alembic(self, name):
    try:
      self.__dccInstance.ExportAlembic(self.path, name)
    except AttributeError:
      print("The instance does not have this method")