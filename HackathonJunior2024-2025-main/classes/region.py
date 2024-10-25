from enum import Enum
class landMarks(Enum): #Enums used by the methods in the main
    CITY = 1
    DUNGEON = 2
    TOWER = 3
    KEEPS = 4
    VILLAGES = 5

class topography(Enum):
    SWAMP = 1
    FOREST = 2
    MOUNTAINS = 3
    DESERT = 4


class region: #Degine and return the main attributes of the class
    def __init__(self, terrain, coordinateX, building):
        self.__topography = topography(terrain)
        self.__coordinate = coordinateX #add y if it s necessary
        self.__landMark = landMarks(building)
         

    def getTopography(self):
        return self.__topography

    def getCoordinate(self):
        return self.__coordinate

    def getLandMark(self):
        return self.__landMark  # Directly return the stored landmark
