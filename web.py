from tkinter import *

import webview

root = Tk()
root.geometry("700x350")


webview.create_window('Ayuda', 'ventana.html')
webview.start()

root.mainloop()