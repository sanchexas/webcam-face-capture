from tkinter import *
import cv2 
from PIL import Image, ImageTk 
from datetime import datetime
  
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 700) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 900) 
  
app = Tk()

label_widget = Label(app)
label_widget.pack() 
  
def run_camera(): 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    _, frame = vid.read() 
    colorful_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    captured_image = Image.fromarray(colorful_image) 
    faces = face_cascade.detectMultiScale(colorful_image, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(colorful_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    captured_image = Image.fromarray(colorful_image) 
    if(len(faces) > 0): 
        now = datetime.now()
        captured_image.save(f'./photos/{now.strftime("%d-%m-%Y %H-%M-%S,%f")}.jpg', 'JPEG')
    photo_image = ImageTk.PhotoImage(image=captured_image) 
    label_widget.photo_image = photo_image 
    label_widget.configure(image=photo_image) 
    label_widget.after(100, run_camera) 
  
button1 = Button(app, text="run camera", command=run_camera) 
button1.pack() 
  
app.mainloop() 