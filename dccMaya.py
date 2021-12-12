import os
from .interface_dcc import InterfaceDcc

try:
    import maya.cmds as cmds
except ImportError:
    pass

class Maya(InterfaceDcc):

  def __init__(self):
    pass

  def Create_Sphere(self, name):
    nName = f'UP_{name}'
    cmds.sphere(r=2, name=nName)
    
  def Create_Cube(self, name):
    nName = f'UP_{name}'
    cmds.polyCube(name=nName)

  def Save_Scene(self, folder, name):
    scenePath = os.path.join( folder, f'maya\\{name}.ma')
    dirPath = os.path.dirname(scenePath)
    if not os.path.exists(dirPath):
      os.makedirs(dirPath)
    cmds.file(rename=scenePath)
    cmds.file(force=True, type='mayaAscii', save=True)
    print(f'Maya File ({name}.ma) Saved')
    return scenePath

  def Export_Alembic(self, folder, name):
    alembicPath = os.path.join( folder, f'maya\\{name}.abc')
    print(f'Alembic file path --> {alembicPath}')
    dirPath = os.path.dirname(alembicPath)
    if not os.path.exists(dirPath):
      os.makedirs(dirPath)

    startFrame = cmds.playbackOptions(q=True, min=True)
    endFrame = cmds.playbackOptions(q=True, max=True)
    command = "-frameRange "+ str(startFrame) + " " + str(endFrame) + " -dataFormat ogawa -file " + str(alembicPath)
    cmds.AbcExport( j = command )

    print(f'Alembic File ({name}.abc) Saved')