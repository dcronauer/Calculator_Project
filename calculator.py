#this program aims to recreate a simple calculator app

#import tkinter and tkk
from cgitb import text
import tkinter
from tkinter import BOTH, ttk
from tkinter import font
from tkinter.constants import LEFT, RIGHT

#orginal DPI
ORIGINAL_DPI = 96

#main function will create gui window, objects, start mainloop
def main():
    #run instance
    height, width, current_dpi = get_display_size()
    instance = CalculatorGui(height,width,current_dpi)
    #setup main loop   
    tkinter.mainloop()


#this function creates a window full screen in window in order to get the size of the display then returns height, width, and dpi
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
class CalculatorGui:
    # x and y are for padding h and w are for sizing buttons then we have bg color and fontsize
    x = 2
    y = 7   
    h = 25
    w = 6
    bg_color_body = '#FFA9A3'
    font_size = 16
    
    #the init gets window dimensions, creates window, creates memory varibales and creates the gui items
    def __init__(self,height,width,current_dpi):
        print(height,width,current_dpi)
        height1, width1, x, y,h_factor,w_factor = self.get_dimensions(height,width)
        print(height1,width1)
        
        self.main_window = tkinter.Tk()
        #geometry = "%dx%d+%d+%d" % (width1,height1,x,y)
        self.main_window.geometry()
        self.main_window.title("Calculator")
        self.main_window.configure(bg=self.bg_color_body)
        self.main_window.minsize(width1,height1)
        #set up memeory variables
        self.memory = tkinter.StringVar()
        self.memory2 = tkinter.StringVar()
        self.operator = tkinter.StringVar()
        #self.reg = self.main_window.register(self.check_digit)
        self.create_objects(height1,width1,w_factor,h_factor)
    
    #this helps create the same size calculator app no matter what resolution is being used. This is currently funciton for 
    #larger screens, I havent adapted to mobile or tablet size yet. It is in python though so that might not happen.
    def get_dimensions(self,height,width):
        #1080 815px height by 1084 width, 2K  823 height 1113px width
        if height >490 and width>790:
            h_factor = height/330
            w_factor = width/328
            height1 = int(height/h_factor)
            width1 = int(width/w_factor)
            x = 100
            y = 5
            return height1, width1, x, y, h_factor, w_factor
        else:
            return 750, 1000,100,5    
    
    #this function creates all the widgets for display, puts them in frames, and packs the widgets and frames   
    def create_objects(self,height1,width1,w_factor,h_factor):
        #working with styles to avoid changing each item individually, also ttk items do not have all the functionality to change inline
        #set grid scaling
        self.main_window.grid_rowconfigure(0,weight=1)
        self.main_window.grid_rowconfigure(1,weight=1)
        self.main_window.grid_columnconfigure(0,weight=1)
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('TButton', foreground='black', font=("Calibri",self.font_size), background="#B9E6FF",height=(self.h), width=(self.w))
        s.configure('TFrame',background="red")
        s.configure('buttons.TFrame',background="yellow")
        s.configure('TLabel',background=self.bg_color_body)
        s.configure('Equal.TButton', background='#5C95FF')
        s.map('TButton',
        background=[('disabled', 'magenta'),
                    ('pressed',  '#F87575'),
                    ('active', '#FFA9A3')])
        s.configure('TLabel', foreground='grey', font =('Calibri,26'), background="#FFF",anchor="e",width=15)
        s.configure('memory.TLabel', foreground='black', font =('Calibri,26'), background="#FFF", width=15)
        
        #create frames
        self.frame = ttk.Frame(self.main_window,style="buttons.TFrame")
        self.total_frame = ttk.Frame(self.main_window)
        self.total_frame.grid_columnconfigure(2,weight=1)
        self.total_frame.grid_columnconfigure(1,weight=1)
        self.total_frame.grid_rowconfigure(0,weight=1)
       

        self.frame.grid_columnconfigure(0,weight=1)
        self.frame.grid_columnconfigure(1,weight=1)
        self.frame.grid_columnconfigure(2,weight=1)
        self.frame.grid_columnconfigure(3,weight=1)
        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_rowconfigure(1,weight=1)
        self.frame.grid_rowconfigure(2,weight=1)
        self.frame.grid_rowconfigure(3,weight=1)
        self.frame.grid_rowconfigure(4,weight=1)
        #keyboard bind upon hitting enter run self.event
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
        #self.memory_box.bind("<KeyRelease>",lambda event: self.change()) #keyup  this was an old method of displaying numbers in event widget
        # couldnt get commas to work so i went a different direction to have a label display the memory variable and use binds to call the button funcitions
        #rather than have both the button and keyboard strokes work on the event widget and using the self.change function which would handle adding to string
        #if it was a digit, or decimal
        
        
        

        #create and pack display frame
        self.memory_box = ttk.Label(self.total_frame,textvariable=self.memory,style="memory.TLabel").grid(row=0,column=2,sticky="nsew")
        self.memory_box2 = ttk.Label(self.total_frame,textvariable=self.memory2, width=15).grid(row=0,column=1,sticky="nsew")
        self.operator_box = ttk.Label(self.total_frame,textvariable=self.operator, width=1).grid(row=0,column=0,sticky="nsew")
        
        #create clear button and +/- frame
        self.clear_button = ttk.Button(self.frame,text="C",command=self.clear).grid(row=0,column=0, sticky="nsew")
        self.clearentry_button = ttk.Button(self.frame, text="CE", command=self.clear_entry).grid(row=0,column=1,sticky="nsew")
        self.toggle_button = ttk.Button(self.frame,text="+/-",command=self.toggle).grid(row=0,column=2,sticky="nsew")
        self.round_button = ttk.Button(self.frame,text="Round",command=self.round).grid(row=0,column=3,sticky="nsew")

        #create the buttons 123
        self.button1 = ttk.Button(self.frame,text="1",command=self.button_1).grid(row=3,column=0,sticky="nsew")
        self.button2 = ttk.Button(self.frame,text="2",command=self.button_2 ).grid(row=3,column=1,sticky="nsew")
        self.button3 = ttk.Button(self.frame,text="3",command=self.button_3 ).grid(row=3,column=2,sticky="nsew")
        self.button_plus = ttk.Button(self.frame,text="+",command=self.add ).grid(row=3,column=3,sticky="nsew")
        
        #create the buttons 456
        self.button4 = ttk.Button(self.frame,text="4",command=self.button_4).grid(row=2,column=0,sticky="nsew")
        self.button5 = ttk.Button(self.frame,text="5",command=self.button_5 ).grid(row=2,column=1,sticky="nsew")
        self.button6 = ttk.Button(self.frame,text="6",command=self.button_6 ).grid(row=2,column=2,sticky="nsew")
        self.button_minus = ttk.Button(self.frame,text="-",command=self.minus).grid(row=2,column=3,sticky="nsew")
        
        #create the buttons 789
        self.button7 = ttk.Button(self.frame,text="7",command=self.button_7).grid(row=1,column=0,sticky="nsew")
        self.button8 = ttk.Button(self.frame,text="8",command=self.button_8).grid(row=1,column=1,sticky="nsew")
        self.button9 = ttk.Button(self.frame,text="9",command=self.button_9).grid(row=1,column=2,sticky="nsew")
        self.button_times = ttk.Button(self.frame,text="*",command=self.multiply).grid(row=1,column=3,sticky="nsew")

        #create the buttons 0 equal .
        self.button0 = ttk.Button(self.frame,text="0",command=self.button_0,).grid(row=4,column=1,sticky="nsew")
        self.button_equal =ttk.Button(self.frame,text="=",command=self.calculate,style='Equal.TButton').grid(row=4,column=0,sticky="nsew")
        self.button_decimal = ttk.Button(self.frame,text='.',command=self.decimal).grid(row=4,column=2,sticky="nsew")
        self.button_divide = ttk.Button(self.frame,text="/",command=self.divide).grid(row=4,column=3,sticky="nsew") 

    

        # #pack the frames
        self.total_frame.grid(row=0,column=0,sticky="nsew")
        self.frame.grid(row=1,column=0,sticky="nsew")
        # self.total_frame.pack()
        # self.frame.pack()
        
    #this function toggles the comma display on the calculator, it looks to see if the memory variable if it already has commas
    # if it does, it strips them out with repace method. Then sets that back to memory, if it didnt find commas in stirng, then
    # it adds them     
    def comma(self,event=None):
        comma_toggle = ''
        string = self.memory.get()
        for letter in string:
            if letter == ",":
                comma_toggle = True
        if comma_toggle == True:
            string_replace = string.replace(',','')
            string = float(string_replace)
            self.memory.set(string)
        else:
            try:
                string = float(string)
                string = "{:,}".format(string)
                print(string)
                
                self.memory.set(str(string))
            except Exception as error:
                print(error)
    
    #this pulls the memory variable, then takes out any commas in order to turn the memory to a float, then round it and set the memory back to 
    # the rounded comma less version   
    def round(self):
        string = self.memory.get()
        string_replace = string.replace(',','')
        string =float(string_replace)
        string = round(string,0)
        self.memory.set(string)
        # self.memory_box.focus()
        # self.memory_box.icursor('end')
                           
    #add a number to entry widget based on hitting one of the calculator buttons
    #these functions used to ineract with a entry widget so I left the box focus and i cursor end in
    #if I ever moved back you would uncomment those lines so the cursor would stay at the right whenever you called
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
    
    # the decimal function degines a lock variable as blank, then runs thourgh the variable string if it finds a comma
    #it sets lock variable to true. Then if its true it passes on, but if it doesnt turn to true, then it adds the decimal to the
    #display label
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

    #operator functions these funcitons remove commas before turning memory variable to a float for calculation
    #this function sets the operator variable to add then it clears the self.memory variable for the next item in the expression
    #it also sets the memory2 variable to be the value of the original value in self.memory. there are two other labels for 
    #displaying the operator and memory2 so you can see how your new value entered in the memory label will interact once you hit enter
    #to evaluate this same concept applies to add, minus, divide, and multiply
    def add(self,event=None):
        
        try:
            string = self.memory.get()
            string_replace = string.replace(',','')
            first_digit =float(string_replace)
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
            string = self.memory.get()
            string_replace = string.replace(',','')
            first_digit =float(string_replace)
        except ValueError as Exception:
            print(Exception)
            first_digit = ''
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
            string = self.memory.get()
            string_replace = string.replace(',','')
            first_digit =float(string_replace)
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
            string = self.memory.get()
            string_replace = string.replace(',','')
            first_digit =float(string_replace)
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
          
    #upon hitting enter or hitting the equal button the calcualtor will
    # get the operator, memory and memrory2 varibles and evaluate them based on the
    # operator chose.          
    def calculate(self):
        string = self.memory.get()
        string_replace = string.replace(',','')
        self.memory.set(string_replace)
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
   
    #the toggle function takes the varaible in memory and turns it from negative to positive or the inverse depending on its current state    
    def toggle(self,event=None):
        try:
            string = self.memory.get()
            string_replace = string.replace(',','')
            current =float(string_replace)
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

            

  

        
        
