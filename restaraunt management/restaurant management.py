from tkinter import*
from tkinter import filedialog,messagebox
import random
import time

#functions

def reset():
    textReceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_sabji.set('0')
    e_lassi.set('0')
    e_coffee.set('0')
    e_tea.set('0')
    e_icecream.set('0')
    e_oreo.set('0')
    e_kitkat.set('0')
    e_vannila.set('0')
    e_brownie.set('0')

def send():
    def send_msg():
        message=textarea.get(1.0,END)
        number=numberfield.get()

    root2=Toplevel()

    root2.title('Send bill')
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')

    logoImage=PhotoImage(file='email.png')
    label=Label(root2,image=logoImage,bg='red4')
    label.pack(pady=5)

    numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberLabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billLabel=Label(root2, text='Bill Details',font=('arial', 18, 'bold underline'),bg='red4',fg='white')
    billLabel.pack(pady=5)

    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

    if costoffoodvar.get()!='0 Rs':
        textarea.insert(END,f'Cost of Food\t\t\t {priceofFood}Rs\n')
    if costofdrinksvar.get() != '0 Rs':
        textarea.insert(END, f'Cost of Drinks\t\t\t {priceofDrink}Rs\n')
    if costofcakesvar.get() != '0 Rs':
        textarea.insert(END, f'Cost of Cakes\t\t\t {priceofCakes}Rs\n')

        textarea.insert(END, f'Cost of subtotal \t\t\t {subtotalofItems}Rs\n')
        textarea.insert(END, f'service tax\t\t\t {50}Rs\n\n')
        textarea.insert(END, f'Total Cost\t\t\t {subtotalofItems+50}Rs\n')


    sendButton=Button(root2,font=('arial',12,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,
                      command=send_msg)
    sendButton.pack()

    root2.mainloop()

def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

    bill_data=textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your bill is successfully saved')
def reciept():
    global billnumber,date
    textReceipt.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d:%m:%y')
    textReceipt.insert(END,'Reciept Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    textReceipt.insert(END,'Items:\t\t Cost of Items(Rs)\n')

    if e_roti.get()!='0':
        textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*35}\n\n')

    if e_daal.get()!='0':
        textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*50}\n\n')

    if e_fish.get()!='0':
        textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')

    if e_sabji.get()!='0':
        textReceipt.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*90}\n\n')

    if e_lassi.get()!='0':
        textReceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*65}\n\n')
    if e_coffee.get()!='0':
        textReceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*75}\n\n')

    if e_tea.get()!='0':
        textReceipt.insert(END,f'Tea\t\t\t{int(e_tea.get())*35}\n\n')

    if e_icecream.get()!='0':
        textReceipt.insert(END,f'Icecream\t\t\t{int(e_icecream.get())*110}\n\n')

    if e_oreo.get()!='0':
        textReceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*120}\n\n')

    if e_kitkat.get()!='0':
        textReceipt.insert(END,f'Kitkat\t\t\t{int(e_kitkat.get())*130}\n\n')

    if e_vannila.get()!='0':
        textReceipt.insert(END,f'Vannila\t\t\t{int(e_vannila.get())*45}\n\n')

    if e_brownie.get()!='0':
        textReceipt.insert(END,f'Brownie\t\t\t{int(e_brownie.get())*50}\n\n')

    if costoffoodvar.get()!='0 Rs':
        textReceipt.insert(END,f'Cost of Food\t\t\t {priceofFood}Rs\n\n')
    if costoffoodvar.get() != '0 Rs':
        textReceipt.insert(END, f'Cost of Drinks\t\t\t {priceofDrink}Rs\n\n')
    if costoffoodvar.get() != '0 Rs':
        textReceipt.insert(END, f'Cost of Cakes\t\t\t {priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Cost of subtotal \t\t\t {subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'service tax\t\t\t {50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t {subtotalofItems+50}Rs\n\n')


def totalcost():
    global priceofFood,priceofDrink,priceofCakes,subtotalofItems
    item1=int(e_roti.get())
    item2=int(e_daal.get())
    item3=int(e_fish.get())
    item4=int(e_sabji.get())
    item5=int(e_lassi.get())
    item6=int(e_coffee.get())
    item7=int(e_tea.get())
    item8=int(e_icecream.get())
    item9=int(e_oreo.get())
    item10=int(e_kitkat.get())
    item11=int(e_vannila.get())
    item12=int(e_brownie.get())
    priceofFood=(item1*35)+(item2*50)+(item3*100)+(item4*90)

    priceofDrink=(item5*65)+(item6*75)+(item7*35)+(item8*110)

    priceofCakes=(item9*120)+(item10*130)+(item11*45)+(item12*50)

    costoffoodvar.set(str(priceofFood)+' Rs')

    costofdrinksvar.set(str(priceofDrink)+' Rs')

    costofcakesvar.set(str(priceofCakes)+' Rs')

    subtotalofItems=priceofFood+priceofDrink+priceofCakes
    subtotalvar.set(str(subtotalofItems)+' Rs')

    servicetaxvar.set('50 Rs')

    totalcost=subtotalofItems+50
    totalcostvar.set(str(totalcost)+' Rs')

def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')
def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')
def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')
def sabji():
    if var4.get()==1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')
def lassi():
    if var1.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')
def coffee():
    if var2.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')
def tea():
    if var3.get()==1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')
def icecream():
    if var4.get()==1:
        texticecream.config(state=NORMAL)
        texticecream.delete(0,END)
        texticecream.focus()
    else:
        texticecream.config(state=DISABLED)
        e_icecream.set('0')
def oreo():
    if var1.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def kitkat():
    if var2.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')
def brownie():
    if var3.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')
def vannila():
    if var4.get()==1:
        textvannila.config(state=NORMAL)
        textvannila.delete(0,END)
        textvannila.focus()
    else:
        textvannila.config(state=DISABLED)
        e_vannila.set('0')


root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('Restaurant Management System')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE)
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Restaurant Management system',font=('arial',30,'bold'),fg='yellow',bg='red4',width=50,bd=9)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE)
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE)
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()
#variable
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_sabji=StringVar()
e_lassi=StringVar()
e_coffee=StringVar()
e_tea=StringVar()
e_icecream=StringVar()
e_oreo=StringVar()
e_kitkat=StringVar()
e_vannila=StringVar()
e_brownie=StringVar()
costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
totalcostvar=StringVar()
servicetaxvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_sabji.set('0')
e_lassi.set('0')
e_coffee.set('0')
e_tea.set('0')
e_icecream.set('0')
e_oreo.set('0')
e_kitkat.set('0')
e_vannila.set('0')
e_brownie.set('0')

##food

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,
                 command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,
                 command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,
                 command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,
                  command=sabji)
sabji.grid(row=3,column=0,sticky=W)

#entry fields
textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=3,column=1)

#drinks
lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,
                  command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,
                   command=coffee)
coffee.grid(row=1,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,
                command=tea)
tea.grid(row=2,column=0,sticky=W)

icecream=Checkbutton(drinksFrame,text='Icecream',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,
                     command=icecream)
icecream.grid(row=3,column=0,sticky=W)
#entry fields
textlassi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

texttea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=2,column=1)

texticecream=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_icecream)
texticecream.grid(row=3,column=1)

#cakes
oreocakes=Checkbutton(cakesFrame,text='oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,
                      command=oreo)
oreocakes.grid(row=0,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,
                       command=kitkat)
kitkatcake.grid(row=1,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=brownie)
browniecake.grid(row=2,column=0,sticky=W)

vannilacake=Checkbutton(cakesFrame,text='vannilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=vannila)
vannilacake.grid(row=3,column=0,sticky=W)

#entry variable
textoreo=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textkitkat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=1,column=1)

textbrownie=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=2,column=1)

textvannila=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vannila)
textvannila.grid(row=3,column=1)

#costlabels&entry fields
labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=14)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=14)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=14)

labelSubTotal=Label(costFrame,text='SubTotal',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=14)

labelServiceTax=Label(costFrame,text='ServiceTax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3)

labelTotalCost=Label(costFrame,text='TotalCost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3)

#buttons
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReciept=Button(buttonFrame,text='Reciept',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                     command=reciept)
buttonReciept.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                  command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt
textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global opeartor
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)


calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
               command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4
                  ,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
               command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=4,
               command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=4,
               command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
                   command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
             command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=4,
               command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=4,
               command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonmult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
                  command=lambda:buttonClick('*'))
buttonmult.grid(row=3,column=3)

buttonans=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
                 command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calculatorFrame,text='clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
                   command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
               command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttondiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=4,
                 command=lambda:buttonClick('/'))
buttondiv.grid(row=4,column=3)


root.mainloop()
