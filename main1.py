import tkinter as tk
# importing the util file
import util
import cv2
from PIL import ImageTk,Image
import os

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
        self._label

    def login(self):
        pass
    
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

        self.db_dir = './db'

        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        roll_number = self.entry_roll_number_register_new_user.get(1.0,"end-1c")
        username = self.entry_username_register_new_user.get(1.0,"end-1c")
        print(roll_number)
        print(username)
        # cv2.imwrite(os.path.join(self.db_dir),f'{roll_number+"_"+username}.jpg',self.register_new_user_capture)
        cv2.imwrite(os.path.join(self.db_dir),'{}.jpg'.format(roll_number+"_"+username),self.register_new_user_capture)

    def add_img_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arc.copy()

if __name__ == "__main__":
    app = App()
    app.start()