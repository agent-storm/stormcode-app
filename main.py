
#Import OS and OS.Path module for accessing files 
import os,os.path,sys,time

#import kivy
import kivy
#import individual kivy modules
from kivy.app import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import *
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.properties import StringProperty
#import kivy MD
import kivymd
#import individual kivyMD modules
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.snackbar import Snackbar
#This is for changing the settings so that kivy doesent close when "ESC" is presses

Config.set('kivy', 'exit_on_escape', '0')
#Al; the required paths are stored in a seperate file
import Paths
#default launching size of the app
Window.size = (1400,800)
 
#Global Variables
global week_path,file_type,file_name,file_ext,code
week_path = str()
file_type = bool()
file_name = code = file_ext = ''



cwd_main = os.getcwd()
#This is a Tabbed Panel class W
class TabbedLayout(TabbedPanel):

    pass

class PdfScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    class FolderPopup2(Popup):#For choosing PDF files to download
        global pdf_path
        def PdfChoosen(self,selection):
            final_path = f'start msedge {selection[0]}'
            os.system(final_path)


# This is the main screen of the app and it contains almost all the tools
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    global data_path,pdf_path
    # This is a popup class and its used to open a file chooser in the popup window in the app 
    data_path = StringProperty(Paths.data_path)
    class FolderPopup(Popup):
        # This function determines the type of path choosen either folder or file 
        def WeekChoosen(self,selection):
            global week_path,file_type
            # If user choose a file the file chooser widget returns a list containing file path if they 
            # choose a folder (week) it returns a direct string format of the path of the folder
            # week_path contains the path of the folder/file choosen by user
            # file_type variable is a boolean value that is set to True or False depending upon the path
            if(isinstance(selection,str)):
                
                file_type = True
                week_path=(selection)
                self.add_widget
            else:
                file_type = False
                week_path=(selection[0])
            #This is a instruction for the user to load files. 
            snackbar_ = Snackbar(text = "Please hit the LOAD FILES button to load the selected files.",snackbar_x = 5)
            snackbar_.open()
            # Dismissing the Foder Chooser Popup 
            self.dismiss()
    
    
    class SavingPopup(Popup):

        def FileName(self): 
            global file_name
            file_name = self.ids.FileNameTextBox.text
            self.dismiss()
            MainScreen().FileSaver()
            
    
    def Save_Button_Pressed(self):
        global file_ext,file_name,code
        if(file_ext == ''):
            snackbar = Snackbar(text="Please choose a language to save file",snackbar_y = 5,snackbar_x = 10)
            snackbar.open()
        else:
            code = self.ids.code_box.text
            self.SavingPopup().open()

        
    def MDSlider(self,value):
        self.ids.code_box.font_size=value*2.5
    def FileSaver(self):
        global file_ext,file_name,code,temp_files_path
        final_name = file_name + file_ext
        user_files_list = os.listdir(Paths.user_files_path)
    
        if(final_name in user_files_list):
            snackbar = Snackbar(text="File with the name alreay exists, please use something else!")
            snackbar.open()
        file_path = f"{Paths.user_files_path}//{final_name}"
        
        temp_file = open(file_path, 'w')
        temp_file.write(code)
        temp_file.close()
        file_name = code = ''
        self.ids.language_spinner.text = ''

        
    # This function is used to Load the  files chosen by the user into the tabbed panel
    def WeekLoader(self):
        
        global week_path
        #We simply ignore the command if the week_path is empty
        if(week_path == ''):
            pass
        else:
            # IF the week_path is not empty we check if the the path points to file or folder
            if(file_type == False):
                # Since the path leads to a file directly we open that file and copy the contents into a Text Input 
                # Widget and add the widget to the new Tabbed Panel Item
                with open(week_path, 'r') as file:
                    # Tabbed Panel Item instance
                    new_tab = TabbedPanelItem()
                    #Setting the title of the new tab
                    new_tab.text = week_path.split('\\')[-1]
                    #Background Picture of the tab
                    new_tab.background_normal = Paths.grey_img
                    #Adding the new TextInput widget to the tab
                    new_tab.add_widget(TextInput(text=file.read(),# Here we open the read the file content by read() 
                                                background_color= (35/255,35/255,35/255,1),
                                                font_size=20,
                                                foreground_color=(1,1,1,1 ),
                                                readonly=True
                                                ))
                    #Adding the new tab to the Tabbed Layout 
                    self.ids.main_tabs.add_widget(new_tab)
            else:
                #Since the chosen path is a folder we iterate through every file and create individual tabs 
                
                #Chaning the wwroking directory 
                os.chdir(week_path)
                #list_of_files contains the names of files present in the given directory 
                list_of_files = os.listdir(week_path)
                #This for loop goes through all the files in the 'list_of_files' and opens them in new tabs.
                for i in list_of_files:
                    with open(i) as file:
                        new_tab = TabbedPanelItem()
                        new_tab.text = i
                        new_tab.background_normal = Paths.grey_img
                        new_tab.add_widget(TextInput(text=file.read(),
                                                background_color= (35/255,35/255,35/255,1),
                                                font_size=20,
                                                foreground_color=(1,1,1,1),
                                                readonly=True
                                                ))
                        self.ids.main_tabs.add_widget(new_tab)
        week_path = ''
    #This function simply Deletes all the existing tabs in the screen along with the widgets present in it
    def TabsCleaner(self):
        if(self.ids.main_tabs.tab_list == []):
            pass
        else:
            self.ids.main_tabs.clear_tabs()
            self.ids.main_tabs.clear_widgets()
    #This function is used to alter the font size of the code box.
    def code_box_font_size(self,*args):
        self.ids.code_box.font_size = args[1]*2.5
    #This function is called to clear all contents from the code box.
    def code_box_cleaner(self):
        self.ids.code_box.text= ''
        self.ids.code_box.hint_text = "You can practice code here. \nPlease choose a language above before beggining."
        
    # This function is used to select the file type ex:Py,Java,C. The corresponding hint text is displayed when different language is selected
    # and the coresponding file extention is also choosen. 
    def Spinner_clicked(self, value):
        global file_ext 
        if(value == 'Python'):
            file_ext = '.py'

            if self.ids.code_box.text == "#include<stdio.h>\n\nvoid main()\n{\n\
                \nprintf(" ");\n\n}" or self.ids.code_box.text == '' :

                self.ids.code_box.text=""
                self.ids.code_box.hint_text='#You can continue to code in python.'

        elif(value == 'C'):
            file_ext = '.c'

            if self.ids.code_box.text == '':
                
                self.ids.code_box.text = "#include<stdio.h>\n\nvoid main()\n{\n\
                \nprintf(" ");\n\n}"

        elif (value == 'Java'):
            file_ext = '.java'
            if self.ids.code_box.text == "#include<stdio.h>\n\nvoid main()\n{\n\
                \nprintf();\n\n}" or self.ids.code_box.text == '':
                self.ids.code_box.text = "public class temp_java_file{\n\tpublic static void main(String[] args) {\nSystem.out.println(\"HEllo\");\n\n}\n}"
    # This method is called when the Run/Execute button is pressed, is it used to execute the code written in the code box.   
    def Run_pressed(self):
        global temp_py_file,temp_C_file,temp_files_path,temp_exe_file,cwd_main
        lang = self.ids.language_spinner.text
        if(self.ids.code_box.text == "" or self.ids.code_box.text == "#include<stdio.h>\n\nint main()\n{\n\
                \nreturn(0);\n\n}" ):pass
        elif(lang == 'Python'):
            
            temp_file = open(Paths.temp_py_file,'w')
            temp_file.write(self.ids.code_box.text)
            final_command = f"start cmd /k {Paths.py_path} {Paths.temp_py_file}"

            os.system(final_command)
            
            temp_file.close()
        elif(lang == 'C'):
            os.system(f"del {Paths.temp_exe_file}")
            temp_file = open(Paths.temp_C_file,'w')
            temp_file.write(self.ids.code_box.text)
            temp_file.close()
            os.chdir(Paths.temp_files_path)

            final_command = f"start cmd /k {Paths.gcc_path} temp_file_C.c -o temp_exe_file"
            final_command2 = f"start cmd /k {Paths.temp_exe_file}"
            os.system(final_command)
            time.sleep(1)
            os.system(final_command2)
            os.chdir(cwd_main)
        
        elif(lang == "Java"):
            temp_file = open(Paths.temp_java_file,"w")
            temp_file.write(self.ids.code_box.text)
            temp_file.close()
            os.chdir(Paths.temp_files_path)
            final_command1 = f"start cmd /k {Paths.javac_path} temp_java_file.java"
            final_command2 = f"start cmd /k {Paths.java_path} temp_java_file"
            os.system(final_command1)
            time.sleep(1)
            os.system(final_command2)
            os.chdir(cwd_main)


class WindowManager(ScreenManager):
    pass
    
class StormCodeApp(MDApp):
    
    data_path = Paths.data_path
    programs_path = Paths.programs_path
    pdf_path = Paths.pdf_path
    def build(self):
        self.title = "StormCode"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
'''
#:import Factory kivy.factory.Factory





<FolderPopup2>:
    name:"PdfChooserPopup"
    title:"PDF Viewer"
    auto_dismiss:False
    size_hint:0.7,0.7
    pos_hint:{"center_x":0.5,"center_y":0.5}
    BoxLayout:

        orientation: 'vertical'
        size:root.width,root.height
        padding:10
        spacing:10
        
        FileChooserIconView:
            id:PdfChooser
            path : app.pdf_path
            on_selection: root.PdfChoosen(PdfChooser.selection) 
        
        Screen:
            size_hint:1,0.1
            MDFillRoundFlatIconButton:
                text:"Close"
                size_hint:1,0.9
                icon:""
                text_color:"white"
                on_press:root.dismiss()
            
<FolderPopup>:
    name:"FolderChooser"
    title:"Hello"
    auto_dismiss:False
    size_hint:0.7,0.7
    pos_hint:{"center_x":0.5,"center_y":0.5}
    BoxLayout:

        orientation: 'vertical'
        size:root.width,root.height
        padding:10
        spacing:10
        
        FileChooserIconView:
            id:FileChooser
            path: app.programs_path
            on_selection: root.WeekChoosen(FileChooser.selection) 
        Screen:
            size_hint:1,0.1
            MDFillRoundFlatIconButton:
                text:"Choose Week"
                size_hint:1,0.9
                icon:""
                text_color:"white"
                on_press:root.WeekChoosen(FileChooser.path)
                # on_release: root.FolderDialog()
                
        Screen:
            size_hint:1,0.1
            MDFillRoundFlatIconButton:
                text:"Close"
                size_hint:1,0.9
                icon:""
                text_color:"white"
                on_press:root.dismiss()
<SavingPopup>:
    size_hint:0.45,0.39
    title:"Save progress"
    auto_dismiss:False
    BoxLayout:
        orientation:"vertical"
        size:root.width,root.height
        padding:10
        spacing:10
        MDTextField:
            id:FileNameTextBox
            multiline:False 
            mode: "rectangle"
            size_hint:1,0.5
            pos_hint:{"center_x":0.5}
            background_color:(35/255,35/255,35/255,1)
            line_color_focus:65/255,245/255,224255,1
            
            font_size:25
            text_color_focus: 65/255,245/255,224255,1
            hint_text:"File Name"
            hint_text_color_focus:65/255,245/255,224255,1
        MDRectangleFlatIconButton:
            text:       "Save"    
            font_size:      25
            icon:      "download"
            icon_color: "white"
            text_color:"white"
            line_color:  65/255,245/255,224255,1
            line_width:1
            size_hint:   1,0.5
            pos_hint:{"center_x":0.5}
            md_bg_color: 38/255,38/255,38/255,1
            on_press:root.FileName()
        MDFillRoundFlatIconButton:
            text:"Close"
            size_hint:1,0.1
            icon:""
            text_color:"white"
            on_press:root.dismiss()
            


        

WindowManager:

    # LoginScreen:

    MainScreen:

    PdfScreen:


<MainScreen>:
    name:"MainPage"
    id:MainPage
    BoxLayout:
        orientation:"vertical"
        padding:10
        spacing:10
        size : root.width,root.height
        GridLayout:
            cols:2
            rows:1
            spacing:10
            size_hint:(1,.18)
            canvas.before:
                Color:
                    rgba: 0,0,0,1
                Rectangle:
                    size:self.size
                    pos:self.pos
                Color:
                    rgba: (4/255,101/255,105/255,1)
                Line:
                    width:2
                    rectangle:self.x, self.y, self.width, self.height
            Label:
                markup:True
                text: "[color=#07dff7] ./[font=STENCIL]Storm[/font][font=COURBD]Code[/font]*"
                
                font_size:root.height/10
                color:7/255,233/255,247/255,1

                halign:"left"
                valign:"middle"
                size:root.width,root.height
            Label:
                markup:True
                text:"  [font=COUR][sub]Everything in one place.[/sup][/font]"
                font_size:self.height/2
                bold:True
                color:7/255,233/255,247/255,1
                halign:"center"
                valign:"bottom"
                
        GridLayout:
            cols:2
            rows:1
            size_hint:1,0.07
            spacing:10
            GridLayout:
                cols:4
                spacing:2
                Screen:
                    size_hint:0.25,1
                    MDFillRoundFlatIconButton:
                        id: FolderButton
                        text:"Open New Folder"
                        size_hint:1,1
                        icon:""
                        font_size:15
                        md_bg_color: (35/255,35/255,35/255,1)

                        line_color: (4/255,101/255,105/255,1)
                        line_width: 1.25

                        on_press: Factory.FolderPopup().open()
                
                Screen:
                    size_hint:0.25,1
                    MDFillRoundFlatIconButton:
                        id:LoadFiles
                        text:"Load Files"
                        size_hint:1,1
                        icon:""
                        font_size:15
                        md_bg_color: (35/255,35/255,35/255,1)

                        line_color: (4/255,101/255,105/255,1)
                        line_width: 1.25
                        
                        on_press:root.WeekLoader()
                
                Screen:
                    size_hint:0.25,1
                    MDFillRoundFlatIconButton:
                        id:TabRemover
                        text:"Clear Present Tabs"
        
                        size_hint:1,1
                        icon:""
                        font_size:15
                        md_bg_color: (35/255,35/255,35/255,1)

                        line_color: (4/255,101/255,105/255,1)

                        line_width: 1.25
                        
                        on_press:root.TabsCleaner()
                Screen:
                    size_hint:0.25,1
                    MDFillRoundFlatIconButton:
                        id:TabViewer
                        text:"View PDFs"
        
                        size_hint:1,1
                        icon:""
                        font_size:15
                        md_bg_color: (35/255,35/255,35/255,1)

                        line_color: (4/255,101/255,105/255,1)

                        line_width: 1.25
                        
                        on_press:Factory.FolderPopup2().open()
                        
            BoxLayout:
                orientation: 'horizontal'
                spacing:5
               
                Spinner:
                    id:language_spinner
                    background_normal:"Assets\Images\GreyBG.jpg"
            
                    size_hint:0.2,1
                    text: "Select language"
                    values:["Python","C","Java"]
                    on_text: root.Spinner_clicked(language_spinner.text)
            
                MDRectangleFlatIconButton:
                    size_hint:0.2,1
                    text: "Run/Execute"
                    icon:""
                    text_color:"white"
                    line_color: 0,0,0,0
                    md_bg_color: (35/255,35/255,35/255,1)
                    on_press:root.Run_pressed()
                    
            
                MDSlider:
                    max:20
                    min:8
                    step:1
                    value: 8
                    hint:True
                    acive:False
                    hint_text_color:"white"
                    hint_bg_color: (35/255,35/255,35/255,1)
                    hint_radius: [6, 0, 6, 0]
                    thumb_color_active: 7/255,233/255,247/255
                    thumb_color_inactive: 7/255,233/255,247/255
                    color:7/255,233/255,247/255
                    # value_track:True
                    # value_track_color:7/255,233/255,247,1
                    
                    size_hint:0.2,1
                    on_value:root.code_box_font_size(*args)
               
        
                MDRectangleFlatIconButton:
                    size_hint:0.2,1
                    text: "Save"  
                    icon:""
                    text_color:"white"
                    line_color: 0,0,0,0
                    md_bg_color: (35/255,35/255,35/255,1)
                    on_press: root.Save_Button_Pressed()
                    
               
            
                MDRectangleFlatIconButton:
                    size_hint:0.2,1
                    text: "Clear all"
                    icon:""
                    text_color:"white"
                    line_color: 0,0,0,0
                    md_bg_color: (35/255,35/255,35/255,1)
                    on_press:root.code_box_cleaner()
                
        BoxLayout:
            orientation: 'horizontal'
            
            TabbedLayout:
                id:main_tabs
                do_default_tab:False
                


            TextInput:
                id:code_box
                multiline:True 
                hint_text:"You can practice code here. Please choose a language above before beggining."
                
                foreground_color:1,1,1,1
                font_size:20
                background_color:(35/255,35/255,35/255,1)



        


'''
        )
    
if __name__ =='__main__':
    StormCodeApp().run()
