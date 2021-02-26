
try:
    from tkinter import*
    from tkinter import ttk
    from tkinter import font
    import math
    import csv
except ImportError as error:
    print('Failed to import',error)


class ToolTip(object):
    '''An object to render tooltip on widgets '''
    def __init__(self,widget):
        self.widget=widget
        self.tip_window = None

    def Show_tip(self,tip_text):
        ''' Display the text in the tooltip'''
        if self.tip_window or not tip_text:
            return
        x,y,_cx,cy  = self.widget.bbox('insert')
        x  = x + self.widget.winfo_rootx() + 50
        y = y + cy + self.widget.winfo_rooty() + 50
        self.tip_window =tw=Toplevel(self.widget)
        tw.wm_overrideredirect(True)                 # remove all window manger decorations
        tw.wm_geometry("+%d+%d"%(x,y))
        label = Label(tw,text=tip_text,justify=LEFT,background='#ffffe0',relief=SOLID,borderwidth=1,font=('tahoma','8','normal'))
        label.pack(ipadx=1)

    def Hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()




class Scientific_Calculator(object):
    ''' A calculator object of type Scientific'''
    def __init__(self,master):
        master.geometry('400x500')
        master.title('Scientific calculator')
        application_font =font.Font(family='Fixedays',size=20)

        contianer_frame = ttk.Frame(master,padding=(5,5,10,10),borderwidth=10,relief=RAISED)
        global calculator_entry
        calculator_entry = ttk.Entry(contianer_frame,font=application_font)
        calculator_entry.focus_set()


        # styling
        style = ttk.Style()
        style.configure('container_frame',font='c',Fontsize=30)

        # digit Buttons

        Button_0= ttk.Button(contianer_frame,text='0',command= lambda :self.clicked_Button('0'))
        Button_1 = ttk.Button(contianer_frame,text='1',command= lambda :self.clicked_Button('1'))
        Button_2 = ttk.Button(contianer_frame,text='2',command= lambda :self.clicked_Button('2'))
        Button_3 = ttk.Button(contianer_frame,text='3',command= lambda :self.clicked_Button('3'))
        Button_4 = ttk.Button(contianer_frame,text='4',command= lambda :self.clicked_Button('4'))
        Button_5 = ttk.Button(contianer_frame,text='5',command= lambda :self.clicked_Button('5'))
        Button_6 = ttk.Button(contianer_frame,text='6',command= lambda :self.clicked_Button('6'))
        Button_7 = ttk.Button(contianer_frame,text='7',command= lambda :self.clicked_Button('7'))
        Button_8 = ttk.Button(contianer_frame,text='8',command= lambda :self.clicked_Button('8'))
        Button_9 = ttk.Button(contianer_frame,text='9',command= lambda :self.clicked_Button('9'))


        # operations buttons

        on_Button = ttk.Button(contianer_frame,text='on')
        enter_Button = ttk.Button(contianer_frame,text='enter',command=self.enter)
        sto_Button = ttk.Button(contianer_frame,text='sto ->')
        equality_sign_Button = ttk.Button(contianer_frame,text='<-->')
        x_variable_Button = ttk.Button(contianer_frame,text='X')

        addition_Button = ttk.Button(contianer_frame,text='+',command=self.addition)
        Button_negative_sign = ttk.Button(contianer_frame,text='(-)')
        Button_dot_sign = ttk.Button(contianer_frame,text='.')

        x_squre_Button = ttk.Button(contianer_frame,text='**',command=self.x_square)
        subtration_Button = ttk.Button(contianer_frame,text='-',command=self.subtraction)

        # row 5
        answer_squre = ttk.Button(contianer_frame,text='^')
        squre_negativ_one_Button = ttk.Button(contianer_frame,text='^-1')
        right_peranthes_Button = ttk.Button(contianer_frame,text='(')
        left_peranthes_Button = ttk.Button(contianer_frame,text=')')
        multiplication_Button = ttk.Button(contianer_frame,text='X',command=self.multiplication)

        # row 4
        pi_Button = ttk.Button(contianer_frame,text='pi',command=lambda :self.clicked_Button(str(math.pi)))
        sin_Button = ttk.Button(contianer_frame,text='sin',command=self.sin)
        cos_Button = ttk.Button(contianer_frame,text='cos',command=self.cos)
        tan_Button = ttk.Button(contianer_frame,text='tan',command= self.tan)
        division_Button = ttk.Button(contianer_frame,text='/',command=self.division)

        # row 3

        natural_log_Button = ttk.Button(contianer_frame,text='ln',command=self.n_log_x)
        rational_form_Button = ttk.Button(contianer_frame,text='n/d')
        x_10_squre_n_Button = ttk.Button(contianer_frame,text='x10^n')
        table_Button = ttk.Button(contianer_frame,text='table')
        clear_Button = ttk.Button(contianer_frame,text='Clear',command=self.clear_entry)

        # row 2
        log_Button = ttk.Button(contianer_frame,text='log',command=self.log_x)
        prb_Button = ttk.Button(contianer_frame,text='prb')
        data_Button = ttk.Button(contianer_frame,text='data')

        # row 1

        reverse_Button  = ttk.Button(contianer_frame,text='2nd')
        mode_Button = ttk.Button(contianer_frame,text='Mode')
        delete_Button = ttk.Button(contianer_frame,text='Delete')

        # direction button

        up_Button = ttk.Button(contianer_frame,text='Up',command=self.scroll_operation)
        dwon_dwon = ttk.Button(contianer_frame,text='Dwon')
        left_Button = ttk.Button(contianer_frame,text='Left')
        right_Button = ttk.Button(contianer_frame,text='Right')

        # griding widgets

        contianer_frame.grid(row=0,column=0,columnspan=5,rows=9,sticky=(W,S,N,E))
        calculator_entry.grid(row=0,column=0,columnspan=5,sticky=(N,W,S,E))

        # griding row 9
        on_Button.grid(row=9,column=0,sticky=(N,W,S,E))
        Button_0.grid(row=9,column=1,sticky=(N,W,S,E))
        Button_dot_sign.grid(row=9,column=2,sticky=(N,W,S,E))
        Button_negative_sign.grid(row=9,column=3,sticky=(N,W,S,E))
        enter_Button.grid(row=9,column=4,sticky=(N,W,S,E))

        # griding row 8

        sto_Button.grid(row=8,column=0,sticky=(N,W,S,E))
        Button_1.grid(row=8,column=1,sticky=(N,W,S,E))
        Button_2.grid(row=8,column=2,sticky=(N,W,S,E))
        Button_3.grid(row=8,column=3,sticky=(N,W,S,E))
        equality_sign_Button.grid(row=8,column=4,sticky=(N,W,S,E))

        #griding row 7
        x_variable_Button.grid(row=7,column=0,sticky=(N,W,S,E))
        Button_4.grid(row=7,column=1,sticky=(N,W,S,E))
        Button_5.grid(row=7,column=2,sticky=(N,W,S,E))
        Button_6.grid(row=7,column=3,sticky=(N,W,S,E))
        addition_Button.grid(row=7,column=4,sticky=(N,W,S,E))

        # griding row 6
        x_squre_Button.grid(row=6,column=0,sticky=(N,W,S,E))
        Button_7.grid(row=6,column=1,sticky=(N,W,S,E))
        Button_8.grid(row=6,column=2,sticky=(N,W,S,E))
        Button_9.grid(row=6,column=3,sticky=(N,W,S,E))
        subtration_Button.grid(row=6,column=4,sticky=(N,W,S,E))

        # griding row 5
        answer_squre.grid(row=5,column=0,sticky=(N,W,S,E))
        squre_negativ_one_Button.grid(row=5,column=1,sticky=(N,W,S,E))
        right_peranthes_Button.grid(row=5,column=2,sticky=(N,W,S,E))
        left_peranthes_Button.grid(row=5,column=3,sticky=(N,W,S,E))
        multiplication_Button.grid(row=5,column=4,sticky=(N,W,S,E))

        # griding row 3

        pi_Button.grid(row=4,column=0,sticky=(N,W,S,E))
        sin_Button.grid(row=4,column=1,sticky=(N,W,S,E))
        cos_Button.grid(row=4,column=2,sticky=(N,W,S,E))
        tan_Button.grid(row=4,column=3,sticky=(N,W,S,E))
        division_Button.grid(row=4,column=4,sticky=(N,W,S,E))

        #griding row 2
        natural_log_Button.grid(row=3,column=0,sticky=(N,W,S,E))
        rational_form_Button.grid(row=3,column=1,sticky=(N,W,S,E))
        x_10_squre_n_Button.grid(row=3,column=2,sticky=(N,W,S,E))
        table_Button.grid(row=3,column=3,sticky=(N,W,S,E))
        clear_Button.grid(row=3,column=4,sticky=(N,W,S,E))

        # griding 2
        log_Button.grid(row=2,column=0,sticky=(N,W,S,E))
        prb_Button.grid(row=2,column=1,sticky=(N,W,S,E))
        data_Button.grid(row=2,column=2,sticky=(N,W,S,E))
        dwon_dwon.grid(row=2,column=3,sticky=(N,W,S,E))
        right_Button.grid(row=2,column=4,sticky=(N,W,S,E))


        # griding row 1
        reverse_Button.grid(row=1,column=0,sticky=(N,W,S,E))
        mode_Button.grid(row=1,column=1,sticky=(N,W,S,E))
        delete_Button.grid(row=1,column=2,sticky=(N,W,S,E))
        up_Button.grid(row=1,column=3,sticky=(N,W,S,E))
        left_Button.grid(row=1,column=4,sticky=(N,W,S,E))


        # Button and frame configurations
        master.rowconfigure(0,weight=1)
        master.columnconfigure(0,weight=1)
        calculator_entry.columnconfigure(0,weight=1)

        # making buttons to reasize accordingly
        for column in range(5):
            contianer_frame.columnconfigure(column,weight=1)
        for row in range(10):
            contianer_frame.rowconfigure(row,weight=1)

        for childern in contianer_frame.winfo_children():
            self.tooltip(childern,'running on radians')


    def tooltip(self,widget,text):
        toolTip = ToolTip(widget)
        def enter(event):
            toolTip.Show_tip(text)
        def leave(event):
            toolTip.Hide_tip()
        widget.bind('<Enter>',enter)
        widget.bind('<Leave>',leave)



    def scroll_operation(self):
        calculator_entry.insert(0,str(self.get_last_operation()))
    def sin(self):
        ''' Returns sin of x measured in radians '''
        global state
        calculator_entry.delete(0,END)
        state = 'sin'

    def cos(self):
        ''' Returns cos of x measured in radians '''
        global state
        calculator_entry.delete(0,END)
        state = 'cos'

    def tan(self):
        ''' Returns tan of x measured in radians '''
        global state
        calculator_entry.delete(0,END)
        state = 'tan'

    def log_x(self):
        ''' set the state to the log '''
        global state
        calculator_entry.delete(0,END)
        state = 'log'

    def n_log_x(self):
        ''' Set the state to nlog = natural log '''
        global state
        calculator_entry.delete(0,END)
        state = 'nlog'

    def x_square(self):
        global state
        global first_num
        state = 'square'
        f_num = calculator_entry.get()
        if f_num:
            try:
                calculator_entry.delete(0,END)
                print(f_num)
                first_num = int(f_num)
            except ValueError as error:
                print('Invalid input',error)
        else:
            first_num = self.get_last_operation()

    def clicked_Button(self,first_num):
        ''' Method to enable the the calculator entry to output proper representation of n-digit decimal number
        '''
        global f_num
        global state
        f_num = calculator_entry.get()
        calculator_entry.delete(0,END)
        calculator_entry.insert(0,str(f_num)+first_num)

    def clear_entry(self):
        """ Clears the calculator entry """
        calculator_entry.delete(0,END)

    def multiplication(self):
        global state
        global first_num
        state = 'multiplication'
        f_num = calculator_entry.get()
        if f_num:
            try:
                calculator_entry.delete(0,END)
                print(f_num)
                first_num = int(f_num)
            except ValueError as error:
                print('Invalid input ,',error)
        else:
            first_num = self.get_last_operation()
    def division(self):
        global state
        global first_num
        state = 'division'
        f_num = calculator_entry.get()
        if f_num:
            try:
                calculator_entry.delete(0, END)
                first_num = int(f_num)
            except ValueError as error:
                print('Invalid input', error)
        else:
            first_num = self.get_last_operation()

    def subtraction(self):
        global state
        global first_num
        state = 'subtraction'
        f_num = calculator_entry.get()
        if f_num:
            try:
                calculator_entry.delete(0, END)
                first_num = int(f_num)
            except ValueError as error:
                print('Invalid input', error)
        else:
            first_num = self.get_last_operation()

    def addition(self):
        global state
        global first_num
        state = 'addition'
        f_num = calculator_entry.get()
        if f_num:
            try:
                calculator_entry.delete(0, END)
                first_num = int(f_num)
            except ValueError as error:
                print('Invalid input', error)
        else:
            first_num = self.get_last_operation()

    def save_history(self,operation):
        with open('backup.TXT','a') as history_file:
            history_file.write(operation+',')
        history_file.close()

    def get_last_operation(self):
        with open('backup.TXT','r') as last_operation:
            csv_reader = csv.reader(last_operation,delimiter=',')
            for operation in csv_reader:
                return (int(operation[-2]))
        last_operation.close()


    def enter(self):
        try:
            second_num = calculator_entry.get()
            #raise ValueError('Cannot accept any other type other than integer')
            calculator_entry.delete(0,END)
        except ValueError as error:
            print('only numeric values',error)
        else:
            if state == 'multiplication':
                try:
                    calculator_entry.insert(0,first_num*int(second_num))
                    self.save_history(str(first_num*int(second_num)))
                except ValueError as error:
                    calculator_entry.insert(0,'Invalid Value')
                    calculator_entry.after(1000,lambda :calculator_entry.delete(0,END))

            elif state == 'division':
                try:
                    calculator_entry.insert(0, first_num/int(second_num))
                    self.save_history(str(first_num/int(second_num)))
                except ValueError as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'addition':
                try:
                    calculator_entry.insert(0, first_num+int(second_num))
                    self.save_history(str(first_num+int(second_num)))
                except ValueError as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'subtraction':
                try:
                    calculator_entry.insert(0, first_num-int(second_num))
                    self.save_history(str(first_num-int(second_num)))
                except ValueError as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'sin':
                try:
                    calculator_entry.insert(0,str(math.sin(((int(second_num))))))
                    self.save_history(str(math.sin(((int(second_num))))))
                except (ValueError,ZeroDivisionError) as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'cos':
                try:
                    calculator_entry.insert(0,str(math.cos(((int(second_num))))))
                    self.save_history(str(math.cos(((int(second_num))))))
                except (ValueError, ZeroDivisionError) as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'tan':
                try:
                    calculator_entry.insert(0,str(math.tan(((int(second_num))))))
                    self.save_history(str(math.tan(((int(second_num))))))
                except (ValueError, ZeroDivisionError) as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'log':
                try:
                    calculator_entry.insert(0,str(math.log10(((int(second_num))))))
                except (ValueError, ZeroDivisionError) as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'nlog':
                try:
                    calculator_entry.insert(0,str(math.log(((int(second_num))))))
                    self.save_history(str(math.log(((int(second_num))))))
                except (ValueError, ZeroDivisionError) as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))

            elif state == 'square':
                try:
                    calculator_entry.insert(0,str(math.pow(first_num,int(second_num))))
                    self.save_history(str(math.pow(first_num,int(second_num))))
                except (ValueError, ZeroDivisionError) as error:
                    calculator_entry.insert(0, 'Invalid Value')
                    calculator_entry.after(1000, lambda: calculator_entry.delete(0, END))


if __name__ == '__main__':
    run_window = Tk()
    test_calculator = Scientific_Calculator(run_window)
    run_window.mainloop()


