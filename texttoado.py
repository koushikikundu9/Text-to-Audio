import gtts
import os
import tkinter as tk
def con():
    fn=n.get()
    with open(fn,'r') as f:
        text=f.read()
        lang=str(l.get())
        aud=gtts.gTTS(text=text,lang=lang,slow=False)
        aud.save("Sample.mp3")
        os.system("Sample.mp3")
        
root=tk.Tk()
root.geometry("300x200")
root.title("Text to audio convertion")
root.resizable(False,False)
root.config(bg="#fff0f3",bd=5)
i=tk.PhotoImage(file="sound.png")
root.iconphoto(False,i)

tk.Label(root,text='Text to audio convertion',height=2,width=100,font=('Times New Roman',18,'underline','italic'),bg="#fff0f3",bd=3).pack(pady=2)

tk.Label(root,text='Enter file name:',font=('aeriel',12),bg="#fff0f3").place(x=2,y=55)
tk.Label(root,text='Enter language:',font=('aeriel',12),bg="#fff0f3").place(x=2,y=100)

n=tk.StringVar()
l=tk.StringVar()

e1=tk.Entry(root,textvariable=n,width=150,font=('ariel',10),bd=3).pack(pady=11,padx=3)
e2=tk.Entry(root,textvariable=l,width=15,font=('ariel',10),bd=3).pack(pady=14,padx=(3,190))

im2=tk.PhotoImage(file="text.png")
im2=im2.subsample(7,7)
tk.Label(root,text='Click',font=('aeriel',10),bg="#fff0f3").place(x=217,y=156)
b=tk.Button(root,image=im2,bd=3,bg='white',command=lambda:con()).place(x=214,y=120)

root.mainloop()
