import tkinter as tk
from tkinter import messagebox
import json

# Informatii fereastra
game_title = "Joc"
geometry = "800x500"

class GUI:
    def __init__(self, root):
        root.title(game_title)
        root.geometry(geometry)

        # ------------------------------------- Create objects -------------------------------------
        self.root = root

        # Create menu and game objects
        self.menu_frame = tk.Frame(root)
        self.game_frame = tk.Frame(root)

        # ----- Create canvases -----
        self.menu_canvas = tk.Canvas(self.menu_frame, width=800, height=500)
        self.game_canvas = tk.Canvas(self.game_frame, width=800, height=500)

        # ------ Create frames ------
        self.car_menu_frame = tk.Frame(self.game_canvas, bg="lightblue", width=550, height=460)
        self.car_infos_frame = tk.Frame(self.game_canvas, bg="white", width=220, height=460)

        # Create canvases and frames to display data
        self.car_frames = []
        for index in range(6):
            frame = tk.Frame(self.car_menu_frame, bg="skyblue", width=170, height=200)
            self.car_frames.append(frame)

        self.car_canvas = []
        for index in range(6):
            canvas = tk.Canvas(self.car_frames[index], width=170, height=170)
            self.car_canvas.append(frame)

        # Create all necessary labels
        self.game_title = tk.Label(self.menu_frame, text=game_title, font=("Arial", 30, "bold"))
        self.instructions = tk.Label(self.game_frame, text=" Apasa Click pe harta!")

        self.car_labels = []
        for index in range(6):
            label = tk.Label(self.car_frames[index], text="")
            self.car_labels.append(label)

        # Create all buttons
        self.start_button = tk.Button(self.menu_frame, text="Start", width=20, height=2, command=self.start_game)
        self.help_button = tk.Button(self.menu_frame, text="Help", width=20, height=2, command=self.show_help)
        self.quit_button = tk.Button(self.menu_frame, text="Quit", width=20, height=2, command=self.quit_game)

        self.back_to_menu_button = tk.Button(self.game_frame, text="Inapoi la meniu", command=self.back_to_menu)
        self.close_data_button = tk.Button(self.car_menu_frame, text="X", command=self.remove_infos)
        self.close_info_button = tk.Button(self.car_infos_frame, text="X", command=self.remove_infos)

        # Store necesary data
        self.game_background = []
        self.game_data = {}
        self.game_map = []
        self.state = 0

    # ------------------------------------- Load data into memory -------------------------------------
    def load_background(self):
        self.game_background.append(tk.PhotoImage(file="..\\resources\\map.png"))
        self.game_background.append(tk.PhotoImage(file="..\\resources\\background.png"))
    
    def load_pictures(self):
        self.game_data["pictures"] = []
        for i in range(3):
            continent = []
            index = i*2+1

            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no1.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no2.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no3.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no4.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no5.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no6.png"))

            self.game_data["pictures"].append(continent)
    
    def load_infos(self):
        self.load_continent_infos(1)
        self.load_continent_infos(3)
        self.load_continent_infos(5)

    def load_continent_infos(self, index):
        self.game_data["data"] = []
        carsInfoContinent = []
        with open(f'..\\infos\\{index}\\data.json') as file:
            data = json.load(file)
            for element in data:
                current = {}

                current['brand'] = element['brand']
                current['model'] = element['model']
                current['an'] = element['fabricatie']
                current['putere'] = element['putere']
                current['motorizare'] = element['motorizare']
                current['ENCAP'] = element['ENCAP']
                
                carsInfoContinent.append(current)
        self.game_data["data"].append(carsInfoContinent)

    def load_narrator(self):
        self.game_data["narrator"] = []
        self.game_data["narrator"].append(tk.PhotoImage(file="..\\resources\\1\\guy.png"))
        self.game_data["narrator"].append(tk.PhotoImage(file="..\\resources\\3\\guy.png"))
        self.game_data["narrator"].append(tk.PhotoImage(file="..\\resources\\5\\guy.png"))
    
    def load_map(self):
        with open("..\\infos\\others\\matrix.txt") as file:
            for line in file:
                row = list(map(int, line.split()))
                self.game_map.append(row)

    def load_data(self):
        self.load_background()
        self.load_pictures()
        self.load_infos()
        self.load_narrator()
        self.load_map()

    # ------------------------------------- What happens on start -------------------------------------
    
    def run(self):
        self.load_data() # Look up
        self.place_menu() # Look down

    # --------------------------------------- Place/Erase items -------------------------------------
    def place_menu(self):
        self.menu_frame.pack()
        self.menu_canvas.pack()
        self.menu_canvas.create_image(0,0,anchor="nw",image=self.game_background[1])
        
        self.game_title.place(relx=0.5, y=100, anchor="center")
        self.start_button.place(relx=0.5, y=200, anchor="center")
        self.help_button.place(relx=0.5, y=260, anchor="center")
        self.quit_button.place(relx=0.5, y=320, anchor="center")

    def place_game(self):
        self.game_frame.pack()
        self.game_canvas.pack()
        self.game_canvas.create_image(0,0,anchor="nw",image=self.game_background[0])

        self.back_to_menu_button.place(x=10,y=0)
        self.bind_event(self.game_canvas, "<Button-1>", self.on_click)

    def clear_frame(self, frame):
        frame.pack_forget()
    
    # ------------------------------------- Button functionalities -------------------------------------
    def start_game(self):
        self.clear_frame(self.menu_frame)
        self.place_game()

    def show_help(self):
        print("help")

    def quit_game(self):
        print("quit")  

    def back_to_menu(self):
        self.clear_frame(self.game_frame)
        self.place_menu()

    def remove_infos(self):
        print("remove")       

    # ------------------------------------------- Mouse events -------------------------------------
    def bind_event(self, map_object, command, function):
        map_object.bind(command, function)

    def unbind_event(self, map_object, command):
        map_object.unbind(command)

    def on_click(self, event):
        index = self.game_map[event.y][event.x]
        if index == 6 and event.y < 300:
            index = 3
        
        if index == 0:
            messagebox.showerror("Eroare", "In ocean nu poti gasi masini :(")
        else:
            self.state_machine(index)

    # ---------------------------------------------- Print infos -------------------------------------------
    def state_machine(self, index):
        if self.state == 0:
            if index == 4:
                messagebox.showinfo("Africa", "Nu sunt producatori aici...\n\nIncearca in AUSTRALIA!")
                self.state = 1
            else:
                messagebox.showerror("Eroare", "Atentie:\n\nSelecteaza AFRICA!")
        
        elif self.state == 1:
            if index == 6:
                messagebox.showinfo("Australia", "Nici aici nu sunt producatori...\n\nIncearca in AMERICA DE SUD!")
                self.state = 2
            else:
                messagebox.showerror("Eroare", "Atentie:\n\nSelecteaza AUSTRALIA!")
        
        elif self.state == 2:
            if index == 2:
                messagebox.showinfo("America de Sud", "Nu sunt producatori nici aici...\n\nTarile producatoare de masini sunt Europa, America de Nord si Asia :3")
                self.state = 3
            else:
                messagebox.showerror("Eroare", "Atentie:\n\nSelecteaza AMERICA DE SUD!")

        elif self.state == 3:
            if index % 2 == 1:

                self.unbind_event(self.game_canvas, "<Button-1>")

                # Prepare the frames
                self.car_menu_frame.place(x=10,y=30)
                self.car_infos_frame.place(x=570, y=30)

                for index in range(3):
                    self.car_frames[index].place(x=10+index*180,y=20)
                    self.car_frames[3+index].place(x=10+index*180,y=240)

                

                print("hello")
            
            else:
                messagebox.showerror("Eroare", "Atentie:\n\nNu se gasesc producatori pe acest continent...")

if __name__ == '__main__':
    root = tk.Tk()
    App = GUI(root)
    App.run()
    root.mainloop()