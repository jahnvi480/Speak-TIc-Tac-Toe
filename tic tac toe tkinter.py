from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import pyttsx3

root = Tk()
root.title('tic-tac-toe')
root.resizable(False,False)
root.geometry('550x755')
root.iconbitmap('tictactoe.ico')
root.configure(bg='#414242')

click = True
count = ps1 = ps2 = 0

tic_toc = []
for i in range(1,10,3):
    t = [i, i+1, i+2]
    tic_toc.append(t)

xp = PhotoImage(file = 'X.png')
op = PhotoImage(file = 'O.png')
spk = PhotoImage(file = 'speaker.png')
ex = PhotoImage(file= 'exit.png')


def clear():
    global tic_toc
    tic_toc = []
    for i in range(1, 10, 3):
        t = [i, i + 1, i + 2]
        tic_toc.append(t)

def voice():
    # Initialize the recognizer
    r = sr.Recognizer()
    # Function to convert text to
    # speech
    def SpeakText(command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            t = MyText.split()

            def clear():
                global tic_toc
                tic_toc = []
                for i in range(1, 10, 3):
                    t = [i, i + 1, i + 2]
                    tic_toc.append(t)

            def press(num, r, c):
                global click, count
                if click == True:
                    lp = Label(root, image=xp, bg='#222626')
                    if c == 0:
                        lp.grid(row=r, column=c, padx=(50, 0))
                    else:
                        lp.grid(row=r, column=c)
                    for i in range(3):
                        for j in range(3):
                            if num == tic_toc[i][j]:
                                tic_toc[i][j] = 'X'
                    count += 1
                    click = False
                    checkWin('X')
                else:
                    lp = Label(root, image=op, bg='#222626')
                    if c == 0:
                        lp.grid(row=r, column=c, padx=(50, 0))
                    else:
                        lp.grid(row=r, column=c)
                    for i in range(3):
                        for j in range(3):
                            if num == tic_toc[i][j]:
                                tic_toc[i][j] = 'O'
                    count += 1
                    click = True
                    checkWin('O')

            def checkWin(o):
                global count, click, ps1, ps2
                for i in range(3):
                    e = s = q = r = 0
                    for j in range(3):
                        if tic_toc[i][j] == o:
                            r += 1
                        if tic_toc[j][i] == o:
                            q += 1
                        if tic_toc[i][i] == o:
                            s += 1
                        if tic_toc[i][2 - i] == o:
                            e += 1

                    if r == 3 or q == 3 or (tic_toc[0][0] == o and tic_toc[1][1] == o and tic_toc[2][2] == o) or (
                            tic_toc[0][2] == o and tic_toc[1][1] == o and tic_toc[2][0] == o):
                        SpeakText("Congratulations! {} wins this game!!".format(o))
                        tkinter.messagebox.showinfo('tic tac toe', o + " wins!!")
                        if o == 'X':
                            click = True
                            ps1 += 1
                        else:
                            click = True
                            ps2 += 1
                        count = 0
                        clear()
                        play()

                if count == 9:
                    tkinter.messagebox.showinfo('tic tac toe', "OOPS! Game Tie!")
                    click = True
                    count = 0
                    clear()
                    play()

            for i in t:
                if i.isdigit():
                    m = int(i)
                    print("Marking on {}".format(m))
                    SpeakText("Marking on {}".format(m))
                    if m == 1:
                        press(1, 4, 0)
                    elif m == 2:
                        press(2,4,1)
                    elif m ==3:
                        press(3,4,2)
                    elif m == 4:
                        press(4,5,0)
                    elif m == 5:
                        press(5,5,1)
                    elif m ==6:
                        press(6,5,2)
                    elif m == 7:
                        press(7,6,0)
                    elif m == 8:
                        press(8,6,1)
                    elif m ==9:
                        press(9,6,2)
                    else:
                        SpeakText("Sorry Wrong Input, Please Repeat")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        SpeakText("Sorry I didn't get you, Please Repeat")

def play():
    welcome = Label(text='Welcome to my tic-tac-toe game',fg='#1af0b7',bg='#414242')
    global ps1, ps2
    p1 = Label(text='Player1 X:  {}'.format(ps1),font=20,fg='#1af0b7',bg='#414242')
    p2 = Label(text='Player2 O:  {}'.format(ps2),font=20,fg='#1af0b7',bg='#414242')
    c = Label(text='Made by Jahnvi Thakkar',fg='#1af0b7',bg='#414242')

    def reset():
        global ps1, ps2
        ps1 = ps2 = 0
        p1['text'] = 'Player1 X:  0'
        p2['text'] = 'Player2 O:  0'
    b = Button(text='Reset', width=20, fg='#00ff00', bg='#222626', command=reset, activebackground='#12b385')
    e = Button(text='Exit', fg='#ff0000',width =12, command=exit, activebackground='#414242',bg='#222626')
    sp = Button(text='Speak to Mark',fg='#ffff00', bg='#222626', command=voice, activebackground='#12b385',relief='raise')
    # Creating a tuple containing
    # the specifications of the font.
    fontwel = ("Comic Sans MS", 20, 'bold')
    fontp = ('Comic Sans Ms',14)
    fontm = ('Comic Sans Ms',10)
    fontb = ('Comic Sans Ms',8)
    # Parsed the specifications to the
    # Text widget using .configure( ) method.
    welcome.configure(font=fontwel)
    b.configure(font=fontp)
    e.configure(font=fontp)
    p1.configure(font=fontp)
    p2.configure(font=fontp)
    c.configure(font=fontm)
    sp.configure(font=fontp)

    bt1 = Button(root,text='1', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(1, 4, 0), activebackground='#12b385')
    bt2 = Button(root,text='2', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(2, 4, 1), activebackground='#12b385')
    bt3 = Button(root,text='3', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(3, 4, 2), activebackground='#12b385')
    bt4 = Button(root,text='4', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(4, 5, 0), activebackground='#12b385')
    bt5 = Button(root,text='5', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(5, 5, 1), activebackground='#12b385')
    bt6 = Button(root,text='6', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(6, 5, 2), activebackground='#12b385')
    bt7 = Button(root,text='7', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(7, 6, 0), activebackground='#12b385')
    bt8 = Button(root,text='8', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(8, 6, 1), activebackground='#12b385')
    bt9 = Button(root,text='9', height=10,fg='#1af0b7', width=20, bd=0.5, relief='ridge', bg='#222626', command=lambda: press(9, 6, 2), activebackground='#12b385')

    bt1.configure(font=fontb)
    bt2.configure(font=fontb)
    bt3.configure(font=fontb)
    bt4.configure(font=fontb)
    bt5.configure(font=fontb)
    bt6.configure(font=fontb)
    bt7.configure(font=fontb)
    bt8.configure(font=fontb)
    bt9.configure(font=fontb)



    bt1.grid(row=4,column=0,padx=(50,0))
    bt2.grid(row=4,column=1)
    bt3.grid(row=4,column=2)
    bt4.grid(row=5,column=0,padx=(50,0))
    bt5.grid(row=5,column=1)
    bt6.grid(row=5,column=2)
    bt7.grid(row=6,column=0,padx=(50,0))
    bt8.grid(row=6,column=1)
    bt9.grid(row=6,column=2)
    welcome.grid(row=0, column=0, columnspan = 9,pady=5,padx=(50,0))
    b.grid(row=1, column=0,columnspan=3,pady= 5,padx=(50,0))
    p1.grid(row=2,column=0,pady= 5,padx=(50,0))
    p2.grid(row=2,column=2,pady= 5)
    e.grid(row=8,column=2,pady=17)
    sp.grid(row=8,column=0,pady=17,padx=(50,0))
    c.grid(row=9,column= 0,columnspan=3,pady=(15,0),padx=(50,0))


def press(num, r, c):
    global click, count
    if click == True:
        lp = Label(root, image=xp, bg='#222626')
        if c == 0:
            lp.grid(row=r, column=c, padx=(50, 0))
        else:
            lp.grid(row=r, column=c)
        for i in range(3):
            for j in range(3):
                if num == tic_toc[i][j]:
                    tic_toc[i][j] = 'X'
        count += 1
        click = False
        checkWin('X')
    else:
        lp = Label(root, image=op, bg='#222626')
        if c == 0:
            lp.grid(row=r, column=c, padx=(50, 0))
        else:
            lp.grid(row=r, column=c)
        for i in range(3):
            for j in range(3):
                if num == tic_toc[i][j]:
                    tic_toc[i][j] = 'O'
        count += 1
        click = True
        checkWin('O')


def checkWin(o):
    global count, click, ps1, ps2
    for i in range(3):
        e = s = q = r = 0
        for j in range(3):
            if tic_toc[i][j] == o:
                r += 1
            if tic_toc[j][i] == o:
                q += 1
            if tic_toc[i][i] == o:
                s += 1
            if tic_toc[i][2 - i] == o:
                e += 1

        if r == 3 or q == 3 or (tic_toc[0][0] == o and tic_toc[1][1] == o and tic_toc[2][2] == o) or (
                tic_toc[0][2] == o and tic_toc[1][1] == o and tic_toc[2][0] == o):
            tkinter.messagebox.showinfo('tic tac toe', o + " wins!!")
            if o == 'X':
                click = True
                ps1 += 1
            else:
                click = True
                ps2 += 1
            count = 0
            clear()
            play()

    if count == 9:
        tkinter.messagebox.showinfo('tic tac toe', "OOPS! Game Tie!")
        click = True
        count = 0
        clear()
        play()

play()

root.mainloop()