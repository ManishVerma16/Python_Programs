from tkinter import *


class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x650+0+0")
        self.root.title('Billing App')

        bg_color = '#2fcaed'
        font1 = 'Rockwell'
        font2 = 'Times'
        title = Label(self.root, text='Billing App', font=(f'{font1}', 30, 'bold'),
                      bd=5, relief=GROOVE, bg=bg_color, fg='white', pady=2).pack(fill=X)

        #  Customer Detail Frame
        F1 = LabelFrame(self.root, text='Customer Details', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F1.place(x=0, y=65, relwidth=1)

        customerNameLabel = Label(F1, text='Customer Name', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, padx=20)
        customerNameInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        customerPhoneLabel = Label(F1, text='Phone', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=2, padx=20)
        customerPhoneInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        customerBillLabel = Label(F1, text='Bill Number', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=4, padx=20)
        customerBillInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        billButton = Button(F1, width=10, text='Search', font=f"{font1} 10 bold").grid(
            row=0, column=6, padx=30, pady=10)

        # Cosmetics
        F2 = LabelFrame(self.root, text='Cosmetics', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F2.place(x=0, y=150, width=300, height=300)

        bathLabel = Label(F2, text='Bath Soap', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, sticky='w')
        bathInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        faceCreamLabel = Label(F2, text='Face Cream', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=1, column=0, sticky='w')
        faceCreamInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        faceWashLabel = Label(F2, text='Face Wash', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=2, column=0, sticky='w')
        faceWashInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        hairSprayLabel = Label(F2, text='Hair Spray', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=3, column=0, sticky='w')
        hairSprayInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        hairGelLabel = Label(F2, text='Hair Gel', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=4, column=0, sticky='w')
        hairGelInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        bodyLotionLabel = Label(F2, text='Body Lotion', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=5, column=0, sticky='w')
        hairLotionInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Grocery
        F3 = LabelFrame(self.root, text='Groceries', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F3.place(x=305, y=150, width=300, height=300)

        bathLabel = Label(F3, text='Bath Soap', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, sticky='w')
        bathInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        oilLabel = Label(F3, text='Vegetable Oil', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=1, column=0, sticky='w')
        oilInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        pulsesLabel = Label(F3, text='Pulses', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=2, column=0, sticky='w')
        pulsesInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        wheatLabel = Label(F3, text='Wheat', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=3, column=0, sticky='w')
        wheatInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        sugarLabel = Label(F3, text='Sugar', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=4, column=0, sticky='w')
        sugarInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        teaLabel = Label(F3, text='Tea', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=5, column=0, sticky='w')
        teaInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Cold Drinks
        F4 = LabelFrame(self.root, text='Cold Drinks', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F4.place(x=610, y=150, width=300, height=300,)

        pepsiLabel = Label(F4, text='Pepsi', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, sticky='w')
        pepsiInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        frootiLabel = Label(F4, text='Frooti', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=1, column=0, sticky='w')
        frootiInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        thumbsUpLabel = Label(F4, text='Thumbs Up', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=2, column=0, sticky='w')
        thumbsUpInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        mirindaLabel = Label(F4, text='Mirinda', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=3, column=0, sticky='w')
        mirindaInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        spriteLabel = Label(F4, text='Sprite', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=4, column=0, sticky='w')
        spriteInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        limcaLabel = Label(F4, text='Limca', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=5, column=0, sticky='w')
        limcaInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # Bill Area
        F5 = Frame(self.root, bg='white', bd=5, relief=GROOVE)
        F5.place(x=915, y=150, relwidth=0.3, height=300)

        billTitle = Label(
            F5, text='Bill Area', font=f'{font1} 13 bold', bd=2, relief=GROOVE, bg=bg_color, fg='white').pack(fill=X)
        scrollY = Scrollbar(F5, orient=VERTICAL)
        self.textArea = Text(F5, yscrollcommand=scrollY.set)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.textArea.yview)
        self.textArea.pack(fill=BOTH, expand=1)

        # Bill Menu
        F6 = LabelFrame(self.root, text='Bill Menu', bg=bg_color,fg='white', font=f'{font1} 18 bold', bd=5, relief=GROOVE)
        F6.place(x=0, y=455, relwidth=1, relheight=1)

        cosmeticPrice = Label(F6, text='Total Cosmetic Price', font=f'{font1} 15 bold', bg=bg_color, fg='white' ).grid(row=0, column=0, sticky=W)
        cosmeticPriceInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        cosmeticTax = Label(F6, text='Cosmetic Tax', font=f'{font1} 15 bold', bg=bg_color, fg='white' ).grid(row=0, column=2, sticky='w')
        cosmeticTaxInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)
        
        groceryPrice = Label(F6, text='Total Grocery Price', font=f'{font1} 15 bold', bg=bg_color, fg='white' ).grid(row=1, column=0, sticky='w')
        groceryPriceInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)

        groceryTax = Label(F6, text='Grocery Tax', font=f'{font1} 15 bold', bg=bg_color, fg='white' ).grid(row=1, column=2, sticky='w')
        groceryTaxInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=5)
        
        coldDrinkPrice = Label(F6, text='Total Cold Drink Price', font=f'{font1} 15 bold', bg=bg_color, fg='white' ).grid(row=2, column=0, sticky='w')
        coldDrinkPriceInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        coldDrinkTax = Label(F6, text='Cold Drink Tax', font=f'{font1} 15 bold', bg=bg_color, fg='white' ).grid(row=2, column=2, sticky='w')
        coldDrinkTaxInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)

        buttonFrame = Frame(F6, bd=2, relief=GROOVE, bg='white',)
        buttonFrame.place(x=680, y=5, width=600, height=115)
        total = Button(buttonFrame, text='Total Amount',font=f'font1 18 bold', bg=bg_color, fg='white', pady=20, padx=5).grid(row=0, column=0, padx=8, pady=10)
        generate = Button(buttonFrame, text='Generate Bill',font=f'font1 18 bold', bg=bg_color, fg='white', pady=20, padx=5).grid(row=0, column=1, padx=8, pady=10)
        clear = Button(buttonFrame, text='Clear', font=f'font1 18 bold', bg=bg_color, fg='white', pady=20, padx=5).grid(row=0, column=2, padx=8, pady=10)
        exit = Button(buttonFrame, text='Exit', font=f'font1 18 bold', bg=bg_color, fg='white', pady=20, padx=5).grid(row=0, column=3, padx=8, pady=10)

root = Tk()
ob = BillingApp(root)
root.mainloop()


'''


'''