from tkinter import *
import math, random, datetime


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

        #  Variables

        # Cosmetics
        self.soap = IntVar()
        self.faceCream = IntVar()
        self.faceWash = IntVar()
        self.hairSpray = IntVar()
        self.hairGel = IntVar()
        self.bodyLotion = IntVar()

        # Grocery
        self.rice = IntVar()
        self.vegetableOil = IntVar()
        self.pulses = IntVar()
        self.flour = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # Cold Drinks
        self.pepsi = IntVar()
        self.limca = IntVar()
        self.frooti = IntVar()
        self.mirinda = IntVar()
        self.thumbsUp = IntVar()
        self.sprite = IntVar()

        # total product price and tax variable

        self.cosmeticPrice = StringVar()
        self.groceryPrice = StringVar()
        self.coldDrinkPrice = StringVar()

        self.cosmeticTax = StringVar()
        self.groceryTax = StringVar()
        self.coldDrinkTax = StringVar()

        # Customer

        self.customerName = StringVar()
        self.customerPhone = StringVar()
        self.billNumber = StringVar()
        x = random.randint(1000,9999)
        self.billNumber.set(x)
        self.billDate = StringVar()
        date= datetime.date.today()
        self.billDate.set(date)

        # self.searchBill = StringVar()

        #  Customer Detail Frame
        F1 = LabelFrame(self.root, text='Customer Details', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F1.place(x=0, y=65, relwidth=1)

        customerNameLabel = Label(F1, text='Customer Name', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, padx=10)
        customerNameInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.customerName).grid(row=0, column=1, padx=10, pady=5)

        customerPhoneLabel = Label(F1, text='Phone', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=2, padx=10)
        customerPhoneInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.customerPhone).grid(row=0, column=3, padx=10, pady=5)

        customerBillLabel = Label(F1, text='Bill Number', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=4, padx=10)
        customerBillInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.billNumber).grid(row=0, column=5, padx=10, pady=5)

        billDateLabel = Label(F1, text='Date', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=6, padx=10)
        billDateInput = Entry(F1, width=15, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.billDate).grid(row=0, column=7, padx=10, pady=5)

        billButton = Button(F1, width=10, text='Search', font=f"{font1} 10 bold").grid(
            row=0, column=8, padx=30, pady=10)

        # Cosmetics
        F2 = LabelFrame(self.root, text='Cosmetics', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F2.place(x=0, y=150, width=300, height=300)

        bathLabel = Label(F2, text='Bath Soap', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, sticky='w')
        bathInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.soap).grid(row=0, column=1, padx=10, pady=10)

        faceCreamLabel = Label(F2, text='Face Cream', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=1, column=0, sticky='w')
        faceCreamInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.faceCream).grid(row=1, column=1, padx=10, pady=10)

        faceWashLabel = Label(F2, text='Face Wash', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=2, column=0, sticky='w')
        faceWashInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.faceWash).grid(row=2, column=1, padx=10, pady=10)

        hairSprayLabel = Label(F2, text='Hair Spray', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=3, column=0, sticky='w')
        hairSprayInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.hairSpray).grid(row=3, column=1, padx=10, pady=10)

        hairGelLabel = Label(F2, text='Hair Gel', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=4, column=0, sticky='w')
        hairGelInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.hairGel).grid(row=4, column=1, padx=10, pady=10)

        bodyLotionLabel = Label(F2, text='Body Lotion', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=5, column=0, sticky='w')
        hairLotionInput = Entry(F2, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.bodyLotion).grid(row=5, column=1, padx=10, pady=10)

        # Grocery
        F3 = LabelFrame(self.root, text='Groceries', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F3.place(x=305, y=150, width=300, height=300)

        riceLabel = Label(F3, text='Rice', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, sticky='w')
        riceInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.rice).grid(row=0, column=1, padx=10, pady=10)

        oilLabel = Label(F3, text='Vegetable Oil', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=1, column=0, sticky='w')
        oilInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.vegetableOil).grid(row=1, column=1, padx=10, pady=10)

        pulsesLabel = Label(F3, text='Pulses', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=2, column=0, sticky='w')
        pulsesInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.pulses).grid(row=2, column=1, padx=10, pady=10)

        flourLabel = Label(F3, text='flour', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=3, column=0, sticky='w')
        flourInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.flour).grid(row=3, column=1, padx=10, pady=10)

        sugarLabel = Label(F3, text='Sugar', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=4, column=0, sticky='w')
        sugarInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.sugar).grid(row=4, column=1, padx=10, pady=10)

        teaLabel = Label(F3, text='Tea', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=5, column=0, sticky='w')
        teaInput = Entry(F3, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.tea).grid(row=5, column=1, padx=10, pady=10)

        # Cold Drinks
        F4 = LabelFrame(self.root, text='Cold Drinks', font=(
            f'{font1}', 18, 'bold'), fg='white', bg=bg_color, bd=5, relief=GROOVE)
        F4.place(x=610, y=150, width=300, height=300,)

        pepsiLabel = Label(F4, text='Pepsi', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=0, column=0, sticky='w')
        pepsiInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.pepsi).grid(row=0, column=1, padx=10, pady=10)

        frootiLabel = Label(F4, text='Frooti', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=1, column=0, sticky='w')
        frootiInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.frooti).grid(row=1, column=1, padx=10, pady=10)

        thumbsUpLabel = Label(F4, text='Thumbs Up', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=2, column=0, sticky='w')
        thumbsUpInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.thumbsUp).grid(row=2, column=1, padx=10, pady=10)

        mirindaLabel = Label(F4, text='Mirinda', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=3, column=0, sticky='w')
        mirindaInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.mirinda).grid(row=3, column=1, padx=10, pady=10)

        spriteLabel = Label(F4, text='Sprite', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=4, column=0, sticky='w')
        spriteInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.sprite).grid(row=4, column=1, padx=10, pady=10)

        limcaLabel = Label(F4, text='Limca', bg=bg_color, fg='white', font=(
            f'{font1}', 15, 'bold')).grid(row=5, column=0, sticky='w')
        limcaInput = Entry(F4, width=10, font=(
            'arial 12'), bd=2, relief=SUNKEN, textvariable=self.limca).grid(row=5, column=1, padx=10, pady=10)

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
        F6 = LabelFrame(self.root, text='Bill Menu', bg=bg_color,
                        fg='white', font=f'{font1} 18 bold', bd=5, relief=GROOVE)
        F6.place(x=0, y=455, relwidth=1, relheight=1)

        cosmeticPrice = Label(F6, text='Total Cosmetic Price',
                              font=f'{font1} 15 bold', bg=bg_color, fg='white').grid(row=0, column=0, sticky=W)
        cosmeticPriceInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN, textvariable=self.cosmeticPrice).grid(
            row=0, column=1, padx=10, pady=5)

        cosmeticTax = Label(F6, text='Cosmetic Tax', font=f'{font1} 15 bold', bg=bg_color, fg='white').grid(
            row=0, column=2, sticky='w')
        cosmeticTaxInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN, textvariable=self.cosmeticTax).grid(
            row=0, column=3, padx=10, pady=5)

        groceryPrice = Label(F6, text='Total Grocery Price', font=f'{font1} 15 bold', bg=bg_color, fg='white').grid(
            row=1, column=0, sticky='w')
        groceryPriceInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN, textvariable=self.groceryPrice).grid(
            row=1, column=1, padx=10, pady=5)

        groceryTax = Label(F6, text='Grocery Tax', font=f'{font1} 15 bold', bg=bg_color, fg='white').grid(
            row=1, column=2, sticky='w')
        groceryTaxInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN, textvariable=self.groceryTax).grid(
            row=1, column=3, padx=10, pady=5)

        coldDrinkPrice = Label(F6, text='Total Cold Drink Price',
                               font=f'{font1} 15 bold', bg=bg_color, fg='white').grid(row=2, column=0, sticky='w')
        coldDrinkPriceInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN, textvariable=self.coldDrinkPrice).grid(
            row=2, column=1, padx=10, pady=10)

        coldDrinkTax = Label(F6, text='Cold Drink Tax', font=f'{font1} 15 bold', bg=bg_color, fg='white').grid(
            row=2, column=2, sticky='w')
        coldDrinkTaxInput = Entry(F6, width=10, font=f'{font1} 15 bold', bd=2, relief=SUNKEN, textvariable=self.coldDrinkTax).grid(
            row=2, column=3, padx=10, pady=10)

        buttonFrame = Frame(F6, bd=2, relief=GROOVE, bg='white',)
        buttonFrame.place(x=680, y=5, width=600, height=115)
        total = Button(buttonFrame, text='Total Amount', command=self.total,font=f'font1 18 bold', bg=bg_color,
                       fg='white', pady=20, padx=5).grid(row=0, column=0, padx=8, pady=10)
        generate = Button(buttonFrame, text='Generate Bill',command=self.billArea, font=f'font1 18 bold',
                          bg=bg_color, fg='white', pady=20, padx=5).grid(row=0, column=1, padx=8, pady=10)
        clear = Button(buttonFrame, text='Clear', font=f'font1 18 bold', bg=bg_color,
                       fg='white', pady=20, padx=5).grid(row=0, column=2, padx=8, pady=10)
        exit = Button(buttonFrame, text='Exit', font=f'font1 18 bold', bg=bg_color,
                      fg='white', pady=20, padx=5).grid(row=0, column=3, padx=8, pady=10)


    def total(self):

        self.soapPrice = self.soap.get()*30
        self.faceCreamPrice = self.faceCream.get()*50
        self.faceWashPrice = self.faceWash.get()*50
        self.hairSprayPrice = self.hairSpray.get()*100
        self.hairGelPrice = self.hairGel.get()*80
        self.bodyLotionPrice = self.bodyLotion.get()*100

        self.ricePrice = self.rice.get()*40
        self.vegetableOilPrice = self.vegetableOil.get()*140
        self.pulsesPrice = self.pulses.get()*100
        self.flourPrice = self.flour.get()*30
        self.sugarPrice = self.sugar.get()*40
        self.teaPrice = self.tea.get()*115

        self.pepsiPrice = self.pepsi.get()*90
        self.limcaPrice = self.limca.get()*40
        self.frootiPrice = self.frooti.get()*99
        self.mirindaPrice = self.mirinda.get()*65
        self.thumbsUpPrice = self.thumbsUp.get()*40
        self.spritePrice = self.sprite.get()*40

        self.totalCosmeticPrice = float(
            (self.soapPrice)+(self.faceCreamPrice)+(self.faceWashPrice) +
            (self.hairSprayPrice)+(self.hairGelPrice)+(self.bodyLotionPrice)
        )
        self.totalGroceryPrice = float(
            (self.ricePrice)+(self.pulsesPrice)+(self.flourPrice) +
            (self.vegetableOilPrice)+(self.sugarPrice)+(self.teaPrice)
        )
        self.totalColdDrinkPrice = float(
            (self.pepsiPrice)+(self.frootiPrice)+(self.mirindaPrice) +
            (self.limcaPrice)+(self.thumbsUpPrice)+(self.spritePrice)
        )

        self.totalCosmeticTax = float(self.totalCosmeticPrice*0.05)
        self.totalGroceryTax = float(self.totalGroceryPrice*0.05)
        self.totalColdDrinkTax = float(self.totalColdDrinkPrice*0.05)
        
        self.cosmeticPrice.set('Rs. '+str(self.totalCosmeticPrice))
        self.groceryPrice.set('Rs. '+str(self.totalGroceryPrice))
        self.coldDrinkPrice.set('Rs. '+str(self.totalColdDrinkPrice))
        
        self.cosmeticTax.set('Rs. '+str(self.totalCosmeticTax))
        self.groceryTax.set('Rs. '+str(self.totalGroceryTax))
        self.coldDrinkTax.set('Rs. '+str(self.totalColdDrinkTax))


    def welcomeBill(self):
        self.textArea.delete('1.0', END)
        self.textArea.insert(END,'\tWelcome To IshVer Retails')
        self.textArea.insert(END,'\n\n--------------------------------------------')
        self.textArea.insert(END,f'\n\nBill Number: {self.billNumber.get()}')
        self.textArea.insert(END,f'\nBill Date: {self.billDate.get()}')
        self.textArea.insert(END,f'\nCustomer Name: {self.customerName.get()}')
        self.textArea.insert(END,f'\nPhone Number: {self.customerPhone.get()}')
        self.textArea.insert(END,'\n\n--------------------------------------------')
        self.textArea.insert(END,f'\nProducts\t\tQty\t\tPrice')
        self.textArea.insert(END,'\n\n--------------------------------------------')

    def billArea(self):
        self.welcomeBill()
        if self.soap.get() != 0:
            self.textArea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\t{self.soapPrice}")
        if self.faceCream.get() != 0:
            self.textArea.insert(END,f"\nFace Cream\t\t{self.faceCream.get()}\t\t{self.faceCreamPrice}")
        if self.faceWash.get() != 0:
            self.textArea.insert(END,f"\nFace Wash\t\t{self.faceWash.get()}\t\t{self.faceWashPrice}")
        if self.hairGel.get() != 0:
            self.textArea.insert(END,f"\nHair Gel\t\t{self.hairGel.get()}\t\t{self.hairGelPrice}")
        if self.hairSpray.get() != 0:
            self.textArea.insert(END,f"\nHair Spray\t\t{self.hairSpray.get()}\t\t{self.hairSprayPrice}")
        if self.bodyLotion.get() != 0:
            self.textArea.insert(END,f"\nBody Lotion\t\t{self.bodyLotion.get()}\t\t{self.bodyLotionPrice}")
            
        if self.frooti.get() != 0:
            self.textArea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t\t{self.frootiPrice}")
        if self.limca.get() != 0:
            self.textArea.insert(END,f"\nLimca\t\t{self.limca.get()}\t\t{self.limcaPrice}")
        if self.thumbsUp.get() != 0:
            self.textArea.insert(END,f"\nThumbs Up\t\t{self.thumbsUp.get()}\t\t{self.thumbsUpPrice}")
        if self.sprite.get() != 0:
            self.textArea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t\t{self.spritePrice}")
        if self.mirinda.get() != 0:
            self.textArea.insert(END,f"\nMirinda\t\t{self.mirinda.get()}\t\t{self.mirindaPrice}")
        if self.pepsi.get() != 0:
            self.textArea.insert(END,f"\nPepsi\t\t{self.pepsi.get()}\t\t{self.pepsiPrice}")

        if self.rice.get() != 0:
            self.textArea.insert(END,f"\nRice\t\t{self.rice.get()}\t\t{self.ricePrice}")
        if self.pulses.get() != 0:
            self.textArea.insert(END,f"\nPulses\t\t{self.pulses.get()}\t\t{self.pulsesPrice}")
        if self.flour.get() != 0:
            self.textArea.insert(END,f"\nFlour\t\t{self.flour.get()}\t\t{self.flourPrice}")
        if self.tea.get() != 0:
            self.textArea.insert(END,f"\nTea\t\t{self.tea.get()}\t\t{self.teaPrice}")
        if self.vegetableOil.get() != 0:
            self.textArea.insert(END,f"\nVegetable Oil\t\t{self.vegetableOil.get()}\t\t{self.vegetableOilPrice}")
        if self.sugar.get() != 0:
            self.textArea.insert(END,f"\nBath Soap\t\t{self.sugar.get()}\t\t{self.sugarPrice}")


root = Tk()
ob = BillingApp(root)
root.mainloop()


'''


'''
