from GameService import GameService
from PlayerService import PlayerService
from ComputerService import ComputerService
from Plane import Plane
from Repository import PlaneRepository,HitRepository
from Validator import *
import unittest

class Test_tests(unittest.TestCase):
    def setUp(self):
        self.plane_validator=PlaneValidator()
        self.player_plane_repository = PlaneRepository(self.plane_validator)
        self.computer_plane_repository = PlaneRepository(self.plane_validator)    
        self.player_hit_repository=HitRepository()
        self.computer_hit_repository=HitRepository()
        self.player_service = PlayerService(self.player_plane_repository,self.computer_hit_repository)
        self.computer_service = ComputerService(self.computer_plane_repository,self.player_hit_repository)
        self.game_service = GameService(self.player_service, self.computer_service)
    def test_A(self):
        cabin_location=['C','1']
        cabin_direction='u'
        self.game_service.PlacePlayerPlane(cabin_location,cabin_direction)
        player_matrix=self.game_service.ShowPlayerMatrix()
        self.assertEqual(player_matrix[0][2],2)
        self.assertEqual(player_matrix[1][2],1)
        self.assertEqual(player_matrix[0][1],0)
        try:
            self.game_service.PlacePlayerPlane(cabin_location,cabin_direction)
            self.assertEqual(0,1)
        except:
            self.assertEqual(0,0)
        cabin_location=['F','4']
        cabin_direction='d'
        self.game_service.PlacePlayerPlane(cabin_location,cabin_direction)
        player_matrix=self.game_service.ShowPlayerMatrix()
        self.assertEqual(player_matrix[3][5],2)
        hit_location=['F','4']
        self.game_service.PlayerHit(hit_location)
        hit_matrix=self.game_service.ShowPlayerHit()
        self.assertEqual(hit_matrix[3][5],1)
        self.game_service._GameService__player_service.LookForHit(hit_location)
        hit_matrix=self.game_service.ShowComputerHit()
        self.assertEqual(hit_matrix[3][5],2)
        self.assertEqual(hit_matrix[2][5],2)
        
        

if __name__ == '__main__':
    unittest.main()
