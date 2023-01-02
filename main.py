import tkinter as tk
# importing the util file
import util
import cv2
from PIL import ImageTk,Image
from test import test

import os
import subprocess
import datetime

# creating a class
class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x500+80+100")

        self.login_button_main_window = util.get_button(self.main_window,'login','green',self.login)
        self.login_button_main_window.place(x=750,y=300)

        self.register_new_user_button_main_window = util.get_button(self.main_window,'register new user','gray',self.register_new_user,fg='black')
        self.register_new_user_button_main_window.place(x=750,y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10,y=0,width=700,height=500)
        self.db_dir = './db'
        self.add_webcam(self.webcam_label)

    def add_webcam(self,label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
        
        self._label = label
        self.process_webcam()
        
    def process_webcam(self):
        ret,frame = self.cap.read()
        self.most_recent_capture_arc = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arc,cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        self._label.after(20,self.process_webcam)

    def login(self):

        labels = test(
            image=self.most_recent_capture_arc,
            model_dir='C:/face/resources/anti_spoof_models',
            device_id=0
        )

        unknown_img_path = './tmp.jpg'
        
        cv2.imwrite(unknown_img_path,self.most_recent_capture_arc)
        output = str(subprocess.check_output(['face_recognition',self.db_dir,unknown_img_path]))

        # the following lines are used to split the lines
        my_id = output.split(',')[1][:-5]

        if labels == 1:

            if my_id in ['unknown_person','no_persons_found']:
                util.msg_box('error','unknow user.Please register or try again')
            else:
                name = my_id.split('_')[1]
                util.msg_box('success','your attendance has been registered')
                self.log_path = './log.txt'
                with open(self.log_path,'a') as f:
                    f.write(f'{name},{datetime.datetime.now()}\n')
                    f.close()
        else:
                util.msg_box('error','dont spoof the system')
                
        # os.remove(unknown_img_path)
    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry('1200x500+80+100')

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window,'Accept','green',self.accept_register_new_user,fg='black')
        self.accept_button_register_new_user_window.place(x=750,y=350)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window,'Reject','red',self.try_again_register_new_user,fg='black')
        self.try_again_button_register_new_user_window.place(x=750,y=430)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=0,y=0,width=750,height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_username_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_username_register_new_user.place(x=750,y=260)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,'username')
        self.text_label_register_new_user.place(x=750,y=210)


        self.entry_roll_number_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_roll_number_register_new_user.place(x=750,y=140)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,'roll number')
        self.text_label_register_new_user.place(x=750,y=90)

        # self.db_dir = './db'

        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        roll_number = self.entry_roll_number_register_new_user.get(1.0,"end-1c")
        username = self.entry_username_register_new_user.get(1.0,"end-1c")
        # cv2.imwrite(os.path.join(self.db_dir),f'{roll_number+"_"+username}.jpg',self.register_new_user_capture)
        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(roll_number+"_"+username)), self.register_new_user_capture)
        # image = cv2.imread(os.path.join(self.db_dir, '{}.jpg'.format(roll_number+"_"+username)))
        # h,w,c = image.shape
        # w = int((h * 3)/4)
        # h = int(h)

        # image = cv2.resize(image,(w,h))
        # cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(roll_number+"_"+username)),image)
        util.msg_box("success",username + "User registration was successful")
        self.register_new_user_window.destroy()

    def add_img_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arc.copy()

if __name__ == "__main__":
    app = App()
    app.start()