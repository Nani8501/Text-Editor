import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
        self.dark_mode = False
        self.text = tk.Text(master, undo=True, bg="white", fg="black")
        self.text.pack(fill=tk.BOTH, expand=1)
        self.add_menu_bar()
        self.add_status_bar()

    def add_menu_bar(self):
        # create the menu bar
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Toggle Dark Mode", command=self.toggle_dark_mode)
        menu_bar.add_cascade(label="View", menu=view_menu)

        self.master.config(menu=menu_bar)

    def add_status_bar(self):
        self.status = tk.Label(self.master, text="")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        # track text changes
        self.text.bind('<KeyRelease>', self.update_status)

    def update_status(self, event=None):
        text = self.text.get('1.0', tk.END)
        words = len(text.split())
        lines = text.count('\n') + 1
        self.status.config(text=f"Words: {words} | Lines: {lines-1}")

    def new_file(self):
        self.text.delete('1.0', tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete('1.0', tk.END)
                self.text.insert(tk.END, file.read())
                self.update_status()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get('1.0', tk.END))

    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.text.configure(bg="#333333", fg="white")
            self.status.configure(bg="#333333", fg="white")
        else:
            self.text.configure(bg="white", fg="black")
            self.status.configure(bg="white", fg="black")

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
