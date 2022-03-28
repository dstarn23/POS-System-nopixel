import tkinter as tk

prices = {"sushi": 500, "chips": 50, "wings": 250, "pizza": 100, "mac": 75,
        "pancakes": 150, "panini": 230, "cocktail": 125 }

order = {"sushi": 0, "chips": 0, "wings": 0, "pizza": 0, "mac": 0,
        "pancakes": 0, "panini": 0, "cocktail": 0 }

labels = []

def add_food(index):
    if index == 0:
        order["sushi"] += 1
        sushi_label.config(text=str(order["sushi"]))
    elif index == 1:
        order["chips"] += 1
        chips_label.config(text=str(order["chips"]))
    elif index == 2:
        order["wings"] += 1
        wings_label.config(text=str(order["wings"]))
    elif index == 3:
        order["pizza"] += 1
        pizza_label.config(text=str(order["pizza"]))
    elif index == 4:
        order["mac"] += 1
        mac_label.config(text=str(order["mac"]))
    elif index == 5:
        order["pancakes"] += 1
        pancakes_label.config(text=str(order["pancakes"]))
    elif index == 6:
        order["panini"] += 1
        panini_label.config(text=str(order["panini"]))
    elif index == 7:
        order["cocktail"] += 1
        cocktail_label.config(text=str(order["cocktail"]))

def comment_print():
    comment = ""
    total = 0

    for food in order:
        if order[food] > 0:
            comment += str(order[food])+'-'+food+","
            total += prices[food] * order[food]
    comment = comment[:-1]
    T.delete(1.0,tk.END)
    T.insert(tk.END,comment)
    T2.delete(1.0,tk.END)
    T2.insert(tk.END,str(total))

def clear():
    for food in order:
        order[food] = 0
    for label in labels:
        label.config(text='')
    comment_print()

def subtract_food(index):
    if index == 0:
        if order["sushi"] > 0:
            order["sushi"] -= 1
            sushi_label.config(text=str(order["sushi"]))
    elif index == 1:
        if order["chips"] > 0:
            order["chips"] -= 1
            chips_label.config(text=str(order["chips"]))
    elif index == 2:
        if order["wings"] > 0:
            order["wings"] -= 1
            wings_label.config(text=str(order["wings"]))
    elif index == 3:
        if order["pizza"] > 0:
            order["pizza"] -= 1
            pizza_label.config(text=str(order["pizza"]))
    elif index == 4:
        if order["mac"] > 0:
            order["mac"] -= 1
            mac_label.config(text=str(order["mac"]))
    elif index == 5:
        if order["pancakes"] > 0:
            order["pancakes"] -= 1
            pancakes_label.config(text=str(order["pancakes"]))
    elif index == 6:
        if order["panini"] > 0:
            order["panini"] -= 1
            panini_label.config(text=str(order["panini"]))
    elif index == 7:
        if order["cocktail"] > 0:
            order["cocktail"] -= 1
            cocktail_label.config(text=str(order["cocktail"]))



root = tk.Tk()
root.geometry("900x300")

sushi = tk.Button(root, text= "SUSHI",command=lambda:add_food(0))
chips = tk.Button(root, text= "CHIPS",command=lambda:add_food(1))
wings = tk.Button(root, text= "WINGS",command=lambda:add_food(2))
pizza = tk.Button(root, text= "PIZZA",command=lambda:add_food(3))
mac = tk.Button(root, text= "MAC",command=lambda:add_food(4))
pancakes = tk.Button(root, text= "PANCAKES",command=lambda:add_food(5))
panini = tk.Button(root, text= "PANINI",command=lambda:add_food(6))
cocktail = tk.Button(root, text= "COCKTAIL",command=lambda:add_food(7))
subtract0 = tk.Button(root, text= "-", command=lambda:subtract_food(0))
subtract1 = tk.Button(root, text= "-", command=lambda:subtract_food(1))
subtract2 = tk.Button(root, text= "-", command=lambda:subtract_food(2))
subtract3 = tk.Button(root, text= "-", command=lambda:subtract_food(3))
subtract4 = tk.Button(root, text= "-", command=lambda:subtract_food(4))
subtract5 = tk.Button(root, text= "-", command=lambda:subtract_food(5))
subtract6 = tk.Button(root, text= "-", command=lambda:subtract_food(6))
subtract7 = tk.Button(root, text= "-", command=lambda:subtract_food(7))

sushi.grid(row=1,column=1)
sushi_label = tk.Label(root, fg="green")
sushi_label.grid(row=1,column=3)
labels.append(sushi_label)
subtract0.grid(row=1,column=2)

chips.grid(row=2,column=1)
chips_label = tk.Label(root, fg="green")
chips_label.grid(row=2,column=3)
labels.append(chips_label)
subtract1.grid(row=2,column=2)

wings.grid(row=3,column=1)
wings_label = tk.Label(root, fg="green")
wings_label.grid(row=3,column=3)
labels.append(wings_label)
subtract2.grid(row=3,column=2)

pizza.grid(row=4,column=1)
pizza_label = tk.Label(root, fg="green")
pizza_label.grid(row=4, column=3)
labels.append(pizza_label)
subtract3.grid(row=4,column=2)

mac.grid(row=5,column=1)
mac_label = tk.Label(root, fg="green")
mac_label.grid(row=5, column=3)
labels.append(mac_label)
subtract4.grid(row=5,column=2)

pancakes.grid(row=6,column=1)
pancakes_label = tk.Label(root, fg="green")
pancakes_label.grid(row=6, column=3)
labels.append(pancakes_label)
subtract5.grid(row=6,column=2)

panini.grid(row=7,column=1)
panini_label = tk.Label(root, fg="green")
panini_label.grid(row=7, column=3)
labels.append(panini_label)
subtract6.grid(row=7,column=2)

cocktail.grid(row=8,column=1)
cocktail_label = tk.Label(root, fg="green")
cocktail_label.grid(row=8, column=3)
labels.append(cocktail_label)
subtract7.grid(row=8,column=2)

button = tk.Button(root,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.grid(row=9,column=3)

print_button = tk.Button(root,
                   text="PRINT",
                   fg="blue",
                   command=comment_print)
print_button.grid(row=9,column=1)

clear_button = tk.Button(root,
                   text="CLEAR",
                   fg="green",
                   command=clear)
clear_button.grid(row=9,column=2)

root.grid_rowconfigure(10, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_rowconfigure(11, weight=1)

T = tk.Text(root, height=2,width=400)
T2 = tk.Text(root, height=2,width=400)
T.grid(row=10,column=4)
T2.grid(row=11,column=4)
comment_label = tk.Label(root, fg="green")
comment_label.grid(row=10, column=3)
comment_label.config(text="Copy This ->")

charge_label = tk.Label(root, fg="green")
charge_label.grid(row=11, column=3)
charge_label.config(text="Charge This ->")

root.mainloop()
