import shotgun_api3

class Shotgun:

    def __init__(self):
        key = 'wrjyn$hcrwkwqjptzy0zbGwgi'
        self.__sg = shotgun_api3.Shotgun(
            "https://angelwiehl-up.shotgrid.autodesk.com/",
            script_name = "DccProyect",
            api_key = key
        )

    def create_shot(self, name):
        shot = self.__sg.find_one( 'Shot', ['code', 'is', name] )
        if not shot:
            
            data = {

            }
            self.__sg.create('Shot', data)