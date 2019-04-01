from random import choice
from queue import Queue
class GameService(object):
    """description of class"""
    def __init__(self, player_service, computer_service):
        self.__player_service = player_service
        self.__computer_service = computer_service
        self.__lee_queue=[]
        self.__neighbours=[[-1,0],[0,1],[1,0],[0,-1]]
        self.__column = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.__inverse_column={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}

    def PlacePlayerPlane(self, cabin_location, cabin_direction):
        self.__player_service.PlacePlane(cabin_location, cabin_direction)

    def ShowPlayerMatrix(self):
        return self.__player_service.ShowPlayerMatrix()

    def PlaceComputerPlane(self):
        placed_planes_counter = 0
        while placed_planes_counter != 2:       
            row=choice("12345678")
            column=choice("ABCDEFGH")
            cabin_direction=choice("udrl")
            cabin_location=[column,row]
            try:
                self.__computer_service.PlacePlane(cabin_location,cabin_direction)
                placed_planes_counter+=1
            except Exception:
                pass
       
    def ShowComputerMatrix(self):
        return self.__computer_service.ShowComputerMatrix()

    def PlayerHit(self,hit_location):
        if self.__computer_service.TryPlayerHit(hit_location)==True:
            return self.__computer_service.LookForHit(hit_location)
                

    def PlaceComputerHit(self):
        ok=0
        hit_value=0
        while ok==0:
            if len(self.__lee_queue)==0:
                row=choice("12345678")
                column=choice("ABCDEFGH")
                hit_location=[column,row]
                if self.__player_service.TryComputerHit(hit_location)==True:
                    ok=1
                    hit_value=self.__player_service.LookForHit(hit_location)
                    if hit_value==1:
                        for index in range(0,4):
                            self.__lee_queue.append([self.__column[hit_location[0]]+self.__neighbours[index][0],int(hit_location[1])-1+self.__neighbours[index][1]])
                    elif hit_value==2:
                        self.__lee_queue.clear()
            else:
                hit_location=self.__lee_queue.pop()
                if hit_location[0]>=0 and hit_location[0]<8:
                    hit_location[0]=self.__inverse_column[hit_location[0]]
                    if hit_location[1]>=0 and hit_location[1]<8:
                        hit_location[1]+=1
                        hit_location[1]=str(hit_location[1])
                        new_location=str(hit_location[0])+str(hit_location[1])
                        if self.__player_service.TryComputerHit(hit_location)==True:
                            ok=1
                            hit_value=self.__player_service.LookForHit(hit_location)
                            if hit_value==1:
                                for index in range(0,4):
                                    self.__lee_queue.append([self.__column[hit_location[0]]+self.__neighbours[index][0],int(hit_location[1])-1+self.__neighbours[index][1]])
                            elif hit_value==2:
                                self.__lee_queue.clear()
           
        return hit_value
    def ShowPlayerHit(self):
        return self.__computer_service.ShowHitMatrix()

    def ShowComputerHit(self):
        return self.__player_service.ShowHitMatrix()
