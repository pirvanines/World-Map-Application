import tkinter as tk

class Window():
    def __init__(self, master):
        master.geometry('100x100')

        # --- frame 1 --- #
        frame1 = tk.Frame(master, bg='blue')
        frame1.pack(fill='both', expand=1)
        frame1.bind('<Button-1>', lambda event: self.callback(event, 1))

        label1 = tk.Label(frame1, text='Label 1 in frame 1')
        label1.pack()

        label2 = tk.Label(frame1, text='Label 2 in frame 1')
        label2.pack()

        # you can get the child widgets inside the frame and set callback
        for child_widget in frame1.winfo_children():
            child_widget.bind('<Button-1>', lambda event: self.callback(event, 1))
            
        # --- frame 1 --- #

        # --- frame 2 --- #
        frame2 = tk.Frame(master, bg='white')
        frame2.pack(fill='both', expand=1)
        frame2.bind('<Enter>', lambda event: self.callback(event, 2))

        label1 = tk.Label(frame2, text='Label 1 in frame 2')
        label1.pack()

        label2 = tk.Label(frame2, text='Label 2 in frame 2')
        label2.pack()

        # you can get the child widgets inside the frame and set callback
        #for child_widget in frame2.winfo_children():
        #    child_widget.bind('<Enter>', lambda event: self.callback(event, 2))
        # --- frame 2 --- #

    def callback(self, event, index):
        print(str(event.x) + " "+ str(index))

root = tk.Tk()
Window(root)
root.mainloop()