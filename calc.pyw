import tkinter

root = tkinter.Tk()
root.resizable(False, False)

root.geometry("200x250")

v_string = ""

l_string = ""

# dicionário para deixar a string lógica mais bonita.
# eu sei que eu poderia colocar diretamente os símbolos, mas quis dar
# uma complexidade maior usando um dicionário.
# (nunca tinha usado, por isso optei por ele)
operations = {
    'mu':'*',
    'di': '/',
    'pl':'+',
    'mi':'-',
    'eq':'='
}

def refresh_entry():
    visor.configure(state="normal")
    visor.delete(0, 'end')
    visor.insert(0, v_string)
    visor.configure(state="disabled")
    
def res_entry(result):
    visor.configure(state="normal")
    visor.delete(0, 'end')
    visor.insert(0, result)
    visor.configure(state="disabled")

#função de todos os botões

def b_one_press():
    logic_value = "1"
    global v_string
    global l_string
    v_string += "1"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    print("updated")
    
def b_two_press():
    logic_value = "2"
    global l_string
    global v_string 
    v_string += "2"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")

def b_three_press():
    logic_value = "3"
    global l_string
    global v_string 
    v_string += "3"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_four_press():
    logic_value = "4"
    global l_string
    global v_string 
    v_string += "4"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_five_press():
    logic_value = "5"
    global l_string
    global v_string 
    v_string += "5"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_six_press():
    logic_value = "6"
    global l_string
    global v_string 
    v_string += "6"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_seven_press():
    logic_value = "7"
    global l_string
    global v_string 
    v_string += "7"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_eight_press():
    logic_value = "8"
    global l_string
    global v_string 
    v_string += "8"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_nine_press():
    logic_value = "9"
    global l_string
    global v_string 
    v_string += "9"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_zero_press():
    logic_value = "0"
    global l_string
    global v_string 
    v_string += "0"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_plus_press():
    logic_value = "$pl$"
    global l_string
    global v_string 
    v_string += "+"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_minus_press():
    logic_value = "$mi$"
    global l_string
    global v_string 
    v_string += "-"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_multiply_press():
    logic_value = "$mu$"
    global l_string
    global v_string 
    v_string += "*"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_divide_press():
    logic_value = "$di$"
    global l_string
    global v_string 
    v_string += "/"
    l_string += logic_value
    refresh_entry()
    l_visor.config(text=l_string)
    
    print("updated")
    
def b_equal_press():
    logic_value = "$eq"
    global l_string
    global v_string 
    v_string = ""
    l_string += logic_value
    res = calc(l_string)
    res_entry(result=res)
    l_visor.config(text=res)
    
    print("updated")
    
def b_clear_press():
    global v_string 
    global l_string
    v_string = ""
    l_string = ""
    refresh_entry()
    l_visor.config(text=l_string)
    print("updated")
    
def calc(l_string):
    operators_done = 0
    sliced = l_string.split("$")
    
    # Deixar a string logica mais bonita e legível
    res = []
    for item in sliced:
        if item.isdigit():
            res.append(int(item))  # Adiciona o número
        elif item in operations:
            res.append(operations[item])  # Adiciona o operador
            
    print(res)
        
    i = 1
    
    first_value = res[0]
    while i < len(res):
        # passa para os operadores seguintes
        operator = res[1+operators_done]
            
        try:
            second_value = res[i+1]
        except:
            print(first_value)
            return first_value
        if (operator == "+"):
            first_value += second_value
        elif (operator == "-"):
            first_value -= second_value
        elif (operator == "*"):
            first_value *= second_value
        elif (operator == "/"):
            first_value /= second_value
        i += 2
        operators_done += 2
    print(first_value)
    return first_value
    
if (__name__ == "__main__"):
    
    visor = tkinter.Entry(root, text=v_string, state="disabled")
    l_visor = tkinter.Label(root, text=l_string)

    b_one = tkinter.Button(root, text="1",command=b_one_press)
    b_two = tkinter.Button(root, text="2",command=b_two_press)
    b_three = tkinter.Button(root, text="3",command=b_three_press)
    b_four = tkinter.Button(root, text="4",command=b_four_press)
    b_five = tkinter.Button(root, text="5",command=b_five_press)
    b_six = tkinter.Button(root, text="6",command=b_six_press)
    b_seven = tkinter.Button(root, text="7",command=b_seven_press)
    b_eight = tkinter.Button(root, text="8",command=b_eight_press)
    b_nine = tkinter.Button(root, text="9",command=b_nine_press)
    b_zero = tkinter.Button(root, text="0",command=b_zero_press)
    b_divide = tkinter.Button(root, text="/",command=b_divide_press)
    b_multiply = tkinter.Button(root, text="*",command=b_multiply_press)
    b_minus = tkinter.Button(root, text="-",command=b_minus_press)
    b_plus = tkinter.Button(root, text="+",command=b_plus_press)
    b_equal = tkinter.Button(root, text="=",command=b_equal_press)
    b_clear = tkinter.Button(root, text="CE",command=b_clear_press)

    # visor.grid(column=3, row=0,padx=10, pady=10)
    visor.place(x=0, y=0, height=50, width=200)
    
    b_seven.place(x=0, y= 50, height=50, width=50)
    b_eight.place(x=50, y= 50, height=50, width=50)
    b_nine.place(x=100, y= 50, height=50, width=50)
    b_divide.place(x=150, y= 50, height=50, width=50)

    # b_seven.grid(column=1, row=1,padx=10, pady=10)
    # b_eight.grid(column=2, row=1,padx=10, pady=10)
    # b_nine.grid(column=3, row=1,padx=10, pady=10)
    # b_divide.grid(column=4, row=1,padx=10, pady=10)
    
    b_four.place(x=0, y= 100, height=50, width=50)
    b_five.place(x=50, y= 100, height=50, width=50)
    b_six.place(x=100, y= 100, height=50, width=50)
    b_multiply.place(x=150, y= 100, height=50, width=50)

    # b_four.grid(column=1, row=2,padx=10, pady=10)
    # b_five.grid(column=2, row=2,padx=10, pady=10)
    # b_six.grid(column=3, row=2,padx=10, pady=10)
    # b_multiply.grid(column=4, row=2,padx=10, pady=10)
    
    b_one.place(x=0, y= 150, height=50, width=50)
    b_two.place(x=50, y= 150, height=50, width=50)
    b_three.place(x=100, y= 150, height=50, width=50)
    b_minus.place(x=150, y= 150, height=50, width=50)

    # b_one.grid(column=1, row=3,padx=10, pady=10)
    # b_two.grid(column=2, row=3,padx=10, pady=10)
    # b_three.grid(column=3, row=3,padx=10, pady=10)
    # b_minus.grid(column=4, row=3,padx=10, pady=10)
    
    b_zero.place(x=0, y= 200, height=50, width=50)
    b_clear.place(x=50, y= 200, height=50, width=50)
    b_equal.place(x=100, y= 200, height=50, width=50)
    b_plus.place(x=150, y= 200, height=50, width=50)

    # b_zero.grid(column=1, row=4,padx=10, pady=10)
    # b_clear.grid(column=2, row=4,padx=10, pady=10)
    # b_equal.grid(column=3, row=4,padx=10, pady=10)
    # b_plus.grid(column=4, row=4,padx=10, pady=10)

    # l_visor.grid(column=1, row=5,padx=10, pady=10)

    root.title("Calculadora")
    root.mainloop()