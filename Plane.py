from copy import deepcopy
class Plane(object):
    """description of class"""
    def __init__(self, cabin_location, cabin_direction):
        self.__cabin_location = cabin_location
        self.__cabin_direction = cabin_direction
        self.__plane=self.CreatePlaneMatrix()
    def GetCabinLocation(self):
        return self.__cabin_location
    
    def GetCabinDirection(self):
        return self.__cabin_direction

    def CreatePlaneMatrix(self):
        '''
        Creates the plane matrix for the up direction if it is another direction it will just rotate the matix
        What the matrix has to look like 
        0 0 1 0 0
        1 1 1 1 1
        0 0 1 0 0
        0 1 1 1 0
        '''
        plane_matrix = []
        unitary_list = [0] * 5
        for index in range(4):
            plane_matrix.append(deepcopy(unitary_list))
        plane_matrix[0][2]=1
        plane_matrix[2][2]=1
        for index in range (0,5):
            plane_matrix[1][index]=1
        for index in range (1,4):
            plane_matrix[3][index]=1
        return plane_matrix
    def GetPlane(self):
        return self.__plane

    def __eq__(self, location):
        if self.__cabin_location[0]==location[0] and self.__cabin_location[1]==location[1]:
            return True
        else:
            return False
