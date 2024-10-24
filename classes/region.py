class landMarks: 
    CITY = "City"
    DUNGEON = "Dungeon"
    TOWER = "Tower"
    KEEPS = "Keeps"
    VILLAGES = "Villages"

class region:
    def __init__(self, population, topography, coordinates, landMark):
        self.__population = population
        self.__topography = topography
        self.__coordinates = coordinates
        self.__landMark = landMark  # Already storing the landmark passed to constructor

    def getPopulation(self):
        return self.__population

    def getTopography(self):
        return self.__topography

    def getCoordinates(self):
        return self.__coordinates

    # Method to return the string name for the landmark
    def getLandMark(self):
        return self.__landMark  # Directly return the stored landmark
