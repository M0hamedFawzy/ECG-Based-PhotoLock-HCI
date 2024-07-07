from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Mohamad Fawzy\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")

# window setup=============
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    1080.0,
    fill="#2C2C2C",
    outline="")

 # design components ===================
canvas.create_text(
    471.0,
    74.0,
    anchor="nw",
    text="Welcome to ECG Based Photo Lock App ",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
choose_file_btn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
choose_file_btn.place(
    x=100.0,
    y=273.0,
    width=288.0,
    height=60.38
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=630.0,
    y=280.0,
    width=860.0,
    height=50.01
)

canvas.create_text(
    630.0,
    240.0,
    anchor="nw",
    text="File Path",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 25 * -1)
)

canvas.create_text(
    100.0,
    420.0,
    anchor="nw",
    text="Electrodes",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 30 * -1)
)

canvas.create_text(
    630.0,
    385.0,
    anchor="nw",
    text="i",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)

canvas.create_text(
    690.0,
    385.0,
    anchor="nw",
    text="ii",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    750.0,
    385.0,
    anchor="nw",
    text="iii",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    810.0,
    385.0,
    anchor="nw",
    text="avr",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    870.0,
    385.0,
    anchor="nw",
    text="avf",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    930.0,
    385.0,
    anchor="nw",
    text="avl",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    990.0,
    385.0,
    anchor="nw",
    text="v1",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1050.0,
    385.0,
    anchor="nw",
    text="v2",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1110.0,
    385.0,
    anchor="nw",
    text="v3",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1170.0,
    385.0,
    anchor="nw",
    text="v4",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1230.0,
    385.0,
    anchor="nw",
    text="v5",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1290.0,
    385.0,
    anchor="nw",
    text="v6",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1350.0,
    385.0,
    anchor="nw",
    text="vx",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1410.0,
    385.0,
    anchor="nw",
    text="vy",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)


canvas.create_text(
    1470.0,
    385.0,
    anchor="nw",
    text="vz",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)

#===================================================
button_image = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_image_hover = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

i_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
i_btn.place(
    x=625.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def i_btn_hover(e):
    i_btn.config(
        image=button_image_hover
    )
def i_btn_leave(e):
    i_btn.config(
        image=button_image
    )

i_btn.bind('<Enter>', i_btn_hover)
i_btn.bind('<Leave>', i_btn_leave)


ii_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
ii_btn.place(
    x=685.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def ii_btn_hover(e):
    ii_btn.config(
        image=button_image_hover
    )
def ii_btn_leave(e):
    ii_btn.config(
        image=button_image
    )

ii_btn.bind('<Enter>', ii_btn_hover)
ii_btn.bind('<Leave>', ii_btn_leave)



iii_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
iii_btn.place(
    x=745.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def iii_btn_hover(e):
    iii_btn.config(
        image=button_image_hover
    )
def iii_btn_leave(e):
    iii_btn.config(
        image=button_image
    )

iii_btn.bind('<Enter>', iii_btn_hover)
iii_btn.bind('<Leave>', iii_btn_leave)



avr_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
avr_btn.place(
    x=805.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def avr_btn_hover(e):
    avr_btn.config(
        image=button_image_hover
    )
def avr_btn_leave(e):
    avr_btn.config(
        image=button_image
    )

avr_btn.bind('<Enter>', avr_btn_hover)
avr_btn.bind('<Leave>', avr_btn_leave)




avf_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
avf_btn.place(
    x=865.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def avf_btn_hover(e):
    avf_btn.config(
        image=button_image_hover
    )
def avf_btn_leave(e):
    avf_btn.config(
        image=button_image
    )

avf_btn.bind('<Enter>', avf_btn_hover)
avf_btn.bind('<Leave>', avf_btn_leave)





avl_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
avl_btn.place(
    x=925.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def avl_btn_hover(e):
    avl_btn.config(
        image=button_image_hover
    )
def avl_btn_leave(e):
    avl_btn.config(
        image=button_image
    )

avl_btn.bind('<Enter>', avl_btn_hover)
avl_btn.bind('<Leave>', avl_btn_leave)



v1_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
v1_btn.place(
    x=985.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def v1_btn_hover(e):
    v1_btn.config(
        image=button_image_hover
    )
def v1_btn_leave(e):
    v1_btn.config(
        image=button_image
    )

v1_btn.bind('<Enter>', v1_btn_hover)
v1_btn.bind('<Leave>', v1_btn_leave)




v2_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
v2_btn.place(
    x=1045.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def v2_btn_hover(e):
    v2_btn.config(
        image=button_image_hover
    )
def v2_btn_leave(e):
    v2_btn.config(
        image=button_image
    )

v2_btn.bind('<Enter>', v2_btn_hover)
v2_btn.bind('<Leave>', v2_btn_leave)




v3_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
v3_btn.place(
    x=1105.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def v3_btn_hover(e):
    v3_btn.config(
        image=button_image_hover
    )
def v3_btn_leave(e):
    v3_btn.config(
        image=button_image
    )

v3_btn.bind('<Enter>', v3_btn_hover)
v3_btn.bind('<Leave>', v3_btn_leave)





v4_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
v4_btn.place(
    x=1165.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def v4_btn_hover(e):
    v4_btn.config(
        image=button_image_hover
    )
def v4_btn_leave(e):
    v4_btn.config(
        image=button_image
    )

v4_btn.bind('<Enter>', v4_btn_hover)
v4_btn.bind('<Leave>', v4_btn_leave)





v5_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
v5_btn.place(
    x=1225.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def v5_btn_hover(e):
    v5_btn.config(
        image=button_image_hover
    )
def v5_btn_leave(e):
    v5_btn.config(
        image=button_image
    )

v5_btn.bind('<Enter>', v5_btn_hover)
v5_btn.bind('<Leave>', v5_btn_leave)




v6_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
v6_btn.place(
    x=1285.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def v6_btn_hover(e):
    v6_btn.config(
        image=button_image_hover
    )
def v6_btn_leave(e):
    v6_btn.config(
        image=button_image
    )

v6_btn.bind('<Enter>', v6_btn_hover)
v6_btn.bind('<Leave>', v6_btn_leave)



vx_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
vx_btn.place(
    x=1345.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def vx_btn_hover(e):
    vx_btn.config(
        image=button_image_hover
    )
def vx_btn_leave(e):
    vx_btn.config(
        image=button_image
    )

vx_btn.bind('<Enter>', vx_btn_hover)
vx_btn.bind('<Leave>', vx_btn_leave)



vy_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
vy_btn.place(
    x=1406.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def vy_btn_hover(e):
    vy_btn.config(
        image=button_image_hover
    )
def vy_btn_leave(e):
    vy_btn.config(
        image=button_image
    )

vy_btn.bind('<Enter>', vy_btn_hover)
vy_btn.bind('<Leave>', vy_btn_leave)





vz_btn = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
vz_btn.place(
    x=1465.0,
    y=450.0,
    width=24.0,
    height=24.0
)

def vz_btn_hover(e):
    vz_btn.config(
        image=button_image_hover
    )
def vz_btn_leave(e):
    vz_btn.config(
        image=button_image
    )

vz_btn.bind('<Enter>', vz_btn_hover)
vz_btn.bind('<Leave>', vz_btn_leave)


#==========================================
canvas.create_text(
    100.0,
    530.0,
    anchor="nw",
    text="Feature Extraction",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 30 * -1)
)
#============================================
bigbutton_image = PhotoImage(
    file=relative_to_assets("button_17.png"))

bigbutton_image_hover = PhotoImage(
    file=relative_to_assets("button_hover_17.png"))


canvas.create_text(
    600.0,
    510.0,
    anchor="nw",
    text="AC/DCT",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)

canvas.create_text(
    850.0,
    510.0,
    anchor="nw",
    text="Wavelet-Coeffecients",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)

ac_btn = Button(
    image=bigbutton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
ac_btn.place(
    x=625.0,
    y=550.0,
    width=33.0,
    height=33.0
)

def ac_btn_hover(e):
    ac_btn.config(
        image=bigbutton_image_hover
    )
def ac_btn_leave(e):
    ac_btn.config(
        image=bigbutton_image
    )

ac_btn.bind('<Enter>', ac_btn_hover)
ac_btn.bind('<Leave>', ac_btn_leave)





w_btn = Button(
    image=bigbutton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
w_btn.place(
    x=935.0,
    y=550.0,
    width=33.0,
    height=33.0
)

def w_btn_hover(e):
    w_btn.config(
        image=bigbutton_image_hover
    )
def w_btn_leave(e):
    w_btn.config(
        image=bigbutton_image
    )

w_btn.bind('<Enter>', w_btn_hover)
w_btn.bind('<Leave>', w_btn_leave)

# ================================================
canvas.create_text(
    100.0,
    630.0,
    anchor="nw",
    text="Classifier",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 30 * -1)
)
# ================================================
canvas.create_text(
    615.0,
    610.0,
    anchor="nw",
    text="SVM",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)

canvas.create_text(
    865.0,
    610.0,
    anchor="nw",
    text="Random Forest",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)

canvas.create_text(
    1140.0,
    610.0,
    anchor="nw",
        text="Sequential Model",
    fill="#FFFFFF",
    font=("SegoeUI Semibold", 22 * -1)
)



svm_btn = Button(
    image=bigbutton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
svm_btn.place(
    x=625.0,
    y=650.0,
    width=33.0,
    height=33.0
)

def svm_btn_hover(e):
    svm_btn.config(
        image=bigbutton_image_hover
    )
def svm_btn_leave(e):
    svm_btn.config(
        image=bigbutton_image
    )

svm_btn.bind('<Enter>', svm_btn_hover)
svm_btn.bind('<Leave>', svm_btn_leave)


rf_btn = Button(
    image=bigbutton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
rf_btn.place(
    x=935.0,
    y=650.0,
    width=33.0,
    height=33.0
)

def rf_btn_hover(e):
    rf_btn.config(
        image=bigbutton_image_hover
    )
def rf_btn_leave(e):
    rf_btn.config(
        image=bigbutton_image
    )

rf_btn.bind('<Enter>', rf_btn_hover)
rf_btn.bind('<Leave>', rf_btn_leave)





seq_btn = Button(
    image=bigbutton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
seq_btn.place(
    x=1210.0,
    y=650.0,
    width=33.0,
    height=33.0
)

def seq_btn_hover(e):
    seq_btn.config(
        image=bigbutton_image_hover
    )
def seq_btn_leave(e):
    seq_btn.config(
        image=bigbutton_image
    )

seq_btn.bind('<Enter>', seq_btn_hover)
seq_btn.bind('<Leave>', seq_btn_leave)

# ===================================================
proceed_btn_image = PhotoImage(
    file=relative_to_assets("button_22.png"))

proceed_btn_image_hover = PhotoImage(
    file=relative_to_assets("button_hover_21.png"))


proceed_btn = Button(
    image=proceed_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
proceed_btn.place(
    x=590.0,
    y=715.0,
    width=281.0,
    height=58.91
)

def proceed_btn_hover(e):
    proceed_btn.config(
        image=proceed_btn_image_hover
    )
def proceed_btn_leave(e):
    proceed_btn.config(
        image=proceed_btn_image
    )

proceed_btn.bind('<Enter>', proceed_btn_hover)
proceed_btn.bind('<Leave>', proceed_btn_leave)

# window display
window.resizable(True, True)
window.mainloop()