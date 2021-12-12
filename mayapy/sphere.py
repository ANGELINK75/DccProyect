import maya.standalone as standalone 
import maya.cmds as cmds 

standalone.initialize(name='python') 
cmds.file(f=True, new=True)

cmds.sphere(r=2, name='UP_Sphere-Bola')

cmds.file(rename='UP_Sphere-Bola.ma')
cmds.file(force=True, type='mayaAscii', save=True)