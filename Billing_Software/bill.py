from tkinter import *


class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x680+0+0")
        self.root.title('Billing App')

root = Tk()
ob = BillingApp(root)
root.mainloop()