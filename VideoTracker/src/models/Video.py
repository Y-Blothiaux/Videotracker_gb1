from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from matplotlib import pyplot as plt
import PIL.Image, PIL.ImageTk
import cv2

class Video:

    def __init__(self, window ,window_title):
        self.window = window
        self.window.title("Video Tracker")
        self.canvas = Canvas(window)
        self.canvas.config(width=0,height=0)
        self.canvas.pack()
        self.delay = 30   # ms
        self.pause = True
        self.frames = []
        self.current_frame_index = 0
        self.click_positions = []
    
    
    def open_file(self):
        self.pause = True
        self.filename = filedialog.askopenfilename(initialdir = "../resources/videos",title = "Select a File",filetypes = (("Vidéo","*.mp4*"),("all files","*.*")))
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)
        self.initialize_frames()


    def initialize_frames(self):
        self.frames = []
        self.canvas.bind('<Button-1>', self.save_click_position)  # Bind left click event to the canvas
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.frames.append(frame)
        self.cap.release()
        self.current_frame_index = 0
        self.click_positions = [None] * len(self.frames)  # Initialize click_positions with None values





    def get_frame(self):
        if self.current_frame_index >= len(self.frames):
            return None
        frame = self.frames[self.current_frame_index]
        self.current_frame_index += 1
        return (True, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


    def play_video(self):
        frame_info = self.get_frame()
        if frame_info is not None:
            ret, frame = frame_info
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
                self.display_click_positions()
        if not self.pause:
            if frame_info is not None:
                self.window.after(self.delay, self.play_video)
        else:
            self.last_saved_frame_index = -1  # Reset last_saved_frame_index when paused


            

    def image_forward(self):
        self.pause = True
        self.current_frame_index += 1
        if self.current_frame_index >= len(self.frames):
            self.current_frame_index = len(self.frames) - 1
        frame = self.frames[self.current_frame_index]
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        self.display_click_positions()

    def image_backward(self):
        self.pause = True
        self.current_frame_index -= 1
        if self.current_frame_index < 0:
            self.current_frame_index = 0
        frame = self.frames[self.current_frame_index]
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        self.display_click_positions()
    

    def show_frame(self, frame):
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.display_click_positions()

    def first_frame(self):
        self.pause = True
        self.current_frame_index = 0
        frame = self.frames[self.current_frame_index]
        self.show_frame(frame)

    def last_frame(self):
        self.pause = True
        self.current_frame_index = len(self.frames) - 1
        frame = self.frames[self.current_frame_index]
        self.show_frame(frame)

    def save_click_position(self, event):
        x = event.x
        y = event.y
        self.click_positions[self.current_frame_index] = (x, y)
        self.image_forward()
        print(self.click_positions)
        


    def display_click_positions(self):
        for frame_index, position in enumerate(self.click_positions):
            if position is not None:
                x, y = position
                if frame_index == self.current_frame_index:
                    self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline='red', width=2)

    def display_values_xy(self):
        data = []
        for elt in self.click_positions:
            if elt is not None:
                data.append([elt[0],elt[1]])
        fig,ax=plt.subplots()
        column_labels=["Column 1", "Column 2"]
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=data,colLabels=column_labels,loc="center")
        plt.show()

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()