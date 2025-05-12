import tkinter as tk

def on_frame_leave(event):
    # Afișează un mesaj când mouse-ul părăsește frame-ul, dar nu interacționează cu copii
    print("Mouse-ul a părăsit frame-ul!")

def on_child_enter(event):
    # Când mouse-ul intră pe un widget copil, prevenim propagarea evenimentului leave
    event.widget.bind("<Enter>", lambda e: e.widget.master.bind("<Leave>", lambda e: None))

def on_child_leave(event):
    # Când mouse-ul părăsește widget-ul copil, permitem propagarea evenimentului leave pentru frame
    event.widget.master.bind("<Leave>", on_frame_leave)

root = tk.Tk()
root.geometry("400x300")

# Creăm un frame
frame = tk.Frame(root, width=300, height=200, bg="lightblue")
frame.pack(pady=50)

# Creăm câteva obiecte (labeluri) în frame
for i in range(3):
    label = tk.Label(frame, text=f"Label {i+1}", bg="yellow", width=20, height=2)
    label.pack(pady=10)

    # Legăm evenimentele pe obiecte copil
    label.bind("<Enter>", on_child_enter)  # Când intră pe label
    label.bind("<Leave>", on_child_leave)  # Când iese de pe label

# Legăm evenimentul de leave pentru frame
frame.bind("<Leave>", on_frame_leave)

root.mainloop()
