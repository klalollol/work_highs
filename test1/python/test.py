
import tkinter as tk

from time import strftime

 

 

root = tk.Tk()

root.title("BMI Calculator")

root.configure(bg = 'black')

root.geometry('500x300+700+300')

root.resizable(False,False)

def calculate_bmi():

    try:

        height = float(height_e.get())

        weight = float(weight_e.get())

        if height <= 0 or weight <= 0:

            result_label.config(text='ความสูงและน้ำหนักต้องมีค่าเป็นบวก',fg='orange')

        elif height >= 251 or weight >= 725:

            result_label.config(text='ความสูงและน้ำหนักต้องมีค่าตามความจริง',fg='orange')

        else:

            bmi = weight / ((height/100) * (height/100))

            bmi_category = bmi_e(bmi)

            result_label.config(text=f'ค่า BMI: {bmi:.2f} ({bmi_category})')

    except ValueError:

        result_label.config(text='โปรดใส่ค่าน้ำหนักและส่วนสูง',fg='orange')

 

def bmi_e(bmi):

    if bmi < 18.5:

        return 'ผอมเกินไป'

    elif 18.5 <= bmi < 24.9:

        return 'น้ำหนักปกติ'

    elif 25 <= bmi < 29.9:

        return 'อ้วน'

    else:

        return 'อ้วนมาก'

 

def clear():

    Name_e.delete(0, tk.END)

    height_e.delete(0, tk.END)

    weight_e.delete(0, tk.END)  

    result_label.config(text='')

 

 

def enter(event):

    event.widget['bg'] = 'green'

 

def leave(event):

   event.widget['bg'] = 'black'

 

def enter1(event):

    event.widget['bg'] = 'red'

 

def time():

    string_t =strftime('%c')

    label_t.config(text=string_t)

    label_t.after(1000,time)

 

def save():

    import csv

    with open('bmi.csv','a+',newline = '' , encoding = 'utf8') as f:

        try:

            na=Name_e.get()

            height=float(height_e.get())

            weight=float(weight_e.get())

            bmi=weight / ((height/100) * (height/100))

            tim=strftime('%c')

            x = csv.writer(f)

            x.writerow([tim,na,height,weight,bmi])

            result_label.config(text='เสร็จสิ้นการsave Data ขอบคุณที่ใช้บริการ',fg='orange')

        except ValueError:

            result_label.config(text='ไม่สามารถsaveได้กรุณาลองใหม่',fg='orange')

 

       

 

 

def close():

    root.destroy()

 

 

 

Name = tk.Label(root, text="ชื่อ-สกุล:",bg =  'black',fg ='darkorchid1',font = 200)

Name.grid(row=0,column=1,ipadx= 15,ipady= 15,sticky="s")

Name_e= tk.Entry(root)

Name_e.grid(row=0,column=2,ipadx= 10,ipady= 10,sticky="s")

 

height = tk.Label(root, text="ส่วนสูง(cm):",bg =  'black',fg ='blue',font = 200)

height.grid(row=2,column=1,ipadx= 15,ipady= 15,sticky="s")

height_e= tk.Entry(root)

height_e.grid(row=2,column=2,ipadx= 10,ipady= 10,sticky="s")

 

weight = tk.Label(root, text="น้ำหนัก(kg):",bg =  'black',fg ='cornflowerblue',font = 200)

weight.grid(row=4,column=1,ipadx= 15,ipady= 15,sticky="s")

weight_e = tk.Entry(root)

weight_e.grid(row=4,column=2,ipadx= 10,ipady= 10,sticky="s")

 

calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi,bg =  'black',fg ='chartreuse1',font = 200,)

calculate.grid(row=5,column=1,ipadx= 25,ipady= 10,sticky="s")

calculate.bind('<Enter>',enter)

calculate.bind('<Leave>',leave)

clear = tk.Button(root, text="Clear", command=clear,bg =  'black',fg ='gold1',font = 200,)

clear.grid(row=6,column=2,ipadx= 75,ipady= 10,sticky="W")

clear.bind('<Enter>',enter1)

clear.bind('<Leave>',leave)

saveb = tk.Button(root,text="Save Data",command=save,fg="sienna4",bg="black",font=200)

saveb.grid(row=6,column=3,ipadx=30,ipady=10,sticky="W")

saveb.bind('<Enter>',enter)

saveb.bind('<Leave>',leave)

 

result_label = tk.Label(root,bg ='black',fg='orange')

result_label.grid(row=5,column=2,sticky="s")  

 

label_t=tk.Label(bg="black",fg = 'red1',font = 100)

label_t.grid(row=8,column=2,sticky="s")

time()

 

exitb = tk.Button(root,text="Exit",command=close,bg="black",fg="lime",font=200)

exitb.grid(row=6,column=1,ipadx=60,ipady=10,sticky="s")

exitb.bind('<Enter>',enter1)

exitb.bind('<Leave>',leave)

 

root.mainloop()