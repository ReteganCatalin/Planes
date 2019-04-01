from texttable import Texttable
from copy import deepcopy
class UI(object):
 
    def __init__(self, game_service, user_validator):
         self.__game_service = game_service
         self.__user_validator = user_validator
         self.__destroyed_computer_planes=0
         self.__destroyed_player_planes=0

    def ShowPlayerMatrix(self):
        table=Texttable()
        player_plane_matrix=self.__game_service.ShowPlayerMatrix()
        for index_row in range(0,8):
            copy_row=deepcopy(player_plane_matrix[index_row])
            table.add_row(copy_row)
        print(table.draw())

    def PlacePlanes(self):
        placed_planes_counter = 0
        while placed_planes_counter != 2:
            self.ShowPlayerMatrix()
            cabin_location = input("Please give the location of the cabin first the column(A-H) then the row(0-8):")
            cabin_direction = input("Please give the direction of the cabin:")
            try:
                self.__user_validator.CheckCabinData(cabin_location, cabin_direction)
                self.__game_service.PlacePlayerPlane(cabin_location, cabin_direction)
                placed_planes_counter += 1
            except Exception as ex:
                print(str(ex))

    def PlaceComputerPlanes(self):
        self.__game_service.PlaceComputerPlane()

    def ShowComputerMatrix(self):
        player_plane_matrix=self.__game_service.ShowComputerMatrix()
        for index_row in range(0,8):
            for index_column in range(0,8):
                print(player_plane_matrix[index_row][index_column], end=" ")
            print()

    def ShowPlayerHitMatrix(self):
        table=Texttable()
        hit_matrix=self.__game_service.ShowPlayerHit()
        for index_row in range(0,8):
            copy_row=deepcopy(hit_matrix[index_row])
            table.add_row(copy_row)
        print(table.draw())
    def ShowComputerHitMatrix(self):
        table=Texttable()
        hit_matrix=self.__game_service.ShowComputerHit()
        for index_row in range(0,8):
            copy_row=deepcopy(hit_matrix[index_row])
            table.add_row(copy_row)
        print(table.draw())
        
    def PlayerTrytoHit(self,destroyed_planes):
        ok=0
        if input("Press 1 if you want to show your planes positions: ")=='1':
            self.ShowPlayerMatrix()
        while ok==0:
            hit_location = input("Please give the location of the hit, first the column(A-H) then the row(0-8):")
            try:
                self.__user_validator.CheckHitData(hit_location)
                hit_value=self.__game_service.PlayerHit(hit_location)
                if hit_value==2:
                    destroyed_planes+=1
                    print("YOU DESTROYED A PLANE !!!")
                elif hit_value==1:
                    print("You hit a plane!")
                elif hit_value==0:
                    print("Missed")
                self.ShowPlayerHitMatrix()
                ok=1
            except Exception as ex:
                print(str(ex))
        return destroyed_planes
    def ComputerTryToHit(self,destroyed_planes):
        try:
            hit_value=self.__game_service.PlaceComputerHit()
            if hit_value==2:
                destroyed_planes+=1
                print("One of your planes got destroyed !!!")
            elif hit_value==1:
                print("One of your planes was hit!")
            else:
                print("The PC missed")
            self.ShowComputerHitMatrix()
            return destroyed_planes
        except Exception as ex:
            self.ComputerTryToHit(destroyed_planes)
    def StartHitting(self):
        while self.__destroyed_computer_planes!=2 or self.__destroyed_player_planes!=2:
            self.__destroyed_computer_planes=self.PlayerTrytoHit(self.__destroyed_computer_planes)
            if self.__destroyed_computer_planes==2:
                print("Player Wins")
                return 0
            self.__destroyed_player_planes=self.ComputerTryToHit(self.__destroyed_player_planes)
            if self.__destroyed_player_planes==2:
                print("Computer Wins")
                return 0
    def StartGame(self):
        self.PlaceComputerPlanes()
        #self.ShowComputerMatrix()
        print()
        self.PlacePlanes()
        self.ShowPlayerMatrix()
        self.StartHitting()