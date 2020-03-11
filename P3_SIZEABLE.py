#<IMPORT>
from tkinter import *
import os
import tkinter.font as tkfont
import P3
from tkinter import ttk
OPERATORS=P3.OPERATORS
STATE_STACK = []
#<COMMON_DATA>
mw = Tk()
Current_State = P3.State()
STATUSBAR_CANVAS = None
index=[0,0,0,0,0,"Move in to a house"]
your_house=["Move in to a house","You are living in Tent City","You are living in Trailer Park","You are living in Apartment","You are living in Duplex","You are living in Mansion"]
families = os.listdir("Family")
faces = os.listdir("Faces")
eggs = os.listdir("Egg")
roles = os.listdir("Roles")
jobs = os.listdir("Jobs")
entertainments = os.listdir("Entertainments")
#get the height of screen and use it as the length of the window
HEIGHT = 1000#mw.winfo_screenheight()
#Create lists for images
father = PhotoImage(file="Roles/" + roles[0]);mother = PhotoImage(file="Roles/" + roles[1]);brother = PhotoImage(file="Roles/" + roles[2]);sister = PhotoImage(file="Roles/" + roles[3])
family = [father,mother,brother,sister]
j1=PhotoImage(file="Jobs/"+jobs[0]);j2=PhotoImage(file="Jobs/"+jobs[1]);j3=PhotoImage(file="Jobs/"+jobs[2]);j4=PhotoImage(file="Jobs/"+jobs[3]);j5=PhotoImage(file="Jobs/"+jobs[4]);j6=PhotoImage(file="Jobs/"+jobs[5])
j7=PhotoImage(file="Jobs/"+jobs[6]);j8=PhotoImage(file="Jobs/"+jobs[7]);j9=PhotoImage(file="Jobs/"+jobs[8]);j10=PhotoImage(file="Jobs/"+jobs[9]);j11=PhotoImage(file="Jobs/"+jobs[10]);j12=PhotoImage(file="Jobs/"+jobs[11])
j13=PhotoImage(file="Jobs/"+jobs[12]);j14=PhotoImage(file="Jobs/"+jobs[13]);j15=PhotoImage(file="Jobs/"+jobs[14]);j16=PhotoImage(file="Jobs/"+jobs[15]);j17=PhotoImage(file="Jobs/"+jobs[16]);j18=PhotoImage(file="Jobs/"+jobs[17])
j19=PhotoImage(file="Jobs/"+jobs[18]);j20=PhotoImage(file="Jobs/"+jobs[19]);j21=PhotoImage(file="Jobs/"+jobs[20]);j22=PhotoImage(file="Jobs/"+jobs[21]);j23=PhotoImage(file="Jobs/"+jobs[22]);j24=PhotoImage(file="Jobs/"+jobs[23])
j25=PhotoImage(file="Jobs/"+jobs[24]);j26=PhotoImage(file="Jobs/"+jobs[25]);j27=PhotoImage(file="Jobs/"+jobs[26])
job = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20,j21,j22,j23,j24,j25,j26,j27]
#<HELPER_FUNCTION>
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
def on_combo_configure(event):
    combo = event.widget
    style = ttk.Style()
    # check if the combobox already has the "postoffest" property
    current_combo_style = combo.cget('style') or "TCombobox"
    if len(style.lookup(current_combo_style, 'postoffset'))>0:
        return
    combo_values = combo.cget('values')
    if len(combo_values) == 0:
        return
    longest_value = max(combo_values, key=len)
    font = tkfont.nametofont(str(combo.cget('font')))
    width = font.measure(longest_value + "0") - event.width
    if (width<0):
        # no need to make the popdown smaller
        return
    # create an unique style name using widget's id
    unique_name='Combobox{}'.format(combo.winfo_id())
    # the new style must inherit from curret widget style (unless it's our custom style!) 
    if unique_name in current_combo_style:
        style_name = current_combo_style 
    else:
        style_name = "{}.{}".format(unique_name, current_combo_style)

    style.configure(style_name, postoffset=(0,0,width,0))
    combo.configure(style=style_name)
def loop_by_three(i):
    if i==0:x=HEIGHT/1000*154;y=154
    if i==1:x=436;y=154
    if i==2:x=718;y=154
    if i==3:x=154;y=436
    if i==4:x=436;y=436
    if i==5:x=718;y=436
    if i==6:x=154;y=718
    if i==7:x=436;y=718
    if i==8:x=718;y=718
    return [x,y]
def createFoolW(cat):
    #create the window
    nw = Toplevel(mw)
    nw.geometry(str(HEIGHT)+"x"+str(HEIGHT)+"+0+0")
    nw.resizable(1,1)
    nw.overrideredirect(True)	
    nw.title(cat)

    #create window frame
    back = Frame(master=nw,bg=bgc)
    back.pack_propagate(1)
    back.pack(fill=BOTH, expand=1)
    if cat == "fool":
        fool(back)

    #quit button for frame
    qbf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*200,master=nw)
    qbf.pack_propagate(0) 
    qbf.pack()
    qb = Button(qbf, text="Go Back", font = optionFont, bg=brown,fg=white, 
              activebackground=actb, activeforeground=actf,
              command=lambda: nw.destroy())
    qbf.place(x=HEIGHT/1000*800, y=HEIGHT/1000*950)
    qb.pack(fill=BOTH, expand=1)
def fool(w):
    fool = PhotoImage(file="Egg/" + eggs[0])
    hapr = Label(w, image=fool,bg=bgc)
    hapr.image=fool
    hapr.place(x=((HEIGHT/2)-500),y=(0))
#<COLOR>
butb = _from_rgb((8,229,37))
butf = _from_rgb((33,48,35))
bgc = _from_rgb((245,219,149))
actb = _from_rgb((245,160,166))
actf = _from_rgb((30,16,233))
chob = _from_rgb((0,76,153))
chof = _from_rgb((102,255,255))
chab = _from_rgb((76,0,153))
barb = _from_rgb((192,192,192))
familyb = _from_rgb((143,92,37))
familyf = _from_rgb((240,179,115))
entertainmentb = _from_rgb((128, 28, 3))
entertainmentf = _from_rgb((247, 218, 210))
houseb = _from_rgb((123, 161, 227))
housef = _from_rgb((34, 55, 92))

white = _from_rgb((255,255,255))
black = _from_rgb((0,0,0))
gray = _from_rgb((172,170,165))
orange = _from_rgb((255,128,0))
yellow = _from_rgb((255,255,0))
blue = _from_rgb((0,100,255))
green = _from_rgb((0,255,0))
red = _from_rgb((255,0,0))
brown = _from_rgb((161,114,5))
#<FONT>
buttonFont = tkfont.Font(family="Times New Roman", size=int(HEIGHT/1000*18))
optionFont = tkfont.Font(family="Courier New", size=int(HEIGHT/1000*12))
choiceFont = tkfont.Font(family="Verdana", size = int(HEIGHT/1000*20))
textFont = tkfont.Font(family="Verdana", size = int(HEIGHT/1000*15))
titleFont = tkfont.Font(family="Verdana", size = int(HEIGHT/1000*25))
#<DEFAULT_SETTING>
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': actb,
                                       'fieldbackground': yellow,
                                       'background': brown
                                       }}}
                         )
combostyle.theme_use('combostyle') 
#title of the main window
mw.title('The Divide')
#Size of the main window
mw.geometry(str(HEIGHT)+"x"+str(HEIGHT)+"+0+0")
mw.resizable(1,1)
#Color of the main window
back = Frame(master=mw,bg=bgc)
back.pack_propagate(1)
back.pack(fill=BOTH, expand=1)
#default of button
mw.option_add("*Button.Background", butb)
mw.option_add("*Button.Foreground", butf)

#Array
operators=[]
options=["Hard Mode","Normal Mode","Easy Mode"]

#Bar Chart for indexes
def show_bar(index):
    global chafra
    chafra = Frame(bg=chab,height=HEIGHT/1000*300,width=HEIGHT/1000*800,master=mw)
    chafra.pack_propagate(1)
    chafra.pack()
    chafra.place(x=HEIGHT/1000*100,y=HEIGHT/1000*100)

    monfra = Frame(bg=barb,height=HEIGHT/1000*25,width=HEIGHT/1000*350,master=chafra)
    monfra.pack_propagate(1)
    monfra.pack()
    monfra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*20)
    monf = Frame(bg=chab,height=HEIGHT/1000*30,width=HEIGHT/1000*100,master=chafra)
    monf.pack_propagate(1)
    monf.pack()
    monf.place(x=HEIGHT/1000*300,y=HEIGHT/1000*15)
    mon = Label(master=monf,text="Money",font=textFont,bg=chab,fg=white)
    mon.pack()
    mon.place(x=0,y=0)

    heafra = Frame(bg=barb,height=HEIGHT/1000*25,width=HEIGHT/1000*350,master=chafra)
    heafra.pack_propagate(1)
    heafra.pack()
    heafra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*80)
    monf = Frame(bg=chab,height=HEIGHT/1000*30,width=HEIGHT/1000*100,master=chafra)
    monf.pack_propagate(1)
    monf.pack()
    monf.place(x=HEIGHT/1000*300,y=HEIGHT/1000*75)
    mon = Label(master=monf,text="Income",font=textFont,bg=chab,fg=white)
    mon.pack()
    mon.place(x=0,y=0)

    incfra = Frame(bg=barb,height=HEIGHT/1000*25,width=HEIGHT/1000*350,master=chafra)
    incfra.pack_propagate(1)
    incfra.pack()
    incfra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*140)
    monf = Frame(bg=chab,height=HEIGHT/1000*30,width=HEIGHT/1000*100,master=chafra)
    monf.pack_propagate(1)
    monf.pack()
    monf.place(x=HEIGHT/1000*300,y=HEIGHT/1000*135)
    mon = Label(master=monf,text="Health",font=textFont,bg=chab,fg=white)
    mon.pack()
    mon.place(x=0,y=0)

    hapfra = Frame(bg=barb,height=HEIGHT/1000*25,width=HEIGHT/1000*350,master=chafra)
    hapfra.pack_propagate(1)
    hapfra.pack()
    hapfra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*200)
    monf = Frame(bg=chab,height=HEIGHT/1000*30,width=HEIGHT/1000*100,master=chafra)
    monf.pack_propagate(1)
    monf.pack()
    monf.place(x=HEIGHT/1000*300,y=HEIGHT/1000*195)
    mon = Label(master=monf,text="Happy",font=textFont,bg=chab,fg=white)
    mon.pack()
    mon.place(x=0,y=0)

    edufra = Frame(bg=barb,height=HEIGHT/1000*25,width=HEIGHT/1000*350,master=chafra)
    edufra.pack_propagate(1)
    edufra.pack()
    edufra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*260)
    monf = Frame(bg=chab,height=HEIGHT/1000*30,width=HEIGHT/1000*100,master=chafra)
    monf.pack_propagate(1)
    monf.pack()
    monf.place(x=HEIGHT/1000*300,y=HEIGHT/1000*255)
    mon = Label(master=monf,text="Eduction",font=textFont,bg=chab,fg=white)
    mon.pack()
    mon.place(x=0,y=0)

    mnfra = Frame(bg=orange,height=HEIGHT/1000*25,width=HEIGHT/1000*index[0],master=chafra)
    mnfra.pack_propagate(1)
    mnfra.pack()
    mnfra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*20)

    hafra = Frame(bg=yellow,height=HEIGHT/1000*25,width=HEIGHT/1000*index[1],master=chafra)
    hafra.pack_propagate(1)
    hafra.pack()
    hafra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*80)

    icfra = Frame(bg=green,height=HEIGHT/1000*25,width=HEIGHT/1000*index[2],master=chafra)
    icfra.pack_propagate(1)
    icfra.pack()
    icfra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*140)

    hpfra = Frame(bg=blue,height=HEIGHT/1000*25,width=HEIGHT/1000*index[3],master=chafra)
    hpfra.pack_propagate(1)
    hpfra.pack()
    hpfra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*200)

    eufra = Frame(bg=red,height=HEIGHT/1000*25,width=HEIGHT/1000*index[4],master=chafra)
    eufra.pack_propagate(0)
    eufra.pack()
    eufra.place(x=HEIGHT/1000*400,y=HEIGHT/1000*260)

    if index[3]>250:
        Happy = PhotoImage(file="Faces/" + faces[0])
        hapr = Label(chafra, image=Happy,bg=chab)
        hapr.image=Happy
        hapr.place(x=HEIGHT/1000*50,y=HEIGHT/1000*50)
    if 250>=index[3]>200:
        Nothing = PhotoImage(file="Faces/" + faces[1])
        notr = Label(chafra, image=Nothing,bg=chab)
        notr.image=Nothing
        notr.place(x=HEIGHT/1000*50,y=HEIGHT/1000*50)
    if index[3]<=200:
        Hey = PhotoImage(file="Faces/" + faces[2])
        heyr = Label(chafra, image=Hey,bg=chab)
        heyr.image=Hey
        heyr.place(x=HEIGHT/1000*50,y=HEIGHT/1000*50)
def update():
    global index
    index[0] = (Current_State.d['profile'][1])/1500000*350
    index[1] = (sum(i for i in Current_State.d['profile'][2]))/500000*350
    index[2] = (sum(i for i in Current_State.d['profile'][3]))/400*350
    index[3] = (sum(i for i in Current_State.d['profile'][4]))/400*350
    index[4] = (sum(i for i in Current_State.d['profile'][5]))/60*350
    return index
def gamedifbp(OPERATOR,s):
    global index
    s = OPERATOR.apply(s)
    update()
    show_bar(index)
def show_house(index):
        honf = Frame(bg=bgc,height=HEIGHT/1000*100,width=HEIGHT/1000*500,master=mw)
        honf.pack_propagate(0)
        honf.pack()
        honf.place(x=HEIGHT/1000*250,y=HEIGHT/1000*0)
        hon = Label(master=honf,text=index[5],font=titleFont,bg=bgc,fg=black)
        hon.pack()
        hon.place(x=HEIGHT/1000*0,y=HEIGHT/1000*0)

    
    

#Game Mode Choose
#PoorFamily
PoorFamily = PhotoImage(file="Family/" + families[1])
porr = Label(mw, image=PoorFamily,bg=bgc)
porr.pack(fill=BOTH,expand=1)
porr.place(x=HEIGHT/1000*100,y=HEIGHT/1000*100)
porf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*200,master=mw)
porf.pack_propagate(0) 
porf.pack()
porb = Button(porf, text=options[0], font = choiceFont,bg=chob,fg=chof,
              activebackground=actb, activeforeground=actf,
              command=lambda: gamedifbp(P3.OPERATORS[0],Current_State))
porf.place(x=HEIGHT/1000*100,y=HEIGHT/1000*300)
porb.pack(fill=BOTH,expand=1)
#MiddleFamily
MiddleFamily = PhotoImage(file="Family/" + families[0])
midr = Label(mw, image=MiddleFamily,bg=bgc)
midr.pack(fill=BOTH,expand=1)
midr.place(x=HEIGHT/1000*400,y=HEIGHT/1000*100)
midf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*200,master=mw)
midf.pack_propagate(0) 
midf.pack()
midb = Button(midf, text=options[1], font = choiceFont,bg=chob,fg=chof,
              activebackground=actb, activeforeground=actf,
              command=lambda: gamedifbp(P3.OPERATORS[1],Current_State))
midf.place(x=HEIGHT/1000*400,y=HEIGHT/1000*300)
midb.pack(fill=BOTH,expand=1)
#RichFamily
RichFamily = PhotoImage(file="Family/" + families[2])
ricr = Label(mw, image=RichFamily,bg=bgc)
ricr.pack(fill=BOTH,expand=1)
ricr.place(x=HEIGHT/1000*700,y=HEIGHT/1000*100)
riff = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*200,master=mw)
riff.pack_propagate(0) 
riff.pack()
rifb = Button(riff, text=options[2], font = choiceFont,bg=chob,fg=chof,
              activebackground=actb, activeforeground=actf,
              command=lambda: gamedifbp(P3.OPERATORS[2],Current_State))
riff.place(x=HEIGHT/1000*700,y=HEIGHT/1000*300)
rifb.pack(fill=BOTH,expand=1)

#Creates the list of buttons for the operators
def createButtonW(cat):

    #create the window
    nw = Toplevel(mw)
    nw.geometry(str(HEIGHT)+"x"+str(HEIGHT)+"+0+0")
    nw.resizable(1, 1)
    nw.overrideredirect(True)	
    nw.title(cat)

    #create window frame
    back = Frame(master=nw,bg=bgc)
    back.pack_propagate(0)
    back.pack(fill=BOTH, expand=1)

    #quit button for frame
    qbf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*200,master=nw)
    qbf.pack_propagate(0) 
    qbf.pack()
    qb = Button(qbf, text="Back", font = optionFont, bg=brown,fg=white, 
            activebackground=actb, activeforeground=actf,
        command=lambda: nw.destroy())
    qbf.place(x=HEIGHT/1000*800, y=HEIGHT/1000*950)
    qb.pack(fill=BOTH, expand=1)


    winTitle = Label(back, text=cat, bg=bgc)
    winTitle.place(x=HEIGHT/1000*500, y=HEIGHT/1000*50)

    if cat == "Family Profile":
        pro_list = ["Income", "Health", "Happiness", "Education", "Occupation",\
        "Age"]
        photo_size = [128, 128]
        Grid = Frame(height=HEIGHT/1000*photo_size[0]*5, width=HEIGHT/1000*photo_size[1]*7, master=back, bg=bgc)
        Grid.place(x=HEIGHT/1000*52, y=HEIGHT/1000*100)
        for i in range(6):
            frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
            frame.grid(row=0, column=i+1)
            frame.pack_propagate(False)
            label = Label(frame, text=pro_list[i], font=textFont, bg=bgc)
            label.pack(fill=BOTH, expand=1)

        for i in range(5):
            frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
            frame.grid(row=i, column=0)
            frame.pack_propagate(False)
            if i >= 1:
                label = Label(frame, image=family[i-1], font=textFont, bg=bgc)
                label.pack(fill=BOTH, expand=1)

        for ind in range(4):
            counter = 1
            for info in [2, 3, 4, 5, 6, 8]:
                frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
                frame.grid(row=ind+1, column=counter)
                frame.pack_propagate(False)
                label = Label(frame, text=Current_State.d['profile'][info][ind], font=textFont, bg=bgc)	
                label.pack(fill=BOTH, expand=1)
                counter += 1

    def bp(operator, s):
        global index
        s = operator.apply(s)
        show_bar(update())
        show_house(update())
        nw.destroy()
        #add update chart option
        return

    if cat == "Insurance":
        Iop = P3.OPERATORS[39:42]
        af = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        af.pack_propagate(False)
        if Iop[0].is_applicable(Current_State):
            ab = Button(af, text="plan 1", font=buttonFont,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Iop[0], Current_State))
        else:
            ab = Button(af, text="plan 1", font=buttonFont,
                                state=DISABLED)
        #add ,command=lambda: bp(1)
        af.place(x=HEIGHT/1000*100, y=HEIGHT/1000*300)
        ab.pack(fill=BOTH, expand=1)

        bf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        bf.pack_propagate(False)
        if Iop[1].is_applicable(Current_State):
            bb = Button(bf, text="plan 2", font=buttonFont,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Iop[1], Current_State))
        else:
            bb = Button(bf, text="plan 2", font=buttonFont,
                                state=DISABLED)
        
        #add ,command=lambda: bp(1)
        bf.place(x=HEIGHT/1000*375, y=HEIGHT/1000*300)
        bb.pack(fill=BOTH, expand=1)

        cf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        cf.pack_propagate(False)
        if Iop[2].is_applicable(Current_State):
            cb = Button(cf, text="plan 3", font=buttonFont,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Iop[2], Current_State))
        else:
            cb = Button(cf, text="plan 3", font=buttonFont,
                                state=DISABLED)
        
        #add ,command=lambda: bp(1)
        cf.place(x=HEIGHT/1000*650, y=HEIGHT/1000*300)
        cb.pack(fill=BOTH, expand=1)

    if cat == "Entertainment":
        Eop = P3.OPERATORS[20:25]


        park = PhotoImage(file="Entertainments/" + entertainments[0])
        r1 = Label(master=back, image=park,bg=bgc)
        r1.image=park
        r1.pack(fill=BOTH,expand=1)
        r1.place(x=HEIGHT/1000*75,y=HEIGHT/1000*130)
        parkf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        parkf.pack_propagate(False)
        if Eop[0].is_applicable(Current_State):
                parkb = Button(parkf, text="Park", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf, 
                                command=lambda: bp(Eop[0], Current_State))
        else:
                parkb = Button(parkf, text="Park", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                state=DISABLED)
        parkf.place(x=HEIGHT/1000*100, y=HEIGHT/1000*350)
        parkb.pack(fill=BOTH, expand=1)


        circus = PhotoImage(file="Entertainments/" + entertainments[1])
        r2 = Label(master=back, image=circus,bg=bgc)
        r2.image=circus
        r2.pack(fill=BOTH,expand=1)
        r2.place(x=HEIGHT/1000*75,y=HEIGHT/1000*415)
        circusf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        circusf.pack_propagate(False)
        if Eop[1].is_applicable(Current_State):
                circusb = Button(circusf, text="Circus", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[1], Current_State))
        else:
                circusb = Button(circusf, text="Circus", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                state=DISABLED)
        circusf.place(x=HEIGHT/1000*100, y=HEIGHT/1000*650)
        circusb.pack(fill=BOTH, expand=1)



        movie = PhotoImage(file="Entertainments/" + entertainments[2])
        r3 = Label(master=back, image=movie,bg=bgc)
        r3.image=movie
        r3.pack(fill=BOTH,expand=1)
        r3.place(x=HEIGHT/1000*75,y=HEIGHT/1000*700)
        moviesf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        moviesf.pack_propagate(False)
        if Eop[2].is_applicable(Current_State):
                moviesb = Button(moviesf, text="Movies", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[2], Current_State))
        else:
                moviesb = Button(moviesf, text="Movies", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                state=DISABLED)
        moviesf.place(x=HEIGHT/1000*100, y=HEIGHT/1000*950)
        moviesb.pack(fill=BOTH, expand=1)


        apark = PhotoImage(file="Entertainments/" + entertainments[3])
        r4 = Label(master=back, image=apark,bg=bgc)
        r4.image=apark
        r4.pack(fill=BOTH,expand=1)
        r4.place(x=HEIGHT/1000*575,y=HEIGHT/1000*135)
        amusementf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        amusementf.pack_propagate(False)
        if Eop[3].is_applicable(Current_State):
                amusementb = Button(amusementf, text="Amusement Park", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[3], Current_State))
        else:
                amusementb = Button(amusementf, text="Amusement Park", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                        state=DISABLED)
        amusementf.place(x=HEIGHT/1000*600, y=HEIGHT/1000*350)
        amusementb.pack(fill=BOTH, expand=1)


        vacation = PhotoImage(file="Entertainments/" + entertainments[4])
        r5 = Label(master=back, image=vacation,bg=bgc)
        r5.image=vacation
        r5.pack(fill=BOTH,expand=1)
        r5.place(x=HEIGHT/1000*625,y=HEIGHT/1000*400)
        vf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*250, master=back)
        vf.pack_propagate(False)
        if Eop[4].is_applicable(Current_State):
                vb = Button(vf, text="Vacation Abroad", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[4], Current_State))
        else:
                vb = Button(vf, text="Vacation Abroad", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                        state=DISABLED)
        vf.place(x=HEIGHT/1000*600, y=HEIGHT/1000*650)
        vb.pack(fill=BOTH, expand=1)

    def cbp(comboBox, s):
        option = comboBox.get()
        print(option)
        op = 0
        for i in P3.OPERATORS:
            if i.name == option:
                op = i
        op.apply(s)
        show_bar(update())
        show_house(update())
        nw.destroy()
        return


    if cat == "Shop":
        Wop = P3.OPERATORS[24:33]
        pro_list = ["Grocery"]
        photo_size = [128, 128]
        Grid = Frame(height=HEIGHT/1000*photo_size[0]*5, width=HEIGHT/1000*photo_size[1]*7, master=back, bg=bgc)
        Grid.place(x=HEIGHT/1000*52, y=HEIGHT/1000*100)
        for i in range(1):
            frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
            frame.grid(row=0, column=i+1)
            frame.pack_propagate(False)
            label = Label(frame, text=pro_list[i], font=textFont, bg=bgc)
            label.pack(fill=BOTH, expand=1)

        comboBoxes = []

        for i in range(5):
            frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1]*3, master=Grid, bg=bgc)
            frame.grid(row=i, column=0)
            frame.pack_propagate(False)
            if i >= 1:
                label = Label(frame, image=family[i-1], font=textFont, bg=bgc)
                label.pack(fill=BOTH, expand=1)          
                frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
                frame.grid(row=i, column=1)
                frame.pack_propagate(False)
                ind = []
                for j in Wop:
                    if j.is_applicable(Current_State):
                        ind.append(j.name)
                variable = ttk.Combobox(values=ind, master=frame)
                variable.bind('<Configure>', on_combo_configure)
                variable.place(x=0, y=64)
        def sob(comboBoxes, Grid, back):
            counter = 0
            for i in comboBoxes:
                if i.get() != "":
                    counter += 1

            if counter > 1 or counter == 0:
                label = Label(back, text="You need to choose only one option")
                label.pack()
            else:
                show_buttons(comboBoxes, Grid)


        showOptions = Button(back, text="Display Apply Button", font=optionFont, bg=brown, fg=white,
                                  activebackground=actb, activeforeground=actf,
                                  command=lambda: sob(comboBoxes, Grid, back))
        showOptions.pack()
        def show_buttons(comboBoxes, Grid):
            for i in range(5):
                frame = Frame(height=HEIGHT / 1000 * photo_size[0], width=HEIGHT / 1000 * photo_size[1] * 3, master=Grid,
                              bg=bgc)
                frame.grid(row=i, column=2)
                frame.pack_propagate(False)
                if i >= 1 and comboBoxes[i-1].get() != "":
                    apButton = Button(frame, text="Apply", font=optionFont, bg=brown, fg=white,
                                      activebackground=actb, activeforeground=actf,
                                      command=lambda: cbp(comboBoxes[i-1], Current_State))
                    apButton.place(x=32, y=56)
                elif i >= 1 and comboBoxes[i-1].get() == "":
                    apButton = Button(frame, text="Apply", font=optionFont, bg=brown, fg=white, state=DISABLED)
                    apButton.place(x=32, y=56)



    if cat == "Schooling":
        Wop = [P3.OPERATORS[11:17],P3.OPERATORS[18:24],[],[]]
        pro_list = ["Job"]
        photo_size = [128, 128]
        Grid = Frame(height=HEIGHT/1000*photo_size[0]*5, width=HEIGHT/1000*photo_size[1]*7, master=back, bg=bgc)
        Grid.place(x=HEIGHT/1000*52, y=HEIGHT/1000*100)
        for i in range(1):
            frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
            frame.grid(row=0, column=i+1)
            frame.pack_propagate(False)
            label = Label(frame, text=pro_list[i], font=textFont, bg=bgc)
            label.pack(fill=BOTH, expand=1)
        comboBoxes = []
        for i in range(5):
            frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1]*3, master=Grid, bg=bgc)
            frame.grid(row=i, column=0)
            frame.pack_propagate(False)
            if i >= 1:
                label = Label(frame, image=family[i-1], font=textFont, bg=bgc)
                label.pack(fill=BOTH, expand=1)
                frame = Frame(height=HEIGHT/1000*photo_size[0], width=HEIGHT/1000*photo_size[1], master=Grid, bg=bgc)
                frame.grid(row=i, column=1)
                frame.pack_propagate(False)
                ind = []
                for j in Wop[i-1]:
                    if j.is_applicable(Current_State):
                        ind.append(j.name)
                variable = ttk.Combobox(values=ind, master=frame)
                variable.bind('<Configure>', on_combo_configure)
                comboBoxes.append(variable)
                variable.place(x=0, y=64)


        for i in range(5):
            frame = Frame(height=HEIGHT / 1000 * photo_size[0], width=HEIGHT / 1000 * photo_size[1] * 3, master=Grid,
                          bg=bgc)
            frame.grid(row=i, column=2)
            frame.pack_propagate(False)
            if i >= 1 and comboBoxes[i-1].get() != "":
                apButton = Button(frame, text="Apply", font=optionFont, bg=brown, fg=white,
                                  activebackground=actb, activeforeground=actf,
                                  command=lambda: cbp(comboBoxes[i-1], Current_State))
                apButton.place(x=32, y=56)
            elif i >= 1 and comboBoxes[i-1].get() == "":
                apButton = Button(frame, text="Apply", font=optionFont, bg=brown, fg=white, state=DISABLED)
                apButton.place(x=32, y=56)




    if cat == "Work Place":

        Who = P3.OPERATORS[3:7]
        What = P3.OPERATORS[11:20]

        def father(what,s):
                for i in range(0,9):
                        parkf = Frame(height=HEIGHT/1000*128, width=HEIGHT/1000*128, master=back)
                        parkf.pack_propagate(False)
                        if what[i].is_applicable(s):
                                parkb = Button(parkf, image=job[i], background=bgc, 
                                                command=lambda: bp(what[i], s))
                        else:
                                parkb = Button(parkf, image=job[i], font=buttonFont,
                                                state=DISABLED)
                        parkf.place(x=HEIGHT/1000*loop_by_three(i)[0], y=HEIGHT/1000*loop_by_three(i)[1])
                        parkb.pack(fill=BOTH, expand=1)         
        faf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*130, master=back)
        faf.pack_propagate(False)
        if Who[0].is_applicable(Current_State):
                fab = Button(faf, text="Father", font=buttonFont,bg=familyb,fg=familyf,
                                activebackground=actb, activeforeground=actf, 
                                command=lambda: father(What,Current_State) )
        else:
                fab = Button(maf, text="Father", font=buttonFont,bg=familyb,fg=familyf,
                                state=DISABLED)
        faf.place(x=HEIGHT/1000*96, y=HEIGHT/1000*846)
        fab.pack(fill=BOTH, expand=1)


        def mother(what,s):
                for i in range(0,9):
                        parkf = Frame(height=HEIGHT/1000*128, width=HEIGHT/1000*128, master=back)
                        parkf.pack_propagate(False)
                        if what[i].is_applicable(s):
                                parkb = Button(parkf, image=job[i+9], background=bgc, 
                                                command=lambda: bp(what[i], s))
                        else:
                                parkb = Button(parkf, image=job[i+9], font=buttonFont,
                                                state=DISABLED)
                        parkf.place(x=HEIGHT/1000*loop_by_three(i)[0], y=HEIGHT/1000*loop_by_three(i)[1])
                        parkb.pack(fill=BOTH, expand=1)         
        maf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*130, master=back)
        maf.pack_propagate(False)
        if Who[1].is_applicable(Current_State):
                mab = Button(maf, text="Mother", font=buttonFont,bg=familyb,fg=familyf,
                                activebackground=actb, activeforeground=actf, 
                                command=lambda: father(What,Current_State) )
        else:
                mab = Button(maf, text="Mother", font=buttonFont,bg=familyb,fg=familyf,
                                state=DISABLED)
        maf.place(x=HEIGHT/1000*322, y=HEIGHT/1000*846)
        mab.pack(fill=BOTH, expand=1)


        def brother(what,s):
                for i in range(0,9):
                        parkf = Frame(height=HEIGHT/1000*128, width=HEIGHT/1000*128, master=back)
                        parkf.pack_propagate(False)
                        if what[i].is_applicable(s):
                                parkb = Button(parkf, image=job[i], background=bgc, 
                                                command=lambda: bp(what[i], s))
                        else:
                                parkb = Button(parkf, image=job[i], font=buttonFont,
                                                state=DISABLED)
                        parkf.place(x=HEIGHT/1000*loop_by_three(i)[0], y=HEIGHT/1000*loop_by_three(i)[1])
                        parkb.pack(fill=BOTH, expand=1)         
        brf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*130, master=back)
        brf.pack_propagate(False)
        if Who[0].is_applicable(Current_State):
                brb = Button(brf, text="Brother", font=buttonFont,bg=familyb,fg=familyf,
                                activebackground=actb, activeforeground=actf, 
                                command=lambda: father(What,Current_State) )
        else:
                brb = Button(brf, text="Brother", font=buttonFont,bg=familyb,fg=familyf,
                                state=DISABLED)
        brf.place(x=HEIGHT/1000*548, y=HEIGHT/1000*846)
        brb.pack(fill=BOTH, expand=1)


        def sister(what,s):
                for i in range(0,9):
                        parkf = Frame(height=HEIGHT/1000*128, width=HEIGHT/1000*128, master=back)
                        parkf.pack_propagate(False)
                        if what[i].is_applicable(s):
                                parkb = Button(parkf, image=job[i], background=bgc, 
                                                command=lambda: bp(what[i], s))
                        else:
                                parkb = Button(parkf, image=job[i], font=buttonFont,
                                                state=DISABLED)
                        parkf.place(x=HEIGHT/1000*loop_by_three(i)[0], y=HEIGHT/1000*loop_by_three(i)[1])
                        parkb.pack(fill=BOTH, expand=1)         
        sif = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*130, master=back)
        sif.pack_propagate(False)
        if Who[0].is_applicable(Current_State):
                sib = Button(sif, text="Sister", font=buttonFont,bg=familyb,fg=familyf,
                                activebackground=actb, activeforeground=actf, 
                                command=lambda: father(What,Current_State) )
        else:
                sib = Button(sif, text="Sister", font=buttonFont,bg=familyb,fg=familyf,
                                state=DISABLED)
        sif.place(x=HEIGHT/1000*774, y=HEIGHT/1000*846)
        sib.pack(fill=BOTH, expand=1)

    

    if cat == "Home":
        Eop = P3.OPERATORS[34:39]

        tcf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*300, master=back)
        tcf.pack_propagate(False)
        if Eop[0].is_applicable(Current_State):
                tcb = Button(tcf, text="Tent City", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf, 
                                command=lambda: bp(Eop[0], Current_State))
        else:
                tcb = Button(tcf, text="Tent City", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                state=DISABLED)
        tcf.place(x=HEIGHT/1000*100, y=HEIGHT/1000*250)
        tcb.pack(fill=BOTH, expand=1)

        trf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*300, master=back)
        trf.pack_propagate(False)
        if Eop[1].is_applicable(Current_State):
                trb = Button(trf, text="Trailer", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[1], Current_State))
        else:
                trb = Button(trf, text="Trailer", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                state=DISABLED)

        trf.place(x=HEIGHT/1000*350, y=HEIGHT/1000*500)
        trb.pack(fill=BOTH, expand=1)

        apf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*300, master=back)
        apf.pack_propagate(False)
        if Eop[2].is_applicable(Current_State):
                apb = Button(apf, text="Apartment", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[2], Current_State))
        else:
                apb = Button(apf, text="Apartment", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                state=DISABLED)
        apf.place(x=HEIGHT/1000*100, y=HEIGHT/1000*750)
        apb.pack(fill=BOTH, expand=1)

        dpf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*300, master=back)
        dpf.pack_propagate(False)
        if Eop[3].is_applicable(Current_State):
                dpb = Button(dpf, text="Duplex", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[3], Current_State))
        else:
                dpb = Button(dpf, text="Duplex", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                        state=DISABLED)

        dpf.place(x=HEIGHT/1000*600, y=HEIGHT/1000*250)
        dpb.pack(fill=BOTH, expand=1)

        mnf = Frame(height=HEIGHT/1000*50, width=HEIGHT/1000*300, master=back)
        mnf.pack_propagate(False)
        if Eop[4].is_applicable(Current_State):
                mnb = Button(mnf, text="Mansion", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                                activebackground=actb, activeforeground=actf,
                                command=lambda: bp(Eop[4], Current_State))
        else:
                mnb = Button(mnf, text="Mansion", font=buttonFont,bg=entertainmentb,fg=entertainmentf,
                        state=DISABLED)
        mnf.place(x=HEIGHT/1000*600, y=HEIGHT/1000*750)
        mnb.pack(fill=BOTH, expand=1)

        
#Insurance

insf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
insf.pack_propagate(0) 
insf.pack()
insb = Button(insf, text="Insurance", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Insurance"))
insf.place(x=HEIGHT/1000*600,y=HEIGHT/1000*500)
insb.pack(fill=BOTH,expand=1)

#Entertainment
entf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
entf.pack_propagate(0) 
entf.pack()
entb = Button(entf, text="Entertainment", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Entertainment"))
entf.place(x=HEIGHT/1000*100,y=HEIGHT/1000*500)
entb.pack(fill=BOTH,expand=1)
#Shop
shof = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
shof.pack_propagate(0) 
shof.pack()
shob = Button(shof, text="Shop", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Shop"))
shof.place(x=HEIGHT/1000*100,y=HEIGHT/1000*600)
shob.pack(fill=BOTH,expand=1)
#Schooling
schf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
schf.pack_propagate(0)
schf.pack()
schb = Button(schf, text="Schooling", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Schooling"))
schf.place(x=HEIGHT/1000*600,y=HEIGHT/1000*600)
schb.pack(fill=BOTH,expand=1)
#Family Profile

famf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
famf.pack_propagate(0) 
famf.pack()
famb = Button(famf, text="Family Profile", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Family Profile"))
famf.place(x=HEIGHT/1000*100,y=HEIGHT/1000*800)
famb.pack(fill=BOTH,expand=1)
#Home
homf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
homf.pack_propagate(0) 
homf.pack()
homb = Button(homf, text="Home", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Home"))
homf.place(x=HEIGHT/1000*600,y=HEIGHT/1000*700)
homb.pack(fill=BOTH,expand=1)
#Work Place
worf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
worf.pack_propagate(0) 
worf.pack()
worb = Button(worf, text="Work Place", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: createButtonW("Work Place"))
worf.place(x=HEIGHT/1000*100,y=HEIGHT/1000*700)
worb.pack(fill=BOTH,expand=1)
#Next Turn

def nextTurn(s):
    s = P3.OPERATORS[42].apply(s)
    show_bar(update())

nexf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
nexf.pack_propagate(0)
nexf.pack()
nexb = Button(nexf, text="Next Turn", font = buttonFont,
              activebackground=actb, activeforeground=actf,
              command=lambda: nextTurn(Current_State))
nexf.place(x=HEIGHT/1000*600,y=HEIGHT/1000*800)
nexb.pack(fill=BOTH,expand=1)
#Exit
exif = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
exif.pack_propagate(0) 
exif.pack()
exib = Button(exif, text="Exit", font = optionFont,
              bg=gray, fg=white, command=quit)
exif.place(x=HEIGHT/1000*600,y=HEIGHT/1000*900)
exib.pack(fill=BOTH,expand=1)
#Option
optf = Frame(height=HEIGHT/1000*50,width=HEIGHT/1000*300,master=mw)
optf.pack_propagate(0) 
optf.pack()
optb = Button(optf, text="Option", font = optionFont,
              bg=gray, fg=white, command=lambda: createFoolW("fool"))
optf.place(x=HEIGHT/1000*100,y=HEIGHT/1000*900)
optb.pack(fill=BOTH,expand=1)








mw.mainloop()


