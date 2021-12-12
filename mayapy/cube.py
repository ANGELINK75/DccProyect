import maya.standalone as standalone 
import maya.cmds as cmds 

standalone.initialize(name='python') 
cmds.file(f=True, new=True)

cmds.polyCube(name='UP_Cube-c')

cmds.file(rename='UP_Cube-c.ma')
cmds.file(force=True, type='mayaAscii', save=True)