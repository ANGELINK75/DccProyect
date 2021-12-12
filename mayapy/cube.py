import maya.standalone as standalone 
import maya.cmds as cmds 

standalone.initialize(name='python') 
cmds.file(f=True, new=True)

cmds.polyCube(name='UP_Cube-Dado')

cmds.file(rename='UP_Cube-Dado.ma')
cmds.file(force=True, type='mayaAscii', save=True)