import kivy.uix.button as kb
import kivy.uix.textinput as kb2
import kivy.uix.popup as kb3
import kivy.uix.label as kb4
from kivy.app import App
from kivy.uix.widget import Widget
import os
from kivy.core.window import Window
import tkinter as tk
import tkinter.filedialog
import tkinter
import kivy.clock as clock
Window.size = (300, 300)
folder = "N"
popup1 = None
popup2 = None

class Button_Widget(Widget):

    def __init__(self, **kwargs):
        super(Button_Widget, self).__init__(**kwargs)
        btn1 = kb.Button(text='Sort By\nExtension', pos=(200, 100))
        btn1.bind(on_release=self.extension)
        self.add_widget(btn1)
        btn2 = kb.Button(text='Sort By\nDay', pos=(0, 100))
        btn2.bind(on_release=self.sortDay)
        self.add_widget(btn2)
        btn3 = kb.Button(text='Sort By\nMonth', pos=(100, 0))
        btn3.bind(on_release=self.sortMonth)
        self.add_widget(btn3)
        btn4 = kb.Button(text='Sort By\nYear', pos=(0, 0))
        btn4.bind(on_release=self.sortYear)
        self.add_widget(btn4)
        btn5 = kb.Button(text='Sort By\nAscending', pos=(100, 200))
        btn5.bind(on_release=self.sortAsc)
        self.add_widget(btn5)
        btn6 = kb.Button(text='Backup', pos=(200, 0))
        btn6.bind(on_release=self.backup)
        self.add_widget(btn6)
        btn7 = kb.Button(text='Extract', pos=(0, 200))
        btn7.bind(on_release=self.extract)
        self.add_widget(btn7)
        btn8 = kb.Button(text='Select\nFolder\n(Do First)', pos=(100, 100), color=[0.92, 0.8, 0.75, 1])
        btn8.bind(on_release=self.browse)
        self.add_widget(btn8)
        self.txt = kb2.TextInput(hint_text='Enter\nPrecision\nValue\n(Integer)', multiline=False, pos=(200, 200))
        self.add_widget(self.txt)
        global popup1
        global popup2
        popup1 = kb3.Popup(title='ERROR', content=kb4.Label(text='Please Enter the\nPrecision Value for\nSort by Ascending'),
                      auto_dismiss=False)
        popup2 = kb3.Popup(title='ERROR', content=kb4.Label(text='Please Select a File'),
                          auto_dismiss=False)

    def extension(self, instance):
        if (folder == "N"):
            popup2.open()
            clock.Clock.schedule_once(popup2.dismiss, 5)
        else:
            os.system("python dcmd.py " + folder + " -e")

    def sortDay(self, instance):
        if (folder == "N"):
            popup2.open()
            clock.Clock.schedule_once(popup2.dismiss, 5)
        else:
            os.system("python dcmd.py " + folder + " -d D")
    def sortMonth(self, instance):
        if (folder == "N"):
            popup2.open()
            clock.Clock.schedule_once(popup2.dismiss, 5)
        else:
            os.system("python dcmd.py " + folder + " -d M")
    def sortYear(self, instance):
        if (folder == "N"):
            popup2.open()
            clock.Clock.schedule_once(popup2.dismiss, 5)
        else:
            os.system("python dcmd.py " + folder + " -d Y")

    def backup(self, instance):
        if (folder == "N"):
            popup2.open()
            clock.Clock.schedule_once(popup2.dismiss, 5)
        else:
            os.system("python dcmd.py " + folder + " -b")
    def extract(self, instance):
        if (folder == "N"):
            popup2.open()
            clock.Clock.schedule_once(popup2.dismiss, 5)
        else:
            os.system("python dcmd.py " + folder + " -x --noswitch")

    def sortAsc(self, instance):
        if (self.txt.text == ""):
            popup1.open()
            clock.Clock.schedule_once(popup1.dismiss, 5)
        else:
            if (folder == "N"):
                popup2.open()
                clock.Clock.schedule_once(popup2.dismiss, 5)
            else:
                temp = "*"*int(self.txt.text)
                print("python dcmd.py " + folder + " -sba " + temp)
                os.system("python dcmd.py " + folder + " -sba " + temp)

    def browse(self, instance):
        # Allow user to select a directory and store it in global var
        # called folder_path
        tkinter.Tk().withdraw()
        global folder
        filename = tk.filedialog.askdirectory()
        folder = str(filename)
        print(filename)


class ButtonApp(App):

    def build(self):
        self.title = "Desktop Organizer"
        return Button_Widget()

if __name__ == "__main__":
    ButtonApp().run()
# import tkinter as tk
# import os
# import tkinter.filedialog
#
#
# var1 = 0
# folder_path = ""
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         global var1
#         self.extension = tk.Checkbutton(text="extension", variable=var1).grid(row=0, sticky=W)
#
#
#         self.browse = tk.Button(self)
#         self.browse["text"] = "Browse"
#         self.browse["command"] = self.browse_button
#         self.browse.grid(row=200, column=0, padx=(10, 50))
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Run"
#         self.hi_there["command"] = self.run
#         self.hi_there.grid(row=200, column=75, padx=(10, 50))
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.grid(row=200, column=150, padx=(10, 50))
#
#     def run(self):
#
#         os.system("ping google.com")
#
#     def browse_button(self):
#         # Allow user to select a directory and store it in global var
#         # called folder_path
#         global folder_path
#         filename = tk.filedialog.askdirectory()
#         folder_path.set(filename)
#         print(filename)
#
# root = tk.Tk()
# root.geometry("500x200")
# app = Application(master=root)
# app.mainloop()