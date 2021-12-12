import maya.standalone as standalone 
import maya.cmds as cmds 

standalone.initialize(name="python") 
cmds.file(f=True, new=True)
startFrame = cmds.playbackOptions(q=True, min=True)endFrame = cmds.playbackOptions(q=True, max=True)command = "-frameRange "+ str(startFrame) + " " + str(endFrame) + " -dataFormat ogawa -file " + D:\Desktop\Trabajos\UP\9no_Semestre\Pipeline\Dcc_Scenes\344\maya\abc.abccmds.AbcExport( j = command )