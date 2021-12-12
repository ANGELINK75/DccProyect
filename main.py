
import os
import sys
import json
import random

from . import factory
#from . import shotgrid

class ProyectoDDCError(Exception):
  pass

class Main:

  #Dentro de un estudio el path seria a 'C\\JobName\\ProyectName\\Secuences\\Shots'
    #Cambiar path antes de ejecutar
  #MAIN_FOLDER = "D:\\Desktop\\Trabajos\\UP\\9no_Semestre\\Pipeline\\Dcc_Scenes"
  MAIN_FOLDER = f"C:\\Users\\{ os.getenv('USERNAME', '') }\\Documents\\DccScenes"

  def __init__(self):
    
    print("-------------------------------------------")
    print(self.MAIN_FOLDER)

    #App and File information
    self.__scenePath = None;
    self.__sceneName = None;
    self.__interpreter = None;

    #App Instances variables
    self.__factory = factory.Factory()
    self.__dccInstance = self.GetDdcInstance()()

    #ShotGrid variables
    self.__sequence = 'dev'
    '''self.__sg = shotgrid.ShotGrid()'''

    #Shot information
    self.__shotNumber = str(random.randrange(100,900))
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
    #print(path)
    self.__sceneName = name
    if path == "": path = self.__shotPath
    self.__scenePath = self.__dccInstance.Save_Scene(path, name)

    #Connection to ShotGrid
    '''self.__sg.Create_Shot( str(self.__shotNumber) )'''

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
      print(f'Metadata File ({metaName}) Saved')

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
      self.__dccInstance.Export_Alembic(self.__shotPath, name)
      return True
    except AttributeError:
      print(f'The instance {self.__interpreter} does not have this method')
      return False

  def Make_Summary(self):

    sumFile = self.MAIN_FOLDER + "\\Summary.json"

    summary = []
    for root, directories, files in os.walk(self.MAIN_FOLDER, topdown=False):
      for name in files:
        path = os.path.join(root, name)
        sPath = path.split('\\')
        file = sPath[ len(sPath)-1 ]
        fType = file.split('.')
        type = fType[1]

        program = ""
        if(type == 'ma'): program = 'Maya'
        if(type == 'hip'): program = 'Houdini'
        if(type == 'nknc'): program = 'Nuke'
        if(type == 'json'): program = 'Json'

        fInfo = [file, path, program]
        if program != "": summary.append(fInfo)
    #print(summary)

    fileData = {}
    for s in summary:
      fileData[ s[0] ] = [ s[1], s[2] ]
    
    with open(sumFile, 'w+') as File:
      json.dump(fileData, File)
    print(f'Summary Created')
  
  def Render_Video(self, path, name):
    try:
      self.__dccInstance.Render_Video( self.__shotPath, name, path)
      return True
    except AttributeError:
      print(f'The instance {self.__interpreter} does not have this method')
      return False