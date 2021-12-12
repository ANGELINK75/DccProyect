import sys
import inspect

try:
    from PySide2 import QtWidgets
    from PySide2.QtCore import QWaitCondition
    from PySide2.QtGui import Qt
except ImportError:
    from PySide6 import QtWidgets
    from PySide6.QtCore import QWaitCondition
    from PySide6.QtGui import Qt

from DccProyect.main import Main
from DccProyect.interface_dcc import InterfaceDcc

class DccWidget(QtWidgets.QWidget):

    def __init__(self):
        super(DccWidget, self).__init__()
        
        self.__main = Main()
        
        self.setWindowTitle('Pipeline')
        self.setFixedSize(300, 200)
        verticalLayout = QtWidgets.QVBoxLayout()
        self.setLayout(verticalLayout)

        iFs =  inspect.getmembers(InterfaceDcc, predicate=inspect.isfunction)
        InterfaceFunctions = [func[0] for func in iFs]
        #print(InterfaceFunctions)

        # CREA LA CANTIDAD DE BOTONES EN BASE A LAS FUNCIONES
        for funcName in InterfaceFunctions:
            try:
                btnName = ' '.join(funcName.split('_'))
                btnFunction = self.__getattribute__(funcName)

                appBtn = QtWidgets.QPushButton(btnName)
                appBtn.clicked.connect(btnFunction)
                verticalLayout.addWidget(appBtn)
            except AttributeError:
                print( f'The method "{funcName}" does not exists in the UI' )
                pass
        
        btnSaveMetadata = QtWidgets.QPushButton('Save Metadata')
        btnSaveMetadata.clicked.connect(self.__Save_Metadata)
        verticalLayout.addWidget(btnSaveMetadata)

        btnExportAlembic = QtWidgets.QPushButton('Export Alembic')
        btnExportAlembic.clicked.connect(self.__Export_Alembic)
        verticalLayout.addWidget(btnExportAlembic)

        '''
        btnSummary = QtWidgets.QPushButton('Make Summary')
        btnSummary.clicked.connect(self.__Make_Summary)
        verticalLayout.addWidget(btnSummary)
        '''

        btnVideo = QtWidgets.QPushButton('Render Video')
        btnVideo.clicked.connect(self.__Render_Video)
        verticalLayout.addWidget(btnVideo)

    def Create_Sphere(self):
        name, option = QtWidgets.QInputDialog().getText(self, 'Poly Name', 'Sphere name:', QtWidgets.QLineEdit.Normal)
        if option: 
            self.__main.Create_Sphere(name)
            print("Sphere Created")

    def Create_Cube(self):
        name, option = QtWidgets.QInputDialog().getText(self, 'Poly Name', 'Cube name:', QtWidgets.QLineEdit.Normal)
        if option:
            self.__main.Create_Cube(name)
            print("Cube Created")
    
    def Save_Scene(self):
        name, nOption = QtWidgets.QInputDialog().getText(self, 'Save Scene', 'Scene name:', QtWidgets.QLineEdit.Normal)
        if nOption:
            path, pOption = QtWidgets.QInputDialog().getText(self, 'Save Scene', 'Scene path \n(Cancel for default):', QtWidgets.QLineEdit.Normal)
            if not pOption: path = ""
            self.__main.Save_Scene(path, name)
            print("Scene Saved")
    
    def __Save_Metadata(self):
        self.__main.Save_Metadata()

    def __Export_Alembic(self):
        name, nOption = QtWidgets.QInputDialog().getText(self, 'Export Alembic', 'Alembic name:', QtWidgets.QLineEdit.Normal)
        if nOption:
            path, pOption = QtWidgets.QInputDialog().getText(self, 'Export Alembic', 'Alembic path \n(Cancel for default):', QtWidgets.QLineEdit.Normal)
            if not pOption: path = ""
            if self.__main.Export_Alembic(name):
                print("Alembic Saved")
    
    def __Make_Summary(self):
        print("Making Summary")
        self.__main.Make_Summary()

    def __Render_Video(self):
        name, nOption = QtWidgets.QInputDialog().getText(self, 'Nuke Render', 'Video name:', QtWidgets.QLineEdit.Normal)
        if nOption:
            path, pOption = QtWidgets.QInputDialog().getText(self, 'Nuke Render', 'Sequence Folder:', QtWidgets.QLineEdit.Normal)
            if pOption or path == "":
                if self.__main.Render_Video(path, name):
                    print("Video Rendered")


def main():
    app = QtWidgets.QApplication()
    widget = DccWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()