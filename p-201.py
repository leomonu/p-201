from email import message
from tkinter import *
#window

window=Tk()
window.title("INTEREST CALCULATOR")
window.geometry("400x400")
window.configure(bg="teal")


def calculateInterest():
    p=float(principalEntry.get())
    r=float(rateEntry.get())
    t=float(timeEntry.get())
    i=(p*r*t)/100
    interest=round(i,2)

    resultLabel.destroy()
    
    
    outputMessage=Label(result_frame,text="Your Interest is  : "+str(interest))
    outputMessage.place(x=20,y=40)
    outputMessage.pack()





appLabel=Label(window,text="INTEREST CALCULATOR" ,fg="black",bg="white",font={"monospace",12},bd=5)
appLabel.place(x=50,y=20)

principalLabel=Label(window,text="Principal",fg="black",bg="teal",font={"monospace",12})
principalLabel.place(x=50,y=100)

rateLabel=Label(window,text="Rate",fg="black",bg="teal",font={"monospace",12})
rateLabel.place(x=50,y=140)

timeLabel=Label(window,text="Time",fg="black",bg="teal",font={"monospace",12})
timeLabel.place(x=50,y=180)

principalEntry=Entry(window,text="",bd=2,width=25)
principalEntry.place(x=200,y=100)

rateEntry=Entry(window,text="",bd=2,width=25)
rateEntry.place(x=200,y=140)


timeEntry=Entry(window,text="",bd=2,width=25)
timeEntry.place(x=200,y=180)


calculate=Button(window,text="CALCULATE INTEREST",fg="white",bg="blue",bd=4,command=calculateInterest)
calculate.place(x=150,y=220)

result_frame = LabelFrame(window,text="RESULT",fg="black",bg="teal",font={"monospace",12})
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

resultLabel = Label(window,text="",bg="white",font={"monospace",12},fg="black",width=30)
resultLabel.place(x=20,y=300)


window.mainloop()
