def mutemusic():
    root.Mutebutton.grid_remove()
    root.Unmutebutton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
def unmutemusic():
    global currentvol
    root.Mutebutton.grid()
    root.Unmutebutton.grid_remove()
    mixer.music.set_volume(currentvol)
def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.1)
def stopmusic():
    mixer.music.stop()
    Audiolabel.configure(text='stop')
def pausemusic():
    mixer.music.pause()
    root.Pausebutton.grid_remove()
    root.Resumebutton.grid()
    Audiolabel.configure(text='pause')
def resumemusic():
    root.Pausebutton.grid()
    root.Resumebutton.grid_remove()
    mixer.music.unpause()
    Audiolabel.configure(text='playing')
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    Audiolabel.configure(text='playing')
def musicurl():
    dd=filedialog.askopenfilename()
    audiotrack.set(dd)
def createwidget():
    global imbrowse,implay,impause,imstop,imvolumeup,imvolumedown,imresume,immute,imunmute,Audiolabel
    ################################################################################image
    imbrowse=PhotoImage(file='search.png')
    implay=PhotoImage(file='play.png')
    impause=PhotoImage(file='pause.png')
    imstop=PhotoImage(file='stop.png')
    imvolumeup=PhotoImage(file='volumeup.png')
    imvolumedown=PhotoImage(file='volumedown.png')
    imresume=PhotoImage(file='play.png')
    immute=PhotoImage(file='pause.png')
    imunmute=PhotoImage(file='play.png')
    ################################################################################changesize
    imbrowse=imbrowse.subsample(2,2)
    implay=implay.subsample(2,2)
    impause=impause.subsample(2,2)
    imstop=imstop.subsample(2,2)
    imvolumeup=imvolumeup.subsample(2,2)
    imvolumedown=imvolumedown.subsample(2,2)
    imresume=imresume.subsample(2,2)
    immute=immute.subsample(2,2)
    imunmute=imunmute.subsample(2,2)
    ################################################################################label
    Tracklabel=Label(root,text='Select Music:',bg='blue',font=('aerial',20))
    Tracklabel.grid(row=0,column=0,padx=20,pady=20)
    Audiolabel = Label(root, text='', bg='blue', font=('aerial', 20),width=20)
    Audiolabel.grid(row=2,column=1)

    ################################################################################entrybox
    Tracklabelentry=Entry(root,font=('aerial',20),width=35,textvariable=audiotrack)
    Tracklabelentry.grid(row=0,column=1,padx=20,pady=20)
    ################################################################################button
    Browsebutton=Button(root,text='Search',bg='red',font=('aerial',15),width=200,bd=5,activebackground='purple',image=imbrowse,compound=RIGHT,command=musicurl)
    Browsebutton.grid(row=0,column=2,padx=20,pady=20)
    Playbutton = Button(root, text='Play', bg='green',font=('aerial',15),width=200,bd=5,activebackground='purple',image=implay,compound=RIGHT,command=playmusic)
    Playbutton.grid(row=1, column=0, padx=20, pady=20)
    root.Pausebutton = Button(root, text='Pause', bg='yellow',font=('aerial',15),width=200,bd=5,activebackground='purple',image=impause,compound=RIGHT,command=pausemusic)
    root.Pausebutton.grid(row=1, column=1, padx=20, pady=20)
    root.Resumebutton = Button(root, text='Resume', bg='green', font=('aerial', 15), width=200, bd=5,activebackground='purple', image=imresume, compound=RIGHT,command=resumemusic)
    root.Resumebutton.grid(row=1, column=1, padx=20, pady=20)
    root.Resumebutton.grid_remove()
    root.Mutebutton=Button(root,text='Mute',width=200,bg='yellow',activebackground='purple',bd=5,image=immute,compound=RIGHT,font=('aerial', 15),command=mutemusic)
    root.Mutebutton.grid(row=3,column=2,padx=20,pady=20)
    root.Unmutebutton = Button(root, text='Unmute', width=200, bg='brown', activebackground='purple', bd=5, image=imunmute,compound=RIGHT, font=('aerial', 15),command=unmutemusic)
    root.Unmutebutton.grid(row=3, column=2,padx=20,pady=20)
    root.Unmutebutton.grid_remove()
    Stopbutton = Button(root, text='Stop', bg='orange',font=('aerial',15),width=200,bd=5,activebackground='purple',image=imstop,compound=RIGHT,command=stopmusic)
    Stopbutton.grid(row=2, column=0, padx=20, pady=20)
    Volumeupbutton = Button(root, text='Volume Up', bg='red',font=('aerial', 15), width=230, bd=5, activebackground='purple',image=imvolumeup,compound=RIGHT,command=volumeup)
    Volumeupbutton.grid(row=1, column=2, padx=20, pady=20)
    Volumedownbutton = Button(root, text='Volume Down', bg='red',font=('aerial', 15), width=230, bd=5, activebackground='purple',image=imvolumedown,compound=RIGHT,command=volumedown)
    Volumedownbutton.grid(row=2, column=2, padx=20, pady=20)


####################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
root=Tk()
root.title("music")
root.geometry('1100x5100')
root.iconbitmap('music_icon.ico')
#root.resizable(False,False)
root.configure(bg='blue')
################################################################################globalvariable
audiotrack=StringVar()
currentvol=0
################################################################################createslider
count=0
text=''
s='Developed By Yash Agrawal'
Sliderlabel=Label(root,text=s,bg='blue', font=('aerial', 50))
Sliderlabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def introlabel():
    global count,text
    if(count>=len(s)):
        count=-1
        text=''
        Sliderlabel.configure(text=text)
    else:
        text=text+s[count]
        Sliderlabel.configure(text=text)
    count=count+1
    Sliderlabel.after(200,introlabel)


mixer.init()
createwidget()
introlabel()
root.mainloop()
