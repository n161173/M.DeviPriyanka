from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algorithm VisualiZer')
root.maxsize(900,600)
root.config(bg="black")
root.iconbitmap('C:/Users/priyanka/Downloads/Awicons-Vista-Artistic-Chart.ico')

#variables
selected_alg = StringVar()
data = []

#plotting rectangles
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]),fill="white",font="Times 20 italic bold")
    
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for i in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))]) 

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])


#frame 
UI_frame = Frame(root, width= 700, height=800, bg='lemon chiffon')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=900, height=900, bg='black')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ",bg="lemon chiffon",font=('bold',20),fg="black").grid(row=0, column=0, padx=0, pady=0,sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]",bg="hot pink")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Size",bg="cyan")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value",bg="cyan")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value",bg="cyan")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='green').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()

