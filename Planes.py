from UI import *
from GameService import GameService
from PlayerService import PlayerService
from ComputerService import ComputerService
from Plane import Plane
from Repository import PlaneRepository,HitRepository
from Validator import *
from GUI import * 
import prettytable as pt

plane_validator=PlaneValidator()
player_plane_repository = PlaneRepository(plane_validator)
computer_plane_repository = PlaneRepository(plane_validator)
player_hit_repository=HitRepository()
computer_hit_repository=HitRepository()
player_service = PlayerService(player_plane_repository,computer_hit_repository)
computer_service = ComputerService(computer_plane_repository,player_hit_repository)
game_service = GameService(player_service, computer_service)
user_validator = UserValidator()
game=UI(game_service, user_validator)
#game=GUI(game_service, user_validator)
game.StartGame()