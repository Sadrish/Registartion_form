from tkinter import *
root=Tk()
root.geometry("500x300")

# defining the command

def getvals():
    print("Accepted")


Label(root, text="Adhaar Registration Form", font="ar 15 bold").grid(row=0, column=3)  #heading

# left field name

name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="Gender")
fathersname=Label(root, text="Fathers Name")
contact=Label(root, text="Contact")

# Packing left fields

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
fathersname.grid(row=4, column=2)
contact.grid(row=5, column=2)

# Variable for storing entries

namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
fathersnamevalue=StringVar
contactvalue=StringVar
checkvalue=IntVar

# right side entry field

nameentry= Entry(root, textvariable=namevalue )
phoneentry= Entry(root, textvariable=phonevalue)
genderentry= Entry(root, textvariable=gendervalue )
fathersnameentry= Entry(root, textvariable=fathersnamevalue )
contactentry= Entry(root, textvariable=contactvalue )

# packing ride fields


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
fathersnameentry.grid(row=4, column=3)
contactentry.grid(row=5, column=3)

# Creating checkbox button

checkbtn=Checkbutton(text="remember me?" , variable=checkvalue)
checkbtn.grid(row=6, column=3)

# Creating Submit button

Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()

