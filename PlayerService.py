from Plane import Plane

class PlayerService(object):
    """description of class"""
    def __init__(self, player_repository,computer_hit_repository):
        self.__player_repository = player_repository
        self.__hit_repository=computer_hit_repository

    def PlacePlane(self, cabin_location, cabin_direction):
        plane = Plane(cabin_location, cabin_direction)
        self.__player_repository.TryToPlacePlane(plane)
        self.__player_repository.PlacePlane(plane)

    def ShowPlayerMatrix(self):
        return self.__player_repository.GetPlaneMatrix()

    
    def TryComputerHit(self,hit_location):
        return self.__hit_repository.TryHit(hit_location)

    def LookForHit(self,hit_location):
        if self.__player_repository.TargetObject(hit_location)==0:
            self.__hit_repository.ChangeValue(hit_location,1)
            return 0
        elif self.__player_repository.TargetObject(hit_location)==1:
            self.__hit_repository.ChangeValue(hit_location,2)
            return 1
        elif self.__player_repository.TargetObject(hit_location)==2:
            plane=self.__player_repository.GetPlane(hit_location)
            self.__hit_repository.DestroyPlane(plane)
            return 2

    def ShowHitMatrix(self):
        return self.__hit_repository.GetHitMatrix()