from tkinter import *
from tkinter.colorchooser import *

class Paint(object):
    
    #sets default pen options
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    
    def __init__(self):
        
        #some basic gui setting
        self.root = Tk()

        self.width = 200
        self.height = 200
        #self.white = (255, 255, 255)

        self.root.title("Some Drawing U Kno")
        
        self.pen_button = Button(self.root, text='PEN', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='BRUSH', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='COLOR', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.choose_size_button = Scale(self.root, from_=1, to=100, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.bgcolorButton = Button(self.root, text = 'BG COLOR', command=self.background_color)
        self.bgcolorButton.grid(row=0, column=5)

        self.clear_button = Button(self.root,text = "CLEAR", command=self.clearbutton)
        self.clear_button.grid(row=0, column=7)
      

        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.grid(row=2, columnspan=8, sticky="nsew")

        #for moving canvas
        '''
        self.xsb = Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.ysb = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(5,5,1000,1000))

        self.ysb.grid(row=2, column=0, sticky="ns")
        self.xsb.grid(rowspan=3, columnspan=8, sticky="ew")
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)
        '''
        self.setup()
        self.root.mainloop()

    def clearbutton(self):
        #clears the canvas
        self.canvas.delete(ALL)

    def setup(self):
        
        #setup for the canvas
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
        #this is used for scrolling the canvas but ig it's not necessary
'''        
    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
'''        

    def use_pen(self):
        #for pen button
        self.activate_button(self.pen_button)

    def use_brush(self):
        #for brush button
        self.activate_button(self.brush_button)

    def choose_color(self):
        #for pen/brush color
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def background_color(self):
        #for bg color
        color = askcolor()[1]
        self.canvas['bg'] = color
        
def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode
        
    def paint(self, event):
        
        self.line_width = self.choose_size_button.get()
        #paint_color = 'white' if self.eraser_on else self.color
        
        #for drawing
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill='black',
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
