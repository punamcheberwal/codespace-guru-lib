# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:47:17 2019

@author: Punam
"""

#%%
import tkinter.messagebox
from tkinter import *
import tkinter.scrolledtext as tkst
#import mysql.connector as sql

import pymysql as sql
    
conn=sql.connect(host="localhost",user="root",password="chintu",database='library')
cur=conn.cursor()

cur.execute('create database if not exists library;')
cur.execute('use library;')
cur.execute('''create table if not exists book
                    (bookid int primary key,
                     bookname varchar(30) not null,
                     author varchar(30) not null,
                     price float not null,
                     dop date not null
                     );''')

cur.execute('''create table if not exists student
                    (bookid int ,
                     std_name varchar(30) not null,
                     admin_no int primary key,
                     std_class varchar(10) not null,
                     issue_dt date not null,
                      foreign key(bookid) references book(bookid));''')
#functions
def loginw():
    
    correct_password = 'password'
    if correct_password == myvar.get():
        
        tkinter.messagebox.showinfo(" password.",'correct password.')
        butons()
                          
    else:
         tkinter.messagebox.showinfo(" password.",'Please type the correct password.')
         
def butons():
    clearframe(down)
    student=Button(down,text="student ",state=NORMAL,font=("Courier",8),command=lambda:student1())    
    student.place(x=250,y=300)
    student.config(height = 2, width = 10)
    inputs=Button(down,text="Inputs",state=NORMAL,font=("Courier",8),command=lambda:inputs1())    
    inputs.place(x=150,y=300)
    inputs.config(height = 2, width = 10)
    exits=Button(down, text="Quit", command=lambda root=root:quit(root),height = 2, width = 10).place(x=450,y=300)

#inputs

def inputs1():
    clearframe(down)
    
    global insert
    global update
    global delete
    global output1
    global display
    global clri
    global back
    global text_entry1
    global text_entry2
    global text_entry3
    global text_entry4
    global text_entry5
    
    left=Frame(down,width=600,height=400,borderwidth=2,relief="solid")
    right=Frame(down,width=600,height=400,borderwidth=2,relief="solid")
    
    left.pack(side="left",expand=True,fill="both")
    right.pack(side="right",expand=True,fill="both")
        
    idd2=Label(down,text="INPUTS:",font=("Courier",16))
    idd2.place(x=100,y=100)

    idd3=Label(down,text="BOOK ID:",font=("Courier",14))
    idd3.place(x=100,y=150)
    text_entry1 = Entry(down, textvariable=book_id)
    text_entry1.place(x=200,y=153)
       
    idd4=Label(down,text="BOOK name:",font=("Courier",14))
    idd4.place(x=100,y=200)    
         
    text_entry2 = Entry(down, textvariable=book_name)
    text_entry2.place(x=210,y=203)
    
    idd5=Label(down,text="AUTHOR:",font=("Courier",14))
    idd5.place(x=100,y=250)
    text_entry3 = Entry(down, textvariable=author)
    text_entry3.place(x=200,y=253)
    
    idd6=Label(down,text="PRICE:",font=("Courier",14))
    idd6.place(x=100,y=300)
    text_entry4 = Entry(down, textvariable=price)
    text_entry4.place(x=200,y=303)
    
    idd7=Label(down,text="DATE_PUR:",font=("Courier",14))
    idd7.place(x=100,y=350)
    text_entry5= Entry(down, textvariable=dop)
    text_entry5.place(x=200,y=353)
    
    idd8=Label(down,text="OUTPUTS:",font=("Courier",16))
    idd8.place(x=750,y=100)
        
    insert=Button(down,text="Insert",state=NORMAL,font=("Courier",8),command=lambda:insertw())    
    insert.place(x=200,y=380)
    insert.configure(height = 2, width = 10)
    
    update=Button(down,text="Update",state=NORMAL,font=("Courier",8),command=lambda:updatew())
    update.place(x=300,y=380)
    update.configure(height = 2, width = 10)

    delete=Button(down,text="Delete",state=NORMAL,font=("Courier",8),command=lambda:deletew())   
    delete.place(x=400,y=380)
    delete.configure(height = 2, width = 10)
    
    clri=Button(down,text="CLEAR-I",state=NORMAL,font=("Courier",8),command=lambda:clr_i())    
    clri.place(x=500,y=380)
    clri.configure(height = 2, width = 10)
    
    display=Button(down, text="display table",state=NORMAL,font=("Courier",8),command=lambda:displayw())    
    display.place(x=25,y=380)
    display.configure(height = 2, width = 20)
    
    search=Button(down,text="search",state=NORMAL,font=("Courier",8),command=lambda:searchw()) 
    search.place(x=600,y=380)
    search.configure(height = 2, width = 10)
    
    back=Button(down,text="back",state=NORMAL,font=("Courier",8),command=lambda:butons())    
    back.place(x=850,y=380)
    back.configure(height = 2, width = 10)
    
def clr_i():
    
    text_entry1.delete('0', END)
    text_entry2.delete('0', END)
    text_entry3.delete('0', END) 
    text_entry4.delete('0', END)
    text_entry5.delete('0', END)
    
def insertw():
        
    b=0
    output1=Text(down,height=15, width=25)    
    output1.configure(state=NORMAL) 
    output1.delete('1.0', END)
    a=(int(book_id.get()),)
    cur.execute("select bookid from book;") 
    
    for i in cur:                        
        if i==a:
            tkinter.messagebox.showinfo("insert.","duplicate entry for bookid.pls enter correct id")
            b=a
                
    if b!=a : 
        if len(book_id.get())==0 or len(book_name.get())==0 or len(author.get())==0 or len(price.get())==0 or len(dop.get())==0:
            tkinter.messagebox.showinfo("insert.","please fill all data ")
       
        else:             
            tkinter.messagebox.showinfo("insert.","data inserted.")
            str="insert into book values(%s,%s,%s,%s,%s)"        
            data=(book_id.get(),book_name.get(),author.get(),price.get(),dop.get())
            cur.execute(str,data)
            conn.commit()
            na=book_id.get()
            str2=("select * from book where bookid={}").format(na)
            cur.execute(str2)
            for i in cur:    
                for j in i:                
                    output1.insert(END,'\n')
                    output1.insert(END,j)
                    conn.commit()            
            output1.configure(state=DISABLED)
            output1.place(x=750,y=150)
                
def updatew():
    output1=Text(down,height=15, width=25)
    output1.config(state=NORMAL) 
    output1.delete('1.0', END)
            
    if len(book_id.get())==0  or len(price.get())==0:
        tkinter.messagebox.showinfo("update.","please fill bookid and price.")
        
    else:
        tkinter.messagebox.showinfo("update.","table updated.")
        data1=int(book_id.get())
        data2=float(price.get())
        str=("update book set price ={} where bookid={}").format(data2,data1)
        cur.execute(str)
        conn.commit()
        na=book_id.get()
        str2=("select * from book where bookid={}").format(na)
        cur.execute(str2)
        for i in cur:    
            for j in i:  
                output1.insert(END,'\n')
                output1.insert(END,j)    
                conn.commit()
        output1.configure(state=DISABLED)
        output1.place(x=750,y=150)
                    
def deletew():
    
    output1=Text(down,height=15, width=25)
    output1.configure(state=NORMAL) 
    output1.delete('1.0', END)
    
    if len(book_id.get())==0:
        tkinter.messagebox.showinfo(" delete.",'Please enter book id.')
    else:
        data1=int(book_id.get())
        str=("delete from book  where bookid={}").format(data1)
        cur.execute(str)
        conn.commit()    
        cur.execute("select * from book;")
        for i in cur:    
            for j in i:  
                output1.insert(END,'\n')
                output1.insert(END,j)            
        output1.configure(state=DISABLED)
        output1.place(x=750,y=150) 
    
def displayw():
    
    output1=tkst.ScrolledText(down,height=15, width=25,wrap=WORD)    
    output1.configure(state=NORMAL) 
   # output1.delete('1.0', END)
    cur.execute("select * from book;")
    
    for i in cur:    
        for j in i:  
            output1.insert(END,'\n')
            output1.insert(END,j)    
    output1.configure(state=DISABLED)
    output1.place(x=750,y=150)
        
def searchw():
    insert.destroy()
    update.destroy()
    delete.destroy()
    display.destroy()
        
    search_au=Button(down,text="search author",state=NORMAL,font=("Courier",8),command=lambda:sear_au())    
    search_au.place(x=200,y=380)
    search_au.configure(height = 2, width = 10)
    
    search_book=Button(down,text="search book",state=NORMAL,font=("Courier",8),command=lambda:sear_boo())
    search_book.place(x=300,y=380)
    search_book.configure(height = 2, width = 10)
        
    back1=Button(down,text="back",state=NORMAL,font=("Courier",8),command=lambda:inputs1())    
    back1.place(x=850,y=380)
    back1.configure(height = 2, width = 10)

def sear_au():
    output1=Text(down,height=15, width=25)
    output1.config(state=NORMAL) 
    output1.delete('1.0', END)
    na=author.get()
    
    str="select * from book where author= '{}'".format(na)  
    cur.execute(str)
    for i in cur:    
        for j in i:  
            output1.insert(END,'\n')
            output1.insert(END,j)   
    x=output1.get('1.0',END)
    
    if len(x)==1:
        tkinter.messagebox.showinfo("search","author not found.")
    output1.configure(state=DISABLED)
    output1.place(x=750,y=150)

def sear_boo():
    output1=Text(down,height=15, width=25)
    output1.configure(state=NORMAL) 
    output1.delete('1.0', END)
    na=book_name.get()
    
    str="select * from book where bookname= '{}'".format(na)  
    cur.execute(str)

    for i in cur:    
        for j in i:  
            output1.insert(END,'\n')
            output1.insert(END,j) 
    x=output1.get('1.0',END)
    
    if len(x)==1:
        tkinter.messagebox.showinfo("search","book  not found.")
    output1.configure(state=DISABLED)
    output1.place(x=750,y=150)
  
#student
def student1():
    
    clearframe(down)
    
    global text_entry10
    global text_entry11
    global text_entry12
    global text_entry13
    global text_entry14
    global text_entry15
    
    left=Frame(down,width=600,height=400,borderwidth=2,relief="solid")
    right=Frame(down,width=600,height=400,borderwidth=2,relief="solid")
    
    left.pack(side="left",expand=True,fill="both")
    right.pack(side="right",expand=True,fill="both")
    
    idd8=Label(down,text="STUDENT DETAILS:",font=("Courier",16))
    idd8.place(x=100,y=50)
    
    idd10=Label(down,text="BOOK ID:",font=("Courier",14))
    idd10.place(x=100,y=100)
    
    text_entry10 = Entry(down, textvariable=book_id)
    text_entry10.place(x=200,y=103)

    
    idd11=Label(down,text="STDname:",font=("Courier",14))
    idd11.place(x=100,y=150)    
         
    text_entry11 = Entry(down, textvariable=std_name)
    text_entry11.place(x=200,y=153)
    
    idd12=Label(down,text="admin_no:",font=("Courier",14))
    idd12.place(x=100,y=200)    
         
    text_entry12 = Entry(down, textvariable=std_roll)
    text_entry12.place(x=200,y=203)
    
    idd13=Label(down,text="STDclass:",font=("Courier",14))
    idd13.place(x=100,y=250)  
    
    text_entry13 = Entry(down, textvariable=std_class)
    text_entry13.place(x=200,y=253)
    
#  idd3=Label(down,text="BOOK ID:",font=("Courier",14))
 #   idd3.place(x=100,y=250)
    
  #  text_entry15 = Entry(down, textvariable=book_id)
   # text_entry15.place(x=200,y=253)

    idd14=Label(down,text="ISSUEDt:",font=("Courier",14))
    idd14.place(x=100,y=300)    
         
    text_entry14 = Entry(down, textvariable=issue_dt)
    text_entry14.place(x=200,y=303)
        
#    idd14=Label(down,text="RETURNDt:",font=("Courier",14))
 #   idd14.place(x=100,y=350)    
         
 #   text_entry14 = Entry(down, textvariable=return_dt)
  #  text_entry14.place(x=200,y=353)
    
    idd15=Label(down,text="OUTPUTS:",font=("Courier",16))
    idd15.place(x=750,y=100)
       
    issue=Button(down,text="Issue",state=NORMAL,font=("Courier",10),command=lambda:issuew())   
    issue.place(x=200,y=380)
    issue.config(height = 2, width = 10)

    return1=Button(down,text="Return",state=NORMAL,font=("Courier",10),command=lambda:returnw())   
    return1.place(x=300,y=380)
    return1.config(height = 2, width = 10)
    
    lis1=Button(down,text="Books_Issued",state=NORMAL,font=("Courier",10),command=lambda:issued())   
    lis1.place(x=400,y=380)
    lis1.config(height = 2, width = 14)
    
    clrstd=Button(down,text="CLEAR-STUDENT ",state=NORMAL,font=("Courier",10),command=lambda:std_i())    
    clrstd.place(x=550,y=380)
    clrstd.config(height = 2, width = 20)
    
    back=Button(down,text="Back",state=NORMAL,font=("Courier",8),command=lambda:butons())    
    back.place(x=850,y=390)
    back.configure(height = 1, width = 10)
    
    
def issuew():
    
    output1=Text(down,height=15, width=25)
    output1.config(state=NORMAL) 
 #   output1.delete('1.0', END)
       
    if len(std_roll.get())==0 or len(std_name.get())==0 or len(std_class.get())==0 or len(issue_dt.get())==0 or len(book_id.get())==0:
            tkinter.messagebox.showinfo("Issue.","Please fill all data.")
    else:
        data=(book_id.get(),std_name.get(),std_roll.get(),std_class.get(),issue_dt.get())
        str="insert into student values(%s,%s,%s,%s,%s)"
 #       data=(book_id.get(),std_name.get(),std_roll.get(),std_class.get(),issue_dt.get())
        cur.execute(str,data)
        conn.commit()
        na=std_roll.get()       
        str2=("select * from student where std_roll={};").format(na)
        cur.execute(str2)
        
        for i in cur:    
            for j in i: 
                 
                output1.insert(END,'\n')
                output1.insert(END,j)
                conn.commit()
                
    output1.place(x=750,y=150)                   
    output1.configure(state=DISABLED)
   # output1.place(x=750,y=150)
    
def std_i():
    text_entry10.delete('0', END)
    text_entry11.delete('0', END)
    text_entry12.delete('0', END)
    text_entry13.delete('0', END)
    text_entry14.delete('0', END)

def issued():
    output1=tkst.ScrolledText(down,height=15, width=25,wrap=WORD)
    output1.config(state=NORMAL) 
 #   output1.delete('1.0', END)
    cur.execute("select * from student;")
    
    for i in cur:    
        for j in i:  
            output1.insert(END,'\n')
            output1.insert(END,j) 
    output1.place(x=750,y=150)  
    output1.configure(state=DISABLED)
   # output1.place(x=750,y=150)    
    
def returnw():
    output1=Text(down,height=15, width=25)
    output1.config(state=NORMAL) 
#    output1.delete('1.0', END)
    if len(std_roll.get())==0:
        tkinter.messagebox.showinfo("issue.","please fill all data especially admin_no. ")
    else:
        data1=int(std_roll.get())
        str=("delete from student  where std_roll={};").format(data1)
            
        cur.execute(str)
        conn.commit()
    
    cur.execute("select * from student;")
    for i in cur:    
        for j in i:  
            output1.insert(END,'\n')
            output1.insert(END,j)   
    output1.place(x=750,y=150)
    output1.configure(state=DISABLED)
  #  output1.place(x=750,y=150)

#brochure
def brochure():
    clearframe(down)       
    v=StringVar(down)
    v.set("GENRE")
    a=OptionMenu(down,v,"FICTION","EDUCATION","ACTION AND ADVENTURE","LITERATURE",command=genre)  
    a.place(x=100,y=50)
    a.config(width=7,height=2,font=("Times New Roman",20))
    
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:home())
    button1.place(x=200,y=300)
    
    
def genre(s):
    clearframe(down)
    if s=="FICTION":
        fiction()
        
    elif s=="EDUCATION":
        edu()
    elif s=="ACTION AND ADVENTURE":
        aaa()
    elif s=="LITERATURE":
        lit()

def fiction():
    clearframe(down)
    
    button1=Button(down,text="lady midnight",font=("Courier",20),command=lambda:lm())
    button2=Button(down,text="the cursed child",font=("Courier",20),command=lambda:cc())
    button3=Button(down,text="the demigod diaries",font=("Courier",20),command=lambda:dg())
    button4=Button(down,text="the world of ice and fire",font=("Courier",20),command=lambda:fire())
    button5=Button(down,text="opal deception",font=("Courier",20),command=lambda:od())
    button6=Button(down,text="BACK",font=("Courier",20),command=lambda:brochure())
    button1.place(x=109,y=10)
    button2.place(x=100,y=90)
    button3.place(x=100,y=170)
    button4.place(x=100,y=240)
    button5.place(x=100,y=320)
    button6.place(x=500,y=380)

def edu():
    clearframe(down)
    button1=Button(down,text="computer science with python class 12",font=("Courier",20),command=lambda:cs())
    button2=Button(down,text="object oriented programming with C++",font=("Courier",20),command=lambda:c())
    button3=Button(down,text="chemistry for class 11 Vol I",font=("Courier",20),command=lambda:chm())
    button4=Button(down,text="mathematics for class 12 vol I",font=("Courier",20),command=lambda:math())
    button5=Button(down,text="concepts of physics class 12 vol II",font=("Courier",20),command=lambda:phy())
    button6=Button(down,text="BACK",font=("Courier",20),command=lambda:brochure())
    button1.place(x=20,y=10)
    button2.place(x=20,y=90)
    button3.place(x=20,y=170)
    button4.place(x=20,y=240)
    button5.place(x=20,y=320)
    button6.place(x=500,y=380)

def aaa():
    clearframe(down)
    
    button1=Button(down,text="the hunger games",font=("Courier",20),command=lambda:hg())
    button2=Button(down,text="the house of silk",font=("Courier",20),command=lambda:hs())
    button3=Button(down,text="the da vinci code",font=("Courier",20),command=lambda:dvc())
    button4=Button(down,text="the scortch trials",font=("Courier",20),command=lambda:st())
    button5=Button(down,text="memory man",font=("Courier",20),command=lambda:mm())
    button6=Button(down,text="BACK",font=("Courier",20),command=lambda:brochure())
    button1.place(x=100,y=10)
    button2.place(x=100,y=90)
    button3.place(x=100,y=170)
    button4.place(x=100,y=240)
    button5.place(x=100,y=320)
    button6.place(x=500,y=380)

def lit():
    clearframe(down)
    
    button1=Button(down,text="oliver twist",font=("Courier",20),command=lambda:ot())
    button2=Button(down,text="merchant of venice",font=("Courier",20),command=lambda:mv())  
    button3=Button(down,text="pride and prejudice",font=("Courier",20),command=lambda:pp())
    button4=Button(down,text="tom sawyer",font=("Courier",20),command=lambda:ts())
    button5=Button(down,text="the final problem",font=("Courier",20),command=lambda:fp())
    button6=Button(down,text="BACK",font=("Courier",20),command=lambda:brochure())
    button1.place(x=100,y=10)
    button2.place(x=100,y=90)
    button3.place(x=100,y=170)
    button4.place(x=100,y=240)
    button5.place(x=100,y=320)
    button6.place(x=500,y=380)

def lm():
    clearframe(down)

    text1 = Text(down, height=15, width=30)
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\lm.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
   
    ladymid=Label(down,text="Name:Lady Midnight \n Author:Cassandra Clare",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
      
   
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
    
    quote = """DESCRIPTION:
    Together with her parabatai 
    Julian Blackthorn, Emma must learn to trust
    her head and her heart as she investigates 
    a demonic plot that stretches across Los 
    Angeles, from the Sunset Strip 
    to the enchanted sea that pounds the 
    beaches of Santa Monica. If only
    her heart didn’t lead her in treacherous 
    directions…Making things even more
    complicated, Julian’s brother Mark
    —who was captured by the faeries five years
    ago—has been  returned as a bargaining chip. 
    The faeries are desperate to find out who 
    is murdering their kind—and they need the 
    Shadowhunters’ help to do it. But time works
    differently in faerie, so Mark has barely aged 
    and doesn’t recognize his family. Can he ever 
    truly return to them? Will the faeries really 
    allow it? Glitz, glamours, and Shadowhunters
    abound in this heartrending opening to 
    Cassandra Clare’s Dark Artifices series.    """
    text2.insert(END, quote)    

    text2.place(x=500,y=100)
    
    text2.configure(state=DISABLED)
    
    
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:fiction())
    button1.place(x=400,y=380)

def cc():
    clearframe(down)
    
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\cc.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    
    ladymid=Label(down,text="Name:Cursed Child \n Author:JK Rowling",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
      
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
      
    quote = """DESCRIPTION:
    It was always difficult being Harry Potter and
    it isn’t much easier now that he is an 
    overworked employee of the Ministry of
    Magic, a husband and father of three 
    school-age children.While Harry
    grapples with a past that refuses to stay
    where it belongs, his youngest son Albus 
    must struggle with the weight of a family 
    legacy he never wanted. As past and present
    fuse ominously,both father and son learn 
    the uncomfortable truth:sometimes, 
    darkness comes from unexpected places. """
    text2.insert(END, quote)    
    text2.place(x=500,y=100)
    
    text2.configure(state=DISABLED)
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:fiction())
    button1.place(x=400,y=380)
    
def dg():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\dg.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:Demigod Diaries \n Author:Rick Riordan",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
      
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
    
    quote = """DESCRIPTION:
    What dangers do runaway demigods Luke and 
    Thalia face on their way to Camp Half-Blood?
    Are Percy and Annabeth up to the task of 
    rescuing stolen goods from a fire-
    breathing giant who doesn't take kindly
    to intruders? How exactly are Leo, Piper,
    and Jason supposed to find a runaway 
    table, dodge a band of party-loving Maenads,
    and stave off a massive explosion...all 
    in one hour or less?With his trademark wit 
    and creativity, Rick Riordan answers these 
    questions and more in three never-before-seen
    short stories that provide vital back-story 
    to the Heroes of Olympus and Percy Jackson
    books.Original art, enlightening character
    interviews and profiles, puzzles, and a 
    quiz add to the  fun in this action
    packed collection. """
    text2.insert(END, quote)    
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    
   
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:fiction())
    button1.place(x=400,y=380)    
    
    
def fire():
    clearframe(down)
   
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\fire.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:The World Of Ice And Fire \n Author:George RR Martin",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=120,y=10)
        
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
      
    quote = """DESCRIPTION:
    This lavishly illustrated volume is a 
    comprehensive history of the Seven Kingdoms, 
    providing vividly constructed accounts of
    the epic battles, bitter rivalries, and
    daring rebellions that lead to the events
    of A Song of Ice and Fire and HBO’s Game of
    Thrones. In a collaboration that’s been years
    in the making, Martin has teamed with 
    Elio M. García, Jr., and Linda Antonsson,
    the founders of the renowned fan site
    Westeros.org—perhaps the only people who know
    this world almost as well as its visionary
    creator.Collected here is all the accumulated 
    knowledge,scholarly speculation, and
    inherited folk tales of maesters and septons,
    maegi and singers, """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
   
    
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:fiction())
    button1.place(x=400,y=380)    
    
   
def od():
    clearframe(down)
 
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\od.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:Opal Deception \n Author:Eoin Colfer",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=120,y=10)
       
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
     
    quote = """DESCRIPTION:
    The evil pixie Opal Koboi has spent the last
    year in a self-induced coma, plotting her
    revenge on all those who foiled her
    attempt to destroy the LEPrecon
    fairy police. And Artemis Fowl is at the
    top of her list.After his last run-in
    with the fairies, Artemis had his 
    mind wiped of his memories of the
    world belowground. But they have not 
    forgotten about him. Once again, he must 
    stop the human and fairy worlds from 
    colliding—only this time, Artemis faces
    an enemy who may have finally outsmarted him."""
    text2.insert(END, quote)
    
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    
    
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:fiction())
    button1.place(x=400,y=380)
   

def cs():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\cs.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
  
    ladymid=Label(down,text="Name:computer science with python class12 \n Author:Sumita Arora",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=0,y=10)
       
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
      
    quote = """DESCRIPTION:
    Paperback
    Published by Dhanpat Rai & Co."""
    text2.insert(END, quote)
    
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    
  
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:edu())
    button1.place(x=400,y=380)

def c():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\c.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:object oriented programming with C++ \n Author:E Balagurusamy",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=0,y=10)
      
    text2 = tkst.ScrolledText(down, height=15, width=50)
      
    quote = """DESCRIPTION:
    Paperback
    Published (first published 1994)"""
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    
    text2.configure(state=DISABLED)
    

    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:edu())
    button1.place(x=400,y=380)


def chm():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\ob\chm.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
   
    ladymid=Label(down,text="Name:chemistry for class 11 Vol I \n Author:Pradeep",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=20,y=10)
        
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
  
      
    quote = """DESCRIPTION:
    Paperback
    Published by Pradeep Publication"""
    text2.insert(END, quote)
    
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)

    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:edu())
    button1.place(x=400,y=380)

def math():
    clearframe(down)
   
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\math.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    
    ladymid=Label(down,text="Name:mathematics for class 12 vol I \n Author:RD Sharma",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=20,y=10)
     
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
   
    quote = """DESCRIPTION:
    Paperback, 829 pages
    Published by Dhanpat Rai Publishing Co Pvt Ltd"""
    text2.insert(END, quote)
   
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
 
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:edu())
    button1.place(x=400,y=380)
    
def phy():
    clearframe(down)

    photo = PhotoImage(file = r"C:\Users\Punam\Documents\phy.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:concepts of physics class 12 vol II \n Author:HC Verma",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=0,y=10)
       
    text2 =tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
     
    quote = """DESCRIPTION:
    Paperback, 450 pages
    Published June 1st 2011 
    by Bharati Bhawan 
    (first published 1999)"""
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)

    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:edu())
    button1.place(x=400,y=380)
    
def hg():
    clearframe(down)
   
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\hg.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
   
    ladymid=Label(down,text="Name:The Hunger Games \n Author:Suzanne Collins",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
        
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
    
    quote = """DESCRIPTION:
    In the ruins of a place once known as
    North America lies the nation of Panem, 
    a shining Capitol surrounded by twelve 
    outlying districts. The Capitol is harsh
    and cruel and keeps the districts in line
    by forcing them all to send one boy and 
    one girl between the ages of twelve and 
    eighteen to participate in the annual
    Hunger Games, a fight to the death on live
    TV. Sixteen-year-old Katniss Everdeen, who 
    lives alone with her mother and younger
    sister, regards it as a death sentence when 
    she is forced to represent her district in the
    Games. But Katniss has been close to dead 
    before - and survival, for her, is second
    nature. Without really meaning to, she becomes 
    a contender. But if she is to win, she will
    have to start making choices that weigh 
    survival against humanity and life against
    love.     """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
  
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:aaa())
    button1.place(x=400,y=380)

def hs():
    clearframe(down)

    photo = PhotoImage(file = r"C:\Users\Punam\Documents\hs.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:The House Of Silk \n Author:Anthony Horowitz",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
      
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
    
    quote = """DESCRIPTION:
    Once again, THE GAME’S AFOOT…
    London, 1890. 221B Baker St. A fine art
    dealer named Edmund Carstairs visits
    Sherlock Holmes and Dr John Watson to beg for
    their help. He is being menaced by a strange 
    man in a flat cap – a wanted criminal who 
    seems to have followed him all the way from 
    America. In the days that follow, his home is 
    robbed, his family is threatened. And then 
    the first murder takes place.Almost
    unwillingly, Holmes and Watson find 
    themselves being drawn ever deeper 
    into an international conspiracy connected
    to the teeming criminal underworld of
    Boston, the gaslit streets of London, 
    opium dens and much, much more. And as 
    they dig, they begin to hear the whispered
    phrase-the House of Silk-a mysterious
    entity that connects the highest levels of
    government to the deepest depths of 
    criminality. Holmes begins to fear that he has
    uncovered a conspiracy that threatens to tear
    apart the very fabric of society.The Arthur 
    Conan Doyle Estate chose the celebrated, """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
  
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:aaa())
    button1.place(x=400,y=380)

def dvc():
    clearframe(down)
 
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\dvc.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:The Da Vinci Code \n Author:Dan Brown",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
       
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
    
    quote = """DESCRIPTION:
    While in Paris, Harvard symbologist
    Robert Langdon is awakened by a phone
    call in the dead of the night. The 
    elderly curator of the Louvre has been
    murdered inside the museum, his body 
    covered in baffling symbols. As Langdon
    and gifted French cryptologist Sophie
    Neveu sort through the bizarre riddles,
    they are stunned to discover a trail of 
    clues hidden in the works of Leonardo 
    da Vinci—clues visible for all to see
    and yet ingeniously disguised by the 
    painter.Even more startling, the late 
    curator was involved in the Priory of
    Sion—a secret society whose members 
    included Sir Isaac Newton, Victor Hugo, 
    and Da Vinci—and he guarded a
    breathtaking historical secret. Unless 
    Langdon and Neveu can decipher the
    labyrinthine puzzle—while avoiding the 
    faceless adversary who shadows their every
    move—the explosive, ancient truth will 
    be lost forever. """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
 
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:aaa())
    button1.place(x=400,y=380)

def st():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\st.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    

    ladymid=Label(down,text="Name:The Scorch Trials \n Author:James Dashner",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)    
    text2 =tkst.ScrolledText(down, height=15, width=50,wrap=WORD) 
    quote = """DESCRIPTION:
    Thomas was sure that escape from the 
    Maze would mean freedom for him and 
    the Gladers. But WICKED isn’t done 
    yet. Phase Two has just begun. The 
    Scorch.There are no rules. There is
    no help. You either make it or you 
    die.The Gladers have two weeks to
    cross through the Scorch—the most
    burned-out section of the world. 
    And WICKED has made sure to adjust
    the variables and stack the odds 
    against them.Friendships will be
    tested. Loyalties will be broken. 
    All bets are off.There are others 
    now. Their survival depends on the
    Gladers’ destruction—and they’re 
    determined to survive.  """
    text2.insert(END, quote)
    
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:aaa())
    button1.place(x=400,y=380)

def mm():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\mm.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    ladymid=Label(down,text="Name:Memory Man \n Author:David Baldacci",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)   
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD) 
    quote = """DESCRIPTION:
    Now a police detective, Decker
    returned from a stakeout one evening and
    entered a nightmare--his wife, young 
    daughter, and brother-in-law had been
    murdered.His family destroyed, their
    killer's identity as mysterious as the
    motive behind the crime, and unable to
    forget a single detail from that horrible
    night, Decker finds his world collapsing
    around him. He leaves the police force,
    loses his home, and winds up on the 
    street, taking piecemeal jobs as a 
    private investigator when he can.
    But over a year later, a man turns 
    himself in to the police and confesses
    to the murders. At the same time a 
    horrific event nearly brings Burlington
    to its knees, and Decker is called back
    in to help with this investigation. 
    Decker also seizes his chance to learn
    what really happened to his family that 
    night. To uncover the stunning truth, he
    must use his remarkable gifts and     
    the burdens that go along with them.
    He must endure the memories he would
    much rather forget. And he may have 
    to make the ultimate sacrifice.  """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:aaa())
    button1.place(x=400,y=380)

def ot():
    clearframe(down)
  
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\ot.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
  
    ladymid=Label(down,text="Name:Oliver Twist \n Author:Charles Dickens",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)    
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
  
    quote = """DESCRIPTION:
    The story of Oliver Twist - orphaned,
    and set upon by evil and adversity
    from his first breath shocked readers
    when it was published. After running 
    away from the workhouse and pompous
    beadle Mr Bumble, Oliver finds himself
    lured into a den of thieves peopled by 
    vivid and memorable characters the
    Artful Dodger, vicious burglar Bill
    Sikes, his dog Bull's Eye, and
    prostitute Nancy, all watched over by
    cunning master-thief Fagin. Combining
    elements of Gothic Romance.  """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
  
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:lit())
    button1.place(x=400,y=380)

def mv():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\mv.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    ladymid=Label(down,text="Name:Merchant Of Venice \n Author:William Shakespeare",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=120,y=10)
        
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)  
    quote = """DESCRIPTION:
    Antonio, an antisemitic merchant,
    takes a loan from the Jew Shylock
    to help his friend to court Portia.
    Antonio can't repay the loan, and
    without mercy, Shylock demands a 
    pound of his flesh. The heiress
    Portia, now the wife of Antonio's
    friend, dresses as a lawyer and
    saves Antonio.  """
    text2.insert(END, quote)
    
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:lit())
    button1.place(x=400,y=380)

def pp():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\pp.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:Pride And Prejudice \n Author:Jane Austen",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
       
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
      
    quote = """DESCRIPTION:
    The romantic clash between the 
    opinionated Elizabeth and her proud 
    beau, Mr. Darcy, is a splendid
    performance of civilized sparring.
    And Jane Austen's radiant wit 
    sparkles as her characters dance a
    delicate quadrille of flirtation 
    and intrigue, making this book the
    most superb comedy of manners of 
    Regency England.  """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
    
   
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:lit())
    button1.place(x=400,y=380)

def ts():
    clearframe(down)

    photo = PhotoImage(file = r"C:\Users\Punam\Documents\ts.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
   
    ladymid=Label(down,text="Name:Tom Sawyer \n Author:Mark Twain",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
   
    text2 =tkst.ScrolledText(down, height=15, width=50,wrap=WORD)
     
    quote = """DESCRIPTION:
    An adventure story for children,
    The Adventures of Tom Sawyer is 
    a fun-filled book that shows life
    along the Mississippi River in 
    the 1840s. Written by Mark Twain,
    the book shows masterfully-done 
    satire, racism, childhood, and 
    the importance of loyalty and 
    courage- no matter the cost. """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
  
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:lit())
    button1.place(x=400,y=380)

def fp():
    clearframe(down)
    
    photo = PhotoImage(file = r"C:\Users\Punam\Documents\fp.png") 
    pic=Label(down,image=photo)
    pic.place(x=200,y=100)
    pic.image=photo    
    
    ladymid=Label(down,text="Name:The Final Problem \n Author:Arthur Canon Doyle",font=("Courier",20))
    ladymid.pack()
    ladymid.place(x=220,y=10)
      
    text2 = tkst.ScrolledText(down, height=15, width=50,wrap=WORD) 
    quote = """DESCRIPTION:
    The death of detective 
    Sherlock Holmes shakes the world.
    Even The Queen herself expresses 
    resentment over the loss of the
    popular Victorian hero. Petr Kopl
    gives us a graphic kick and picks
    up his third World heroes of 
    tomorrow through the eyes of genius
    writer Sir Arthur Conan Doyle
    . He takes us to a place where
    evil has a true face, men are 
    gentlemen and women are ladies. We
    visit his comic world of excitement
    and adventure. Come and bear witness
    to the last heroic battle where 
    Sherlock Holmes paid with his life.
    Or did he? """
    text2.insert(END, quote)
    text2.place(x=500,y=100)
    text2.configure(state=DISABLED)
   
    button1=Button(down,text="BACK",font=("Courier",20),command=lambda:lit())
    button1.place(x=400,y=380)


    
def quit(root):
    root.destroy()

root=Tk(className="book")
root.geometry("1050x650")

global right
global left
global up
global down

#window
root.resizable(width=False,height=False)

#frames
up=Frame(root,height=100,borderwidth=2, relief="solid",)
down=Frame(root,height=400,borderwidth=2, relief="solid")       
up.pack(side="top",expand=True,fill="both")
down.pack(side="bottom",expand=True,fill="both")

#content of up
title=Label(up,text="""Welcome to 
GURUKUL 
Library""",font=("Courier",40))
title.pack()
icon=PhotoImage(file=r"C:\Users\Punam\Documents\library.png")
pic=Label(up,image=icon)
pic.place(x=870,y=0)


def clearframe(x):
    #i need an empty frame to place widget
    for widget in x.winfo_children():
        widget.destroy() 
 
    
myvar = StringVar()
book_id=StringVar()
book_name=StringVar()
author=StringVar()
price=StringVar()
dop=StringVar()
std_name=StringVar()
std_roll=StringVar()
std_class=StringVar()
issue_dt=StringVar()
return_dt=StringVar()


def loginw2():
    clearframe(down)
    idd=Label(down,text="BOOK STORE MANAGEMENT SYSTEM  PASSWORD:",font=("Courier",20))
    idd.place(x=100,y=20)
    text_entry = Entry(down, textvariable=myvar,show="*")
    text_entry.place(x=400,y=100)
    myvar.get()
    
    vali=Button(down,text="validate",font=("Courier",8),command=lambda:loginw())    
    vali.place(x=550,y=100)

    
#on first page
def home():
    clearframe(down)
    user=Button(down,text="brochure",font=("Courier",20),command=lambda:brochure())    
    user.place(x=100,y=80)
    admin=Button(down,text="admin",font=("Courier",20),command=lambda:loginw2())
    admin.place(x=100,y=180)
home()

root.mainloop()



