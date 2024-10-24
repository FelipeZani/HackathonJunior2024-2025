class region:
    __population = None
    __topography = None
    __coordinates = None
    def __init__(self,population,topography,coordinates):
        self.__population = population
        self.__topography = topography
        self.__coordinates = coordinates

    def getPopulation(self):
        return self.__population
    def getTopography(self):
        return self.__topography
    def getCoordinates(self):
        return self.__coordinates
    
