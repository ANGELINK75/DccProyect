from PySide6 import QtWidgets

from ..main import Main

class DccWidget(QtWidgets.QWidget):

    def __init__(self):
        super(DccWidget, self).__init__()
        
        self.__main = Main()
        
        self.setWindowTitle('Pipeline')
        verticalLayout = QtWidgets.QVBoxLayout()
        self.setLayout(verticalLayout)

        btnCreateSphere = QtWidgets.QPushButton('Crear Esfera')
        btnCreateSphere.clicked.connect(self.__CreateSphere)
        verticalLayout.addWidget(btnCreateSphere)

        btnSaveScene = QtWidgets.QPushButton('Guardar Escena')
        btnCreateSphere.clicked.connect(self.__SaveScene)
        verticalLayout.addWidget(btnSaveScene)

    def __CreateSphere(self):
        name = QtWidgets.QInputDialog().getText(title='Name', label='Sphere name:')
        self.__main.CreatePoly('sphere', name)

def main():
    pass

if __name__ == "__main__":
    main()