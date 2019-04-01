
import tkinter
from tkinter import *
from tkinter import messagebox

class GUI:
    widgets = []

    def __init__(self,game_service,user_validator ):
        self.__game_service = game_service
        self.__user_validator= user_validator
        self.computer_destroyed_planes=0
        self.player_destroyed_planes=0

    def PlaceComputerPlanes(self):
        self.__game_service.PlaceComputerPlane()

    def PlacePlaneonGrid(self):
        if self.placed_planes_counter != 2:
            try:
                cabin_location=self.location_textbox.get()
                cabin_direction=self.direction_textbox.get()
                self.__user_validator.CheckCabinData(cabin_location, cabin_direction)
                self.__game_service.PlacePlayerPlane(cabin_location, cabin_direction)
                self.placed_planes_counter += 1
            except Exception as ex: 
                messagebox.showinfo("Error",str(ex))
            else:
                messagebox.showinfo("Success!","Plane Placed")
        else:
            messagebox.showinfo("Error","You already placed 2 planes")
    def Destroy_placing_frame(self):
        if self.placed_planes_counter==2:
            self.place_planes.destroy()
        else:
            messagebox.showinfo("Error","You have to place 2 planes before starting the game!  ")
    def PlacePlanes(self):
        self.placed_planes_counter = 0
        self.place_planes=tkinter.Tk()
        self.place_planes.title("Place planes")
        place_planes_frame= Frame(self.place_planes)
        place_planes_frame.pack()
        label_location = Label(place_planes_frame, text="Location of the cabin first the column(A-H) then the row(0-8:")
        label_location.pack(side=LEFT)
        self.location_textbox = Entry(place_planes_frame, {})
        self.location_textbox.pack(side=LEFT)

        label_direction = Label(place_planes_frame, text="Direction of the cabin:")
        label_direction.pack(side=LEFT)
        self.direction_textbox = Entry(place_planes_frame, {})
        self.direction_textbox.pack(side=LEFT)
        self.PlaceButton = Button(place_planes_frame, text="Place a plane at the given position", command=self.PlacePlaneonGrid)
        self.PlaceButton.pack(side=LEFT)
        self.DestroyButton = Button(place_planes_frame, text="Start the game", command=self.Destroy_placing_frame)
        self.DestroyButton.pack(side=LEFT)
        
        self.place_planes.mainloop()
       
    def ShowPlaneMatrix(self):
        self.place_planes=tkinter.Tk()
        self.place_planes.title("Show your planes")
        place_planes_frame= Frame(self.place_planes)
        place_planes_frame.pack()
        player_plane_matrix=self.__game_service.ShowPlayerMatrix()
        def create_board(main):
            for index_row in range(8):
               for index_column in range(8):
                    DrawAtPosition(index_row, index_column, main, player_plane_matrix[index_row][index_column])
        def DrawAtPosition(ii, jj, frame , value):
            def create(i=ii, j=jj, master=frame , values=value):
               GUI.color="white"
               canvas = tkinter.Canvas(master,height=32, width=32)
               canvas.grid(row=i, column =j, sticky = tkinter.N+tkinter.E+tkinter.S+tkinter.W)
               if values==1:
                   canvas.create_rectangle(2, 2, 30, 30, fill="blue")
               elif values==2:
                   canvas.create_rectangle(2,2, 30, 30 , fill="black")
               else:
                   canvas.create_rectangle(2, 2, 30, 30, fill="white")
               return
            return create()
        create_board(place_planes_frame)
        self.place_planes.mainloop()
    def ComputerTryToHit(self):
        try:
            hit_value=self.__game_service.PlaceComputerHit()
            if hit_value==2:
                self.player_destroyed_planes+=1
                messagebox.showinfo("Danger","One of your planes got destroyed !!!")
            elif hit_value==1:
                messagebox.showinfo("Be careful","One of your planes was hit!")
            else:
                messagebox.showinfo("Yay","The PC missed")
        except Exception as ex:
            self.ComputerTryToHit()
    def TryPlayerHit(self):
         ok=0
         while ok==0:
            hit_location = self.hit_location_textbox.get()
            try:
                self.__user_validator.CheckHitData(hit_location)
                hit_value=self.__game_service.PlayerHit(hit_location)
                if hit_value==2:
                    self.computer_destroyed_planes+=1
                    messagebox.showinfo("Success","YOU DESTROYED A PLANE !!!")
                elif hit_value==1:
                    messagebox.showinfo("Success","You hit a plane!")
                elif hit_value==0:
                    messagebox.showinfo("Miss","Missed")
                ok=1
            except Exception as ex:
                messagebox.showinfo("Error",str(ex))
                self.main_window.destroy()
                self.StartHitting()
         
         if self.computer_destroyed_planes==2:
             messagebox.showinfo("Win","You Won")
             self.main_window.destroy()
             return
         else:
             self.ComputerTryToHit()
             if self.player_destroyed_planes==2:
                messagebox.showinfo("Lose","You Lose")
                self.main_window.destroy()
                return
             else:
                self.main_window.destroy()
                self.StartHitting()
    def StartHitting(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("1200x480")
        
        main_frame = tkinter.Frame(self.main_window)
        frame = tkinter.LabelFrame(self.main_window)
        label = tkinter.Label(frame, text="Planes")
        frame.grid(row=0)
        main_frame.config(height=480, width=480)
        main_frame.rowconfigure(8)
        main_frame.columnconfigure(8)
        main_frame.grid(row=1)

        label.grid(row=0, column=6)
        computer_hit_matrix=self.__game_service.ShowComputerHit()
        player_hit_matrix=self.__game_service.ShowPlayerHit()
        def create_board(main):
            for index_row in range(8):
                for index_column in range(17):
                    if index_column<8:
                        DrawHitBoardAtPosition(index_row, index_column, main, player_hit_matrix[index_row][index_column])
                    elif index_column==8:
                        DrawHitBoardAtPosition(index_row, index_column, main, 1)
                    else:
                        DrawHitBoardAtPosition(index_row, index_column, main, computer_hit_matrix[index_row][index_column-9])
        def DrawHitBoardAtPosition(ii, jj, frame , value ):
            def create(i=ii, j=jj, master=frame , values=value):
               GUI.color="white"
               canvas = tkinter.Canvas(master,height=32, width=32)
               canvas.grid(row=i, column =j, sticky = tkinter.N+tkinter.E+tkinter.S+tkinter.W)
               if values==2:
                   canvas.create_rectangle(2, 2, 30, 30, fill="blue")
               elif values==1:
                   canvas.create_rectangle(2, 2, 30, 30, fill="black")
               else:
                   canvas.create_rectangle(2, 2, 30, 30, fill="white")
               return
            return create()
       
        label_location = Label(main_frame, text="Location of the hit first the column(A-H) then the row(0-8):")
        label_location.grid(row=1,column=18,sticky = tkinter.N+tkinter.E+tkinter.S+tkinter.W)
        self.hit_location_textbox = Entry(main_frame, {})
        self.hit_location_textbox.grid(row=3,column=18,sticky = tkinter.N+tkinter.E+tkinter.S+tkinter.W)
        self.PlaceButton = Button(main_frame, text="Try a hit", command=self.TryPlayerHit)
        self.PlaceButton.grid(row=5,column=18,sticky = tkinter.N+tkinter.E+tkinter.S+tkinter.W)
            
        create_board(main_frame)
        self.main_window.mainloop()
    def StartGame(self):
        self.PlaceComputerPlanes()
        self.PlacePlanes()
        self.ShowPlaneMatrix()
        self.StartHitting()
        

        

        
        



