#!/usr/bin/env python3
#PRACTICAL-Code
from tkinter import * #IMORTING TKINTER AND MATH MODULE#
import math as M
#Bhavesh Jadhav F080 FYCS
Exp = "" #ASSIGNED AN VARIABLE EMPTY STRING AND GLOBALING TH VARIABLE#
def press(Event): #FUNCTION CALLED AFTER CERTAIN BUTTON ARE PRESSED WITH PARAMITOR NAMED EVENT#
    global Exp 
    Exp = Exp + str(Event) #ANY BUTTON WE PRESSED STORING ITS VALUE IN STRING#
    eq.set(Exp) #TO DISPLAY THE PRESSED BUTTON#
def clear(): #FUNCTION TO CLEAR THE ENTRY WIDGET#
    global Exp 
    Exp = ""        #SETTING IT TO EMPTY#
    eq.set("")      #SETTING IT TO EMPTY#
def equalpress(): #FUNCTION CALLED IF PRESSED EQUAL TO#
    try: #TRY AND EXCEPT TO EXCEPT THE ERROR OF WRONG SYNTAX#
        global Exp 
        total = str(eval(Exp)) #EVAL DOES THE CALCULATION OF EXPRESSIONS AND STORE THE VALUE AT TOTAL#
        eq.set(total) #DISPLAY THE TOTAL VALUE(ANSWER)#
        Exp = ""        #SETTING IT TO EMPTY#
    except: 
        eq.set("Syntax Error ") #IF ANY INVALID SYNTAX FOUND IT SETS ENTRY TO THIS MESSAGE#
        Exp = "" 
practical_cal = Tk() #CREATING A TK() WINDOW#
practical_cal.configure(background="black") #SET ITS BG COLOR#
practical_cal.title("Practical - Simple Calculator")  #SET ITS TITLE#
practical_cal.geometry("630x648")  #WINDOWS GEOMETRY#
eq = StringVar()   #TEXT VARIABLE IN STRINGVAR THAT STORES EVERY THING IN STRING#
Pc_dAta = Entry(practical_cal,font=("Arial Black",27) ,highlightcolor='orange',textvariable=eq,bg='orange',bd=10,fg='black', width=6) #ENTRY WIDGET#
Pc_dAta.insert(0,'')  #INSERT USED FOR PLACING CURSOR#
Pc_dAta.grid(columnspan=700, ipadx=234) #USED GRID FOR PLACING#
eq.set('{START CALCULATING}')  #DISPLAYING DEFAULT MESSAGE ON ENTRY WIDGET#
#CREATING BUTTONS #
#USING LAMBDA IN COMMAND AND GIVING PARAMETER TO THE FUNCTION PRESS#
BTncaL1 = Button(practical_cal,text=' 1 ',bd=10,fg='black', bg='orange',command=lambda: press(1),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL1.grid(row=2, column=0) 
BTncaL2 = Button(practical_cal,text=' 2 ',bd=10,fg='black', bg='orange',command=lambda: press(2),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL2.grid(row=2, column=1) 
BTncaL3 = Button(practical_cal,text=' 3 ',bd=10,fg='black', bg='orange',command=lambda: press(3),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL3.grid(row=2, column=2) 
BTncaL4 = Button(practical_cal,text=' 4 ',bd=10,fg='black', bg='orange',command=lambda: press(4),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL4.grid(row=3, column=0) 
BTncaL5 = Button(practical_cal,text=' 5 ',bd=10,fg='black', bg='orange', command=lambda: press(5),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL5.grid(row=3, column=1) 
BTncaL6 = Button(practical_cal,text=' 6 ',bd=10,fg='black', bg='orange',command=lambda: press(6),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL6.grid(row=3, column=2) 
BTncaL7 = Button(practical_cal,text=' 7 ',bd=10,fg='black', bg='orange',command=lambda: press(7),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL7.grid(row=4, column=0)
BTncaL8 = Button(practical_cal,text=' 8 ',bd=10,fg='black', bg='orange',command=lambda: press(8),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL8.grid(row=4, column=1) 
BTncaL9 = Button(practical_cal,text=' 9 ',bd=10,fg='black', bg='orange',command=lambda: press(9),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL9.grid(row=4, column=2) 
BTncaL0 = Button(practical_cal,text=' 0 ',bd=10,fg='black', bg='orange', command=lambda: press(0),width=10 ,height=5,activebackground='black',activeforeground='orange') 
BTncaL0.grid(row=5, column=0) 
Add_It = Button(practical_cal,text=' + ',bd=10,fg='black', bg='orange', command=lambda: press("+"),width=10 ,height=5,activebackground='black',activeforeground='orange') 
Add_It.grid(row=2, column=3) 
Minus_It = Button(practical_cal,text=' - ',bd=10,fg='black', bg='orange', command=lambda: press("-"),width=10 ,height=5,activebackground='black',activeforeground='orange') 
Minus_It.grid(row=3, column=3) 
Into_It = Button(practical_cal,text=' * ',bd=10,fg='black', bg='orange',command=lambda: press("*"),width=10 ,height=5,activebackground='black',activeforeground='orange') 
Into_It.grid(row=4, column=3) 
Divide_It = Button(practical_cal,text=' ÷ ',bd=10,fg='black', bg='orange',command=lambda: press("/"),width=10 ,height=5,activebackground='black',activeforeground='orange') 
Divide_It.grid(row=5, column=3) 
Equal_It = Button(practical_cal,text=' = ',bd=10,fg='black', bg='orange',command=equalpress,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Equal_It.grid(row=6, column=3) 
Clear_It = Button(practical_cal,text='Clear',bd=10,fg='black', bg='orange',command=clear,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Clear_It.grid(row=5, column='1') 
Point= Button(practical_cal,text='.',bd=10,fg='black',bg='orange', command=lambda: press('.'),width=10 ,height=5,activebackground='black',activeforeground='orange') 
Point.grid(row=6, column=0)
brlft= Button(practical_cal,text='(',bd=10,fg='black',bg='orange', command=lambda: press('('),width=10 ,height=5,activebackground='black',activeforeground='orange') 
brlft.grid(row=6, column=1)
brrgt= Button(practical_cal,text=')',bd=10,fg='black',bg='orange', command=lambda: press(')'),width=10 ,height=5,activebackground='black',activeforeground='orange') 
brrgt.grid(row=6, column=2)
def backspace():#CLEARING IT BACKWARDS#
    global Exp
    Exp=eq.get()[0:-1]#REVERSE DELETE
    eq.set(Exp) # NEW EXPRESSION AFTER DELETING FROM BACKWARDS
Cancel_It= Button(practical_cal,text='⌫',bd=10,fg='black',bg='orange', command=backspace,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Cancel_It.grid(row=5, column=2)
def sqrts():
    global Exp
    Exp=M.sqrt(int(eq.get()))#USED MATH MODULE TO GET SQUARE-ROOT
    eq.set(Exp)
    Exp=""
Percent_It= Button(practical_cal,text='√',bd=10,fg='black',bg='orange', command=sqrts,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Percent_It.grid(row=6, column=4)
Percent_It= Button(practical_cal,text='π',bd=10,fg='black',bg='orange', command=lambda: press('(22/7)'),width=10 ,height=5,activebackground='black',activeforeground='orange') 
Percent_It.grid(row=5, column=4)
def degree():
    global Exp
    Exp=M.degrees(int(eq.get()))#USED MATH MODULE TO GET DEGREE
    eq.set(f'{Exp}°')
    Exp=""
Degree_It= Button(practical_cal,text='°',bd=10,fg='black',bg='orange', command=degree,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Degree_It.grid(row=4, column=4)
def RAD():
    global Exp
    Exp=M.radians(int(eq.get()))#USED MATH MODULE TO GET RADIANS
    eq.set(f'{Exp} rad')
    Exp=""
Rad_It= Button(practical_cal,text='c',bd=10,fg='black',bg='orange', command=RAD,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Rad_It.grid(row=3, column=4)
def lets_go():
    exit()#EXITED THE CODE
Ex_It= Button(practical_cal,text='✘',bd=10,fg='black',bg='orange', command=lets_go,width=10 ,height=5,activebackground='black',activeforeground='orange') 
Ex_It.grid(row=2, column=4)

practical_cal.mainloop() #THE MAINLOOP