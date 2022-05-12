# importing modules necessary for program to run properly
# verify that this packages are installed in your system
# if packages are not installled then install using pip install packagename
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as st
import threading
import time
import os
import pyautogui
import random
from fpdf import FPDF

flag=0

# file creation for storing student data
# if files does not exist then and then only new files will be created 
# files will be created in same folder where this .py program file is stored
f=open("data.txt","a")
if os.path.getsize("data.txt")==0:
    f.write(",Roll no,First name,Last name,Password,Position,Question,Answer,\n")
    askuser=int(input("Do you want to generate Student and Faculty data with default values (1 for yes/0 for no) : "))
    if (askuser!=0):
    	flag=1
    	global nos
    	nos=int(input("Enter total number of students : "))
    	for i in range(nos) :
    		f.write(",19BCE{:03d},first name,last name,changeme,Student,Your Primary School Name,Nirma,\n".format(i+1))
    	for i in range(int(input("Enter total number of faculties : "))):
    		f.write(",NUFCE{:03d},first name,last name,changeme,Faculty,Your Primary School Name,Nirma,\n".format(i+1))
    else :
    	print("\nEnter data manually in data.txt or program won't work!!\n")
f.close()

# file creation for student result information
f=open("result.txt","a")
if os.path.getsize("result.txt")==0:
    f.write(",Roll no,PSC,CA,PS,OS,DBMS,\n")
    askuser1=int(input("Do you want to generate Student marks randomly (1 for yes/0 for no) : "))
    if (flag==1 and askuser1!=0):
    	for i in range(nos) :
    		f.write(",19BCE{:03d},{},{},{},{},{},\n".format(i+1,random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)))
    else :
    	print("\nPlease Enter data manually in result.txt keeping data.txt in mind!!")
    	time.sleep(1)
f.close()

# graphical main window creation using tkinter module
master = Tk()
master.title("Nirma University Result Portal")

bg=PhotoImage(file="nirmabackground1.png")
Label(master,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

master.geometry("1080x680+150+10")
master.resizable(False,False)

frame=Frame(master,bg="white")
frame.place(x=340,y=180,height=300,width=400)
bg2=PhotoImage(file="background4.png")

def create(): 
    
    newWindow = Toplevel(master) 
    newWindow.title("Registration Window") 
    Label(newWindow,image=bg2).place(x=0,y=0,relwidth=1,relheight=1)
    newWindow.geometry("1080x680+150+10")
    newWindow.resizable(False,False)

    n=StringVar()
    p=StringVar()
    q=StringVar()
    r=StringVar()
    s=StringVar()
    t=StringVar()
    u=StringVar()
    w=StringVar()
        
    def submit():
    
        first=n.get()
        last=p.get()
        name=q.get()
        password=r.get()
        password2=s.get()
        select=w.get()
        answer=u.get()
        position=t.get()
        
        f=open("data.txt","r")
        content=f.read()
        words=content.split(",")
        f.close()
        
        c=0
        for i in range(9,len(words)-1,8):
            if(words[i]==name.upper()):
                c=c+1
                break;
        
        f=open("result.txt","r")
        content=f.read()
        words2=content.split(",")
        f.close()

        d=0
        for j in range(8,len(words2)-1,7):
            if(words2[j]==name.upper()):
                d=d+1
                break;

        if(password=="" or password2=="" or first=="" or last=="" or name=="" or select=="Choose Recovery Option" or answer=="Answer" or position=="You are a-"):
            messagebox.showerror('Error','All fields are Required!',parent=newWindow)
        elif(len(name)!=8):
            messagebox.showerror('Error','Username must contain exactly 8 Characters!',parent=newWindow)
        elif(len(password)<6):
            messagebox.showerror('Error','Password must contain at least 6 Characters!',parent=newWindow)
        elif(password!=password2):
            messagebox.showerror('Error','Password Mismatch!',parent=newWindow)
        elif(position=="Faculty" and (name[0]+name[1]+name[2]).upper()!="NUF"):
            messagebox.showerror('Error','Faculty Username format is Not Correct!',parent=newWindow)
        elif(c==1 and words[i+1]!="first name" and words[i+2]!="last name" and words[i+3]!="changeme"):
            messagebox.showerror('Error','User already Exists!',parent=newWindow)
            newWindow.destroy()
        elif(position=="Student" and d==0):
            messagebox.showerror('Error','You are not registered by the Institute!',parent=newWindow)
            newWindow.destroy()
        else:
            messagebox.showinfo('Done','You are registered Successfully!',parent=newWindow)
            newWindow.destroy()

            # student information update in data.txt file
            words[i+1]=first
            words[i+2]=last
            words[i+3]=password
            words[i+4]=position
            words[i+5]=select
            words[i+6]=answer
            
            f=open("data.txt","w")
            f.truncate(0)
            
            b=","+words[1]+","+words[2]+","+words[3]+","+words[4]+","+words[5]+","+words[6]+","+words[7]+",\n"
            f.write(b)
            for j in range(9,len(words)-1,8):
                a="\n,"+words[j]+","+words[j+1]+","+words[j+2]+","+words[j+3]+","+words[j+4]+","+words[j+5]+","+words[j+6]+","
                f.write(a)   
                
            f.close()
    
    def useranswer(event) :
        
        uentry.delete(0,END)

    label2 = Label(newWindow,text ="Register Yourself",font=("calibre",25,"bold"),fg="white",bg="#555",anchor="center")
    label2.place(x=250,y=50,height=50,width=600)

    nlabel = Label(newWindow, text = 'First Name', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    nlabel.place(x=360,y=140,height=35,width=170)
    nentry = Entry(newWindow,textvariable = n, font=("cambria",15,"normal"),bg="white",relief="flat")
    nentry.place(x=540,y=140,height=35,width=190)

    plabel = Label(newWindow, text = 'Last Name', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    plabel.place(x=360,y=185,height=35,width=170)
    pentry = Entry(newWindow, textvariable = p, font=("cambria",15,"normal"),bg="white",relief="flat")
    pentry.place(x=540,y=185,height=35,width=190)

    qlabel = Label(newWindow, text = 'Username', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    qlabel.place(x=360,y=232,height=35,width=170)
    qentry = Entry(newWindow, textvariable = q, font=("cambria",15,"normal"),bg="white",relief="flat")
    qentry.place(x=540,y=232,height=35,width=190)
    
    rlabel = Label(newWindow, text = 'Password', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    rlabel.place(x=360,y=277,height=35,width=170)
    rentry = Entry(newWindow, textvariable = r, font = ('cambria',15,'normal'), show = '*')
    rentry.place(x=540,y=277,height=35,width=190)

    slabel = Label(newWindow, text = 'Confirm Password', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    slabel.place(x=348,y=322,height=35,width=185)
    sentry = Entry(newWindow, textvariable = s, font = ('cambria',15,'normal'), show = '*')
    sentry.place(x=540,y=322,height=35,width=190)

    option=["Faculty","Student"]
    t.set("You are a-")
    drop1=OptionMenu(newWindow,t,*option)
    drop1.config(bd=0,font=("calibre",14,"bold"),fg="white",bg="purple",activebackground="white",activeforeground="purple",cursor="hand2")
    drop1.place(x=390,y=380,width=300)
    drop1['menu'].config(font=("cambria",14,"normal"),fg="black",bg="white")
    
    option=["Your Primary School Name","Your Favourite Sports Man","Your Favourite Hero","Your Favorite Color"]
    w.set("Choose Recovery Question")
    drop1=OptionMenu(newWindow,w,*option)
    drop1.config(bd=0,font=("calibre",14,"bold"),fg="white",bg="purple",activebackground="white",activeforeground="purple",cursor="hand2")
    drop1.place(x=390,y=422,width=300)
    drop1['menu'].config(font=("cambria",14,"normal"),fg="black",bg="white")

    uentry = Entry(newWindow, textvariable = u, font=("cambria",15,"normal"),bg="white",relief="flat")
    uentry.place(x=450,y=464,height=30,width=190)
    uentry.insert(0,"Answer")
    uentry.bind("<Button>",useranswer)
       
    btn=Button(newWindow,text='Sign Up',command=submit,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
    btn.place(x=450,y=506,height=45,width=190)

    newWindow.mainloop()

def loginvalidate(): 
    
    name=n.get()
    password=p.get()
    
    f=open("data.txt","r")
    content=f.read()
    words=content.split(",")
    f.close()

    c=0
    for i in range(9,len(words)-1,8):
        if(words[i]==name.upper()):
            c=c+1
            break;

    if(name=="" or password==""):
        messagebox.showerror('Error','All fields are Required!')
    elif(len(password)<6):
        messagebox.showerror('Error','Password must contain at least 6 Characters!')
    elif(len(name)!=8):
        messagebox.showerror('Error','Username must contain exactly 8 Characters!')
    elif(c==0):
        messagebox.showerror('Error','You are not Registered!')
    elif(words[i+1]=="first name" or words[i+2]=="last name" or words[i+3]=="changeme"):
    	messagebox.showinfo('Sign Up','{} Register yourself using Sign Up!'.format(words[i]))
    elif(words[i]==name.upper() and password==words[i+3]):
        messagebox.showinfo('Done','You are Logged in Successfully!')
        fn=words[i+1].capitalize()+" "+words[i+2].capitalize()
    
        # Creates result window if user is student
        if(words[i+4]=="Student"):
            nw = Toplevel(master)
            nw.title("View your result")
            nw.attributes('-fullscreen',True)
            nw.config(bg='white')

            f2=open("result.txt","r")
            content=f2.read()
            words=content.split(",")
            f2.close()
      
            for l in range(8,len(words)-1,7):
                if(words[l]==name.upper()):
                    break
            
            list1=[]
            list2=[]
            def grade(o):
                if(o>=90 and o<=100):
                    list1.append(40)
                    return "A+"
                elif(o>=80):
                    list1.append(36)
                    return "A "
                elif(o>=70):
                    list1.append(32)
                    return "B+"
                elif(o>=60):
                    list1.append(28)
                    return "B "
                elif(o>=50):
                    list1.append(24)
                    return "C"
                elif(o>=40):
                    list1.append(20)
                    return "D "
                else:
                    list2.append(1)
                    list1.append(16)
                    return "F "

            # to store grades of student at given instance
            fgrades=[]

            Label(nw,text ="\nNirma University, Ahmedabad",font = ('cambria',18,'bold'),bg='white').pack()
            Label(nw,text ="Program Name : B.Tech in Computer Science and Engineering",font = ('cambria',18,'bold'),bg='white').pack()
            Label(nw,text ="Roll No. : {}".format(name.upper()),font = ('cambria',18,'bold'),bg='white').pack()
            Label(nw,text ="Student Name : {}".format(fn),font = ('cambria',18,'bold'),bg='white').pack()
            
            Label(nw,text ="-------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            Label(nw,text ="| Semester |  Course  | Name | Marks | Grade |",font = ('calibre',16),bg='white').pack()
            Label(nw,text ="--------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            fgrades.append(grade(int(words[l+1])))
            Label(nw,text =r"|       4        | 2CS404  | PSC  |    {}   |     {}     |".format(words[l+1],fgrades[0]),font = ('calibre',16),bg='white').pack()
            Label(nw,text ="--------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            fgrades.append(grade(int(words[l+2])))
            Label(nw,text =r"|       4        | 2CS401  |  CA  |    {}   |     {}     |".format(words[l+2],fgrades[1]),font = ('calibre',16),bg='white').pack()
            Label(nw,text ="--------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            fgrades.append(grade(int(words[l+3])))
            Label(nw,text =r"|       4        | 2MA402  |  PS  |    {}   |     {}     |".format(words[l+3],fgrades[2]),font = ('calibre',16),bg='white').pack()
            Label(nw,text ="--------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            fgrades.append(grade(int(words[l+4])))
            Label(nw,text =r"|       4        | 2CS403  |  OS  |    {}   |     {}     |".format(words[l+4],fgrades[3]),font = ('calibre',16),bg='white').pack()
            Label(nw,text ="--------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            fgrades.append(grade(int(words[l+5])))
            Label(nw,text =r"|       4        | 2CS402  | DBMS |    {}   |     {}     |".format(words[l+5],fgrades[4]),font = ('calibre',16),bg='white').pack()
            Label(nw,text ="--------------------------------------------------------------",font = ('calibre',16),bg='white').pack()
            Label(nw,text ="Your Score : {}           Total Score : 200".format(sum(list1)),font = ('cambria',18,'bold'),bg='white').pack()
            if (sum(list2)==0):
                Label(nw,text="Remark : Congratulations, you are Pass in all Subjects",font = ('cambria',18,'bold'),bg='white').pack()
                spi=sum(list1)/20
                Label(nw,text="Your SPI : {:.2f}".format(spi),font = ('cambria',18,'bold'),bg='white').pack()
            else:
                Label(nw,text="Remark : Better luck next time, you are Fail in {} Subject".format(sum(list2)),font = ('cambria',18,'bold'),bg='white').pack()

            def logout():
                messagebox.showinfo("Thank You","Thank you for Visiting!",parent=nw)
                nw.destroy()
                usertext("<Button>")
                
            def download():

                def downloadpdf():
                    # pdf creation starts from here
                    pdf=FPDF()
                    pdf.add_page()
                    pdf.image('a4cover.png',0,0,210,0)
                    pdf.set_font('Arial','B',size=16)
                    pdf.set_left_margin(5)

                    pdf.ln(30)
                    pdf.cell(200,10,txt="Nirma University, Ahmedabad",ln=1,align="C")
                    pdf.cell(200,10,txt="Program Name : B.Tech in Computer Science and Engineering",ln=1,align="C")
                    pdf.cell(200,10,txt="Roll No. : {}".format(name.upper()),ln=1,align="C")
                    pdf.cell(200,10,txt="Student Name : {}".format(fn),ln=1,align="C")
                    pdf.cell(200,10,txt="\n-------------------------------------------------------------",ln=1,align="C")
                    pdf.cell(200,10,txt="| Semester |  Course  | Name | Marks | Grade |",ln=1,align="C")
                    pdf.cell(200,10,txt="--------------------------------------------------------------",ln=1,align="C")
                    pdf.set_font('Arial',size=16)
                    pdf.cell(200,10,txt=r"|       4        | 2CS404  | PSC  |    {}   |     {}     |".format(words[l+1],fgrades[0]),ln=1,align="C")
                    pdf.cell(200,10,txt="--------------------------------------------------------------",ln=1,align="C")
                    pdf.cell(200,10,txt=r"|       4        | 2CS401  |  CA  |    {}   |     {}     |".format(words[l+2],fgrades[1]),ln=1,align="C")
                    pdf.cell(200,10,txt="--------------------------------------------------------------",ln=1,align="C")
                    pdf.cell(200,10,txt=r"|       4        | 2MA402  |  PS  |    {}   |     {}     |".format(words[l+3],fgrades[2]),ln=1,align="C")
                    pdf.cell(200,10,txt="--------------------------------------------------------------",ln=1,align="C")
                    pdf.cell(200,10,txt=r"|       4        | 2CS403  |  OS  |    {}   |     {}     |".format(words[l+4],fgrades[3]),ln=1,align="C")
                    pdf.cell(200,10,txt="--------------------------------------------------------------",ln=1,align="C")
                    pdf.cell(200,10,txt=r"|       4        | 2CS402  | DBMS |    {}   |     {}     |".format(words[l+5],fgrades[4]),ln=1,align="C")
                    pdf.set_font('Arial','B',size=16)
                    pdf.cell(200,10,txt="--------------------------------------------------------------\n",ln=1,align="C")
                    pdf.cell(200,10,txt="Your Score : {}           Total Score : 200".format(sum(list1)),ln=1,align="C")
                    if (sum(list2)==0) :
                        pdf.cell(200,10,txt="Remark : Congratulations, you are Pass in all Subjects",ln=1,align="C")
                        pdf.cell(200,10,txt="Your SPI : {:.2f}".format(spi),ln=1,align="C")
                    else :
                        pdf.cell(200,10,txt="Remark : Better luck next time, you are Fail in {} Subject".format(sum(list2)),ln=1,align="C")

                    pdf.output('{}_Result.pdf'.format(name.upper()))
                    messagebox.showinfo('Done','{}_Result.pdf is Downloaded!'.format(name.upper()),parent=nw)

                def downloadpng():
                    s=pyautogui.screenshot()
                    s.save(r'{}_Result.png'.format(name.upper()))
                    messagebox.showinfo('Done','{}_Result.png is Downloaded!'.format(name.upper()),parent=nw)

                # execution order
                downloadpng()
                jtrix=messagebox.askquestion('Download','Do you want to download PDF as well?',parent=nw)
                if(jtrix=='yes'):
                    def progressbar_update():
                        lime=threading.Thread(target=downloadpdf)
                        lime.start()
                        # pdf creation takes approx 30 seconds
                        # if we need more time, then increase seconds
                        seconds=25
                        i=0
                        while (i<seconds):
                            time.sleep(1)
                            progress['value']=i*(100/seconds)
                            i+=1
                            temp.update_idletasks()
                            perc='{:.2f}'.format(i*(100/seconds))
                            percent.set(str(perc)+'%')
                        progress['value']=100
                        if (lime.is_alive()):
                            temp.destroy()

                    # new window to display progressbar
                    temp = Toplevel(master) 
                    temp.title("PDF Download")
                    temp.geometry("250x130+570+300")
                    temp.resizable(False,False)

                    percent=StringVar()
                    progress=Progressbar(temp, orient=HORIZONTAL, length=200, mode='determinate')
                    progress.pack(pady=10)
                    percentlabel=Label(temp, textvariable=percent).pack()
                    Button(temp, text='Start Downloading', command=progressbar_update,font=("Helvetica",13,"bold"),fg="white",bg="black",relief="raise").pack(pady=10)

            btn=Button(nw,text='Logout',font=("Inconsolata",20,"bold"),command = logout,fg="white",bg="#555",relief="raise",cursor="hand2")
            btn.place(x=750,y=680,height=35,width=180)
            btn=Button(nw,text='Download',font=("Inconsolata",20,"bold"),command = download,fg="white",bg="#555",relief="raise",cursor="hand2")
            btn.place(x=450,y=680,height=35,width=190)

        # Creates window if user is faculty
        else:
            newWindow = Toplevel(master)
            newWindow.title("Create the Result of Student")

            bg2=PhotoImage(file="background3.png")
            Label(newWindow,image=bg2).place(x=0,y=0,relwidth=1,relheight=1)

            newWindow.geometry("1080x680+150+10")
            newWindow.resizable(False,False)

            n1=StringVar()
            p1=StringVar()
            q=StringVar()
            r=StringVar()
            s=StringVar()
            w=StringVar()
            n11=StringVar()
            p11=StringVar()
            q1=StringVar()
            r1=StringVar()
            
            def add():
                name2=n1.get()
                psc=p1.get()
                ps=q.get()
                ca=r.get()
                os=s.get()
                dbms=w.get()
                    
                f2=open("result.txt","r")
                content=f2.read()
                words=content.split(",")
                f2.close()

                c=0
                for l in range(8,len(words)-1,7):
                    if(words[l]==name2.upper()):
                        c=1
                        break;

                error=0
                negativemarks=0
                error1=0
                try:
                    if(int(psc)>100 or int(ps)>100 or int(ca)>100 or int(os)>100 or int(dbms)>100):
                        error=1
                    if(int(psc)<0 or int(ps)<0 or int(ca)<0 or int(os)<0 or int(dbms)<0):
                        negativemarks=1
                except ValueError:
                    error1=1        
              
                if(ca=="" or os=="" or name2=="" or psc=="" or ps=="" or dbms==""):
                    messagebox.showerror('Error','All field are Required!',parent=newWindow)
                elif(len(name2)!=8):
                    messagebox.showerror('Error','Roll number must contain exactly 8 Characters!',parent=newWindow)
                elif(error==1):
                    messagebox.showerror('Error','Student can have maximum 100 Marks!',parent=newWindow)
                elif(negativemarks==1):
                    messagebox.showerror('Error','Student can not have Negative Marks!',parent=newWindow)
                elif(error1==1):
                    messagebox.showerror('Error','Student marks must be an integer!',parent=newWindow)
                elif(c==1):
                    messagebox.showerror('Error','Marks of {} already Exists,use Update!'.format(name2.upper()),parent=newWindow)
                else:
                    messagebox.showinfo('Done','Marks added Successfully!',parent=newWindow)
                    
                    a="\n,"+name2.upper()+","+psc+","+ps+","+ca+","+os+","+dbms+","
                    f=open("result.txt","a")
                    f.write(a)
                    f.close()

                    pentry.delete(0,END)
                    qentry.delete(0,END)
                    rentry.delete(0,END)
                    sentry.delete(0,END)
                    wentry.delete(0,END)
                            
            def update():
                name2=n1.get()
                psc=p1.get()
                ps=q.get()
                ca=r.get()
                os=s.get()
                dbms=w.get()
                    
                f2=open("result.txt","r")
                content=f2.read()
                words=content.split(",")
                f2.close()
                
                c=0
                for l in range(8,len(words)-1,7):
                    if(words[l]==name2.upper()):
                        c=1
                        break;

                error=0
                negativemarks=0
                error1=0
                try:
                    if(int(psc)>100 or int(ps)>100 or int(ca)>100 or int(os)>100 or int(dbms)>100):
                        error=1
                    if(int(psc)<0 or int(ps)<0 or int(ca)<0 or int(os)<0 or int(dbms)<0):
                        negativemarks=1
                except ValueError:
                    error1=1
                
                if(ca=="" or os=="" or name2=="" or psc=="" or ps=="" or dbms==""):
                    messagebox.showerror('Error','All field are Required!',parent=newWindow)
                elif(len(name2)!=8):
                    messagebox.showerror('Error','Roll number must contain exactly 8 Characters!',parent=newWindow)
                elif(error==1):
                    messagebox.showerror('Error','Student can have maximum 100 Marks!',parent=newWindow)
                elif(negativemarks==1):
                    messagebox.showerror('Error','Student can not have Negative Marks!',parent=newWindow)
                elif(error1==1):
                    messagebox.showerror('Error','Student marks must be an integer!',parent=newWindow)
                elif(c==0):
                    messagebox.showerror('Error','You can\'t update Marks of {}!'.format(name2.upper()),parent=newWindow)
                else:
                    messagebox.showinfo('Done','Marks updated Successfully!',parent=newWindow)
                    
                    words[l+1]=psc
                    words[l+2]=ps
                    words[l+3]=ca
                    words[l+4]=os
                    words[l+5]=dbms
                    f=open("result.txt","w")
                    f.truncate(0)
                    
                    b=","+words[1]+","+words[2]+","+words[3]+","+words[4]+","+words[5]+","+words[6]+",\n"
                    f.write(b)
                    for j in range(8,len(words)-1,7):
                        a="\n,"+words[j]+","+words[j+1]+","+words[j+2]+","+words[j+3]+","+words[j+4]+","+words[j+5]+","
                        f.write(a)   
                    f.close()

                    pentry.delete(0,END)
                    qentry.delete(0,END)
                    rentry.delete(0,END)
                    sentry.delete(0,END)
                    wentry.delete(0,END)
                    
            def delete():
                name2=n1.get()
                
                f2=open("result.txt","r")
                content=f2.read()
                words=content.split(",")
                f2.close()
                
                c=0
                for l in range(8,len(words)-1,7):
                    if(words[l]==name2.upper()):
                        w=l
                        c=1
                        break;  
                            
                if(name2==""):
                    messagebox.showerror('Error','Enter Student Roll Number!',parent=newWindow)
                elif(len(name2)!=8):
                    messagebox.showerror('Error','Roll number must contain 8 Characters!',parent=newWindow)
                elif(c==0):
                    messagebox.showerror('Error','You can\'t delete Marks of {}!'.format(name2.upper()),parent=newWindow)
                else:
                    messagebox.showinfo('Done','Marks deleted Successfully!',parent=newWindow)
                    
                    del words[w:w+7]
                    
                    f=open("result.txt","w")
                    f.truncate(0)
                    b=","+words[1]+","+words[2]+","+words[3]+","+words[4]+","+words[5]+","+words[6]+",\n"
                    f.write(b)
                    for j in range(8,len(words)-1,7):
                        a="\n,"+words[j]+","+words[j+1]+","+words[j+2]+","+words[j+3]+","+words[j+4]+","+words[j+5]+","
                        f.write(a)   
                    f.close()

                    pentry.delete(0,END)
                    qentry.delete(0,END)
                    rentry.delete(0,END)
                    sentry.delete(0,END)
                    wentry.delete(0,END)

            def search():
                name2=n1.get()

                f2=open("result.txt","r")
                content=f2.read()
                words=content.split(",")
                f2.close()
                
                c=0
                for l in range(8,len(words)-1,7):
                    if(words[l]==name2.upper()):
                        w=l
                        c=1
                        break;  
                
                if(name2==""):
                    messagebox.showerror('Error','Enter Student Roll Number!',parent=newWindow)
                elif(len(name2)!=8):
                    messagebox.showerror('Error','Roll number must contain 8 Characters!',parent=newWindow)
                elif(c==0):
                    messagebox.showerror('Error','Data of {} not Found!'.format(name2.upper()),parent=newWindow)
                else:
                    messagebox.showinfo('Done','{} is found in Database!'.format(name2.upper()),parent=newWindow)

                    pentry.delete(0,END)
                    qentry.delete(0,END)
                    rentry.delete(0,END)
                    sentry.delete(0,END)
                    wentry.delete(0,END)
                    
                    pentry.insert(INSERT,words[l+1])
                    qentry.insert(INSERT,words[l+2])
                    rentry.insert(INSERT,words[l+3])
                    sentry.insert(INSERT,words[l+4])
                    wentry.insert(INSERT,words[l+5])

            def ss():
	            mark=n11.get()
	            op=p11.get()
	            su=q1.get()

	            error=0
	            negativemarks=0
	            error1=0
	            try:
	            	if(int(mark)>100):
	            		error=1
	            	if(int(mark)<0):
	            		negativemarks=1
	            except ValueError:
	            	error1=1

	            if(op=="Choose Your Option" or mark=="" or su=="Select a Subject"):
	                messagebox.showerror('Error','All field are Required!',parent=newWindow)
	            elif(error==1) :
	                messagebox.showerror('Error','Student can have maximum 100 Marks!',parent=newWindow)
	            elif(negativemarks==1):
	            	messagebox.showerror('Error','Student can not have Negative Marks!',parent=newWindow)
	            elif(error1==1):
	            	messagebox.showerror('Error','Student marks must be an integer!',parent=newWindow)
	            else:
	                messagebox.showinfo('Done','Search Completed!',parent=newWindow)

	                mark=int(mark)
	                index=option1.index(op)
	                index1=option2.index(su)
	                
	                f2=open("result.txt","r")
	                content=f2.read()
	                words=content.split(",")
	                f2.close()
	                
	                c=0
	                a="Roll Number-Marks\n"
	                tempchecker=a
	                for l in range(8,len(words)-1,7):
	                    if(index==0):
	                        if(int(words[l+1+index1])>mark):
	                            c=c+1
	                            a=a+words[l]+"-"+words[l+3]+"\n"
	                    elif(index==1):
	                        if(int(words[l+1+index1])<mark):
	                            c=c+1
	                            a=a+words[l]+"-"+words[l+3]+"\n"
	                    else:
	                        if(int(words[l+1+index1])==mark):
	                            c=c+1
	                            a=a+words[l]+"-"+words[l+3]+"\n"
	                
	                r1entry.delete(0,END)
	                s1entry.delete('0.0',END)
	                r1entry.insert(INSERT,c)
	                if a!=tempchecker:
	                	s1entry.insert(INSERT,a)

            def logout():
                messagebox.showinfo("Thank You","Thank you for Visiting!",parent=newWindow)
                newWindow.destroy()
                usertext("<Button>")
            
            label2 = Label(newWindow,text ="Welcome {}".format(fn),font=("calibre",25,"bold"),fg="white",bg="#555",anchor="center")
            label2.place(x=250,y=50,height=50,width=600)

            btn=Button(newWindow,text='Logout',command=logout,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
            btn.place(x=960,y=20,height=35,width=100)

            # Left Part of window creation
            label2 = Label(newWindow,text ="Add/Delete/Update/Search".format(fn),font=("calibre",22,"bold"),fg="white",bg="#555",anchor="center")
            label2.place(x=50,y=135,height=45,width=440)

            nlabel = Label(newWindow, text = 'Roll no.', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            nlabel.place(x=85,y=215,height=35,width=170)
            nentry = Entry(newWindow,textvariable = n1, font=("cambria",15,"normal"),bg="white",relief="flat")
            nentry.place(x=265,y=215,height=35,width=190)

            plabel = Label(newWindow, text = 'PSC Marks', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            plabel.place(x=85,y=265,height=35,width=170)
            pentry = Entry(newWindow, textvariable = p1, font=("cambria",15,"normal"),bg="white",relief="flat")
            pentry.place(x=265,y=265,height=35,width=190)

            qlabel = Label(newWindow, text = 'PS Marks', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            qlabel.place(x=85,y=315,height=35,width=170)
            qentry = Entry(newWindow, textvariable = q, font=("cambria",15,"normal"),bg="white",relief="flat")
            qentry.place(x=265,y=315,height=35,width=190)
                
            rlabel = Label(newWindow, text = 'CA Marks', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            rlabel.place(x=85,y=365,height=35,width=170)
            rentry = Entry(newWindow, textvariable = r, font = ('cambria',15,'normal'),bg="white",relief="flat")
            rentry.place(x=265,y=365,height=35,width=190)

            slabel = Label(newWindow, text = 'OS Marks', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            slabel.place(x=85,y=415,height=35,width=170)
            sentry = Entry(newWindow, textvariable = s, font = ('cambria',15,'normal'),bg="white",relief="flat")
            sentry.place(x=265,y=415,height=35,width=190)

            wlabel = Label(newWindow, text = 'DBMS Marks', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            wlabel.place(x=85,y=465,height=35,width=170)
            wentry = Entry(newWindow, textvariable = w, font = ('cambria',15,'normal'),bg="white",relief="flat")
            wentry.place(x=265,y=465,height=35,width=190)
                   
            btn=Button(newWindow,text='Add',command=add,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
            btn.place(x=85,y=525,height=45,width=170)
            
            btn=Button(newWindow,text='Update',command=update,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
            btn.place(x=285,y=525,height=45,width=170)
            
            btn=Button(newWindow,text='Delete',command=delete,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
            btn.place(x=85,y=585,height=45,width=170)
            
            btn=Button(newWindow,text='Search',command=search,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
            btn.place(x=285,y=585,height=45,width=170)
            
            # Right Part of window creation
            label2 = Label(newWindow,text ="Search Student using marks",font=("calibre",22,"bold"),fg="white",bg="#555",anchor="center")
            label2.place(x=590,y=135,height=45,width=450)
            
            label = Label(newWindow, text = 'Enter Marks', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            label.place(x=625,y=215,height=35,width=170)
            entry = Entry(newWindow,textvariable = n11, font=("cambria",15,"normal"),bg="white",relief="flat")
            entry.place(x=805,y=215,height=35,width=190)
                
            option1=["Greater than Marks","Less than Marks","Equal to Marks"]
            p11.set("Choose Your Option")
            drop1=OptionMenu(newWindow,p11,*option1)
            drop1.config(bd=0,font=("calibre",14,"bold"),fg="white",bg="purple",activebackground="white",activeforeground="purple",cursor="hand2")
            drop1.place(x=660,y=265,width=300)
            drop1['menu'].config(font=("cambria",14,"normal"),fg="black",bg="white")
    
            option2=["PSC","PS","CA","OS","DBMS"]
            q1.set("Select a Subject")
            drop1=OptionMenu(newWindow,q1,*option2)
            drop1.config(bd=0,font=("calibre",14,"bold"),fg="white",bg="purple",activebackground="white",activeforeground="purple",cursor="hand2")
            drop1.place(x=660,y=315,width=300)
            drop1['menu'].config(font=("cambria",14,"normal"),fg="black",bg="white")
                
            btn=Button(newWindow,text='Search Students',command=ss,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
            btn.place(x=685,y=365,height=45,width=250)
                
            r1label = Label(newWindow, text = 'Total Students', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            r1label.place(x=625,y=465,height=35,width=170)
            r1entry = Entry(newWindow,textvariable = r1, font=("cambria",15,"normal"),bg="white",relief="flat")
            r1entry.place(x=805,y=465,height=35,width=190)
                
            s1label = Label(newWindow, text = 'Roll No.', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
            s1label.place(x=625,y=515,height=35,width=170)
            s1entry = st.ScrolledText(newWindow,font=("cambria",15,"normal"),bg="white",relief="flat")
            s1entry.place(x=805,y=515,height=110,width=190)

            newWindow.mainloop()

    else:
        messagebox.showerror('Error','Password Mismatch!')

def change(): 
    
    newWindow = Toplevel(master)
    newWindow.title("Change Password")

    bg2=PhotoImage(file="nirmabackground3.png")
    Label(newWindow,image=bg2).place(x=0,y=0,relwidth=1,relheight=1)

    newWindow.geometry("1080x680+150+10")
    newWindow.resizable(False,False)
            
    n=StringVar()
    x=StringVar()
    y=StringVar()
    
    def submit():
        name=n.get()
        password=x.get()
        password2=y.get()

        if(name=="" or password=="" or password2==""):
            messagebox.showerror('Error','All fields are Required!',parent=newWindow)
        elif(len(password)<6):
            messagebox.showerror('Error','Password should contain at least 6 Characters!',parent=newWindow)
        elif(password!=password2):
            messagebox.showerror('Error','Password Mismatch!',parent=newWindow)
        else:
            messagebox.showinfo('Done','Your password is changed Successfully!',parent=newWindow)
            newWindow.destroy()
            
            f=open("data.txt","r")
            content=f.read()
            words=content.split(",")
            f.close()

            c=0
            for i in range(9,len(words)-1,8):
                if(words[i]==name.upper()):
                    c=c+1
                    break;
                    
            words[i+3]=password
            f=open("data.txt","w")
            f.truncate(0)
            b=","+words[1]+","+words[2]+","+words[3]+","+words[4]+","+words[5]+","+words[6]+","+words[7]+",\n"
            f.write(b)
            for j in range(9,len(words)-1,8):
                a="\n,"+words[j]+","+words[j+1]+","+words[j+2]+","+words[j+3]+","+words[j+4]+","+words[j+5]+","+words[j+6]+","
                f.write(a)
                
            f.close()

    label = Label(newWindow,text ="Change Password",font=("calibre",25,"bold"),fg="white",bg="#555",anchor="center")
    label.place(x=250,y=40,height=50,width=600)

    nlabel = Label(newWindow, text = 'Username', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    nlabel.place(x=352,y=220,height=35,width=170)
    nentry = Entry(newWindow, textvariable = n, font=("cambria",15,"normal"),bg="white",relief="flat")
    nentry.place(x=540,y=220,height=35,width=190)
    nentry.insert(0,gname)

    xlabel = Label(newWindow, text = 'Password', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    xlabel.place(x=352,y=270,height=35,width=170)
    xentry = Entry(newWindow, textvariable = x, font=("cambria",15,"normal"), show='*',bg="#eee",relief="flat")
    xentry.place(x=540,y=270,height=35,width=190)

    ylabel = Label(newWindow, text = 'Confirm Password', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    ylabel.place(x=345,y=320,height=35,width=185)
    yentry = Entry(newWindow, textvariable = y, font=('cambria',15,'normal'), show = '*')
    yentry.place(x=540,y=320,height=35,width=190)

    btn=Button(newWindow,text='Confirm',command=submit,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
    btn.place(x=430,y=395,height=45,width=190)
    
    newWindow.mainloop()

def forgot():
    
    newWindow = Toplevel(master)
    newWindow.title("Forgot Password")

    bg2=PhotoImage(file="nirmabackground2.png")
    Label(newWindow,image=bg2).place(x=0,y=0,relwidth=1,relheight=1)

    newWindow.geometry("1080x680+150+10")
    newWindow.resizable(False,False)
    
    n=StringVar()
    t=StringVar()
    u=StringVar()
    
    def submit():
        name=n.get()
        select=t.get()
        password=u.get()
        
        f=open("data.txt","r")
        content=f.read()
        words=content.split(",")
        f.close()
        
        c=0
        for i in range(9,len(words),8):
            if(words[i]==name.upper()):
                c=c+1
                break;
        
        if(name=="" or password=="" or select=="Select Recovery Question"):
            messagebox.showerror('Error','All field are Required!',parent=newWindow)
        elif(c==0):
            messagebox.showerror('Error','You are not registered by Institute!',parent=newWindow)
        elif(select!=words[i+5] or password!=words[i+6]):
            messagebox.showerror('Error','Question/Answer Mismatch!',parent=newWindow)
        else:
            messagebox.showinfo('Done','Choose Your Password Carefully!',parent=newWindow)
            newWindow.destroy()
            global gname
            gname=n.get()
            change()
    
    def username(event) :

        nentry.delete(0,END)
       
    def useranswer(event) :

        uentry.delete(0,END)

    label = Label(newWindow,text ="Forgot Password",font=("calibre",25,"bold"),fg="white",bg="#555",anchor="center")
    label.place(x=250,y=40,height=50,width=600)

    nlabel = Label(newWindow, text = 'Username', font=("calibre",15,"bold"),fg="white",bg="purple",anchor="center")
    nlabel.place(x=360,y=320,height=35,width=170)
    nentry = Entry(newWindow, textvariable = n, font=("cambria",15,"normal"),bg="white",relief="flat")
    nentry.place(x=540,y=320,height=35,width=200)
    nentry.insert(0,"19BCE028/NUFCE028")
    nentry.bind("<Button>",username)

    option=["Your Primary School Name","Your Favourite Sports Man","Your Favourite Hero","Your Favorite Color"]
    t.set("Select Recovery Question")
    drop1=OptionMenu(newWindow,t,*option)
    drop1.config(bd=0,font=("calibre",14,"bold"),fg="white",bg="purple",activebackground="white",activeforeground="purple",cursor="hand2")
    drop1.place(x=390,y=375,width=300)
    drop1['menu'].config(font=("cambria",14,"normal"),fg="black",bg="white")

    uentry = Entry(newWindow, textvariable = u, font=("cambria",15,"normal"),bg="white",relief="flat")
    uentry.place(x=450,y=425,height=30,width=190)
    uentry.insert(0,"Answer")
    uentry.bind("<Button>",useranswer)
    
    btn=Button(newWindow,text='Verify Answer',command=submit,font=("Inconsolata",20,"bold"),fg="purple",bg="lightgray",activebackground="black",activeforeground="white",cursor="hand2")
    btn.place(x=450,y=500,height=45,width=190)
    
    newWindow.mainloop()

def usertext(event) :

    nentry.delete(0,END)
    pentry.delete(0,END)
    nentry.focus()

def loginfocus() :

    usertext("<Button>")
    nentry.focus()

    messagebox.showinfo('Password','Default Password is changeme!')


label = Label(master,text ="Welcome to Nirma University",font=("calibre",30,"bold"),fg="white",bg="#555",anchor="center")
label.place(x=250,y=50,height=50,width=600)

btn = Button(frame,text ="Sign Up",relief="raise",font=("cambria",15,"bold"),fg="black",bg="white",command = create,activebackground="white",activeforeground="green")
btn.place(x=6,y=8,height=35,width=190)

btn = Button(frame,text ="Log In",relief="raise",font=("cambria",15,"bold"),fg="black",bg="white",command = loginfocus,activebackground="white",activeforeground="green")
btn.place(x=203,y=8,height=35,width=190) 

n=StringVar()
p=StringVar()

nlabel = Label(frame, text = 'Username', font=("cambria",15,"bold"),fg="#d37377",bg="white")
nlabel.place(x=26,y=80,height=35,width=130)
nentry = Entry(frame,textvariable = n, font=("cambria",15,"normal"),bg="#eee",relief="flat")
nentry.place(x=163,y=80,height=35,width=200)
nentry.insert(0,"19BCE028/NUFCE012")
nentry.bind("<Button>",usertext)

plabel = Label(frame, text = 'Password', font=("cambria",15,"bold"),fg="#d37377",bg="white")
plabel.place(x=26,y=130,height=35,width=130)
pentry = Entry(frame, textvariable = p, font=("cambria",15,"normal"), show='*',bg="#eee",relief="flat")
pentry.place(x=163,y=130,height=35,width=200)

btn=Button(frame,text='Login',font=("Inconsolata",20,"bold"),command = loginvalidate,fg="white",bg="#555",relief="raise",cursor="hand2")
btn.place(x=110,y=195,height=35,width=190)

btn = Button(frame,text ="Forgot Your Password?",font=("cambria",14,"bold","underline"),fg="red",bg="white",command = forgot,relief="flat",activebackground="white",cursor="hand2") 
btn.place(x=160,y=250,height=30,width=230)

master.mainloop()