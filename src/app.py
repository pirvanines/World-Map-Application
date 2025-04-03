import tkinter as tk
from tkinter import messagebox
import json
from calculus import *

# Informatii fereastra
game_title = "Joc"
geometry = "800x500"

# Dimensiunea chenarului de informatii
width_info = 550
height_info = 490

# ------------------------------------- User Interface -------------------------------------
class GUI:
    def __init__(self, root):
        root.title(game_title)
        root.geometry(geometry)

        # Create objects
        self.root = root
        self.window = tk.Frame(root)
        self.window.pack(padx=0, pady=0)
        
        self.canvas = tk.Canvas(root, width=800, height=500)
        self.car_frames = []
        for index in range(6):
            frame = tk.Frame(self.root, width=170, height=215, relief='raised', borderwidth=2)
            self.car_frames.append(frame)
        
        # Incarca datele de afisat pe ecran
        self.background = []
        self.story_teller = []
        self.cars = []
        self.labels = []

        self.load_background()
        self.load_storry_teller()
        self.load_cars()

        # Creaza butoanele de care am nevoie pe parcurs
        self.start_button = tk.Button(self.root, text="Start", width=20, command=self.start_game)
        self.help_button = tk.Button(self.root, text="Help", width=20, command=self.show_help)
        self.quit_button = tk.Button(self.root, text="Quit", width=20, command=self.quit_game)

        self.back_to_menu_button = tk.Button(self.root, text="Inapoi la meniu", command=self.back_to_menu)
        self.close_info_button = tk.Button(self.root, text="X", command=self.remove_infos)

        # Display buttons
        self.place(self.start_button, 330, 200)
        self.place(self.help_button, 330, 230)
        self.place(self.quit_button, 330, 260)

        # Load infos about cars
        self.carInfos = []
        self.load_infos()
        
        # Starea initiala a jocului
        self.state = 0

    # -------------------------------------- Functions to load images --------------------------------------
    def load_cars(self):
        for i in range(3):
            continent = []
            index = i*2+1

            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no1.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no2.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no3.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no4.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no5.png"))
            continent.append(tk.PhotoImage(file=f"..\\resources\\{index}\\no6.png"))

            self.cars.append(continent)


    def load_storry_teller(self):
        self.story_teller.append(tk.PhotoImage(file="..\\resources\\1\\guy.png"))
        self.story_teller.append(tk.PhotoImage(file="..\\resources\\3\\guy.png"))
        self.story_teller.append(tk.PhotoImage(file="..\\resources\\5\\guy.png"))

    def load_background(self):
        self.background.append(tk.PhotoImage(file="..\\resources\\map.png"))
        #self.background.append(tk.PhotoImage(file="..\\resources\\map.png"))

    def load_infos(self):
        self.load_continent_infos(1)
        self.load_continent_infos(3)
        self.load_continent_infos(5)

    def load_continent_infos(self, index):
        # Load infos about cars
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
        self.carInfos.append(carsInfoContinent)

    # ------------------------------------- Functions to print objects -------------------------------------
    def place(self, _object, x_pos, y_pos):
        _object.place(x=x_pos, y=y_pos)

    def hide(self, _object):
        _object.place_forget()

    # ------------------------------------------- Button functions -----------------------------------------
    def start_game(self):
        self.hide(self.start_button)
        self.hide(self.help_button)
        self.hide(self.quit_button)
        
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.background[0])
        self.canvas.first_image = self.background
        
        self.activate_mouse_event()
        self.place(self.back_to_menu_button, 10, 0)

        if self.state != 3:
            messagebox.showinfo("Help", "Instructiuni:\n\nApasa AFRICA pentru a incepe jocul!")



    def show_help(self):
        messagebox.showinfo("Ajutor", "Instructiuni:\n\nApasa Start pentru a incepe jocul!")

    def quit_game(self):
        self.root.quit()

    def back_to_menu(self):
        # deactivate the canvas
        # deactivate the buttons
        self.canvas.pack_forget()
        self.hide(self.back_to_menu_button)
        self.hide(self.close_info_button)

        # Destroy car infos
        for car in range(6):
            self.labels[car].destroy()
        self.labels.clear()

        # Place menu buttons again
        self.place(self.start_button, 330, 200)
        self.place(self.help_button, 330, 230)
        self.place(self.quit_button, 330, 260)
        
    
    def remove_infos(self):
        # deactivate the canvas
        # deactivate the buttons
        self.hide(self.close_info_button)
        self.canvas.delete("infos")
        self.canvas.delete("storry_teller")

        for car in range(6):
            self.canvas.delete("place"+str(car))
            self.canvas.delete("place"+str(car+3))
            self.labels[car].destroy()

        self.labels.clear()
        self.activate_mouse_event()

    # --------------------------------------------- Mouse events -----------------------------------------
    def activate_mouse_event(self):
        self.canvas.bind("<Button-1>", lambda event: self.on_click(event))

    def deactivate_mouse_event(self):
        self.canvas.unbind("<Button-1>")

    def on_click(self, event):
        index = self.calculate_pos(event.x, event.y)

        if index == -1:
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
                # Desenam dreptunghiul opac pe canvas
                #self.canvas.create_rectangle(
                #    10, 30, width_info, height_info, 
                #    fill="lightblue",  
                #    outline="black",  
                #    stipple="gray50",  
                #    tags="infos"
                #)

                image_x = width_info + 10
                image_y = height_info

                self.canvas.create_image(image_x, 30, anchor="nw", image=self.story_teller[int(index/2)], tags="storry_teller")
                self.canvas.story_t = self.story_teller

                self.place(self.close_info_button, 529, 35)
                self.deactivate_mouse_event()

                self.print_cars(index)
            
            else:
                messagebox.showerror("Eroare", "Atentie:\n\nNu se gasesc producatori pe acest continent...")

    
    def print_cars(self, index):
        #print(self.carInfos[index-1]['country'])
        # Load infos about the top 6 cars
        for car in range(6):
            self.labels.append(tk.Label(self.canvas, text = self.carInfos[int(index/2)][car]['brand'] + '\n' + self.carInfos[int(index/2)][car]['model'], wraplength=170))
        
        for car in range(3):
            self.canvas.create_image(15 + car*180, 40, anchor="nw", image=self.cars[int(index/2)][car], tags="place"+str(car))
            self.canvas.create_image(15 + car*180, 255, anchor="nw", image=self.cars[int(index/2)][3 + car], tags="place"+str(car+3))

            self.labels[car].place(x=15 + car*180,y=215)
            self.labels[3 + car].place(x=15 + car*180,y=430)


    # ------------------------------------- Get the country index based on mouse pos ----------------------------------
    def calculate_pos(self, x, y):
        print(f"Click la pozitia ({x}, {y})")

        if UndefinedSpace(x, y) or OceanulAtlantic(x, y) or OceanulIndian(x,y) or OceanulPacific(x,y):
            return -1
        elif y < 235:
            res_d1 = d1(x,y)
            if res_d1 < 0:
                return 1
            elif x > 435:
                return 5
            else:
                return 3
        elif y < 300:
            res_d1 = d1(x,y)
            res_d4 = d4(x,y)
            if res_d1 < 0:
                return 1
            elif res_d4 < 0:
                return 5
            else:
                return 4
        elif y < 324:
            res_d2 = d2(x,y)
            res_d4 = d4(x,y)
            if res_d2 > 0:
                return 2
            elif res_d4 > 0:
                return 4
            else:
                return 5
        else:
            res_d2 = d2(x,y)
            res_d3 = d3(x,y)
            if res_d2 > 0:
                return 2
            elif res_d3 > 0:
                return 6
            else:
                return 4
        
        
if __name__ == '__main__':
    root = tk.Tk()
    App = GUI(root)
    root.mainloop()
