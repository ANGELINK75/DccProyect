import os.path
from .interface_dcc import InterfaceDcc

try:
  import nuke
except ImportError:
  pass

class Nuke(InterfaceDcc):
  
  def __init__(self):
    pass
  
  def Create_Sphere(self, name):
    nName = f'UP_{name}'
    viewer = nuke.toNode('Viewer1')
    node = nuke.nodes.Sphere(name=nName)
    viewer.setInput(0,node)
  
  def Create_Cube(self, name):
    nName = f'UP_{name}'
    viewer = nuke.toNode('Viewer1')
    node = nuke.nodes.Cube(name=nName)
    viewer.setInput(0, node)

  def Save_Scene(self, folder, name):
    scenePath = os.path.join( folder, f'nuke\\{name}.nknc')
    dirName = os.path.dirname(scenePath)
    if not os.path.exists( dirName ):
      os.makedirs( dirName )
    nuke.scriptSaveAs(filename=scenePath,overwrite=-1)
    return scenePath

  def Render_Video(self, folder, name, sequence ):
    
    sequence = str(sequence).replace("\\", "\\\\") + "\\"
    for seq in nuke.getFileNameList(sequence):
        readNode = nuke.nodes.Read()
        readNode.knob('file').fromUserText(sequence + seq)
    readNode.knob('name').setText(name)
    
    print(folder)
    print(sequence)

    viewer = nuke.toNode('Viewer1')
    viewer.setInput(0, readNode)

    file = nuke.nodes.Write(file_type='mov')
    readNode.setInput(0, file)
    file.knob('mov64_codec').setValue('h.264')
    
    renderPath = os.path.join(folder, 'nuke\\' + name + '.mov')
    dirPath = os.path.dirname(renderPath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    file.knob('file').setValue(renderPath)
    lastFrame = readNode.knob('last').getValue()
    nuke.execute("Write1", 1, int(lastFrame), 1)

