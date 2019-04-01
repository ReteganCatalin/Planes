from Plane import Plane
class ComputerService(object):
    """description of class"""
    def __init__(self, computer_repository,player_hit_repository):
        self.__computer_repository = computer_repository
        self.__hit_repository=player_hit_repository

    def PlacePlane(self, cabin_location, cabin_direction):
        plane = Plane(cabin_location, cabin_direction)
        self.__computer_repository.TryToPlacePlane(plane)
        self.__computer_repository.PlacePlane(plane)

    def ShowComputerMatrix(self):
        return self.__computer_repository.GetPlaneMatrix()

    def TryPlayerHit(self,hit_location):
        return self.__hit_repository.TryHit(hit_location)

    def LookForHit(self,hit_location):
        if self.__computer_repository.TargetObject(hit_location)==0:
            self.__hit_repository.ChangeValue(hit_location,1)
            return 0
        elif self.__computer_repository.TargetObject(hit_location)==1:
            self.__hit_repository.ChangeValue(hit_location,2)
            return 1
        elif self.__computer_repository.TargetObject(hit_location)==2:
            plane=self.__computer_repository.GetPlane(hit_location)
            self.__hit_repository.DestroyPlane(plane)
            return 2
    
    def ShowHitMatrix(self):
        return self.__hit_repository.GetHitMatrix()


