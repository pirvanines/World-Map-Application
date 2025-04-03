import tkinter as tk

def fake_bsod():
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Fullscreen
    root.configure(bg="blue")  # Fundal albastru

    label = tk.Label(root, text=":(\nYour PC ran into a problem and needs to restart.", 
                     fg="white", bg="blue", font=("Consolas", 24), justify="center")
    label.pack(expand=True)

    root.bind("<Escape>", lambda e: root.destroy())  # Inchide cu Escape
    root.mainloop()

fake_bsod()