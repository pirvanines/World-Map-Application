tari = ["America de Nord", "America de Sud", "Europa", "Africa", "Asia", "Australia"]
state = 0

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
            self.canvas.create_rectangle(
                10, 30, width_info, height_info, 
                fill="lightblue",  
                outline="black",  
                stipple="gray50",  
                tags="infos"
            )

            image_x = width_info + 10
            image_y = height_info

            self.canvas.create_image(image_x, 30, anchor="nw", image=self.story_teller, tags="storry_teller")
            self.canvas.story_t = self.story_teller

            self.place(self.close_info_button, 529, 35)
            self.deactivate_mouse_event()

            self.print_infos(index)
        
        else:
            messagebox.showerror("Eroare", "Atentie:\n\nNu segasesc producatori pe acest continent...")

    

    



