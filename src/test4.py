try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

root = tk.Tk()

MainFrame = tk.Frame(root, width=385, height=460)
LabelFrame = tk.Frame(MainFrame, width=375, height=115, relief='raised', borderwidth=3)
ButtonFrame = tk.Frame(MainFrame, width=375, height=330, relief='raised', borderwidth=3)

some_label = tk.Label(LabelFrame, text='Simple Text')
some_button = tk.Button(ButtonFrame, text='Quit', command=root.destroy)

for frame in [MainFrame, LabelFrame, ButtonFrame]:
    frame.pack(expand=True, fill='both')
    frame.pack_propagate(0)

for widget in [some_label, some_button]:
    widget.pack(expand=True, fill='x', anchor='s')

root.mainloop()