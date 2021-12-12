import os
import subprocess
from .interface_dcc import InterfaceDcc

'''
cmd = [
  "C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe", 
  "D:\\Desktop\\Trabajos\\UP\\9no_Semestre\\Pipeline\\DccProyect\\ui\\main_window.py" ]
subprocess.run(cmd)
'''

class dccMayaPython(InterfaceDcc):

  MAYAPY_PATH = "C:\\Program Files\\Autodesk\\Maya2022\\bin\\mayapy.exe"
  CMD_PATH = "D:\\Desktop\\Trabajos\\UP\9no_Semestre\\Pipeline\\DccProyect\\mayapy"
  CMD = [MAYAPY_PATH, ""]

  def __init__(self):
    pass

  def Create_Sphere(self, name):
    nName = f'UP_Sphere-{name}'
    nPath = f"C:\\Users\\{ os.getenv('USERNAME', '') }\\Documents\\DccScenes\\mayapy"
    scenePath = os.path.join( nPath, f'maya\\{nName}.ma')
    dirPath = os.path.dirname(scenePath)
    if not os.path.exists(dirPath):
      os.makedirs(dirPath)

    with open("mayapy/sphere.py", "w") as f:
      f.write( "import maya.standalone as standalone \nimport maya.cmds as cmds \n\nstandalone.initialize(name='python') \ncmds.file(f=True, new=True)\n\n")
      f.write( f"cmds.sphere(r=2, name='{nName}')\n\n" )
      f.write( f"cmds.file(rename='{nName}.ma')\n"  )
      f.write( "cmds.file(force=True, type='mayaAscii', save=True)" )
      f.close()

    print( "File on 'C:\\Users\\<User>\\Documents\\maya\\projects\\default\\scenes'" )
    self.CMD[1] = self.CMD_PATH+"\\sphere.py"
    subprocess.run(self.CMD)
    
  def Create_Cube(self, name):
    nName = f'UP_Cube-{name}'
    nPath = f"C:\\Users\\{ os.getenv('USERNAME', '') }\\Documents\\DccScenes\\mayapy"
    scenePath = os.path.join( nPath, f'maya\\{nName}.ma')
    dirPath = os.path.dirname(scenePath)
    if not os.path.exists(dirPath):
      os.makedirs(dirPath)

    with open("mayapy/cube.py", "w") as f:
      f.write( "import maya.standalone as standalone \nimport maya.cmds as cmds \n\nstandalone.initialize(name='python') \ncmds.file(f=True, new=True)\n\n")
      f.write( f"cmds.polyCube(name='{nName}')\n\n" )
      f.write( f"cmds.file(rename='{nName}.ma')\n"  )
      f.write( "cmds.file(force=True, type='mayaAscii', save=True)" )
      f.close()

    print( "File on 'C:\\Users\\<User>\\Documents\\maya\\projects\\default\\scenes'" )
    self.CMD[1] = self.CMD_PATH+"\\cube.py"
    subprocess.run(self.CMD)

  def Save_Scene(self, folder, name):
    scenePath = os.path.join( folder, f'{name}.ma')
    dirPath = os.path.dirname(scenePath)
    if not os.path.exists(dirPath):
      os.makedirs(dirPath)

    scenePath = str(scenePath).replace("\\", "\\\\")
    with open( "mayapy/safe.py", "w") as f:
      f.write( "import maya.standalone as standalone \nimport maya.cmds as cmds \n\nstandalone.initialize(name='python') \ncmds.file(f=True, new=True)\n")
      f.write( f"cmds.file(rename='{ scenePath }')\n" )
      f.write( "cmds.file(force=True, type='mayaAscii', save=True)" )
      f.close()

    self.CMD[1] = self.CMD_PATH+"\\safe.py"
    subprocess.run(self.CMD)

    print(f'Maya File ({name}.ma) Saved')
    return scenePath