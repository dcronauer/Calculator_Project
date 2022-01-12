#this program aims to recreate a simple calculator app

#import tkinter and tkk
import tkinter
from tkinter import ttk
from tkinter import font
#from tkinter.constants import END, FALSE
ORIGINAL_DPI = 96
#main function will create gui window, objects, start mainloop
def main():
    #run instance
    height, width, current_dpi = get_display_size()
    instance = Calculator_Gui(height,width,current_dpi)
    #setup main loop   
    tkinter.mainloop()
def get_display_size():
        root = tkinter.Tk()
        root.update_idletasks()
        root.attributes('-fullscreen', True)
        root.state('iconic')
        height = int(root.winfo_screenheight())
        width = int(root.winfo_screenwidth())
        current_dpi = root.winfo_fpixels('1i')
        print(current_dpi)
        root.destroy()
        return height, width, current_dpi
#create gui class
class Calculator_Gui:
    x = 0
    y = 10
    bg_color_body = '#FFA9A3'
    font_size = 16
    
    
    
    
    def __init__(self,height,width,current_dpi):
        print(height,width,current_dpi)
        height1, width1, x, y = self.get_dimensions(height,width)
        print(height1,width1)
        self.main_window = tkinter.Tk()

        geometry = "%dx%d+%d+%d" % (width1,height1,x,y)
        self.main_window.geometry(geometry)
        self.main_window.title("Calculator")
        self.main_window.configure(bg=self.bg_color_body)
        self.main_window.minsize(width1,height1)
        
        self.memory = tkinter.StringVar()
        self.memory2 = tkinter.StringVar()
        self.operator = tkinter.StringVar()
        #self.reg = self.main_window.register(self.check_digit)
        self.create_objects(height1,width1)
    def get_dimensions(self,height,width):
        #1080 815px height by 1084 width, 2K  823 height 1113px width
        if height >490 and width>790:
            h_factor = height/575
            w_factor = width/850
            height1 = int(height/h_factor)
            width1 = int(width/w_factor)
            x = 100
            y = 5
            return height1, width1, x, y
        else:
            return 750, 1000,100,5    
       
    def create_objects(self,height1,width1):
        s = ttk.Style()
        s.theme_use('alt')
        #background="#B9E6FF"
        s.configure('TButton', foreground='black', font=("Calibri",26), background="#B9E6FF")
        s.configure('TFrame',background=self.bg_color_body)
        s.configure('TLabel',background=self.bg_color_body)
        s.configure('Equal.TButton', background='#5C95FF')
        s.map('TButton',
        background=[('disabled', 'magenta'),
                    ('pressed',  '#F87575'),
                    ('active', '#FFA9A3')])
        #create frames
        self.clear_frame = ttk.Frame(self.main_window)
        self.display_frame = ttk.Frame(self.main_window)
        self.number123_frame = ttk.Frame(self.main_window)
        self.number456_frame = ttk.Frame(self.main_window)
        self.number789_frame = ttk.Frame(self.main_window)
        self.number0_frame = ttk.Frame(self.main_window)
        self.functional_frame = ttk.Frame(self.main_window)
       
        #create and pack display frame
        self.memory_box = ttk.Label(self.display_frame,textvariable=self.memory, width =300,font=("Calibri 30"),justify="right")
        #self.memory_box.config(validate="key",validatecommand=(self.reg,"%P",'%d'))
        self.memory_box2 = ttk.Label(self.display_frame,textvariable=self.memory2, width=15)
        self.operator_box = ttk.Label(self.display_frame,textvariable=self.operator, width=1)

        #keyboard bind upon hitting enter run self.calculate_event
        self.main_window.bind('<Return>', lambda event: self.calculate())
        self.main_window.bind('+', lambda event: self.add())
        self.main_window.bind('-', lambda event: self.minus())
        self.main_window.bind('*', lambda event: self.multiply())
        self.main_window.bind('/', lambda event: self.divide())
        self.main_window.bind('<Delete>', lambda event: self.clear())
        self.main_window.bind('<End>',lambda event: self.clear_entry())
        self.main_window.bind('<Insert>',lambda event: self.toggle())
        self.main_window.bind('<Home>',lambda event: self.round())
        self.main_window.bind(',', lambda event: self.comma())
        self.main_window.bind('1',lambda event: self.button_1())
        self.main_window.bind('2',lambda event: self.button_2())
        self.main_window.bind('3',lambda event: self.button_3())
        self.main_window.bind('4',lambda event: self.button_4())
        self.main_window.bind('5',lambda event: self.button_5())
        self.main_window.bind('6',lambda event: self.button_6())
        self.main_window.bind('7',lambda event: self.button_7())
        self.main_window.bind('8',lambda event: self.button_8())
        self.main_window.bind('9',lambda event: self.button_9())
        self.main_window.bind('0',lambda event: self.button_0())
        self.main_window.bind('.', lambda event: self.decimal())
        #self.memory_box.bind("<KeyRelease>",lambda event: self.change()) #keyup 
        #pack display frame
        self.memory_box.pack(ipady=50)
        self.memory_box2.pack()
        self.operator_box.pack()

        #create clear button and +/- frame
        self.clear_button = ttk.Button(self.clear_frame,text="C",command=self.clear)
        self.clearentry_button = ttk.Button(self.clear_frame, text="CE", command=self.clear_entry)
        self.toggle_button = ttk.Button(self.clear_frame,text="+/-",command=self.toggle)
        self.round_button = ttk.Button(self.clear_frame,text="Round",command=self.round)

        #pack clear_button
        self.clear_button.pack(side="left",ipadx=self.x,ipady=self.y)
        self.clearentry_button.pack(side="left",ipadx=self.x,ipady=self.y)
        self.toggle_button.pack(side="left",ipadx=self.x,ipady=self.y)
        self.round_button.pack(side="left",ipadx=self.x, ipady=self.y)

        #create the buttons 123
        self.button1 = ttk.Button(self.number123_frame,text="1",command=self.button_1)
        self.button2 = ttk.Button(self.number123_frame,text="2",command=self.button_2 )
        self.button3 = ttk.Button(self.number123_frame,text="3",command=self.button_3 )
        self.button_plus = ttk.Button(self.number123_frame,text="+",command=self.add )
        
        #pack the buttons123+
        self.button1.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button2.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button3.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button_plus.pack(side="left",ipadx=self.x,ipady=self.y)
        
        #create the buttons 456
        self.button4 = ttk.Button(self.number456_frame,text="4",command=self.button_4)
        self.button5 = ttk.Button(self.number456_frame,text="5",command=self.button_5 )
        self.button6 = ttk.Button(self.number456_frame,text="6",command=self.button_6 )
        self.button_minus = ttk.Button(self.number456_frame,text="-",command=self.minus)

        #pack the buttons456
        self.button4.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button5.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button6.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button_minus.pack(side="left",ipadx=self.x,ipady=self.y)
        
        #create the buttons 789
        self.button7 = ttk.Button(self.number789_frame,text="7",command=self.button_7)
        self.button8 = ttk.Button(self.number789_frame,text="8",command=self.button_8)
        self.button9 = ttk.Button(self.number789_frame,text="9",command=self.button_9)
        self.button_times = ttk.Button(self.number789_frame,text="*",command=self.multiply)

        #pack the buttons789
        self.button7.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button8.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button9.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button_times.pack(side="left",ipadx=self.x,ipady=self.y)
        
        #create the buttons 0 equal .
        self.button0 = ttk.Button(self.number0_frame,text="0",command=self.button_0,)
        self.button_equal =ttk.Button(self.number0_frame,text="=",command=self.calculate,style='Equal.TButton')
        self.button_decimal = ttk.Button(self.number0_frame,text='.',command=self.decimal)
        self.button_divide = ttk.Button(self.number0_frame,text="/",command=self.divide)

        #pack the buttons0
        self.button_equal.pack(side='left',ipadx=self.x,ipady=self.y)
        self.button0.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button_decimal.pack(side="left",ipadx=self.x,ipady=self.y)
        self.button_divide.pack(side="left",ipadx=self.x,ipady=self.y)

        #pack the frames
        self.display_frame.pack()
        self.clear_frame.pack()
        self.number123_frame.pack()
        self.number456_frame.pack()
        self.number789_frame.pack()
        self.number0_frame.pack()
        
        self.memory_box.focus()
    

    def comma(self,event=None):
        string = self.memory.get()
        try:
            string = string.format(string,",d")
            print(string)
            
            self.memory.set(f'{string:,}')
        except Exception as error:
            print(error)
       
    def round(self):
        string = float(self.memory.get())
        string = round(string,0)
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor('end')

    #validate string
    
    # def change(self, event=None):
        
        
    #     string = str(self.memory.get())
        
    #     length = len(string)
        
    #     if len(string)> 1 and string[0] == "-":
    #         string2 = '-'
    #     else:    
    #         string2 = ""
    #     count = 0
        
    #     for letter in string:
    #         if letter.isdigit():
                
    #             string2 = string2 + letter
               
                
                
    #         elif letter == ".":
    #             if count == 0:
    #                 string2 = string2 + letter    
    #                 count +=1
                    
       
    #     self.memory.set(string2)
    #     self.memory_box.focus()
    #     self.memory_box.icursor("end")   

                           
    #add a number to entry widget based on hitting one of the calculator buttons
    def button_1(self, event=None):
        string = self.memory.get() + "1"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_2(self, event=None):
        string = self.memory.get() + "2"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_3(self, event=None):
        string = self.memory.get() + "3"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_4(self, event=None):
        string = self.memory.get() + "4"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_5(self, event=None):
        string = self.memory.get() + "5"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_6(self, event=None):
        string = self.memory.get() + "6"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_7(self, event=None):
        string = self.memory.get() + "7"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_8(self, event=None):
        string = self.memory.get() + "8"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_9(self, event=None):
        string = self.memory.get() + "9"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def button_0(self, event=None):
        string = self.memory.get() + "0"
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")
    def decimal(self,event=None):
        lock = ''
        string = self.memory.get()
        
        for letter in string:
            if letter == ".":
                lock = True
        if lock == True:
            print("too many decimals")   
            

        else:
            string = string + "."
            self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor("end")

    #operator functions
    def add(self,event=None):
        
        try:
            
            first_digit =float(self.memory.get())
        except ValueError:
            print('box is empty')
            first_digit = ""
            self.operator.set('+')
            # self.memory_box.focus()
        else:    
            if first_digit != '' and self.memory2.get() != '':
                self.operator.set('+')
                # self.memory_box.focus()
                # self.memory_box.icursor("end")
            else:
                self.memory2.set(first_digit)
                self.operator.set('+')
                self.memory.set('')
                # self.memory_box.focus()
            
    def minus(self,event=None):
        
        try:
            first_digit =float(self.memory.get())
        except ValueError:
            print('box is empty')
            first_digit = ""
            self.operator.set('-')
            # self.memory_box.focus()
        else:    
            if first_digit != '' and self.memory2.get() != '':
                self.operator.set('-')
                # self.memory_box.focus()
                # self.memory_box.icursor("end")
            else:
                self.memory2.set(first_digit)
                self.operator.set('-')
                self.memory.set('')
                # self.memory_box.focus()
            
    def multiply(self,event=None):
        try:
            first_digit =float(self.memory.get())
        except ValueError:
            print('box is empty')
            first_digit = ""
            self.operator.set('*')
            # self.memory_box.focus()
        else:    
            if first_digit != '' and self.memory2.get() != '':
                self.operator.set('*')
                # self.memory_box.focus()
                # self.memory_box.icursor("end")
            else:
                self.memory2.set(first_digit)
                self.operator.set('*')
                self.memory.set('')
                # self.memory_box.focus()
        
    def divide(self,event=None):
        try:

            first_digit =float(self.memory.get())
        except ValueError:
            print('box is empty')
            first_digit = ""
            self.operator.set('/')
            # self.memory_box.focus()
        else:    
            if first_digit != '' and self.memory2.get() != '':
                self.operator.set('/')
                # self.memory_box.focus()
                # self.memory_box.icursor("end")
            else:
                self.memory2.set(first_digit)
                self.operator.set('/')
                self.memory.set('')
                # self.memory_box.focus()
          
             
    def calculate(self):
        if self.operator.get() == '+':
            result = float(self.memory.get()) + float(self.memory2.get()) 
        elif self.operator.get() == '-':
            result = float(self.memory2.get()) - float(self.memory.get())
        elif self.operator.get() == '*':
            result = float(self.memory2.get()) * float(self.memory.get())  
            
        elif self.operator.get() == '/':
            result = float(self.memory2.get()) / float(self.memory.get())
        else:
            result = self.memory.get()
        
        self.clear_entry
        self.memory.set(result)
        self.memory2.set('')
        self.operator.set('')   
        # self.memory_box.focus()
        # self.memory_box.icursor("end") 
    def clear(self,event=None):
        self.memory.set('')
        self.memory2.set('')
        self.operator.set('')
        # self.memory_box.focus()
    def clear_entry(self,event=None):
        self.memory.set('')
        # self.memory_box.focus()
    """def check_digit(self,p,d):
        
        if p.isdigit():
            return True 
       
        else:
            return False"""
        
    def toggle(self,event=None):
        try:
            current = float(self.memory.get())
            if current !="":
                toggled = current *-1
                self.memory.set(str(toggled))
                # self.memory_box.focus()
                # self.memory_box.icursor("end")
        except ValueError or TypeError as Exception:
            print(Exception)
            #self.memory_box.focus()
            #self.memory_box.icursor("end")
if __name__ == "__main__":
    main()

            



        
        
