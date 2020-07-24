import logging
import os
import tkinter as tk
from tkinter import Frame,ttk,messagebox, StringVar, Toplevel, filedialog

from PIL import Image, ImageTk

import LessonList,Data_Flow_Edit

import Lesson_File_Manager

logger = logging.getLogger("MagicLogger")
class MagicEditWizard(Toplevel):
    def __init__(self,parent,*args,**kwargs):

        super().__init__(*args, **kwargs)
        logger.info("Entering Edit Wizard Initialize")
        self.base_frame = tk.Frame(self, background="gray20")
        
        #self.base_frame.rowconfigure(0, weight=1)
        self.base_frame.columnconfigure(0, weight=1)
        self.base_frame.grid(row=0, column=0)

        self.title_frame = Frame(self.base_frame)
        self.index = 0
        self.parent = parent
        self.factual_frame = Frame(self.base_frame)
        self.apply_activity_frame = Frame(self.base_frame)
        self.apply_activity_steps_frame = Frame(self.apply_activity_frame)
        self.ip_frame = Frame(self.base_frame)
        #self.rowconfigure(0, weight=1)
        self.configure(background='gray20')
        self.columnconfigure(0, weight=1)
        self.title_frame.configure(background='gray20')
        self.factual_frame.configure(background='gray20')
        self.apply_activity_frame.configure(background='gray20')
        self.ip_frame.configure(background='gray20')
        self.apply_activity_steps_frame.configure(background='gray20')
        self.data_collector = {}
        s  = ttk.Style()
        self.bind("<Configure>",self.resize)
        s.theme_use('clam')

        s.configure('Edit.TLabelframe', background='gray22')
        s.configure('Edit.TLabelframe.Label', font=('helvetica', 14, 'bold'))
        s.configure('Edit.TLabelframe.Label', background='gray22', foreground='white')

        s.configure('Firebrick.Label',background='gray22',foreground='white',font=('helvetica', 9, 'bold'))

        s.configure('Firebrick.TButton', background='steel blue', foreground='white',font=('helvetica', 12, 'bold'))
        s.configure('Green.TMenubutton', background='gray22', foreground='gray55')
        s.map('Firebrick.TButton',background=[('active', '!disabled', 'dark turquoise'), ('pressed', 'white')],
              foreground=[('pressed', 'white'), ('active', 'white')])

        app = LessonList.MagicLessonList(parent=self)
        app.geometry("350x800+100+100")
        self.wait_window(app)
        if hasattr(self,"selected_lessons") is False:
            self.destroy()
        else:    
            
            self.to_edit_lesson = self.selected_lessons[0]
           
            Data_Flow_Edit.LESSON_ID = int(self.to_edit_lesson)
            self.imageroot = Data_Flow_Edit.file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(self.to_edit_lesson) + os.path.sep + "images"
            self.videoroot = Data_Flow_Edit.file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(self.to_edit_lesson) + os.path.sep + "videos"

            self.lesson_dict = Data_Flow_Edit.select_lesson_data(int(self.to_edit_lesson))
            print(self.lesson_dict)
            self.create_title_edit_page(8)
            bottom_frame = tk.Frame(self, background="gray20")
            self.next_button = ttk.Button(bottom_frame, text='Next', command=self.next_page, style='Firebrick.TButton')
            self.back_button = ttk.Button(bottom_frame, text="Back", command=self.previous_page, style='Firebrick.TButton')
            self.back_button.grid(row=0,column=0,padx=10)
            self.next_button.grid(row=0, column=1)
            bottom_frame.grid(row=1)
            self.data_collector['Lesson_Type'] = 'Science'
            self.data_collector['Lesson_Template'] = 'Hogwarts'
            self.data_collector['Lesson_Title'] = ''
            self.data_collector['Title_Image'] = ''
            self.data_collector['Title_Video'] = ''
            self.data_collector['Title_Running_Notes'] = ''

            self.data_collector['Factual_Term1'] = ''
            self.data_collector['Factual_Term1_Description'] = ''
            self.data_collector['Factual_Term2'] = ''
            self.data_collector['Factual_Term2_Description'] = ''
            self.data_collector['Factual_Term3'] = ''
            self.data_collector['Factual_Term3_Description'] = ''
            self.data_collector['Factual_Image1'] = ''
            self.data_collector['Factual_Image2'] = ''
            self.data_collector['Factual_Image3'] = ''
            self.data_collector['Application_Mode'] = ''
            self.data_collector['Application_Steps_Number'] = 0
            self.data_collector['Application_Step_Description_1'] = ''
            self.data_collector['Application_Step_Description_2'] = ''
            self.data_collector['Application_Step_Description_3'] = ''
            self.data_collector['Application_Step_Description_4'] = ''
            self.data_collector['Application_Step_Description_5'] = ''
            self.data_collector['Application_Step_Description_6'] = ''
            self.data_collector['Application_Step_Description_7'] = ''
            self.data_collector['Application_Step_Description_8'] = ''
            self.data_collector['Application_Steps_Widget_1'] = ''
            self.data_collector['Application_Steps_Widget_2'] = ''
            self.data_collector['Application_Steps_Widget_3'] = ''
            self.data_collector['Application_Steps_Widget_4'] = ''
            self.data_collector['Application_Steps_Widget_5'] = ''
            self.data_collector['Application_Steps_Widget_6'] = ''
            self.data_collector['Application_Steps_Widget_7'] = ''
            self.data_collector['Application_Steps_Widget_8'] = ''
            self.data_collector['Answer_Key'] = ''
            self.data_collector['Video_Audio_Assessment_Flag'] = 0
            self.data_collector['Application_Video_Link'] = ''
            self.data_collector['Application_Video_Running_Notes'] = ''

            self.data_collector["NumberOfQuestions"] = 0

            self.title_image_path_full = ""
            self.factual_image1_path_full = ""
            self.factual_image2_path_full =""
            self.factual_image3_path_full =""
            self.filename_vid_title_full = ""
            self.application_image1_path_full =""
            self.application_image2_path_full =""
            self.application_image3_path_full =""
            self.application_image4_path_full =""
            self.application_image5_path_full =""
            self.application_image6_path_full =""
            self.application_image7_path_full =""
            self.application_image8_path_full =""


    def add_file(self,fileroot,window):
        filename_img_title_full = filedialog.askopenfilename(initialdir=fileroot,title='Select Image',parent=window)
        filename_img_title = os.path.basename(filename_img_title_full)
        print(filename_img_title)
        return filename_img_title_full, filename_img_title



    def resize(self,event):
        self.base_frame.grid_forget()
        self.base_frame.grid(row=0,column=0)

    def create_title_edit_page(self,edit_lesson):
        logger.info("Entering create_title_edit_page Initialze")
        self.title_label = ttk.Label(self.title_frame, text="Title of your topic", style='Edit.TLabelframe.Label')
        self.title_text_var = StringVar()
        self.title_text_var.set((self.lesson_dict[0].get("Lesson_Title")))
        self.title_text = tk.Entry(self.title_frame,textvariable=self.title_text_var)

        self.title_image_label = ttk.Label(self.title_frame, text="Image Related to Title", style='Edit.TLabelframe.Label')
        self.title_image_button = ttk.Button(self.title_frame, text="Add Image", command=self.add_title_image, style='Firebrick.TButton')
        self.title_image_video_label = ttk.Label(self.title_frame, text="Video Related to Title", style='Edit.TLabelframe.Label')
        self.title_video_button = ttk.Button(self.title_frame, text="Add Video", command=self.add_title_video, style='Firebrick.TButton')

        self.title_running_notes_label = ttk.Label(self.title_frame, text="Topic Introduction\n(2 to 3 lines)", style='Edit.TLabelframe.Label')
        self.running_notes = self.lesson_dict[0].get("Title_Running_Notes")
        self.title_running_notes = tk.Text(self.title_frame, wrap=tk.WORD, width=30, height=5, pady=2)
        self.title_running_notes.insert("1.0",self.running_notes)

        self.video_var = StringVar()
        self.video_var.set(self.lesson_dict[0].get("Title_Video"))
        #self.title_video_file_label = ttk.Label(self.title_frame,textvariable=self.video_var,style="Edit.TLabelframe.Label")
        self.image_var = StringVar()
        self.image_var.set(self.lesson_dict[0].get("Title_Image"))
        self.image_title_preview_path = self.imageroot + os.path.sep + self.image_var.get()
        if self.image_var.get() is not None and self.image_var.get() != "":
            title_image = Image.open(self.image_title_preview_path)
            title_image.thumbnail((100, 100))
            self.title_image_display_preview = ImageTk.PhotoImage(title_image)
        else:
            self.title_image_display_preview = None
        self.title_image_file_label = ttk.Label(self.title_frame, image=self.title_image_display_preview,background="gray22")
        self.title_url_label = ttk.Label(self.title_frame, text="(OR) youtube URL", style='Edit.TLabelframe.Label')
        self.title_video_url = ttk.Entry(self.title_frame,textvariable = self.video_var )

        self.title_label.grid(row=0,column=0,padx=20,pady=10,sticky=tk.W)
        self.title_text.grid(row=0,column=1,padx=20,pady=10,sticky=tk.W)
        self.title_image_label.grid(row=1,column=0,padx=20,pady=10,sticky=tk.W)
        self.title_image_button.grid(row=1,column=1,padx=20,pady=10,sticky=tk.W)
        self.title_image_video_label.grid(row=2,column=0,padx=20,pady=10,sticky=tk.W)
        self.title_video_button.grid(row=2,column=1,padx=20,pady=10,sticky=tk.W)
        self.title_url_label.grid(row=2, column=2, pady=2,sticky=tk.W)
        self.title_video_url.grid(row=2, column=3, pady=2, padx=5,sticky=tk.W)
        self.title_running_notes_label.grid(row=3,column=0,padx=20,pady=10,sticky=tk.W)
        self.title_running_notes.grid(row=3,column=1,columnspan=2,padx=20,pady=10,sticky=tk.W)
        self.title_image_file_label.grid(row=1, column=3,pady=10,sticky=tk.W)
       # self.title_video_file_label.grid(row=2, column=3,pady=10)
        self.title_frame.grid(row=0,column=0,pady=50,sticky=tk.NSEW)
        self.index += 1

    def create_factual_edit_page(self, edit_lesson):
        logger.info("Entering create_factual_edit_page Initialze")
        self.factual_image_var = StringVar()
        self.factual_text_term1_var = StringVar()
        self.factual_term_label = ttk.Label(self.factual_frame, text="Definition or New Term", style='Edit.TLabelframe.Label')
        self.factual_term_text = ttk.Entry(self.factual_frame,textvariable=self.factual_text_term1_var)
        self.factual_term_desc_text = tk.Text(self.factual_frame, wrap=tk.WORD, width=30, height=4)
        text_insert_desc1 = self.lesson_dict[0]["Factual_Term1_Description"]
        self.factual_term_desc_text.insert("1.0",text_insert_desc1)
        self.factual_text_term1_var.set(self.lesson_dict[0]["Factual_Term1"])
        self.factual_image_var.set(self.lesson_dict[0]["Factual_Image1"])
        self.factual_term_desc_label = ttk.Label(self.factual_frame, text="Description", style='Edit.TLabelframe.Label')
        self.factual_term_image_button = ttk.Button(self.factual_frame, text='Add Image',
                                               command=lambda id=1: self.add_factual_image(id), style='Firebrick.TButton')
        if self.factual_image_var.get() is not None and self.factual_image_var.get() != "":
            factual_image = Image.open(self.imageroot + os.path.sep + self.factual_image_var.get())
            factual_image.thumbnail((80, 80))
            self.factual_image_display_preview = ImageTk.PhotoImage(factual_image)
        else:
            self.factual_image_display_preview = None
        self.factual_image_label = ttk.Label(self.factual_frame, image = self.factual_image_display_preview,
                                            background="gray22")


        self.factual_term_label.grid(row=0, column=0, pady=3,sticky=tk.W)
        self.factual_term_text.grid(row=0, column=1,padx=5, pady=3,sticky=tk.W)

        self.factual_term_desc_label.grid(row=1, column=0, pady=3,sticky=tk.W)
        self.factual_term_desc_text.grid(row=1, column=1,columnspan=2,padx=5, pady=3,sticky=tk.W)


        self.factual_term_image_button.grid(row=3,column=0,pady=5,sticky=tk.W)
        self.factual_image_label.grid(row=3, column=1,padx=5, pady=5,sticky=tk.W)

        self.factual_image2_var = StringVar()
        self.factual_text_term2_var = StringVar()

        self.factual_term2_label = ttk.Label(self.factual_frame, text="Definition or New Term", style='Edit.TLabelframe.Label')
        self.factual_term2_text = ttk.Entry(self.factual_frame,textvariable=self.factual_text_term2_var)
        self.factual_term2_desc_text = tk.Text(self.factual_frame, wrap=tk.WORD, width=30, height=4)
        self.factual_term2_desc_label = ttk.Label(self.factual_frame, text="Description", style='Edit.TLabelframe.Label')
        self.factual_term2_image_button = ttk.Button(self.factual_frame, text='Add Image',
                                               command=lambda id=2: self.add_factual_image(id), style='Firebrick.TButton')
        self.factual_image2_var.set(self.lesson_dict[0]["Factual_Image2"])
        if self.factual_image2_var.get() is not None and self.factual_image2_var.get() != "":
            factual_image = Image.open(self.imageroot + os.path.sep + self.factual_image2_var.get())
            factual_image.thumbnail((80, 80))
            self.factual_image_display_preview2 = ImageTk.PhotoImage(factual_image)
        else:
            self.factual_image_display_preview2 = None
        self.factual_image_label2 = ttk.Label(self.factual_frame, image =   self.factual_image_display_preview2  ,
                                            background="gray22")
        self.factual_term2_label.grid(row=5, column=0, pady=5,sticky=tk.W)
        self.factual_term2_text.grid(row=5, column=1, padx=5,pady=5,sticky=tk.W)
        self.factual_term2_desc_label.grid(row=6, column=0, pady=5,sticky=tk.W)

        self.factual_term2_desc_text.grid(row=6, column=1,padx=5, pady=5,columnspan=2,sticky=tk.W)
        text_insert_desc2 = self.lesson_dict[0]["Factual_Term2_Description"]
        self.factual_term2_desc_text.insert("1.0", text_insert_desc2)
        self.factual_text_term2_var.set(self.lesson_dict[0]["Factual_Term2"])

        self.factual_term2_image_button.grid(row=7, column=0, pady=5,sticky=tk.W)
        self.factual_image_label2.grid(row=7, column=1,padx=5, pady=5,sticky=tk.W)

        self.factual_image3_var = StringVar()
        self.factual_text_term3_var = StringVar()
        self.factual_term3_label = ttk.Label(self.factual_frame, text="Definition or New Term", style='Edit.TLabelframe.Label')
        self.factual_term3_text = ttk.Entry(self.factual_frame,textvariable=self.factual_text_term3_var)
        self.factual_term3_desc_text = tk.Text(self.factual_frame, wrap=tk.WORD, width=30, height=4)
        self.factual_term3_desc_label = ttk.Label(self.factual_frame, text="Description", style='Edit.TLabelframe.Label')
        self.factual_term3_image_button = ttk.Button(self.factual_frame, text='Add Image',
                                               command=lambda id=3: self.add_factual_image(id), style='Firebrick.TButton')
        self.factual_image3_var.set(self.lesson_dict[0]["Factual_Image3"])
        if self.factual_image3_var.get() is not None and self.factual_image3_var.get() != "":
            factual_image = Image.open(self.imageroot + os.path.sep + self.factual_image3_var.get())
            factual_image.thumbnail((80, 80))
            self.factual_image_display_preview3 = ImageTk.PhotoImage(factual_image)
        else:
            self.factual_image_display_preview3 = None

        self.factual_image_label3 = ttk.Label(self.factual_frame, image=self.factual_image_display_preview3,
                                              background="gray22")
        self.factual_term3_label.grid(row=9, column=0, pady=5,sticky=tk.W)
        self.factual_term3_text.grid(row=9, column=1, padx=5,pady=5,sticky=tk.W)
        self.factual_term3_desc_label.grid(row=10, column=0, pady=5,sticky=tk.W)
        self.factual_term3_desc_text.grid(row=10, column=1,padx=5, columnspan=2,pady=5,sticky=tk.W)
        text_insert_desc3 = self.lesson_dict[0]["Factual_Term3_Description"]
        self.factual_term3_desc_text.insert("1.0", text_insert_desc3)
        self.factual_text_term3_var.set(self.lesson_dict[0]["Factual_Term3"])

        self.factual_term3_image_button.grid(row=11, column=0, pady=5,sticky=tk.W)
        self.factual_image_label3.grid(row=11, column=1,padx=5, pady=5,sticky=tk.W)
        self.index = 2

    def create_application_edit_page(self, edit_lesson):

        logger.info("Entering create_application_edit_page Initialze")
        self.apply_steps_label = ttk.Label(self.apply_activity_frame, text="Number of Steps?", style='Edit.TLabelframe.Label')
        self.selected_steps = tk.StringVar()
        self.selected_steps.set(str(self.lesson_dict[0]["Application_Steps_Number"]))
        print("sdasdas"+self.selected_steps.get())
        self.apply_steps_dropdown = tk.OptionMenu(self.apply_activity_frame, self.selected_steps, '0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                  command=self.show_individual_steps)
        self.apply_steps_dropdown.configure(background="white")
        self.apply_steps_dropdown["menu"].configure(background="white")
        self.apply_steps_label.grid(row=0, column=0, pady=2,padx=5)
        self.apply_steps_dropdown.grid(row=0, column=1,pady=2)

        self.number_of_steps = self.lesson_dict[0]['Application_Steps_Number']
        self.configure_steps(self.number_of_steps)
        self.index += 1



    def show_individual_steps(self,selected_number):
        logger.info("Entering show_individual_steps")
        for widget in self.apply_activity_steps_frame.winfo_children():
             widget.destroy()
        self.configure_steps(int(selected_number))




    def configure_steps(self,number_of_steps):
        logger.info("Entering configre_steps")
        self.step_text1_var = StringVar()
        self.step_text1_var.set(self.lesson_dict[0]["Application_Step_Description_1"])
        self.step_text2_var = StringVar()
        self.step_text2_var.set(self.lesson_dict[0]["Application_Step_Description_2"])
        self.step_text3_var = StringVar()
        self.step_text3_var.set(self.lesson_dict[0]["Application_Step_Description_3"])
        self.step_text4_var = StringVar()
        self.step_text4_var.set(self.lesson_dict[0]["Application_Step_Description_4"])
        self.step_text5_var = StringVar()
        self.step_text5_var.set(self.lesson_dict[0]["Application_Step_Description_5"])
        self.step_text6_var = StringVar()
        self.step_text6_var.set(self.lesson_dict[0]["Application_Step_Description_6"])
        self.step_text7_var = StringVar()
        self.step_text7_var.set(self.lesson_dict[0]["Application_Step_Description_7"])
        self.step_text8_var = StringVar()
        self.step_text8_var.set(self.lesson_dict[0]["Application_Step_Description_8"])

        self.step1_label = ttk.Label(self.apply_activity_steps_frame)
        self.step2_label = ttk.Label(self.apply_activity_steps_frame)
        self.step3_label = ttk.Label(self.apply_activity_steps_frame)
        self.step4_label = ttk.Label(self.apply_activity_steps_frame)
        self.step5_label = ttk.Label(self.apply_activity_steps_frame)
        self.step6_label = ttk.Label(self.apply_activity_steps_frame)
        self.step7_label = ttk.Label(self.apply_activity_steps_frame)
        self.step8_label = ttk.Label(self.apply_activity_steps_frame)

        self.step_text1 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text1_var)
        self.step_text2 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text2_var)
        self.step_text3 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text3_var)
        self.step_text4 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text4_var)
        self.step_text5 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text5_var)
        self.step_text6 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text6_var)
        self.step_text7 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text7_var)
        self.step_text8 = ttk.Entry(self.apply_activity_steps_frame,textvariable=self.step_text8_var)
        self.step_image_button1 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=1: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button2 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=2: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button3 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=3: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button4 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=4: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button5 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=5: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button6 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=6: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button7 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=7: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')
        self.step_image_button8 = ttk.Button(self.apply_activity_steps_frame, command=lambda id=8: self.add_application_image(id), text='Add Image', style='Firebrick.TButton')




        self.step1_image1 = StringVar()
        self.step1_image1.set(self.lesson_dict[0]["Application_Steps_Widget_1"])
        self.step2_image2 = StringVar()
        self.step2_image2.set(self.lesson_dict[0]["Application_Steps_Widget_2"])
        self.step3_image3 = StringVar()
        self.step3_image3.set(self.lesson_dict[0]["Application_Steps_Widget_3"])
        self.step4_image4 = StringVar()
        self.step4_image4.set(self.lesson_dict[0]["Application_Steps_Widget_4"])
        self.step5_image5 = StringVar()
        self.step5_image5.set(self.lesson_dict[0]["Application_Steps_Widget_5"])
        self.step6_image6 = StringVar()
        self.step6_image6.set(self.lesson_dict[0]["Application_Steps_Widget_6"])
        self.step7_image7 = StringVar()
        self.step7_image7.set(self.lesson_dict[0]["Application_Steps_Widget_7"])
        self.step8_image8 = StringVar()
        self.step8_image8.set(self.lesson_dict[0]["Application_Steps_Widget_8"])
        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step1_image1.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview1 = ImageTk.PhotoImage(apply_image)
            self.step1_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview1,
                                         background="gray22")
        except:
            print("invalid image")
            logger.exception("Invalid Image - step 1")


        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step2_image2.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview2 = ImageTk.PhotoImage(apply_image)
            self.step2_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview2
                                         )
        except:
            print("Invalid Image")
            logger.exception("Invalid Image - step 2")
        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step3_image3.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview3 = ImageTk.PhotoImage(apply_image)
            self.step3_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview3)

        except:
            print("invalid image")
            logger.exception("Invalid Image - step 3")

        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step4_image4.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview4 = ImageTk.PhotoImage(apply_image)
            self.step4_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview4
                                         )
        except:
            print("invalid image")
            logger.exception("Invalid Image - step 4")

        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step5_image5.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview5 = ImageTk.PhotoImage(apply_image)
            self.step5_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview5
                                         )
        except:
            print("invalid image")
            logger.exception("Invalid Image - step 5")

        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step6_image6.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview6 = ImageTk.PhotoImage(apply_image)
            self.step6_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview6
                                         )
        except:
            print("invalid image")
            logger.exception("Invalid Image - step 6")

        try:

            apply_image = Image.open(self.imageroot + os.path.sep + self.step7_image7.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview7 = ImageTk.PhotoImage(apply_image)
            self.step7_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview7,
                                         )
        except:
            logger.exception("Invalid Image - step 7")
        try:
            apply_image = Image.open(self.imageroot + os.path.sep + self.step8_image8.get())
            apply_image.thumbnail((60, 60))
            self.apply_image_display_preview8 = ImageTk.PhotoImage(apply_image)
            self.step8_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview8,
                                         )
        except:
            print("invalid image")
            logger.exception("Invalid Image - step 8")


        self.htmlvar = StringVar()
        self.html_link = ttk.Entry(self.apply_activity_steps_frame, textvariable=self.htmlvar, width=20)
        self.link_label = ttk.Label(self.apply_activity_steps_frame, text="Add an external link",
                               style='Edit.TLabelframe.Label')
        self.htmlvar.set(self.lesson_dict[0]["Apply_External_Link"])

        steps = 1
        while steps < number_of_steps + 1:
            self.step_label = ttk.Label(self.apply_activity_steps_frame, text="Step Description",
                                        style='Edit.TLabelframe.Label')
            if steps == 1:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text1.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button1.grid(row=steps, column=2,pady=2, padx=20)
                if hasattr(self,"step1_label"):
                    self.step1_label.grid(row=steps,pady=2, column=4)
            if steps == 2:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text2.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button2.grid(row=steps, column=2,pady=2, padx=20)
                if hasattr(self, "step2_label"):
                    self.step2_label.grid(row=steps, column=4,pady=2)

            if steps == 3:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text3.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button3.grid(row=steps, column=2,pady=2, padx=20)
                self.step3_label.grid(row=steps,pady=2, column=4)
                if hasattr(self, "step3_label"):
                    self.step3_label.grid(row=steps, column=4)
            if steps == 4:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text4.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button4.grid(row=steps,pady=2, column=2, padx=20)
                if hasattr(self, "step4_label"):
                    self.step4_label.grid(row=steps,pady=2, column=4)

            if steps == 5:
                self.step_label.grid(row=steps,pady=2, column=0, padx=20)
                self.step_text5.grid(row=steps,pady=2, column=1, padx=20)
                self.step_image_button5.grid(row=steps,pady=2, column=2, padx=20)
                if hasattr(self, "step5_label"):
                    self.step5_label.grid(row=steps,pady=2, column=4)

            if steps == 6:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text6.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button6.grid(row=steps, column=2, pady=2,padx=20)
                if hasattr(self, "step6_label"):
                    self.step6_label.grid(row=steps, column=4)
            if steps == 7:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text7.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button7.grid(row=steps, column=2,pady=2, padx=20)
                if hasattr(self, "step7_label"):
                     self.step7_label.grid(row=steps,pady=2, column=4)
            if steps == 8:
                self.step_label.grid(row=steps, column=0,pady=2, padx=20)
                self.step_text8.grid(row=steps, column=1,pady=2, padx=20)
                self.step_image_button8.grid(row=steps, column=2,pady=2, padx=20)
                if hasattr(self, "step8_label"):
                    self.step8_label.grid(row=steps, pady=2,column=4)
            steps += 1
        self.link_label.grid(row=steps, column=0, pady=10)
        self.html_link.grid(row=steps, column=1, pady=10, padx=20)
        self.apply_activity_steps_frame.grid(row=1,column=0,pady=2,columnspan=2)

    def create_ip_edit_page(self, edit_lesson):
        logger.info("Inside create_ip_edit_page")
        self.create_question_Label = ttk.Label(self.ip_frame, text='Assessment Questions', wraplength=300,
                                          style='Edit.TLabelframe.Label')

        self.create_question_text = tk.Text(self.ip_frame, wrap=tk.WORD, width=70, height=20)
        question_text = self.lesson_dict[0]["IP_Questions"]
        self.create_question_text.insert("1.0", question_text)
        self.create_question_Label.grid(row=1, column=0)
        self.create_question_text.grid(row=1, column=1,padx=10)
        self.index += 1


    def add_title_image(self):
        logger.info("add_title_image")
        self.title_image_path_full, title_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
        self.image_var.set(title_image_basename)
        title_image = Image.open(self.title_image_path_full)
        title_image.thumbnail((100, 100))
        self.title_image_file_label.grid_forget()

        self.title_image_display_preview = ImageTk.PhotoImage(title_image)
        self.title_image_file_label = ttk.Label(self.title_frame, image=self.title_image_display_preview,
                                                background="gray22")
        self.title_image_file_label.grid(row=1, column=3, padx=20, pady=10)

    def add_factual_image(self,index):
        logger.info("Inside add_factual_image")
        factual_image = None
        if index == 1:
            self.factual_image1_path_full, factual_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.factual_image_var.set(factual_image_basename)
            factual_image = Image.open(self.factual_image1_path_full)
            factual_image.thumbnail((80, 80))
            self.factual_image_label.grid_forget()
            self.factual_image_display_preview = ImageTk.PhotoImage(factual_image)
            self.factual_image_label = ttk.Label(self.factual_frame, image=self.factual_image_display_preview,
                                                    background="gray22")
            self.factual_image_label.grid(row=3, column=3, padx=20, pady=5)


        elif index == 2:
            self.factual_image2_path_full, factual_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.factual_image2_var.set(factual_image_basename)
            factual_image = Image.open(self.factual_image2_path_full)
            factual_image.thumbnail((80, 80))
            self.factual_image_label2.grid_forget()
            self.factual_image_display_preview2 = ImageTk.PhotoImage(factual_image)
            self.factual_image_label2 = ttk.Label(self.factual_frame, image=self.factual_image_display_preview2,
                                                 background="gray22")
            self.factual_image_label2.grid(row=7, column=3, padx=20, pady=5)
        else:
            self.factual_image3_path_full, factual_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.factual_image3_var.set(factual_image_basename)
            factual_image = Image.open(self.factual_image3_path_full)
            factual_image.thumbnail((80, 80))
            self.factual_image_label3.grid_forget()
            self.factual_image_display_preview3 = ImageTk.PhotoImage(factual_image)
            self.factual_image_label3 = ttk.Label(self.factual_frame, image=self.factual_image_display_preview3,
                                                 background="gray22")
            self.factual_image_label3.grid(row=11, column=3, padx=20, pady=5)




    def add_application_image(self, index):


        if index == 1:
            self.application_image1_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step1_image1.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image1_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview1 = ImageTk.PhotoImage(apply_image)
                self.step1_label.grid_forget()
                self.step1_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview1,
                                             )
                self.step1_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 1")

        elif index == 2:
            self.application_image2_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step2_image2.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image2_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview2 = ImageTk.PhotoImage(apply_image)
                self.step2_label.grid_forget()
                self.step2_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview2,
                                             )
                self.step2_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 2")
        elif index == 3:
            self.application_image3_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step3_image3.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image3_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview3 = ImageTk.PhotoImage(apply_image)
                self.step3_label.grid_forget()
                self.step3_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview3,
                                             )
                self.step3_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 3")
        elif index == 4:
            self.application_image4_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step4_image4.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image4_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview4 = ImageTk.PhotoImage(apply_image)
                self.step4_label.grid_forget()
                self.step4_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview4,
                                             )
                self.step4_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 4")
        elif index == 5:
            self.application_image5_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step5_image5.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image5_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview5 = ImageTk.PhotoImage(apply_image)
                self.step5_label.grid_forget()
                self.step5_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview5,
                                             )
                self.step5_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 5")
        elif index == 6:
            self.application_image6_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step6_image6.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image6_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview6 = ImageTk.PhotoImage(apply_image)
                self.step6_label.grid_forget()
                self.step6_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview6,
                                             )
                self.step6_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 6")
        elif index == 7:
            self.application_image7_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step7_image7.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image7_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview7 = ImageTk.PhotoImage(apply_image)
                self.step7_label.grid_forget()
                self.step7_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview7,
                                             )
                self.step7_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 7")
        elif index == 8:
            self.application_image8_path_full, application_image_basename = self.add_file(Data_Flow_Edit.file_root,self)
            self.step8_image8.set(application_image_basename)
            try:
                apply_image = Image.open(self.application_image8_path_full)
                apply_image.thumbnail((60, 60))
                self.apply_image_display_preview8 = ImageTk.PhotoImage(apply_image)
                self.step8_label.grid_forget()
                self.step8_label = ttk.Label(self.apply_activity_steps_frame, image=self.apply_image_display_preview8,
                                             )
                self.step8_label.grid(row=index, column=4, padx=20, pady=10)
            except:
                print("invalid image")
                logger.exception("Invalid image - add_application_image - 8")

    def add_title_video(self):

        self.filename_vid_title_full, title_video_basename = self.add_file(Data_Flow_Edit.file_root,self)
        self.video_var.set(title_video_basename)


    def save_data(self):

        logger.info("Inside save_data of edit UI")

        lesson_file_manager = Lesson_File_Manager.LessonFileManager(Data_Flow_Edit.file_root, self.to_edit_lesson)

        if (self.title_image_path_full != ""):
            lesson_file_manager.add_image_file(self.title_image_path_full)

        if (self.filename_vid_title_full != ""):
            lesson_file_manager.add_video_file(self.filename_vid_title_full)
        if (self.factual_image1_path_full != ""):
            lesson_file_manager.add_image_file(self.factual_image1_path_full)
        if (self.factual_image2_path_full != ""):
            lesson_file_manager.add_image_file(self.factual_image2_path_full)
        if (self.factual_image3_path_full != ""):
            lesson_file_manager.add_image_file(self.factual_image3_path_full)

        if (self.application_image1_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image1_path_full)
        if (self.application_image2_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image2_path_full)
        if (self.application_image3_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image3_path_full)
        if (self.application_image4_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image4_path_full)
        if (self.application_image5_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image5_path_full)
        if (self.application_image6_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image6_path_full)
        if (self.application_image7_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image7_path_full)
        if (self.application_image8_path_full != ""):
            lesson_file_manager.add_image_file(self.application_image8_path_full)

        Data_Flow_Edit.save_all_data(self.data_collector, lesson_file_manager,self)

        self.destroy()

    def process_save(self,index):
        logger.info("Inside process_Save of edit UI")
        if index == 1:
            self.data_collector["Lesson_Title"]=self.title_text_var.get()
            self.data_collector["Title_Image"]=self.image_var.get()
            self.data_collector["Title_Video"] = self.video_var.get()
            self.data_collector["Title_Running_Notes"] = self.title_running_notes.get('1.0', tk.END)
        if index == 2:
            self.data_collector["Factual_Term1"] = self.factual_term_text.get()
            self.data_collector["Factual_Term1_Description"] = self.factual_term_desc_text.get('1.0', 'end')
            self.data_collector["Factual_Image1"]= self.factual_image_var.get()

            self.data_collector['Factual_Term2'] = self.factual_term2_text.get()
            self.data_collector['Factual_Term2_Description'] = self.factual_term2_desc_text.get('1.0', 'end')
            self.data_collector["Factual_Image2"] = self.factual_image2_var.get()

            self.data_collector["Factual_Term3"] = self.factual_term3_text.get()
            self.data_collector["Factual_Term3_Description"] = self.factual_term3_desc_text.get('1.0', 'end')
            self.data_collector["Factual_Image3"] = self.factual_image3_var.get()
        if index == 3:
            self.data_collector["Application_Steps_Number"]=self.selected_steps.get()
            final_steps = int(self.selected_steps.get())
            final_step_index = 1


            while final_step_index <= final_steps:
                if final_step_index == 1:
                    self.data_collector["Application_Step_Description_1"] = self.step_text1_var.get()
                    self.data_collector["Application_Steps_Widget_1"] = self.step1_image1.get()
                if final_step_index == 2:
                    self.data_collector["Application_Step_Description_2"] = self.step_text2_var.get()
                    self.data_collector["Application_Steps_Widget_2"] = self.step2_image2.get()
                if final_step_index == 3:
                    self.data_collector["Application_Step_Description_3"] = self.step_text3_var.get()
                    self.data_collector["Application_Steps_Widget_3"] = self.step3_image3.get()
                if final_step_index == 4:
                    self.data_collector["Application_Step_Description_4"] = self.step_text4_var.get()
                    self.data_collector["Application_Steps_Widget_4"] = self.step4_image4.get()
                if final_step_index == 5:
                    self.data_collector["Application_Step_Description_5"] = self.step_text5_var.get()
                    self.data_collector["Application_Steps_Widget_5"] = self.step5_image5.get()
                if final_step_index == 6:
                    self.data_collector["Application_Step_Description_6"] = self.step_text6_var.get()
                    self.data_collector["Application_Steps_Widget_6"] = self.step6_image6.get()
                if final_step_index == 7:
                    self.data_collector["Application_Step_Description_7"] = self.step_text7_var.get()
                    self.data_collector["Application_Steps_Widget_7"] = self.step7_image7.get()
                if final_step_index == 8:
                    self.data_collector["Application_Step_Description_8"] = self.step_text8_var.get()
                    self.data_collector["Application_Steps_Widget_8"] = self.step8_image8.get()
                final_step_index += 1
            self.data_collector["Apply_External_Link"] = self.htmlvar.get()
        if index == 4:
            text_notes = self.create_question_text.get("1.0", tk.END)
            #self.data_collector["IP_Questions"]=self.add_new_lines(text_notes,70)
            self.data_collector["IP_Questions"] = self.create_question_text.get("1.0",tk.END)

            self.data_collector["Lesson_Type"] = ""
            self.data_collector["Lesson_Template"] = ""
            self.data_collector["Application_Mode"] = "Activity"
            self.data_collector['Answer_Key'] = ""
            self.data_collector['Video_Audio_Assessment_Flag']= ""
            self.data_collector['Application_Video_Link'] = ""
            self.data_collector['Application_Video_Running_Notes'] = ""
            self.data_collector['NumberOfQuestions'] = ""

    def add_new_lines(self,text_notes,wrap_length):
        logger.info("Inside add_new_lines of edit screen")
        string_list = []
        for i in range(0,len(text_notes),wrap_length):
            string_list.append(text_notes[i:i+wrap_length])
        return '\n'.join(string_list)



    def next_page(self):
        logger.info("Inside next_page of edit screen")
        if (self.index == 1):
            self.title_frame.grid_forget()
            self.process_save(self.index)
            self.create_factual_edit_page(self.to_edit_lesson)
            self.factual_frame.grid(row=0,column=0,pady=20,sticky=tk.NSEW)

            return
        if (self.index == 2):
            self.factual_frame.grid_forget()
            self.process_save(self.index)
            self.create_application_edit_page(self.to_edit_lesson)
            self.apply_activity_frame.grid(row=0, column=0, pady=50, sticky=tk.NSEW)

            return
        if (self.index == 3):
            self.apply_activity_frame.grid_forget()
            self.process_save(self.index)
            self.create_ip_edit_page(self.to_edit_lesson)
            self.next_button.configure(text="Submit")
            self.ip_frame.grid(row=0, column=0, pady=50, sticky=tk.NSEW)
            return
        if (self.index == 4):
            #self.ip_frame.grid_forget()
            self.process_save(self.index)
            self.save_data()
            #self.parent.destroy()


    def previous_page(self):
        logger.info("Inside previous_page of edit screen")
        self.next_button.config(text='Next')
        if self.index == 2:
            self.index = 1
            self.factual_frame.grid_forget()
            self.title_frame.grid(row=0,column=0,pady=50,sticky=tk.NSEW)
            return
        if self.index == 3:
            self.index = 2
            self.apply_activity_frame.grid_forget()
            self.factual_frame.grid(row=0,column=0,pady=20,sticky=tk.NSEW)
            return
        if self.index == 4:
            self.index = 3
            self.ip_frame.grid_forget()
            self.apply_activity_frame.grid(row=0, column=0, pady=50, sticky=tk.NSEW)



#if __name__== "__main__":
       #pass
       #  edit_app = tk.Tk()
       #  edit_app.title("Edit Learning Room Wizard")
       #  edit_app.selected_lessons = ""
       #  edit_app.geometry("1000x600")
       #  edit_app.configure(background='gray22')
       #
       #
       #  frame = MagicEditWizard(edit_app)
       # # edit_app.rowconfigure(0,weight=1)
       #  edit_app.columnconfigure(0,weight=1)
       #  frame.grid(row=0,column=0,pady=20)
       #  edit_app.mainloop()

