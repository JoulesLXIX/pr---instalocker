import tkinter                                                       # IMPORTS
from tkinter import *
import pyautogui
import pydirectinput
import os
from threading import *
import time
from PIL import Image, ImageTk
pyautogui.FAILSAFE = False

window = tkinter.Tk()                                          # SCREEN SETTINGS
root = tkinter.Toplevel(window, cursor = ' crosshair')
root.overrideredirect(True)
root.title('Instalocker for toxic players')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - 600 / 2)
center_y = int(screen_height/2 - 200 / 2)
root.geometry(f'{600}x{900}+{center_x}+{center_y - 400}')
root.iconbitmap(os.path.abspath('icon1.ico'))
window.iconify()

def on_closing():
    global stop1
    stop1 = 1
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)

def info():
    print('?')
global min
min = 0
def check():
    global min
    if min==1 or min==2 or min==3:
        min += 1
        #print('added')
        if min == 4:
            #print('root overriding')
            root.overrideredirect(True)
            min = 0
def minim():
    global min
    #print('root un-overriding----------------------------')
    root.overrideredirect(False)
    #print('root iconing')
    root.iconify()
    #print('window overriding')
    window.overrideredirect(True)
    min = 1
def close():
    window.destroy()
stop_1 = 0
def drawleft():
    global stop_1
    if stop_1 == 0:
        stop_1 = 1
        c_main.itemconfig(l_left, state='hidden')
        c_main.itemconfig(l_right, state='hidden')
        c_main.coords(l_left, 140,90,160,90)
        c_main.itemconfig(l_left, state='normal')
        for i in range(11):
            length = i * 10
            c_main.coords(l_left, 150 - length,90,150 + length,90)
            #c_main.itemconfig(l_left, state='normal')
            time.sleep(0.01)
    stop_1 = 0
def drawright():
    global stop_1
    if stop_1 == 0:
        stop_1 = 1
        c_main.itemconfig(l_left, state='hidden')
        c_main.itemconfig(l_right, state='hidden')
        c_main.coords(l_right, 438.5,90,461.5,90)
        c_main.itemconfig(l_right, state='normal')
        for i in range(11):
            length = i * 11.5
            c_main.coords(l_right, 450 - length,90,450 + length,90)
            #c_main.itemconfig(l_right, state='normal')
            time.sleep(0.01)
    stop_1 = 0
def thread_dr():
    #print('Entered')
    thread  = Thread(target = drawright)
    thread.start()
def thread_dl():
    #print('Entered')
    thread  = Thread(target = drawleft)
    thread.start()
def trileft():
    c_main.itemconfig(l_right2, state='hidden')
    c_main.itemconfig(l_left, state='hidden')
    c_main.itemconfig(left_tri, state='hidden')
    c_main.itemconfig(right_tri, state='hidden')
    time.sleep(0.05)
    c_main.itemconfig(left_tri, state='normal')
    drawleft()

    #time.sleep(0.1)
    c_main.itemconfig(l_left2, state='normal')
def triright():
    c_main.itemconfig(l_left2, state='hidden')
    c_main.itemconfig(l_right, state='hidden')
    c_main.itemconfig(left_tri, state='hidden')
    c_main.itemconfig(right_tri, state='hidden')
    time.sleep(0.1)
    c_main.itemconfig(right_tri, state='normal')
    drawright()

    #time.sleep(0.1)
    c_main.itemconfig(l_right2, state='normal')
def thread_tr():
    thread  = Thread(target = triright)
    thread.start()
def thread_tl():
    thread  = Thread(target = trileft)
    thread.start()
def delete_l():
    #print('Left')
    time.sleep(0.11)
    c_main.itemconfig(l_left, state='hidden')
def delete_r():
    #print('Left')
    time.sleep(0.11)
    c_main.itemconfig(l_right, state='hidden')
def thread_delr():
    thread  = Thread(target = delete_r)
    thread.start()
def thread_dell():
    thread  = Thread(target = delete_l)
    thread.start()
def raise_frame2():
    canvas2.place_forget()
    canvas1.place(x = 0, y = 150)
    thread_tl()
def raise_frame1():
    canvas1.place_forget()
    canvas2.place(x = 0, y = 150)
    thread_tr()
def threadit3(dir):
    thread  = Thread(target = change, args = (dir))
    thread.start()
def change(dir,loc):
    global canvas1
    incr = 200
    total = dir*incr
    for t in range(1,7):
        total = total / 2
        canvas1.move(b_astra,0 ,total)
        canvas1.move(b_breach,0 ,total)
        canvas1.move(b_brimstone,0 ,total)
        canvas1.move(b_chamber,0 ,total)
        canvas1.move(b_cypher,0 ,total)
        canvas1.move(b_fade,0 ,total)
        canvas1.move(b_harbor,0 ,total)
        canvas1.move(b_jett,0 ,total)
        canvas1.move(b_kayo,0 ,total)
        canvas1.move(b_killjoy,0 ,total)
        canvas1.move(b_neon,0 ,total)
        canvas1.move(b_omen,0 ,total)
        canvas1.move(b_phoenix,0 ,total)
        canvas1.move(b_raze,0 ,total)
        canvas1.move(b_reyna,0 ,total)
        canvas1.move(b_sage,0 ,total)
        canvas1.move(b_skye,0 ,total)
        canvas1.move(b_sova,0 ,total)
        canvas1.move(b_viper,0 ,total)
        canvas1.move(b_yoru,0 ,total)
        time.sleep(0.01)
count = 0
def mouse_wheel(event):
    global count
    loc = count
    dir = 1
    if event.num == 5 or event.delta == -120:
        count -= 1
        dir = -1
    if event.num == 4 or event.delta == 120:
        count += 1
        dir = 1
    threadit3([dir,loc])
def jk():
    pass
def selected(agent):
    print(agent[1])
    select(agent[1])
    threadit([agent[0]])
def select(num):
    list1 = content_selection[8].split('-')
    if len(list1) > 40:
        list1.pop(22)
    list1[-1] = num
    list1.append('\n')
    content_selection[8] = '-'.join(list1)
    with open('agentlist.txt','w') as file:
        file.writelines(content_selection)

    list2 = content_selection[8].split('-')
    list2.pop(-1)
    list2.reverse()
    coord_order = []
    for n in list2:
        n = int(n)
        if n not in coord_order:
            coord_order.append(n)
    agent_coords = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    rank = 0
    for agentno in coord_order:
        agent_coords[agentno] = coords[rank]
        rank+=1
    canvas1.coords(b_astra, agent_coords[0][0], agent_coords[0][1])
    canvas1.coords(b_breach, agent_coords[1][0], agent_coords[1][1])
    canvas1.coords(b_brimstone, agent_coords[2][0], agent_coords[2][1])
    canvas1.coords(b_chamber, agent_coords[3][0], agent_coords[3][1])
    canvas1.coords(b_cypher, agent_coords[4][0], agent_coords[4][1])
    canvas1.coords(b_fade, agent_coords[5][0], agent_coords[5][1])
    canvas1.coords(b_harbor, agent_coords[6][0], agent_coords[6][1])
    canvas1.coords(b_jett, agent_coords[7][0], agent_coords[7][1])
    canvas1.coords(b_kayo, agent_coords[8][0], agent_coords[8][1])
    canvas1.coords(b_killjoy, agent_coords[9][0], agent_coords[9][1])
    canvas1.coords(b_neon, agent_coords[10][0], agent_coords[10][1])
    canvas1.coords(b_omen, agent_coords[11][0], agent_coords[11][1])
    canvas1.coords(b_phoenix, agent_coords[12][0], agent_coords[12][1])
    canvas1.coords(b_raze, agent_coords[13][0], agent_coords[13][1])
    canvas1.coords(b_reyna, agent_coords[14][0], agent_coords[14][1])
    canvas1.coords(b_sage, agent_coords[15][0], agent_coords[15][1])
    canvas1.coords(b_skye, agent_coords[16][0], agent_coords[16][1])
    canvas1.coords(b_sova, agent_coords[17][0], agent_coords[17][1])
    canvas1.coords(b_viper, agent_coords[18][0], agent_coords[18][1])
    canvas1.coords(b_yoru, agent_coords[19][0], agent_coords[19][1])
def threadit(agent):
    thread  = Thread(target = locate_and_click_the_target, args = (agent))
    thread.start()
def threadit2():
    thread2 = Thread(target = locate_by_map)
    thread2.start()
def locked():
    canvas1.place_forget()
    canvas2.place_forget()
    f3.place(x = 170, y = 100)
    f4.place(x = 170, y = 200)
def locked2():
    canvas2.place_forget()
    f3.place(x = 170, y = 100)
    f4.place(x = 170, y = 200)
def locate_and_click_the_target(image):
     locked()
     global stop1
     t = None
     while t == None and stop1 == 0:
         print(t)
         t = pyautogui.locateCenterOnScreen(image,grayscale = True,confidence = 0.8)
     print(t)
     if stop1 == 1:
         pass
     else:
         pydirectinput.click(t[0],t[1])
         pydirectinput.click(959,812)
     print('clicked')
     f3.place_forget()
     f4.place_forget()
     canvas1.place(x = 0, y = 150)
     stop1 = 0
def locate_by_map():
    global stop1
    locked2()
    with open('agentlist.txt','r') as file:
        data = file.readlines()
    a1 = None
    a2 = None
    a3 = None
    a4 = None
    a5 = None
    a6 = None
    a7 = None
    while a1 == None and a2 == None and a3 == None and a4 == None and a5 == None and a6 == None and a7 == None and stop1 == 0:
        print('n')
        n = 0
        a1 = pyautogui.locateCenterOnScreen('ascent.png',grayscale = True,confidence = 0.8)
        if a1 != None:
            break
        n = 1
        a2 = pyautogui.locateCenterOnScreen('bind.png',grayscale = True, confidence = 0.8)
        if a2 != None:
            break
        n = 2
        a3 = pyautogui.locateCenterOnScreen('breeze.png',grayscale = True,confidence = 0.8)
        if a3 != None:
            break
        n = 3
        a4 = pyautogui.locateCenterOnScreen('haven.png',grayscale = True,confidence = 0.8)
        if a4 != None:
            break
        n = 4
        a5 = pyautogui.locateCenterOnScreen('icebox.png',grayscale = True,confidence = 0.8)
        if a5 != None:
            break
        n = 5
        a6 = pyautogui.locateCenterOnScreen('pearl.png',grayscale = True,confidence = 0.8)
        if a6 != None:
            break
        n = 6
        a7 = pyautogui.locateCenterOnScreen('fracture.png',grayscale = True,confidence = 0.8)
        if a7 != None:
            break
    print('n', n)
    print(data[n])
    locate_and_click_the_target(data[n].replace('\n','')+'.png')
def show(lno,clickedno,no):
    with open('agentlist.txt','r') as file:
        data = file.readlines()
        data[no - 1] = clickedno.get() + '\n'
    with open('agentlist.txt','w') as file:
        file.writelines(data)
    lno.config(text = clickedno.get())
def stop():
    global stop1
    stop1 = 1
    f3.place_forget()
    f4.place_forget()
    canvas1.place(x = 0, y = 150)

###################### MAIN CANVAS ####################

p_bg = ImageTk.PhotoImage(Image.open("bgbg1.png"))       # MAIN FRAME BACKGROUND
c_main = Canvas(root, width = 600, height = 900, bd=0,highlightthickness=0)
c_main.place(x=0,y=0)
bgmain = c_main.create_image(300, 450, image = p_bg)

p_x = ImageTk.PhotoImage(Image.open("text x dull.png"))           # MAIN MENU BUTTONS
b_x = c_main.create_image(570, 20, image = p_x)
c_main.tag_bind(b_x, "<Button-1>", lambda x:window.destroy())
p_min = ImageTk.PhotoImage(Image.open("text min dull.png"))
b_min = c_main.create_image(520, 20, image = p_min)
c_main.tag_bind(b_min, "<Button-1>",  lambda x: minim())
root.bind("<Configure>", lambda x: check())
p_q = ImageTk.PhotoImage(Image.open("text q big.png"))
b_q = c_main.create_image(470, 20, image = p_q)
c_main.tag_bind(b_q, "<Button-1>",  lambda x: info())
p_all = ImageTk.PhotoImage(Image.open("text all.png"))
b_all = c_main.create_image(150, 70, image = p_all)
c_main.tag_bind(b_all, "<Button-1>", lambda x: raise_frame2())
p_map = ImageTk.PhotoImage(Image.open("text map.png"))
b_map = c_main.create_image(450, 70, image = p_map)
c_main.tag_bind(b_map, "<Button-1>", lambda x: raise_frame1())

l_left = c_main.create_line(50,70,250,70, fill='#18b4a0', width=5) # LINE ANIMATIONS
l_right = c_main.create_line(335,70,565,70, fill='#18b4a0', width=5)
drawleft()
c_main.tag_bind(b_map, "<Enter>", lambda x: thread_dr())
c_main.tag_bind(b_all, "<Enter>", lambda x: thread_dl())
c_main.tag_bind(b_map, "<Leave>", lambda x: thread_delr())
c_main.tag_bind(b_all, "<Leave>", lambda x: thread_dell())
left_tri = c_main.create_line(130,90,170,90,150,110,130,90,
                                fill='#18b4a0',
                                width=5
                                )
right_tri = c_main.create_line(430,90,470,90,450,110,430,90,
                                fill='#18b4a0',
                                width=5,
                                state='hidden'
                                )
l_left2 = c_main.create_line(50,90,250,90, fill='#18b4a0', width=5, state='hidden')
l_right2 = c_main.create_line(335,90,565,90, fill='#18b4a0', width=5, state='hidden')
trileft()
c_main.create_line(15,92,585,92, fill='#a7aeba', width=1)
c_main.create_line(15,149,585,149, fill='#a7aeba', width=1)
c_main.create_line(15,850,585,850, fill='#a7aeba', width=1)

###################### ALL AGENt CANVAS ####################

photo_astra = ImageTk.PhotoImage(Image.open( 'astra full.png'))
photo_breach = ImageTk.PhotoImage(Image.open( 'breach full.png'))
photo_sage = ImageTk.PhotoImage(Image.open( 'sage full.png'))
photo_sova = ImageTk.PhotoImage(Image.open( 'sova full.png'))
photo_omen = ImageTk.PhotoImage(Image.open( 'omen full.png'))
photo_yoru = ImageTk.PhotoImage(Image.open( 'yoru full.png'))
photo_killjoy = ImageTk.PhotoImage(Image.open( 'killjoy full.png'))
photo_raze = ImageTk.PhotoImage(Image.open( 'raze full.png'))
photo_reyna = ImageTk.PhotoImage(Image.open( 'reyna full.png'))
photo_viper = ImageTk.PhotoImage(Image.open( 'viper full.png'))
photo_harbor = ImageTk.PhotoImage(Image.open( 'harbor full.png'))
photo_jett = ImageTk.PhotoImage(Image.open( 'jett full.png'))
photo_brimstone = ImageTk.PhotoImage(Image.open( 'brimstone full.png'))
photo_chamber = ImageTk.PhotoImage(Image.open( 'chamber full.png'))
photo_cypher = ImageTk.PhotoImage(Image.open( 'cypher full.png'))
photo_fade = ImageTk.PhotoImage(Image.open( 'fade full.png'))
photo_kayo = ImageTk.PhotoImage(Image.open( 'kayo full.png'))
photo_neon = ImageTk.PhotoImage(Image.open( 'neon full.png'))
photo_phoenix = ImageTk.PhotoImage(Image.open( 'phoenix full.png'))
photo_skye = ImageTk.PhotoImage(Image.open( 'skye full.png'))

with open('agentlist.txt','r') as file:
    global content_selection
    content_selection = file.readlines()

coords = [  (120, 159),(320, 159),(500, 159),
            (120, 460),(320, 460),(500, 460),
            (120, 760),(320, 760),(500, 760),
            (120, 1060),(320, 1060),(500, 1060),
            (120, 1360),(320, 1360),(500, 1360),
            (120, 1660),(320, 1660),(500, 1660),
            (120, 1960),(320, 1960)]
list2 = content_selection[8].split('-')
list2.pop(-1)
list2.reverse()
coord_order = []
for n in list2:
    n = int(n)
    if n not in coord_order:
        coord_order.append(n)
agent_coords = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rank = 0
for agentno in coord_order:
    agent_coords[agentno] = coords[rank]
    rank+=1

canvas1 = tkinter.Canvas(root, width = 600, height = 700, bd=0, highlightthickness=0)
canvas1.place(x = 0, y = 150)
bg1 = canvas1.create_image(300, 300, image = p_bg)        # ALL FRAME BACKGROUND

b_astra =  canvas1.create_image(agent_coords[0][0], agent_coords[0][1], image = photo_astra)
b_breach =  canvas1.create_image(agent_coords[1][0], agent_coords[1][1], image = photo_breach)
b_brimstone =  canvas1.create_image(agent_coords[2][0], agent_coords[2][1], image = photo_brimstone)
b_chamber =  canvas1.create_image(agent_coords[3][0], agent_coords[3][1], image = photo_chamber)
b_cypher =  canvas1.create_image(agent_coords[4][0], agent_coords[4][1], image = photo_cypher)
b_fade =  canvas1.create_image(agent_coords[5][0], agent_coords[5][1], image = photo_fade)
b_harbor =  canvas1.create_image(agent_coords[6][0], agent_coords[6][1], image = photo_harbor)
b_jett =  canvas1.create_image(agent_coords[7][0], agent_coords[7][1], image = photo_jett)
b_kayo =  canvas1.create_image(agent_coords[8][0], agent_coords[8][1], image = photo_kayo)
b_killjoy =  canvas1.create_image(agent_coords[9][0], agent_coords[9][1], image = photo_killjoy)
b_neon =  canvas1.create_image(agent_coords[10][0], agent_coords[10][1], image = photo_neon)
b_omen =  canvas1.create_image(agent_coords[11][0], agent_coords[11][1], image = photo_omen)
b_phoenix =  canvas1.create_image(agent_coords[12][0], agent_coords[12][1], image = photo_phoenix)
b_raze =  canvas1.create_image(agent_coords[13][0], agent_coords[13][1], image = photo_raze)
b_reyna =  canvas1.create_image(agent_coords[14][0], agent_coords[14][1], image = photo_reyna)
b_sage =  canvas1.create_image(agent_coords[15][0], agent_coords[15][1], image = photo_sage)
b_skye =  canvas1.create_image(agent_coords[16][0], agent_coords[16][1], image = photo_skye)
b_sova =  canvas1.create_image(agent_coords[17][0], agent_coords[17][1], image = photo_sova)
b_viper =  canvas1.create_image(agent_coords[18][0], agent_coords[18][1], image = photo_viper)
b_yoru =  canvas1.create_image(agent_coords[19][0], agent_coords[19][1], image = photo_yoru)
canvas1.tag_bind(b_astra, "<Button-1>", lambda x:selected(['astra.png','0']))
canvas1.tag_bind(b_breach, "<Button-1>", lambda x:selected(['breach.png','1']))
canvas1.tag_bind(b_brimstone, "<Button-1>", lambda x:selected(['brimstone.png','2']))
canvas1.tag_bind(b_chamber, "<Button-1>", lambda x:selected(['chamber.png','3']))
canvas1.tag_bind(b_cypher, "<Button-1>", lambda x:selected(['cypher.png','4']))
canvas1.tag_bind(b_fade, "<Button-1>", lambda x:selected(['fade.png','5']))
canvas1.tag_bind(b_harbor, "<Button-1>", lambda x:selected(['harbor.png','6']))
canvas1.tag_bind(b_jett, "<Button-1>", lambda x:selected(['jett.png','7']))
canvas1.tag_bind(b_kayo, "<Button-1>", lambda x:selected(['kayo.png','8']))
canvas1.tag_bind(b_killjoy, "<Button-1>", lambda x:selected(['killjoy.png','9']))
canvas1.tag_bind(b_neon, "<Button-1>", lambda x:selected(['neon.png','10']))
canvas1.tag_bind(b_omen, "<Button-1>", lambda x:selected(['omen.png','1']))
canvas1.tag_bind(b_phoenix, "<Button-1>", lambda x:selected(['phoenix.png','12']))
canvas1.tag_bind(b_raze, "<Button-1>", lambda x:selected(['raze.png','13']))
canvas1.tag_bind(b_reyna, "<Button-1>", lambda x:selected(['reyna.png','14']))
canvas1.tag_bind(b_sage, "<Button-1>", lambda x:selected(['sage.png','15']))
canvas1.tag_bind(b_skye, "<Button-1>", lambda x:selected(['skye.png','16']))
canvas1.tag_bind(b_sova, "<Button-1>", lambda x:selected(['sova.png','17']))
canvas1.tag_bind(b_viper, "<Button-1>", lambda x:selected(['viper.png','18']))
canvas1.tag_bind(b_yoru, "<Button-1>", lambda x:selected(['yoru.png','19']))
root.bind("<MouseWheel>", mouse_wheel)



###################### MAP VISE AGENT CANVAS ####################


canvas2 = tkinter.Canvas(root, width = 600, height = 700, bd=0, highlightthickness=0)
canvas2.place(x = 0, y = 150)
bg2 = canvas2.create_image(300, 300, image = p_bg)
Label(canvas2, text = 'ASCENT').grid(row = 0, column = 0, pady = 20)
Label(canvas2, text = 'BIND').grid(row = 1, column = 0, pady = 20)
Label(canvas2, text = 'BREEZE').grid(row = 2, column = 0, pady = 20)
Label(canvas2, text = 'HAVEN').grid(row = 3, column = 0, pady = 20)
Label(canvas2, text = 'ICEBOX').grid(row = 4, column = 0, pady = 20)
Label(canvas2, text = 'PEARL').grid(row = 5, column = 0, pady = 20)
Label(canvas2, text = 'FRACTURE').grid(row = 6, column = 0, pady = 20)
canvas2.grid_columnconfigure(0, minsize = 100)
canvas2.grid_columnconfigure(1, minsize = 200)
canvas2.grid_columnconfigure(2, minsize = 100)
canvas2.grid_columnconfigure(3, minsize = 100)
canvas2.grid_rowconfigure(0, minsize = 100)
canvas2.grid_rowconfigure(1, minsize = 100)
canvas2.grid_rowconfigure(2, minsize = 100)
canvas2.grid_rowconfigure(3, minsize = 100)
canvas2.grid_rowconfigure(4, minsize = 100)
canvas2.grid_rowconfigure(5, minsize = 100)
canvas2.grid_rowconfigure(6, minsize = 100)
options = [ "sage","jett","chamber","neon",
            "reyna","viper","raze","breach",
            "cypher","brimstone","sova","skye",
            "killjoy","omen","yoru","astra",
            "kayo","sova","phoenix","fade",
            "harbor"
            ]
file1 = open('agentlist.txt', 'r+')
content = file1.readlines()
clicked1 = StringVar()
clicked1.set((content[0]).replace('/n',''))
OptionMenu(canvas2, clicked1, *options).grid(row = 0, column = 1, pady = 20, padx = 20)
Button(canvas2 , bg = '#3A7EB8', text = "set" , command = lambda: show(l1,clicked1,1) ).grid(row = 0, column = 2, pady = 20, padx = 20)
l1 = Label(canvas2 , text = clicked1.get())
l1.grid(row = 0, column = 3, pady = 20, padx = 20)
clicked2 = StringVar()
clicked2.set((content[1]).replace('/n',''))
OptionMenu(canvas2, clicked2, *options).grid(row = 1, column = 1, pady = 20, padx = 20)
Button(canvas2 , text = "set" , command = lambda: show(l2,clicked2,2) ).grid(row = 1, column = 2, pady = 20, padx = 20)
l2 = Label(canvas2 , text = clicked2.get())
l2.grid(row = 1, column = 3, pady = 20, padx = 20)
clicked3 = StringVar()
clicked3.set((content[2]).replace('/n',''))
OptionMenu(canvas2, clicked3, *options).grid(row = 2, column = 1, pady = 20, padx = 20)
Button(canvas2 , text = "set" , command = lambda: show(l3,clicked3,3) ).grid(row = 2, column = 2, pady = 20, padx = 20)
l3 = Label(canvas2 , text = clicked3.get())
l3.grid(row = 2, column = 3, pady = 20, padx = 20)
clicked4 = StringVar()
clicked4.set((content[3]).replace('/n',''))
OptionMenu(canvas2, clicked4, *options).grid(row = 3, column = 1, pady = 20, padx = 20)
Button(canvas2 , text = "set" , command = lambda: show(l4,clicked4,4) ).grid(row = 3, column = 2, pady = 20, padx = 20)
l4 = Label(canvas2 , text = clicked4.get())
l4.grid(row = 3, column = 3, pady = 20, padx = 20)
clicked5 = StringVar()
clicked5.set((content[4]).replace('/n',''))
OptionMenu(canvas2, clicked5, *options).grid(row = 4, column = 1, pady = 20, padx = 20)
Button(canvas2 , text = "set" , command = lambda: show(l5,clicked5,5) ).grid(row = 4, column = 2, pady = 20, padx = 20)
l5 = Label(canvas2 , text = clicked5.get())
l5.grid(row = 4, column = 3, pady = 20, padx = 20)
clicked6 = StringVar()
clicked6.set((content[5]).replace('/n',''))
OptionMenu(canvas2, clicked6, *options).grid(row = 5, column = 1, pady = 20, padx = 20)
Button(canvas2 , text = "set" , command = lambda: show(l6,clicked6,6) ).grid(row = 5, column = 2, pady = 20, padx = 20)
l6 = Label(canvas2 , text = clicked6.get())
l6.grid(row = 5, column = 3, pady = 20, padx = 20)
clicked7 = StringVar()
clicked7.set((content[6]).replace('/n',''))
OptionMenu(canvas2, clicked7, *options).grid(row = 6, column = 1, pady = 20, padx = 20)
Button(canvas2 , text = "set" , command = lambda: show(l7,clicked7,7) ).grid(row = 6, column = 2, pady = 20, padx = 20)
l7 = Label(canvas2 , text = clicked7.get())
l7.grid(row = 6, column = 3, pady = 20, padx = 20)
button_start = tkinter.Button(  canvas2,
                                text = 'START',
                                relief = 'solid',
                                activeforeground = 'red',
                                activebackground = 'red',
                                command=lambda:threadit2()
                                ).grid(row = 7, columnspan = 4, padx = 20, pady = 20)

   ###################### STOP CANVAS ####################

f3 = Frame(root)
Label(f3, text = ' SELECTED AGENT WILL BE INSTALOCKED ').pack()
Label(f3, text = 'AS SOON AS THE MATCH STARTES').pack()

f4 = Frame(root)
global stop1
stop1 = 0
button_stop = tkinter.Button(
                            f4,
                            text = 'STOP AND SELECT AGAIN',
                            relief = 'solid',
                            activeforeground = 'red',
                            activebackground = 'red',
                            command=lambda:stop()
                            ).pack()
raise_frame2()
mainloop()
