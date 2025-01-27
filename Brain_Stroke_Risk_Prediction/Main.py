import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import Preprocess as pre
import Logisticregression as LR
import RF as RF
import DT as dt
import GB as gb
import LGBM as lgbm
import KNN as knn
import time 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

bgcolor="lightblue"
bgcolor1="#288BA8"
fgcolor="black"
def Home():
        global window4
        def clear():
            print("Clear1")
            txt.delete(0, 'end')
            txt1.delete(0, 'end')
            txt2.delete(0, 'end')
            txt3.delete(0, 'end')
            txt4.delete(0, 'end')
            txt5.delete(0, 'end')
            txt6.delete(0, 'end')
            txt7.delete(0, 'end')
            txt8.delete(0, 'end')
            txt9.delete(0, 'end')
            txt10.delete(0, 'end')
             
            
  



        window4 = tk.Tk()
        window4.title("STROKE RISK PREDICTION USING MACHINE LEARNING ALGORITHMS")
        
 
        window4.geometry('1240x720')
        window4.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window4.grid_rowconfigure(0, weight=1)
        window4.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window4, text="STROKE RISK PREDICTION USING ML ALGORITHMS" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=1)

        lbl = tk.Label(window4, text="Dataset",width=10  ,height=1  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=10, y=100)
        
        txt = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=300, y=115)
        lbl1 = tk.Label(window4, text="Gender (M/F)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=10, y=150)

        txt1 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=300, y=165)

        lbl2 = tk.Label(window4, text="Age",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=10, y=200)

        txt2 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=300, y=215)
        
        lbl3 = tk.Label(window4, text="Hypertension (Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=10, y=250)

        txt3 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt3.place(x=300, y=265)
        
        lbl4 = tk.Label(window4, text="Heart Disease (Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl4.place(x=10, y=300)

        txt4 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt4.place(x=300, y=315)
        
        lbl5 = tk.Label(window4, text="Ever Married (Y/N)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl5.place(x=10, y=350)

        txt5 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt5.place(x=300, y=365)
        
        lbl6 = tk.Label(window4, text="Residence Type(Urban/Rural)",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl6.place(x=10, y=400)

        txt6 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt6.place(x=300, y=415)
        lbl7 = tk.Label(window4, text="avg glucose level",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl7.place(x=500, y=150)

        txt7 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt7.place(x=900, y=165)
        lbl8 = tk.Label(window4, text="BMI",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl8.place(x=500, y=200)

        txt8 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt8.place(x=900, y=215)
        lbl9 = tk.Label(window4, text="smoking status \n (formerly smoked/ never smoked/ smokes/ Unknown)",width=50  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl9.place(x=500, y=250)
        
        txt9 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt9.place(x=900, y=250)
        lbl10 = tk.Label(window4, text="Work Type \n (Private/Self-employed/Govt_job/Children/Never_worked)",width=50  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl10.place(x=500, y=300)

        txt10 = tk.Entry(window4,width=10,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt10.place(x=900, y=300)
        def browse():
                path=filedialog.askopenfilename()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Datset")
        def LRprocess():
                sym=txt.get()
                if sym != "":
                        LR.process(sym)
                        tm.showinfo("Input", "Logistic Regression Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def RFprocess():
                sym=txt.get()
                if sym != "":
                        RF.process(sym)
                        tm.showinfo("Input", "Random Forest Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def DTprocess():
                sym=txt.get()
                if sym != "":
                        dt.process(sym)
                        tm.showinfo("Input", "Decision Tree Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def GBprocess():
                sym=txt.get()
                if sym != "":
                        gb.process(sym)
                        tm.showinfo("Input", "Garient Boosting Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        def LGBMprocess():
                sym=txt.get()
                if sym != "":
                        lgbm.process(sym)
                        tm.showinfo("Input", "Light Garient Boosting Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")
        
        def KNNprocess():
                sym=txt.get()
                if sym != "":
                        knn.process(sym)
                        tm.showinfo("Input", "KNN Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset File")

        def Predictprocess():
                sym=txt.get()
                a=txt1.get()
                if a=='M' or a=="MALE" or a=='m' or "male" or a=="Male":
                        a=1
                else:
                        a=0
                b=txt2.get()
                c=txt3.get()
                if c=='y' or c=="yes" or c=='Y' or c=="YES" or c=="Yes":
                        c=1
                else:
                        c=0
                d=txt4.get()
                if d=='y' or d=="yes" or d=='Y' or d=="YES" or d=="Yes":
                        d=1
                else:
                        d=0
                e=txt5.get()
                if e=='y' or e=="yes" or e=='Y' or e=="YES" or e=="Yes":
                        e=1
                else:
                        e=0
                f=txt10.get()
                f=f.lower()
                if f=="private":
                        f=2
                if f=="self-employed" or f=="self employed":
                        f=3
                if f=="govt_job" or f=="govt job" or f=="govtjob":
                        f=0
                if f=="children":
                        f=4
                if f=="never_worked" or f=="never worked" or f=="neverworked":
                        f=1
                g=txt6.get()
                g=g.lower()
                if g=="urban":
                        g=1
                else:
                        g=0
                h=txt7.get()
                i=txt8.get()
                j=txt9.get()
                j=j.lower()
                if j=="formerly smoked" or j=="formely smoked":
                        j=1
                if j=="never smoked" or j=="never_smoked":
                        j=2
                if j=="smokes":
                        j=3
                if j=="unknown":
                        j=0
                es=[a,b,c,d,e,f,g,h,i,j]
                print("input==",es)
                testdata=[int(a),int(b),int(c),int(d),int(e),int(f),int(g),float(h),float(i),int(j)]
                with open('test.csv', 'w') as out_file:# writing the user input values into test.csv file
                        writer = csv.writer(out_file)
                        writer.writerow(('gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status'))
                        writer.writerow(testdata)
                        print("row=",testdata)               
                if sym != "":
                        #print(sym)
                        data=pd.read_csv("Balanced_data.csv")
                        X=data.drop(["id", "stroke"],axis = 1) #droping out index from features too
                        y=data["stroke"]

                            #Splitting the data into test and training sets

                        X_train,X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)
                            #Fitting the RandomForestClassifier to the training set

                        rfc = LogisticRegression(random_state = 0)
                        rfc.fit(X_train, y_train)
                        df1 = pd.read_csv("test.csv")
                        X_test=df1
                        xes=np.array(X_test)
                        x_text=np.array(xes)
                        res=rfc.predict(x_text)
                        print("res==",res)
                        result=""
                        medicine=""
                        newWindow=Toplevel(window4)
                        newWindow.title("Prediction Results")
                        
                        if res==0:
                                newWindow.geometry("900x100")
                                Label(newWindow,text="There is a low possibilty of you having a stroke\n Eat a healthy diet",fg="green", font=('Times',26)).pack()

                        
                        else:
                                newWindow.geometry("1000x200")
                                Label(newWindow,text="There is a high possibilty of you having a stroke!!!\n Please Consult a Medical expert as soon as possible", fg="red",font=('Times',26)).pack()

                                #result=PR.process(sym)
                        #print("medicine=",medicine)
                        # tm.showinfo("Output", "Prediction : " +str(result))
                        # tm.showinfo("Medicie Recommendation", str(medicine))
                else:
                        tm.showinfo("Input error", "Select Dataset File")
                        
        browse = tk.Button(window4, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=500, y=115)

        clearButton = tk.Button(window4, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=700, y=115)
        LRButton = tk.Button(window4, text="Logistic Regression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        LRButton.place(x=100, y=500)
        KNNButton = tk.Button(window4, text="KNN", command=KNNprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        KNNButton.place(x=300, y=500)
        DTButton = tk.Button(window4, text="Decision Tree", command=DTprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        DTButton.place(x=500, y=500)
        RFButton = tk.Button(window4, text="Random Forest", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        RFButton.place(x=700, y=500)
        GBButton = tk.Button(window4, text="Garient Boosting", command=GBprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        GBButton.place(x=900, y=500)
        LGBButton = tk.Button(window4, text="Light GB", command=LGBMprocess ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        LGBButton.place(x=400, y=550)
        quitWindow = tk.Button(window4, text="Predict", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=600, y=550)
        quitWindow = tk.Button(window4, text="Quit", command=window4.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=800, y=550)
        window4.mainloop()

       
Home()

