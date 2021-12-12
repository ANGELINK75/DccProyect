import os
from .interface_dcc import InterfaceDcc

try:
  import hou
except ImportError:
  pass

class Houdini(InterfaceDcc):
  
  def __init__(self):
    pass
  
  def Create_Sphere(self, name):
    nName = f'UP_{name}'
    objNode = hou.node('obj')
    geoNode = objNode.createNode('geo')
    polyNode = geoNode.createNode('sphere', nName)
  
  def Create_Cube(self, name):
    nName = f'UP_{name}'
    objNode = hou.node('obj')
    geoNode = objNode.createNode('geo')
    polyNode = geoNode.createNode('box', nName)

  def Save_Scene(self, folder, name):
    scenePath = os.path.join( folder, f'houdini\\{name}.hip')
    dirName = os.path.dirname(scenePath)
    if not os.path.exists( dirName ):
      os.makedirs( dirName )
    hou.hipFile.save(file_name = scenePath)
    print(f'Houdini File ({name}.hip) Saved')
    return scenePath