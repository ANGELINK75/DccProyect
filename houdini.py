
try:
  import hou
except ImportError:
  pass

class Houdini:
  
  def __init__(self):
    pass
  
  def CreatePoly(self, poly, name):
    objNode = hou.node('obj')
    geoNode = objNode.createNode('geo')
    polyNode = geoNode.createNode(poly)
    polyNode.setName(name)

  def SaveScene(self, path, name):
    hou.hipfile.save(file_name=path)