
try:
    import maya.cmds as cmds
except ImportError:
    pass

class Maya:

  def __init__(self):
    pass

  def HelloWorld(self):
    print('Hello World')

  def CreatePoly(self, poly, name):
    nName = f'UP_{name}'

    if poly == 'sphere':
      cmds.sphere(r=10, name=nName)
    elif poly == 'cube':
      cmds.polyCube(name=nName)

  def SaveScene(self, path):
    cmds.file(rename=path)
    cmds.file(force=True, type='mayaAscii', save=True)

  def ExportAlembic(self, path, name):
    alembicPath = os.path.join(path, f'maya\\{name}.abc')
    dirPath = os.path.dirname(alembicPath)