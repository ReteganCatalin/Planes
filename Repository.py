from copy import deepcopy

class PlaneRepository(object):
    """description of class"""
    def __init__(self,plane_validator):
        matrix = []
        unitary_list = [0] * 8
        for index in range(8):
            matrix.append(deepcopy(unitary_list))
        self.__matrix = matrix
        self.__column = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.__plane_validator=plane_validator
        self.__planes=[]
    def TryToPlacePlane(self, plane):
        cabin_location = plane.GetCabinLocation()
        cabin_row = int(cabin_location[1]) - 1
        cabin_column = self.__column[cabin_location[0]]
        cabin_direction=plane.GetCabinDirection()
        if self.__plane_validator.CheckIfPlaneFitsInGrid(cabin_column,cabin_row,cabin_direction)==False:
            raise Exception("The plane doesn't fit in the grid")
        else:
            plane_matrix=plane.GetPlane()
            if self.__plane_validator.CheckIfPlaneDoesntOverlap(cabin_row,cabin_column,cabin_direction,plane_matrix,self.__matrix)==False:
                raise Exception("The planes overlaps")
    
    def PlacePlane(self,plane):
        cabin_location = plane.GetCabinLocation()
        cabin_row = int(cabin_location[1]) - 1
        cabin_column = self.__column[cabin_location[0]]
        cabin_direction=plane.GetCabinDirection()
        plane_matrix=plane.GetPlane()
        self.InsertPlane(cabin_row,cabin_column,cabin_direction,plane_matrix)
        self.__planes.append(plane)

    def InsertPlane(self,row,column,direction,plane_matrix):
        if direction=='u':
            for index_row in range (0,4):
                for index_column in range (0,5):
                    if plane_matrix[index_row][index_column]==1:
                        self.__matrix[index_row+row][index_column+column-2]=1
        if direction=='d':
            for index_row in range (0,4):
                for index_column in range (0,5):
                    if plane_matrix[3-index_row][index_column]==1:
                        self.__matrix[index_row+row-3][index_column+column-2]=1
        if direction=='r':
            for index_row in range (0,5):
                for index_column in range (0,4):
                    if plane_matrix[index_column][index_row]==1:
                        self.__matrix[index_row+row-2][index_column+column]=1
        if direction=='l':
            for index_row in range (0,5):
                for index_column in range (0,4):
                    if plane_matrix[3-index_column][index_row]==1:
                        self.__matrix[index_row+row-2][index_column+column-3]=1
        self.__matrix[row][column]=2 #position of the cabin
    
    def GetPlaneMatrix(self):
        return self.__matrix

    def TargetObject(self,hit_location):
        '''
        I want to return what was hitted
        '''
        hit_row = int(hit_location[1]) - 1
        hit_column = self.__column[hit_location[0]]
        return self.__matrix[hit_row][hit_column]
    def GetPlane(self,hit_location):
        #hit_location=str(hit_location)
        for plane_index in range(0,2):
            if self.__planes[plane_index]==hit_location:
                return self.__planes[plane_index]


class HitRepository():
    def __init__(self):
        matrix = []
        unitary_list = [0] * 8
        for index in range(8):
            matrix.append(deepcopy(unitary_list))
        self.__matrix = matrix
        self.__column = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    def TryHit(self,hit_location):
        hit_row = int(hit_location[1]) - 1
        hit_column = self.__column[hit_location[0]]
        if self.__matrix[hit_row][hit_column]==0:
            return True
        else:
            raise Exception("You already tried that position")
    def ChangeValue(self,hit_location,value):
        hit_row = int(hit_location[1]) - 1
        hit_column = self.__column[hit_location[0]]
        self.__matrix[hit_row][hit_column]=value

    def DestroyPlane(self,plane):
        cabin_location = plane.GetCabinLocation()
        cabin_row = int(cabin_location[1]) - 1
        cabin_column = self.__column[cabin_location[0]]
        cabin_direction=plane.GetCabinDirection()
        plane_matrix=plane.GetPlane()
        self.DoDestroyPlane(cabin_row,cabin_column,cabin_direction,plane_matrix)

    def DoDestroyPlane(self,row,column,direction,plane_matrix):
        if direction=='u':
            for index_row in range (0,4):
                for index_column in range (0,5):
                    if plane_matrix[index_row][index_column]==1:
                        self.__matrix[index_row+row][index_column+column-2]=2
        if direction=='d':
            for index_row in range (0,4):
                for index_column in range (0,5):
                    if plane_matrix[3-index_row][index_column]==1:
                        self.__matrix[index_row+row-3][index_column+column-2]=2
        if direction=='r':
            for index_row in range (0,5):
                for index_column in range (0,4):
                    if plane_matrix[index_column][index_row]==1:
                        self.__matrix[index_row+row-2][index_column+column]=2
        if direction=='l':
            for index_row in range (0,5):
                for index_column in range (0,4):
                    if plane_matrix[3-index_column][index_row]==1:
                        self.__matrix[index_row+row-2][index_column+column-3]=2
        self.__matrix[row][column]=2 #position of the cabin

    def GetHitMatrix(self):
        return self.__matrix
