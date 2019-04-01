class UserValidator(object):
    """description of class"""
    def CheckCabinData(self, cabin_location, cabin_direction):
        if len(cabin_location) != 2:
            raise Exception('more than 2 characters for location')
        if cabin_location[0] not in 'ABCDEFGH':
            raise Exception('invalid column')
        if cabin_location[1] not in '12345678':
            raise Exception('invalid row')
        if cabin_direction not in ['u', 'd', 'r', 'l']:
            raise Exception('invalid entered direction')

    def CheckHitData(self, hit_location):
        if len(hit_location) != 2:
            raise Exception('more than 2 characters for location')
        if hit_location[0] not in 'ABCDEFGH':
            raise Exception('invalid column')
        if hit_location[1] not in '12345678':
            raise Exception('invalid row')

class PlaneValidator(object):
    def CheckIfPlaneFitsInGrid(self, row, column, direction):
        if direction == 'u':
            return row in range(2, 6) and column in range(0, 5)
        elif direction == 'd':
            return row in range(2, 6) and column in range(3, 8)
        elif direction == 'l':
            return row in range(3, 8) and column in range(2, 6)
        elif direction == 'r':
            return row in range(0, 5) and column in range(2, 6)

    def CheckIfPlaneDoesntOverlap(self,row,column,direction,plane_matrix, matrix):
        '''
        Looks if in both matrices there exist a position in which they are both equal to 1 if there is this case then they overlap
        '''

        if direction=='u':
            for index_row in range (0,4):
                for index_column in range (0,5):
                    if matrix[index_row+row][index_column+column-2]>=1 and plane_matrix[index_row][index_column]==1:
                        return False
        if direction=='d':
            for index_row in range (0,4):
                for index_column in range (0,5):
                    if matrix[index_row+row-3][index_column+column-2]>=1 and plane_matrix[3-index_row][index_column]==1:
                        return False
        if direction=='r':
            for index_row in range (0,5):
                for index_column in range (0,4):
                    if matrix[index_row+row-2][index_column+column]>=1 and plane_matrix[index_column][index_row]==1:
                        return False
        if direction=='l':
            for index_row in range (0,5):
                for index_column in range (0,4):
                    if matrix[index_row+row-2][index_column+column-3]>=1 and plane_matrix[3-index_column][index_row]==1:
                        return False
        return True
