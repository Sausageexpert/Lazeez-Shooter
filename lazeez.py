from msilib.schema import CheckBox
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # For backgrounds
from tkinter import filedialog  # For saving the bill
from tkinter import messagebox  # For warning (if no food is ordered and bill is requested)
import customtkinter
import spaceShooter2 as ss

setup = False

global login

global tableNo
global name
global location
global totalStuff


def startSet():
  global totalStuff
  global expression
  global setup

  def clearAll():

    global totalStuff
    global invoiceTextVar
    global checkvar
    checkvar = True
    totalStuff = ""
    invoiceTextVar.set("")
    invoiceLabel.configure(text=invoiceTextVar.get())
    global foodCost
    foodCost = 0
    global drinkCost
    drinkCost = 0
    global dessertCost
    dessertCost = 0
    food_cost_var.set(" ")
    drink_cost_var.set(" ")
    dessert_cost_var.set(" ")
    subtotal_cost_var.set(" ")
    taxes_var.set(" ")
    total_var.set(" ")
    submitButton.configure(state=DISABLED)

    for i in range(len(dessert_variables)):
      dessertText[i].set('0')
      dessert_variables[i].set(0)
      dessertBox[i].config(state=DISABLED)

    for j in range(len(food_variables)):
      foodText[j].set('0')
      food_variables[j].set(0)
      foodBox[j].config(state=DISABLED)

    for k in range(len(drink_variables)):
      drinkText[k].set('0')
      drink_variables[k].set(0)
      drinkBox[k].config(state=DISABLED)
    billingScreen.destroy()
    root.destroy()
    global setup
    setup = False
    dontSet()


  # Main Screen Setup
  root = tk.Tk()
  root.geometry('1300x650+0+0')  # Length by width, x position + y position
  root.resizable(False, False)  # X direction and y direction (0,1 works too)
  root.title('The Incredible Spice: Invoicing System')

  img = (
    Image.open('background.jpg'))
  resized = img.resize((1300, 650))
  newimg = ImageTk.PhotoImage(resized)
  root.config(bg='#3a5311')

  submittable = False

  # Background

  label = Label(root, image=newimg)
  label.place(x=0, y=0)

  # Top Panel

  topPanel = Frame(
    root, bd=1, relief=RAISED
  )  # Container to organise widgets, relief can be raised, sunken, groove, ridge, flat
  topPanel.pack(side=TOP)
  top_title = Label(topPanel,
                    text='The Incredible Spice',
                    fg='#ffd700',
                    font=('Dosis', 58),
                    bg='#234f1e',
                    width=25)  # fg = foreground
  top_title.grid(row=0, column=0)

  # Left Panel (with food, drinks, dessert and cost)

  leftPanel = Frame(root, bd=1, relief=RAISED, bg='black')
  leftPanel.place(relx=0.0625, rely=0.15)

  # Cost Panel

  costPanel = Frame(leftPanel, bd=1, relief=FLAT, bg='black', padx=50)
  costPanel.pack(side=BOTTOM)

  submitPanel = Frame(leftPanel, bd=1, relief=FLAT, bg='black')
  submitPanel.pack(side=BOTTOM)

  # Food Panel

  foodPanel = LabelFrame(leftPanel,
                         bd=1,
                         relief=FLAT,
                         text='Food',
                         fg='#2e1503',
                         font=('Dosis', 22, 'bold', 'underline'),
                         bg='#74b72e')
  foodPanel.pack(side=LEFT)

  # Drink Panel

  drinkPanel = LabelFrame(leftPanel,
                          bd=1,
                          relief=FLAT,
                          text='Drinks',
                          fg='#2e1503',
                          font=('Dosis', 22, 'bold', 'underline'),
                          padx=10,
                          bg='#74b72e')
  drinkPanel.pack(side=LEFT)

  # Dessert Panel

  dessertPanel = LabelFrame(leftPanel,
                            bd=1,
                            relief=FLAT,
                            text='Dessert',
                            fg='#2e1503',
                            font=('Dosis', 22, 'bold', 'underline'),
                            padx=10,
                            bg='#74b72e')
  dessertPanel.pack(side=LEFT)

  # Back-End Stuff

  foods = [
    'Lazeez Biriyani', 'Paneer Roll', 'Fried Salad', 'Boiled Ice Cream',
    'Khuska', 'Kebabs', 'Fried Rice', 'Cinnamon Toast'
  ]
  foodCosts = [350, 80, 150, 130, 100, 450, 180, 70]
  drinks = [
    'Choice of Fruit Juice', 'Mint Mojito', 'Soda', 'Ginger ale', 'Coke',
    'Liquid Cake', 'Choice of Milkshake', 'Water'
  ]
  drinkCosts = [50, 70, 80, 80, 50, 100, 20, 20]
  desserts = [
    'Dragonfruit Curd', 'Paneer Milk', 'Sugared Almonds', 'Cheesecake',
    'Brownies', 'Pudding', 'Candyfloss', 'Chocolate Muffin'
  ]
  dessertCosts = [175, 75, 225, 250, 180, 120, 15, 250]

  food_cost_var = StringVar()
  drink_cost_var = StringVar()
  dessert_cost_var = StringVar()
  subtotal_cost_var = StringVar()
  taxes_var = StringVar()
  total_var = StringVar()

  # Check boxes

  # Creating food items

  counter = 0
  food_variables = []
  foodBox = []
  foodText = []

  global invoiceTextVar
  global foodCost
  global drinkCost
  global dessertCost

  def checkFoodClicked():
    for i in range(len(food_variables)):
      if food_variables[i].get() == 1:
        foodBox[i].configure(state=NORMAL)
        submitButton.configure(state=NORMAL)
      else:
        foodText[i].set('0')
        food_variables[i].set(0)
        foodBox[i].configure(state=DISABLED)

  invoiceTextVar = StringVar()
  nameInfo = str("Name: " + str(name) + "\n")
  locationInfo = str("Location: " + str(location) + "\n")
  tableInfo = str("Table No.: " + str(tableNo) + "\n")
  totalStuff = nameInfo + locationInfo + tableInfo + "\n Item - Number - Cost \n \n"

  foodCost = 0
  drinkCost = 0
  dessertCost = 0

  expression = ""
  equation = StringVar()

  checkvar = True

  def check():
    global addvar
    addvar = False
    submitButton.configure(state=DISABLED)
    totalText = foodText + drinkText + dessertText
    global checkvar
    for i in range(len(totalText)):
      if totalText[i].get() != '0':
          addvar=True
          break
    if addvar==True:
      addEverything()
      checkvar = False
    else:
      messagebox.showwarning("Gotcha", "At least order something...")
      clearAll2()

  def update():
    if checkvar == True:
      global invoiceTextVar
      global totalStuff
      foodCost = 0
      drinkCost = 0
      dessertCost = 0

      for i in range(len(foodText)):
        if not foodText[i].get():
          foodText[i].set('0')
      for j in range(len(drinkText)):
        if not drinkText[j].get():
          drinkText[j].set('0')
      for k in range(len(dessertText)):
        if not dessertText[k].get():
          dessertText[k].set('0')
      for i in range(len(foodText)):
        foodCost += int(foodText[i].get()) * foodCosts[i]
      for j in range(len(drinkText)):
        drinkCost += int(drinkText[j].get()) * drinkCosts[j]
      for k in range(len(dessertText)):
        dessertCost += int(dessertText[k].get()) * dessertCosts[k]
      food_cost_var.set(str(foodCost))
      drink_cost_var.set(str(drinkCost))
      dessert_cost_var.set(str(dessertCost))
      subtotal_cost_var.set(str(foodCost + drinkCost + dessertCost))
      taxes_var.set(str((foodCost + drinkCost + dessertCost) / 10))
      total_var.set(str(int(1.1 * (foodCost + drinkCost + dessertCost))))
      if setup != False:
        try:
          root.after(1000, update)
        except:
          print("nope")

  def addEverything():
    global invoiceTextVar
    global totalStuff
    global foodCost
    global drinkCost
    global dessertCost
    global setup
    setup = False

    for i in range(len(foodText)):
      if not foodText[i].get():
        foodText[i].set('0')
    for j in range(len(drinkText)):
      if not drinkText[j].get():
        drinkText[j].set('0')
    for k in range(len(dessertText)):
      if not dessertText[k].get():
        dessertText[k].set('0')

    for i in range(len(foodText)):
      foodCost += int(foodText[i].get()) * foodCosts[i]
    for j in range(len(drinkText)):
      drinkCost += int(drinkText[j].get()) * drinkCosts[j]
    for k in range(len(dessertText)):
      dessertCost += int(dessertText[k].get()) * dessertCosts[k]
    food_cost_var.set(str(foodCost))
    drink_cost_var.set(str(drinkCost))
    dessert_cost_var.set(str(dessertCost))
    subtotal_cost_var.set(str(foodCost + drinkCost + dessertCost))
    taxes_var.set(str((foodCost + drinkCost + dessertCost) / 10))
    total_var.set(str(int(1.1 * (foodCost + drinkCost + dessertCost))))
    for i in range(len(foodText)):
      global totalStuff
      if int(foodText[i].get()) != 0:
        #print(foods[i], foodText[i].get(), int(foodText[i].get())*foodCosts[i], sep = " - ")
        totalStuff += str(
          str(foods[i]) + " - " + str(foodText[i].get()) + " - " +
          str(int(foodText[i].get()) * foodCosts[i]))
        totalStuff += "\n"
    for i in range(len(drinkText)):
      if int(drinkText[i].get()) != 0:
        #print(foods[i], foodText[i].get(), int(foodText[i].get())*foodCosts[i], sep = " - ")
        totalStuff += str(
          str(drinks[i]) + " - " + str(drinkText[i].get()) + " - " +
          str(int(drinkText[i].get()) * drinkCosts[i]))
        totalStuff += "\n"
    for i in range(len(dessertText)):
      if int(dessertText[i].get()) != 0:
        #print(foods[i], foodText[i].get(), int(foodText[i].get())*foodCosts[i], sep = " - ")
        totalStuff += str(
          str(desserts[i]) + " - " + str(dessertText[i].get()) + " - " +
          str(int(dessertText[i].get()) * dessertCosts[i]))
        totalStuff += "\n"
    totalStuff += "\n **************************** \n"
    game = ss.SpaceShooter()
    game.run()
    discount = game.ret()
    if discount[0] < 1800 :
      discount_per = discount[0]/20
    else:
      discount_per = 90
    discount = (foodCost+drinkCost+dessertCost)*discount_per/100
    
    totalStuff += str(
      str("Subtotal ") + str(" - ") + str(foodCost + drinkCost + dessertCost ) +
      str("\n"))
    totalStuff += str( f"Discount percentage - {discount_per}% \n")
    totalStuff += str(
      str("Total ") + str(" - ") +
      str((foodCost + drinkCost + dessertCost - discount)//1 + 1) + str("\n"))
    totalStuff += str("Thank you!")
    invoiceTextVar.set(totalStuff)
    global billingScreen
    billingScreen = tk.Tk()
    billingScreen.config(bg='black')
    billingScreen.geometry('500x600+0+0')
    billingScreen.title('Invoice')
    billingScreen.resizable(False, False)

    # Right Panel
    rightPanel = Frame(billingScreen, bd=1, relief=RAISED, bg='black')
    rightPanel.pack(side=LEFT)

    # Calculator

    calculatorOutput = Frame(billingScreen, bd=1, relief=RAISED, bg='black')
    calculatorOutput.pack()

    calculator = Frame(billingScreen, bd=1, relief=RAISED, bg='black')
    calculator.pack()  # Top by default

    titleLabel = Label(calculatorOutput,
                       text="Calculator and Invoice",
                       font=('Dosis', 19, 'bold', 'underline'),
                       fg='black',
                       bg='green',
                       relief=FLAT)
    titleLabel.pack()
    box = Label(calculatorOutput,
                text=equation.get(),
                width=50,
                state=NORMAL,
                font=('Dosis', 12))
    box.pack()

    def press(val):
      global expression
      expression += str(val)
      equation.set(expression)
      box.config(text=expression)

    def equate():
      try:
        expression = (eval(equation.get()))
        box.config(text=expression)
      except:
        equation.set("error")
        expression = ""

    def clear():
      global expression
      equation.set("")
      expression = ""
      box.config(text=expression)

    button1 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='1',
                     width=15,
                     height=2,
                     command=lambda: press(1))
    button1.grid(row=1, column=0)
    button2 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='2',
                     width=15,
                     height=2,
                     command=lambda: press(2))
    button2.grid(row=1, column=1)
    button3 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='3',
                     width=15,
                     height=2,
                     command=lambda: press(3))
    button3.grid(row=1, column=2)
    button4 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='4',
                     width=15,
                     height=2,
                     command=lambda: press(4))
    button4.grid(row=1, column=3)
    button5 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='5',
                     width=15,
                     height=2,
                     command=lambda: press(5))
    button5.grid(row=2, column=0)
    button6 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='6',
                     width=15,
                     height=2,
                     command=lambda: press(6))
    button6.grid(row=2, column=1)
    button7 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='7',
                     width=15,
                     height=2,
                     command=lambda: press(7))
    button7.grid(row=2, column=2)
    button8 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='8',
                     width=15,
                     height=2,
                     command=lambda: press(8))
    button8.grid(row=2, column=3)
    button9 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='9',
                     width=15,
                     height=2,
                     command=lambda: press(9))
    button9.grid(row=3, column=0)
    button0 = Button(calculator,
                     bg='#03ac13',
                     fg='black',
                     text='0',
                     width=15,
                     height=2,
                     command=lambda: press(0))
    button0.grid(row=3, column=1)

    add = Button(calculator,
                 bg='#03ac13',
                 fg='black',
                 text='+',
                 width=15,
                 height=2,
                 command=lambda: press('+'))
    add.grid(row=3, column=2)
    subtract = Button(calculator,
                      bg='#03ac13',
                      fg='black',
                      text='-',
                      width=15,
                      height=2,
                      command=lambda: press('-'))
    subtract.grid(row=3, column=3)
    multiply = Button(calculator,
                      bg='#03ac13',
                      fg='black',
                      text='x',
                      width=15,
                      height=2,
                      command=lambda: press('*'))
    multiply.grid(row=4, column=0)
    divide = Button(calculator,
                    bg='#03ac13',
                    fg='black',
                    text='/',
                    width=15,
                    height=2,
                    command=lambda: press('/'))
    divide.grid(row=4, column=1)
    equal = Button(calculator,
                   bg='#03ac13',
                   fg='black',
                   text='=',
                   width=15,
                   height=2,
                   command=equate)
    equal.grid(row=4, column=2)
    clear = Button(calculator,
                   bg='#03ac13',
                   fg='black',
                   text='clear',
                   width=15,
                   height=2,
                   command=clear)
    clear.grid(row=4, column=3)

    # Put this back
    invoicePanel = Frame(billingScreen, bd=1, relief=FLAT, bg='burlywood')
    invoicePanel.pack()

    # Buttons

    buttonPanel = Frame(billingScreen, bd=1, relief=FLAT, bg='burlywood')
    buttonPanel.pack()  # Specify only from left to right

    saveButton = Button(buttonPanel,
                        text='Save',
                        relief=RAISED,
                        font=('Dosis', 19, 'bold'),
                        fg='black',
                        bg='green',
                        bd=1,
                        width=8,
                        command=createFile)
    saveButton.grid(row=0, column=0)

    clearButton = Button(buttonPanel,
                         text='Clear',
                         relief=RAISED,
                         font=('Dosis', 19, 'bold'),
                         fg='black',
                         bg='green',
                         bd=1,
                         width=8,
                         command=clearAll)
    clearButton.grid(row=0, column=1)

    closeButton = Button(buttonPanel,
                         text='Close',
                         relief=RAISED,
                         font=('Dosis', 19, 'bold'),
                         fg='black',
                         bg='green',
                         bd=1,
                         width=8,
                         command=clearAll)
    closeButton.grid(row=0, column=2)

    invoiceText = LabelFrame(invoicePanel,
                             width=450,
                             height=275,
                             font=('Dosis', 10, 'bold'),
                             text="Invoice - The Incredible Spice")
    invoiceText.pack()
    global invoiceLabel
    invoiceLabel = Label(invoiceText,
                         width=50,
                         height=15,
                         font=('Dosis', 10, 'bold'))
    invoiceLabel.pack(expand=True, fill='both')
    invoiceLabel.configure(text=invoiceTextVar.get())
    billingScreen.protocol("WM_DELETE_WINDOW", clearAll)
    billingScreen.mainloop()

  def clearAll2():
    global totalStuff
    global invoiceTextVar
    global billingScreen
    global setup
    setup = True
    #totalStuff = ""
    #invoiceTextVar.set("")
    global foodCost
    global checkvar
    checkvar = True
    foodCost = 0
    global drinkCost
    drinkCost = 0
    global dessertCost
    dessertCost = 0
    food_cost_var.set(" ")
    drink_cost_var.set(" ")
    dessert_cost_var.set(" ")
    subtotal_cost_var.set(" ")
    taxes_var.set(" ")
    #total_var.set(" ")
    submitButton.configure(state=DISABLED)

    for i in range(len(dessert_variables)):
      dessertText[i].set('0')
      dessert_variables[i].set(0)
      dessertBox[i].config(state=DISABLED)

    for j in range(len(food_variables)):
      foodText[j].set('0')
      food_variables[j].set(0)
      foodBox[j].config(state=DISABLED)

    for k in range(len(drink_variables)):
      drinkText[k].set('0')
      drink_variables[k].set(0)
      drinkBox[k].config(state=DISABLED)

  for food in foods:
    food_variables.append('')
    food_variables[counter] = IntVar(
    )  # Creates an integer variable (type-casting)
    food = customtkinter.CTkCheckBox(
      master=foodPanel,
      text=str(food.title() + " - " + str(foodCosts[foods.index(food)])),
      variable=food_variables[counter],
      font=('Dosis', 19),
      onvalue=1,
      offvalue=0,
      bg_color='#74b72e',
      command=checkFoodClicked,
      text_color='black',
      width=20,
      height=44,
      corner_radius=15,
      border_color='black',
      border_width=3
    )  # Every element becomes a check button; when checked, check's value is 1 else 0
    # Creates a variable (checkbox) for every item
    food.grid(row=counter, column=0, sticky=W)  # West
    # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
    foodBox.append('')
    foodText.append('')
    foodText[counter] = StringVar()
    foodText[counter].set(
      '0')  # When using the value, use an integer, when entering, use a string
    foodBox[counter] = Entry(
      foodPanel,
      bd=1,
      font=('Dosis', 19, 'bold'),
      width=6,
      state=DISABLED,
      textvariable=foodText[counter],
    )  # Until checking the checkbox, the input is disabled
    foodBox[counter].grid(row=counter, column=1, padx=20)
    counter += 1

  # Creating drink items

  counter = 0
  drink_variables = []
  drinkBox = []
  drinkText = []

  def checkDrinkClicked():
    for i in range(len(drink_variables)):
      if drink_variables[i].get() == 1:
        drinkBox[i].config(state=NORMAL)
        submitButton.configure(state=NORMAL)
      else:
        drinkText[i].set('0')
        drink_variables[i].set(0)
        drinkBox[i].config(state=DISABLED)

  for drink in drinks:
    drink_variables.append('')
    drink_variables[counter] = IntVar(
    )  # Creates an integer variable (type-casting)
    drink = customtkinter.CTkCheckBox(
      drinkPanel,
      text=str(drink.title() + " - " + str(drinkCosts[drinks.index(drink)])),
      font=('Dosis', 19),
      onvalue=1,
      offvalue=0,
      variable=drink_variables[counter],
      bg_color='#74b72e',
      command=checkDrinkClicked,
      text_color='black',
      width=20,
      height=44,
      corner_radius=15,
      border_color='black',
      border_width=3
    )  # Every element becomes a check button; when checked, check's value is 1 else 0
    # Creates a variable (checkbox) for every item
    drink.grid(row=counter, column=0, sticky=W)  # West
    # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
    drinkBox.append('')
    drinkText.append('')
    drinkText[counter] = StringVar()
    drinkText[counter].set('0')
    drinkBox[counter] = Entry(
      drinkPanel,
      bd=1,
      font=('Dosis', 19, 'bold'),
      width=6,
      state=DISABLED,
      textvariable=drinkText[counter]
    )  # Until checking the checkbox, the input is disabled
    drinkBox[counter].grid(row=counter, column=1, padx=20)
    counter += 1

  # Creating dessert items

  counter = 0
  dessert_variables = []
  dessertBox = []
  dessertText = []

  def checkDessertClicked():
    for i in range(len(dessert_variables)):
      if dessert_variables[i].get() == 1:
        dessertBox[i].config(state=NORMAL)
        submitButton.configure(state=NORMAL)
      else:
        dessertText[i].set('0')
        dessert_variables[i].set(0)
        dessertBox[i].config(state=DISABLED)

  for dessert in desserts:
    dessert_variables.append(
      'placeholder'
    )  # All the placeholders are going to be changed later, these are checkboxes
    dessert_variables[counter] = IntVar(
    )  # Creates an integer variable (type-casting)
    dessert = customtkinter.CTkCheckBox(
      dessertPanel,
      text=str(dessert.title() + " - " +
               str(dessertCosts[desserts.index(dessert)])),
      font=('Dosis', 19),
      onvalue=1,
      offvalue=0,
      variable=dessert_variables[counter],
      bg_color='#74b72e',
      command=checkDessertClicked,
      text_color='black',
      width=20,
      height=44,
      corner_radius=15,
      border_color='black',
      border_width=3
    )  # Every element becomes a check button; when checked, check's value is 1 else 0
    # Creates a variable (checkbox) for every item
    dessert.grid(row=counter, column=0, sticky=W)  # West
    # Creating input boxes (no. of items), food box is a list which stores the food input boxes, food text stores the text in those boxes
    dessertBox.append('')
    dessertText.append('')
    dessertText[counter] = StringVar()
    dessertText[counter].set('0')
    dessertBox[counter] = Entry(
      dessertPanel,
      bd=1,
      font=('Dosis', 19, 'bold'),
      width=6,
      state=DISABLED,
      textvariable=dessertText[counter]
    )  # Until checking the checkbox, the input is disabled
    dessertBox[counter].grid(row=counter, column=1, padx=20)
    counter += 1

  submitButton = customtkinter.CTkButton(master=submitPanel,
                                         width=400,
                                         height=50,
                                         bg_color=('black'),
                                         fg_color=('green'),
                                         text='Submit',
                                         font=('Dosis', 25, 'bold'),
                                         text_color='black',
                                         text_color_disabled='gray',
                                         state=DISABLED,
                                         command=check,
                                         corner_radius=20)
  submitButton.grid(row=0, column=1)
  '''for i in range(len(totalText)):
    if totalText[i].get()==1:
      submitButton.configure(state=NORMAL)
    else:
      submitButton.configure(state=DISABLED)'''

  food_cost_label = Label(costPanel,
                          text='Food Costs',
                          font=('Dosis', 12, 'bold'),
                          bg='black',
                          fg='#ffd700')
  food_cost_label.grid(row=1, column=0)
  food_cost_text = Entry(costPanel,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=food_cost_var)
  food_cost_text.grid(row=1, column=1, padx=60)

  drink_cost_label = Label(costPanel,
                           text='Drink Costs',
                           font=('Dosis', 12, 'bold'),
                           fg='#ffd700',
                           bg='black')
  drink_cost_label.grid(row=2, column=0)
  drink_cost_text = Entry(costPanel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=drink_cost_var)
  drink_cost_text.grid(row=2, column=1)

  dessert_cost_label = Label(costPanel,
                             text='Dessert Costs',
                             font=('Dosis', 12, 'bold'),
                             fg='#ffd700',
                             bg='black')
  dessert_cost_label.grid(row=3, column=0)
  dessert_cost_text = Entry(costPanel,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=dessert_cost_var)
  dessert_cost_text.grid(row=3, column=1)

  subtotal_cost_label = Label(costPanel,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              fg='#ffd700',
                              bg='black')
  subtotal_cost_label.grid(row=1, column=2, padx=60)
  subtotal_cost_text = Entry(costPanel,
                             font=('Dosis', 12, 'bold'),
                             bd=1,
                             width=10,
                             state='readonly',
                             textvariable=subtotal_cost_var)
  subtotal_cost_text.grid(row=1, column=3)

  def createFile():
    try:
      text_file = filedialog.asksaveasfile(
        mode='w',
        initialdir='C://Users//soham//Desktop',
        title='Save As',
        filetypes=[("text", "*.txt"), ("pdf", "*.pdf"), ("png", "*.png")])
      text_file.write(totalStuff)
    except:
      messagebox.showwarning("Cancelled", "Bill not saved")
      clearAll()

  taxes_cost_label = Label(costPanel,
                           text='Taxes',
                           font=('Dosis', 12, 'bold'),
                           fg='#ffd700',
                           bg='black')
  taxes_cost_label.grid(row=2, column=2)
  taxes_cost_text = Entry(costPanel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=taxes_var)
  taxes_cost_text.grid(row=2, column=3)

  total_cost_label = Label(costPanel,
                           text='Total',
                           font=('Dosis', 12, 'bold'),
                           fg='#ffd700',
                           bg='black')
  total_cost_label.grid(row=3, column=2)
  total_cost_text = Entry(costPanel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=total_var)
  total_cost_text.grid(row=3, column=3)
  if setup != False:
    root.after(1000, update)
    root.mainloop()
    root.protocol("WM_DELETE_WINDOW", clearAll)


def dontSet():
  login = tk.Tk()
  login.geometry('1300x650+0+0')
  login.resizable(False, False)
  login.title("The Incredible Spice: Login Screen")

  img = (Image.open(
    'background2.jpeg'))
  resized = img.resize((1300, 650))
  newimg = ImageTk.PhotoImage(resized)
  #root.config(image=img)
  login.config(bg='#3a5311')

  submittable = False
  passString = StringVar()
  # Background

  label = Label(login, image=newimg)
  label.place(x=0, y=0)

  titlePane = Label(login,
                    bd=1,
                    relief=RAISED,
                    fg='yellow',
                    bg='black',
                    text='The Incredible Spice: Login or Signup',
                    width=70,
                    height=3,
                    font=('Dosis', 21, 'bold'))
  titlePane.place(x=70, y=20)

  inputForm = Frame(login, relief=FLAT, bg='#aef359')
  inputForm.place(x=250, y=150)

  buttonPane = Frame(login, relief=FLAT, bg='#aef359')
  buttonPane.place(x=680, y=450)

  nameLabel = Label(inputForm,
                    text='Name: ',
                    fg='black',
                    bg='#aef359',
                    font=('Dosis', 19, 'bold'),
                    padx=20,
                    pady=50)
  nameLabel.grid(row=0, column=0)

  nameEntry = Entry(inputForm, width=20, font=('Dosis', 15, 'bold'))
  nameEntry.grid(row=0, column=1)

  locationLabel = Label(inputForm,
                        text='Location: ',
                        fg='black',
                        bg='#aef359',
                        font=('Dosis', 19, 'bold'),
                        padx=20,
                        pady=50)
  locationLabel.grid(row=1, column=0)

  locationEntry = Entry(inputForm, width=20, font=('Dosis', 15, 'bold'))
  locationEntry.grid(row=1, column=1)

  phoneLabel = Label(inputForm,
                     text='Phone: ',
                     fg='black',
                     bg='#aef359',
                     font=('Dosis', 19, 'bold'),
                     padx=20,
                     pady=50)
  phoneLabel.grid(row=2, column=0)

  phoneEntry = Entry(inputForm, width=20, font=('Dosis', 15, 'bold'))
  phoneEntry.grid(row=2, column=1)

  tableLabel = Label(inputForm,
                     text='Table No: ',
                     fg='black',
                     bg='#aef359',
                     font=('Dosis', 19, 'bold'),
                     pady=50,
                     padx=50)
  tableLabel.grid(row=0, column=2)

  tableEntry = Entry(inputForm, width=20, font=('Dosis', 15, 'bold'))
  tableEntry.grid(row=0, column=4, padx=20)

  verificationLabel = Label(inputForm,
                            text='Verification: ',
                            fg='black',
                            bg='#aef359',
                            font=('Dosis', 19, 'bold'))
  verificationLabel.grid(row=1, column=2)

  verificationEntry = Entry(inputForm,
                            width=20,
                            font=('Dosis', 15, 'bold'),
                            textvariable=passString,
                            show='*')
  verificationEntry.grid(row=1, column=4, padx=20)

  def signUp():
    global setup
    global name
    global location
    global tableNo
    name = nameEntry.get()
    tableNo = tableEntry.get()
    location = locationEntry.get()
    login.destroy()
    setup = True
    startSet()

  def checkFirst():
    if (verificationEntry.get() == "password" and phoneEntry.get().isnumeric()
        and nameEntry.get() != ""
        and locationEntry.get() != ""):
      signUp()
    else:
      messagebox.showwarning("Gotcha", "Please recheck entries")

  signButton = Button(buttonPane,
                      width=9,
                      height=1,
                      text='See Menu',
                      bg='green',
                      font=('Dosis', 19, 'bold'),
                      command=checkFirst)
  signButton.grid(row=0, column=0, padx=10)

  def showPass():
    if verificationEntry['show'] == '*':
      verificationEntry.configure(show='')
      showButton.configure(text='Hide')
    else:
      verificationEntry.configure(show='*')
      showButton.configure(text='Show')

  showButton = Button(buttonPane,
                      width=7,
                      height=1,
                      text='Show',
                      bg='green',
                      font=('Dosis', 19, 'bold'),
                      command=showPass)
  showButton.grid(row=0, column=2, padx=10)

  login.mainloop()


if setup == False:
  dontSet()