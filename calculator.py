#this program aims to recreate a simple calculator app

#import tkinter and tkk
import tkinter
from tkinter import ttk


#main function will create gui window, objects, start mainloop
def main():
    instance = Calculator_Gui()
   
    tkinter.mainloop()

#create gui class
class Calculator_Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.create_objects()


    def create_objects(self):
        #create frames
        self.clear_frame = ttk.Frame(self.main_window)
        self.display_frame = tkinter.Frame(self.main_window)
        self.number123_frame = tkinter.Frame(self.main_window)
        self.number456_frame = tkinter.Frame(self.main_window)
        self.number789_frame = tkinter.Frame(self.main_window)
        self.number0_frame = tkinter.Frame(self.main_window)
        self.operations_frame = tkinter.Frame(self.main_window)
        self.functional_frame = tkinter.Frame(self.main_window)

        #create and pack display frame
        self.memory = tkinter.StringVar()
        self.memory2 = tkinter.StringVar()
        self.operator = tkinter.StringVar()

        self.memory_box = ttk.Entry(self.display_frame,textvariable=self.memory, width =15)
        self.memory_box2 = ttk.Label(self.display_frame,textvariable=self.memory2, width=15)
        self.operator_box = ttk.Label(self.display_frame,textvariable=self.operator, width=1)

        #keyboard bind upon hitting enter run self.calculate_event
        self.memory_box.bind('<Return>', self.calculate_event)

        #pack display frame
        self.memory_box.pack()
        self.memory_box2.pack()
        self.operator_box.pack()


        #create the buttons 123
        self.button1 = ttk.Button(self.number123_frame,text="1",command=self.button_1)
        self.button2 = ttk.Button(self.number123_frame,text="2",command=self.button_2)
        self.button3 = ttk.Button(self.number123_frame,text="3",command=self.button_3)
        
        #pack the buttons123
        self.button1.pack(side="left")
        self.button2.pack(side="left")
        self.button3.pack(side="left")
        
        #create the buttons 456
        self.button4 = ttk.Button(self.number456_frame,text="4",command=self.button_4)
        self.button5 = ttk.Button(self.number456_frame,text="5",command=self.button_5)
        self.button6 = ttk.Button(self.number456_frame,text="6",command=self.button_6)

        #pack the buttons456
        self.button4.pack(side="left")
        self.button5.pack(side="left")
        self.button6.pack(side="left")
        
        #create the buttons 789
        self.button7 = ttk.Button(self.number789_frame,text="7",command=self.button_7)
        self.button8 = ttk.Button(self.number789_frame,text="8",command=self.button_8)
        self.button9 = ttk.Button(self.number789_frame,text="9",command=self.button_9)

        #pack the buttons789
        self.button7.pack(side="left")
        self.button8.pack(side="left")
        self.button9.pack(side="left")
        
        
        #create the buttons 0 equal .
        self.button0 = ttk.Button(self.number0_frame,text="0",command=self.button_0)
        self.button_equal =ttk.Button(self.number0_frame,text="=",command=self.calculate)
        self.button_decimal = ttk.Button(self.number0_frame,text='.',command=self.decimal)

        #create key bind for button_equal to run when enter is hit on keyboard
        

        #pack the buttons0
        self.button_equal.pack(side='left')
        self.button0.pack(side="left")
        self.button_decimal.pack(side="left")

        #create the operator buttons + - * /
        
        self.button_plus = ttk.Button(self.operations_frame,text="+",command=self.add)

        #pack operator buttons to operations frame
        self.button_plus.pack()

        #pack the frames
        self.display_frame.pack()
        self.number123_frame.pack()
        self.number456_frame.pack()
        self.number789_frame.pack()
        self.number0_frame.pack()
        self.operations_frame.pack()
        self.functional_frame.pack()
        self.memory_box.focus()
    #add a number to entry widget based on hitting one of the calculator buttons
    def button_1(self):
        string = self.memory.get() + "1"
        self.memory.set(string)
    def button_2(self):
        string = self.memory.get() + "2"
        self.memory.set(string)
    def button_3(self):
        string = self.memory.get() + "3"
        self.memory.set(string)
    def button_4(self):
        string = self.memory.get() + "4"
        self.memory.set(string)
    def button_5(self):
        string = self.memory.get() + "5"
        self.memory.set(string)
    def button_6(self):
        string = self.memory.get() + "6"
        self.memory.set(string)
    def button_7(self):
        string = self.memory.get() + "7"
        self.memory.set(string)
    def button_8(self):
        string = self.memory.get() + "8"
        self.memory.set(string)
    def button_9(self):
        string = self.memory.get() + "9"
        self.memory.set(string)
    def button_0(self):
        string = self.memory.get() + "0"
        self.memory.set(string)
    def decimal(self):
        string = self.memory.get() + "."
        self.memory.set(string)
    
    #operator functions
    def add(self):
        if self.memory.get() != '':
            first_digit = float(self.memory.get())
            self.memory2.set(first_digit)
            self.operator.set('+')
            self.memory.set('')
            self.memory_box.focus()
    def calculate(self):
        if self.operator.get() == '+':
            result = float(self.memory.get()) + float(self.memory2.get())
            self.memory.set(str(result))
            self.memory2.set("")
            self.operator.set('')    
    def calculate_event(self,event):
        if self.operator.get() == '+':
            result = float(self.memory.get()) + float(self.memory2.get())
            self.memory.set(str(result))
            self.memory2.set("")
            self.operator.set('')            
if __name__ == "__main__":
    main()

            



        
        