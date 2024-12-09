
import tkinter as tk
from gui2 import Gui
#reference video used for calculator https://www.youtube.com/watch?v=NzSCNjn4_RI


calculation = ""

def add_to_calculation(symbol):
    
    '''Adds symbol to calculation string that is global and changes the display result.
        updates, text_result, for the calculation and makes it read-only
    
    '''
    
    global calculation
    calculation += str(symbol)
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    text_result.config(state=tk.DISABLED)


def evaluate_calculation():
    
    '''Evaluates calculation string that is global and changes the display result.
        updates, text_result, for the calculation and makes it read-only.
        
        Also catches errors and displays messages if invalid input is entered.
    
    '''
    
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.config(state=tk.NORMAL)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        text_result.config(state=tk.DISABLED)
    except:
        clear_field()
        text_result.config(state=tk.NORMAL)
        text_result.insert(1.0, "Error")
        text_result.config(state=tk.DISABLED)
        

def clear_field():
    '''Clears calculation string that is global and changes the display result to empty.
        updates, text_result, for the calculation and makes it read-only.
        
        
    '''

    global calculation
    calculation = ""
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, "end")
    text_result.config(state=tk.DISABLED)
    
def area_calculation():
    '''Provides and option to calculate the area of shapes.
    '''
    Gui(window)
    


root = tk.Tk()
root.geometry("300x215")
root.resizable(False, False)
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.config(state=tk.NORMAL)
text_result.config(state=tk.DISABLED)
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=1)


btn_area = tk.Button(root, text="area", command=lambda:Gui(tk.Toplevel(root)), width=5, font=("Arial", 14))
btn_area.grid(row=6, column=2, columnspan=1)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=1)


root.mainloop()


