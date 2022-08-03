class Credits:
    def __init__(self):
        self.Dario = self.crediting('Dario','Developing LibXenoverse and understanding how LibXenoverse works')
        self.Creeps = self.crediting('Creeps','help with developing the Xenoverse Shader')
        self.Unleashed = self.crediting('Unleashed','Helping understand C++ to understand how LibXenoverse works')
        self.Revamp_Team = self.crediting('Revamp_Team','Understanding what the Xenoverse file types are')
        self.RED_EYE = self.crediting('RED_EYE','Inspiration and Blender API help')
        self.Pandas = self.crediting('Pandas','assistance with understanding the ESK')

        self.Cawthon = self.crediting('Scott Cawthon', 'Inspiration and personal Role Model (Did not actually work on this Project)')

        self.DemonBoy = self.crediting('Demon Boy: Shader Expert','helping me understand the in game shaders')

        self.Krigeta = self.crediting('Krigeta', 'Shader Testing')
    def crediting(self,person:str,credit:str):
        return 'Credit to '+person+' for ' + credit
