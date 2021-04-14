from tkinter import*


class QRGenerator:
    def __init__(self, root):
        self.root = root
        # setting the dimension of window
        self.root.geometry("900x500+200+50")
        # providing the title for the window
        self.root.title('Q R Generator | Developed by.get() ishVer')
        # Restricting the size of window
        self.root.resizable(False, False)
        title = Label(self.root, text='Qr Code Generator', font=(
            'times new roman', 30), bg='#07ad39', fg='white', anchor='w').place(x=0, y=0, relwidth=1)

        # Variables for text fields
        self.rollNumber = StringVar()
        self.name = StringVar()
        self.branch = StringVar()
        self.year = StringVar()
        

        #  Student Details Window

        studentFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        studentFrame.place(x=50, y=100, width=500, height=380)

        studentTitle = Label(studentFrame, text='Student Details', font=(
            'goudy old style', 20), bg='#09ad37', fg='white')
        studentTitle.place(x=0, y=0, relwidth=1)

        studentId = Label(studentFrame, text='Student Roll Number', font=(
            'times new roman', 15, 'bold'), bg='white', fg='navyblue')
        studentId.place(x=20, y=50)

        studentName = Label(studentFrame, text='Student Name', font=(
            'times new roman', 15, 'bold'), bg='white', fg='navyblue')
        studentName.place(x=20, y=100)

        studentBranch = Label(studentFrame, text='Student Branch', font=(
            'times new roman', 15, 'bold'), bg='white', fg='navyblue')
        studentBranch.place(x=20, y=150)

        currentYear = Label(studentFrame, text='Current Year', font=(
            'times new roman', 15, 'bold'), bg='white', fg='navyblue')
        currentYear.place(x=20, y=200)

        inputStudentId = Entry(studentFrame, textvariable=self.rollNumber, font=(
            'times new roman', 15), bg='lightyellow', fg='red')
        inputStudentId.place(x=210, y=50)

        inputStudentName = Entry(studentFrame, textvariable=self.name,  font=(
            'times new roman', 15), bg='lightyellow', fg='red')
        inputStudentName.place(x=210, y=100)

        inputStudentBranch = Entry(studentFrame, textvariable=self.branch, font=(
            'times new roman', 15), bg='lightyellow', fg='red')
        inputStudentBranch.place(x=210, y=150)

        inputCurrentYear = Entry(studentFrame, textvariable=self.year, font=(
            'times new roman', 15), bg='lightyellow', fg='red')
        inputCurrentYear.place(x=210, y=200)

        qrButton = Button(studentFrame, text='Generate QR Code', command=self.generate, font=(
            'goudy old style', 15), bg='green', fg='white')
        qrButton.place(x=100, y=250, width=180, height=30)

        clearButton = Button(studentFrame, text='Clear', command=self.clear, font=(
            'goudy old style', 15), bg='maroon', fg='white')
        clearButton.place(x=310, y=250, width=100, height=30)

        self.msg = '' #QR Code Generated Successfully!!!
        self.labelMsg = Label(studentFrame, text=self.msg, font=(
            'goudy old style', 20), fg='green', bg='white')
        self.labelMsg.place(x=0, y=300, relwidth=1)

        # QR Code Frame
        qrCodeFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qrCodeFrame.place(x=600, y=100, width=250, height=380)

        qrCodeTitle = Label(qrCodeFrame, text='Student QR Code', font=(
            'goudy old style', 20), bg='#09ad37', fg='white')
        qrCodeTitle.place(x=0, y=0, relwidth=1)

        qrCodeLabel = Label(qrCodeFrame, text='QR Code \n Not Available', font=('goudy old style', 20, 'bold'), bg='lightyellow', fg='navyblue', bd=2, relief=RIDGE)
        qrCodeLabel.place(x=25, y=100, width=200, height=200)

    def clear(self):
        self.rollNumber.set('')
        self.name.set('')
        self.branch.set('')
        self.year.set('')
        self.msg = ''
        self.labelMsg.config(text=self.msg)


    def generate(self):
        if self.rollNumber.get()=='' or self.name.get()=='' or self.branch.get()=='' or self.year.get()=='':
            self.msg = 'All fields must be required!!!'
            self.labelMsg.config(text=self.msg, fg='red')
        else:
            self.msg = 'QR Code Generated Successfully!!!'
            self.labelMsg.config(text=self.msg, fg='green')

root = Tk()
ob = QRGenerator(root)
root.mainloop()
