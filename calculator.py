#this program aims to recreate a simple calculator app

#import tkinter and tkk
import tkinter
from tkinter import ttk
from tkinter.constants import END, FALSE

#main function will create gui window, objects, start mainloop
def main():
    #run instance
    instance = Calculator_Gui()
    #setup main loop   
    tkinter.mainloop()

#create gui class
class Calculator_Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.memory = tkinter.StringVar()
        self.memory2 = tkinter.StringVar()
        self.operator = tkinter.StringVar()
        #self.reg = self.main_window.register(self.check_digit)
        self.create_objects()
        
       
    def create_objects(self):
        #create frames
        self.clear_frame = ttk.Frame(self.main_window)
        self.display_frame = tkinter.Frame(self.main_window)
        self.number123_frame = tkinter.Frame(self.main_window)
        self.number456_frame = tkinter.Frame(self.main_window)
        self.number789_frame = tkinter.Frame(self.main_window)
        self.number0_frame = tkinter.Frame(self.main_window)
        self.functional_frame = tkinter.Frame(self.main_window)
       
        #create and pack display frame
        self.memory_box = ttk.Entry(self.display_frame,textvariable=self.memory, width =15)
        #self.memory_box.config(validate="key",validatecommand=(self.reg,"%P",'%d'))
        self.memory_box2 = ttk.Label(self.display_frame,textvariable=self.memory2, width=15)
        self.operator_box = ttk.Label(self.display_frame,textvariable=self.operator, width=1)

        #keyboard bind upon hitting enter run self.calculate_event
        self.memory_box.bind('<Return>', lambda event: self.calculate())
        self.memory_box.bind('+', lambda event: self.add())
        self.memory_box.bind('-', lambda event: self.minus())
        self.memory_box.bind('*', lambda event: self.multiply())
        self.memory_box.bind('/', lambda event: self.divide())
        #self.memory_box.bind('.', lambda event: self.decimal())
        self.memory_box.bind("<KeyRelease>",lambda event: self.change()) #keyup 
        #pack display frame
        self.memory_box.pack()
        self.memory_box2.pack()
        self.operator_box.pack()

        #create clear button and +/- frame
        self.clear_button = ttk.Button(self.clear_frame,text="C",command=self.clear)
        self.clearentry_button = ttk.Button(self.clear_frame, text="CE", command=self.clear_entry)
        self.toggle = ttk.Button(self.clear_frame,text="+/-",command=self.toggle)

        #pack clear_button
        self.clear_button.pack(side="left")
        self.clearentry_button.pack(side="left")
        self.toggle.pack(side="left")

        #create the buttons 123
        self.button1 = ttk.Button(self.number123_frame,text="1",command=self.button_1)
        self.button2 = ttk.Button(self.number123_frame,text="2",command=self.button_2)
        self.button3 = ttk.Button(self.number123_frame,text="3",command=self.button_3)
        self.button_plus = ttk.Button(self.number123_frame,text="+",command=self.add)
        
        #pack the buttons123+
        self.button1.pack(side="left")
        self.button2.pack(side="left")
        self.button3.pack(side="left")
        self.button_plus.pack(side="left")
        
        #create the buttons 456
        self.button4 = ttk.Button(self.number456_frame,text="4",command=self.button_4)
        self.button5 = ttk.Button(self.number456_frame,text="5",command=self.button_5)
        self.button6 = ttk.Button(self.number456_frame,text="6",command=self.button_6)
        self.button_minus = ttk.Button(self.number456_frame,text="-",command=self.minus)

        #pack the buttons456
        self.button4.pack(side="left")
        self.button5.pack(side="left")
        self.button6.pack(side="left")
        self.button_minus.pack(side="left")
        
        #create the buttons 789
        self.button7 = ttk.Button(self.number789_frame,text="7",command=self.button_7)
        self.button8 = ttk.Button(self.number789_frame,text="8",command=self.button_8)
        self.button9 = ttk.Button(self.number789_frame,text="9",command=self.button_9)
        self.button_times = ttk.Button(self.number789_frame,text="*",command=self.multiply)

        #pack the buttons789
        self.button7.pack(side="left")
        self.button8.pack(side="left")
        self.button9.pack(side="left")
        self.button_times.pack(side="left")
        
        #create the buttons 0 equal .
        self.button0 = ttk.Button(self.number0_frame,text="0",command=self.button_0)
        self.button_equal =ttk.Button(self.number0_frame,text="=",command=self.calculate)
        self.button_decimal = ttk.Button(self.number0_frame,text='.',command=self.decimal)
        self.button_divide = ttk.Button(self.number0_frame,text="/",command=self.divide)

        #pack the buttons0
        self.button_equal.pack(side='left')
        self.button0.pack(side="left")
        self.button_decimal.pack(side="left")
        self.button_divide.pack(side="left")

        #pack the frames
        self.display_frame.pack()
        self.clear_frame.pack()
        self.number123_frame.pack()
        self.number456_frame.pack()
        self.number789_frame.pack()
        self.number0_frame.pack()
        
        self.memory_box.focus()
    #validate string
    def change(self, event=None):
        print("called")
        
        string = str(self.memory.get())
        print(string)
        string2 = ""
        count = 0
        for letter in string:
            if letter.isdigit():
                print('if')
                string2 = string2 + letter
            elif letter == ".":
                if count == 0:
                    print(count)
                    string2 = string2 + letter    
                    count +=1
                
            
        self.memory.set(string2)
        print(string2)

                  
    #add a number to entry widget based on hitting one of the calculator buttons
    def button_1(self):
        string = self.memory.get() + "1"
        self.memory.set(string)
        self.memory_box.focus()
    def button_2(self):
        string = self.memory.get() + "2"
        self.memory.set(string)
        self.memory_box.focus()
    def button_3(self):
        string = self.memory.get() + "3"
        self.memory.set(string)
        self.memory_box.focus()
    def button_4(self):
        string = self.memory.get() + "4"
        self.memory.set(string)
        self.memory_box.focus()
    def button_5(self):
        string = self.memory.get() + "5"
        self.memory.set(string)
        self.memory_box.focus()
    def button_6(self):
        string = self.memory.get() + "6"
        self.memory.set(string)
        self.memory_box.focus()
    def button_7(self):
        string = self.memory.get() + "7"
        self.memory.set(string)
        self.memory_box.focus()
    def button_8(self):
        string = self.memory.get() + "8"
        self.memory.set(string)
        self.memory_box.focus()
    def button_9(self):
        string = self.memory.get() + "9"
        self.memory.set(string)
        self.memory_box.focus()
    def button_0(self):
        string = self.memory.get() + "0"
        self.memory.set(string)
        self.memory_box.focus()
    def decimal(self,event=None):
        lock = ''
        string = self.memory.get()
        print(string)
        
        for letter in string:
            if letter == ".":
                lock = True
        if lock == True:
            print("too many decimals")   
            

        else:
            string = string + "."
            self.memory.set(string)

            


    
    #operator functions
    def add(self,event=None):
        if self.memory.get() != '':
            first_digit = float(self.memory.get())
            self.memory2.set(first_digit)
            self.operator.set('+')
            self.memory.set('')
            self.memory_box.focus()
    def minus(self,event=None):
        if self.memory.get() !="":
            first_digit =float(self.memory.get())
            self.memory2.set(first_digit)
            self.operator.set('-')
            self.memory.set('')
            self.memory_box.focus()
    def multiply(self,event=None):
        if self.memory.get() !="":
            first_digit =float(self.memory.get())
            self.memory2.set(first_digit)
            self.operator.set('*')
            self.memory.set('')
            self.memory_box.focus()
    def divide(self,event=None):
        if self.memory.get() !="":
            first_digit =float(self.memory.get())
            self.memory2.set(first_digit)
            self.operator.set('/')
            self.memory.set('')
            self.memory_box.focus()        
    def calculate(self):
        if self.operator.get() == '+':
            result = float(self.memory.get()) + float(self.memory2.get()) 
        elif self.operator.get() == '-':
            result = float(self.memory2.get()) - float(self.memory.get())
        elif self.operator.get() == '*':
            result = float(self.memory2.get()) * float(self.memory.get())  
            
        elif self.operator.get() == '/':
            result = float(self.memory2.get()) / float(self.memory.get())
        
        self.clear_entry
        self.memory.set(result)
        self.memory2.set('')
        self.operator.set('')    
    def clear(self):
        self.memory.set('')
        self.memory2.set('')
        self.operator.set('')
        self.memory_box.focus()
    def clear_entry(self):
        self.memory.set('')
        self.memory_box.focus()
    """def check_digit(self,p,d):
        
        if p.isdigit():
            return True 
       
        else:
            return False"""
        
    def toggle(self):
        try:
            current = float(self.memory.get())
            if current !="":
                toggled = current *-1
                self.memory.set(str(toggled))
                self.memory_box.focus()
        except ValueError:
            self.memory_box.focus()
if __name__ == "__main__":
    main()

            



        
        
