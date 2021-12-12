import libs.shotgun_api3

class ShotGrid:

    def __init__(self):
        #Cambiar link y llave de ShotGrid antes de ejecutar 
        key = 'yhgkywu5dw@rtxsbadkumgByp'
        self.__sg = shotgun_api3.Shotgun(
            "https://angelwiehl-up.shotgrid.autodesk.com/",
            script_name = "DccProyect",
            api_key = key
        )

    def Create_Shot(self, name):
        shot = self.__sg.find_one( 'Shot', [['code', 'is', name]] )
        if not shot:
            sgProyect = self.__sg.find_one('Proyect', [['code', 'is', name]] )
            sgSequence = self.__sg.find_one('Sequence', [['code', 'is', 'dev']] )
            data = {
                'sg_sequence': sgSequence,
                'project': sgProyect,
                'code': name
            }
            self.__sg.create('Shot', data)
