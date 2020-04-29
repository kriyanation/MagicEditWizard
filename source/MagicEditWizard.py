import tkinter as tk
from tkinter import Frame,ttk,messagebox, StringVar
import LessonList,Data_Flow,Edit_Utils


class MagicEditWizard(Frame):
    def __init__(self,parent,*args,**kwargs):

        super().__init__(*args, **kwargs)
        self.title_frame = Frame(self)
        self.index = 0
        self.factual_frame = Frame(self)
        self.apply_activity_frame = Frame(self)
        self.apply_activity_steps_frame = Frame(self.apply_activity_frame)
        self.rowconfigure(0, weight=1)
        self.configure(background='beige')
        self.columnconfigure(0, weight=1)
        self.title_frame.configure(background='beige')
        self.factual_frame.configure(background='beige')
        self.apply_activity_frame.configure(background='beige')
        self.apply_activity_steps_frame.configure(background='beige')
        s  = ttk.Style()
        self.bind("<Configure>",self.resize)
        s.theme_use('clam')

        s.configure('Edit.TLabelframe', background='beige')
        s.configure('Edit.TLabelframe.Label', font=('courier', 14, 'bold', 'italic'))
        s.configure('Edit.TLabelframe.Label', background='beige', foreground='brown')

        s.configure('Firebrick.Label', background='beige', foreground='dark blue', font=('courier', 9, 'bold'))

        s.configure('Green.TButton', background='firebrick', foreground='snow')
        s.configure('Green.TMenubutton', background='peachpuff2', foreground='firebrick')
        s.configure('Horizontal.Green.TScale', background='firebrick', foreground='snow')
        s.map('Green.TButton', background=[('active', '!disabled', 'maroon'), ('pressed', 'snow')],
              foreground=[('pressed', 'snow'), ('active', 'snow')])

        app = LessonList.MagicLessonList(bg='dark slate gray', fg='white', buttonbg='dark olive green',
                                       selectmode=tk.SINGLE,
                                        buttonfg='snow', parent=self)
        self.wait_window(app)
        print(self.selected_lessons)
        self.to_edit_lesson = self.selected_lessons[0]
        Data_Flow.LESSON_ID = int(self.to_edit_lesson)
        self.lesson_dict = Data_Flow.select_lesson_data(int(self.to_edit_lesson))
        print(self.lesson_dict)
        self.create_title_edit_page(8)
        bottom_frame = tk.Frame(parent, background="beige")
        next_button = ttk.Button(bottom_frame, text='Next', command=self.next_page, style='Green.TButton')
        back_button = ttk.Button(bottom_frame, text="Back", command=self.previous_page, style='Green.TButton')
        back_button.grid(row=0,column=0,padx=10)
        next_button.grid(row=0, column=1)
        bottom_frame.grid(sticky=tk.S)


    def resize(self,event):
        self.grid_forget()
        self.grid(row=0,column=0)

    def create_title_edit_page(self,edit_lesson):
        self.title_label = ttk.Label(self.title_frame, text="Title of your topic", style='Edit.TLabelframe.Label')
        self.title_text_var = StringVar()
        self.title_text_var.set((self.lesson_dict[0].get("Lesson_Title")))
        self.title_text = tk.Entry(self.title_frame,textvariable=self.title_text_var)

        self.title_image_label = ttk.Label(self.title_frame, text="Image Related to Title", style='Edit.TLabelframe.Label')
        self.title_image_button = ttk.Button(self.title_frame, text="Add Image", command=self.add_title_image, style='Green.TButton')
        self.title_image_video_label = ttk.Label(self.title_frame, text="Video Related to Title", style='Edit.TLabelframe.Label')
        self.title_video_button = ttk.Button(self.title_frame, text="Add Video", command=self.add_title_video, style='Green.TButton')

        self.title_running_notes_label = ttk.Label(self.title_frame, text="Running Notes", style='Edit.TLabelframe.Label')
        self.running_notes = self.lesson_dict[0].get("Title_Running_Notes")
        self.title_running_notes = tk.Text(self.title_frame, wrap=tk.WORD, width=30, height=5, pady=2)
        self.title_running_notes .insert("1.0",self.running_notes)

        self.video_var = StringVar()
        self.video_var.set(self.lesson_dict[0].get("Title_Video"))
        self.title_video_file_label = ttk.Label(self.title_frame,textvariable=self.video_var,style="Edit.TLabelframe.Label")
        self.image_var = StringVar()
        self.image_var.set(self.lesson_dict[0].get("Title_Image"))
        self.title_image_file_label = ttk.Label(self.title_frame, textvariable=self.image_var,style="Edit.TLabelframe.Label")


        self.title_label.grid(row=0,column=0,padx=20,pady=10)
        self.title_text.grid(row=0,column=1,padx=20,pady=10)
        self.title_image_label.grid(row=1,column=0,padx=20,pady=10)
        self.title_image_button.grid(row=1,column=1,padx=20,pady=10)
        self.title_image_video_label.grid(row=2,column=0,padx=20,pady=10)
        self.title_video_button.grid(row=2,column=1,padx=20,pady=10)
        self.title_running_notes_label.grid(row=3,column=0,padx=20,pady=10)
        self.title_running_notes.grid(row=3,column=1,padx=20,pady=10)
        self.title_image_file_label.grid(row=1, column=3,pady=10)
        self.title_video_file_label.grid(row=2, column=3,pady=10)
        self.title_frame.grid(row=0,column=0,pady=50,sticky=tk.NSEW)
        self.index += 1

    def create_factual_edit_page(self, edit_lesson):
        self.factual_image_var = StringVar()
        self.factual_text_term1_var = StringVar()
        self.factual_term_label = ttk.Label(self.factual_frame, text="Definition or New Term", style='Edit.TLabelframe.Label')
        self.factual_term_text = ttk.Entry(self.factual_frame,textvariable=self.factual_text_term1_var)
        self.factual_term_desc_text = tk.Text(self.factual_frame, wrap=tk.WORD, width=30, height=5)
        text_insert_desc1 = self.lesson_dict[0]["Factual_Term1_Description"]
        self.factual_term_desc_text.insert("1.0",text_insert_desc1)
        self.factual_text_term1_var.set(self.lesson_dict[0]["Factual_Term1"])
        self.factual_image_var.set(self.lesson_dict[0]["Factual_Image1"])
        self.factual_term_desc_label = ttk.Label(self.factual_frame, text="Description", style='Edit.TLabelframe.Label')
        self.factual_term_image_button = ttk.Button(self.factual_frame, text='Add Image',
                                               command=lambda id=2: self.add_factual_image(id), style='Green.TButton')
        self.factual_image_label = ttk.Label(self.factual_frame, textvariable=self.factual_image_var,
                                            style='Edit.TLabelframe.Label')


        self.factual_term_label.grid(row=0, column=0, pady=10)
        self.factual_term_text.grid(row=0, column=1, pady=10)

        self.factual_term_desc_label.grid(row=1, column=0, pady=10)
        self.factual_term_desc_text.grid(row=1, column=1, pady=10)
        text_insert_desc1 = self.lesson_dict[0]["Factual_Term1_Description"]
        self.factual_term_desc_text.insert("1.0", text_insert_desc1)
        self.factual_text_term1_var.set(self.lesson_dict[0]["Factual_Term1"])
        self.factual_image_var.set(self.lesson_dict[0]["Factual_Image1"])
        self.factual_term_image_button.grid(row=3,column=0,pady=10)
        self.factual_image_label.grid(row=3, column=3, pady=10)

        self.factual_image2_var = StringVar()
        self.factual_text_term2_var = StringVar()

        self.factual_term2_label = ttk.Label(self.factual_frame, text="Definition or New Term", style='Edit.TLabelframe.Label')
        self.factual_term2_text = ttk.Entry(self.factual_frame,textvariable=self.factual_text_term2_var)
        self.factual_term2_desc_text = tk.Text(self.factual_frame, wrap=tk.WORD, width=30, height=5)
        self.factual_term2_desc_label = ttk.Label(self.factual_frame, text="Description", style='Edit.TLabelframe.Label')
        self.factual_term2_image_button = ttk.Button(self.factual_frame, text='Add Image',
                                               command=lambda id=2: self.add_factual_image(id), style='Green.TButton')

        self.factual_image_label2 = ttk.Label(self.factual_frame, textvariable=self.factual_image2_var,
                                            style='Edit.TLabelframe.Label')
        self.factual_term2_label.grid(row=5, column=0, pady=10)
        self.factual_term2_text.grid(row=5, column=1, pady=10)
        self.factual_term2_desc_label.grid(row=6, column=0, pady=10)

        self.factual_term2_desc_text.grid(row=6, column=1, pady=10)
        text_insert_desc2 = self.lesson_dict[0]["Factual_Term2_Description"]
        self.factual_term2_desc_text.insert("1.0", text_insert_desc2)
        self.factual_text_term2_var.set(self.lesson_dict[0]["Factual_Term2"])
        self.factual_image2_var.set(self.lesson_dict[0]["Factual_Image2"])
        self.factual_term2_image_button.grid(row=7, column=0, pady=10)
        self.factual_image_label2.grid(row=7, column=3, pady=10)

        self.factual_image3_var = StringVar()
        self.factual_text_term3_var = StringVar()
        self.factual_term3_label = ttk.Label(self.factual_frame, text="Definition or New Term", style='Edit.TLabelframe.Label')
        self.factual_term3_text = ttk.Entry(self.factual_frame,textvariable=self.factual_text_term2_var)
        self.factual_term3_desc_text = tk.Text(self.factual_frame, wrap=tk.WORD, width=30, height=5)
        self.factual_term3_desc_label = ttk.Label(self.factual_frame, text="Description", style='Edit.TLabelframe.Label')
        self.factual_term3_image_button = ttk.Button(self.factual_frame, text='Add Image',
                                               command=lambda id=2: self.add_factual_image(id), style='Green.TButton')
        self.factual_image_label3 = ttk.Label(self.factual_frame, textvariable=self.factual_image3_var,
                                              style='Edit.TLabelframe.Label')
        self.factual_term3_label.grid(row=9, column=0, pady=10)
        self.factual_term3_text.grid(row=9, column=1, pady=10)
        self.factual_term3_desc_label.grid(row=10, column=0, pady=10)
        self.factual_term3_desc_text.grid(row=10, column=1, pady=10)
        text_insert_desc3 = self.lesson_dict[0]["Factual_Term3_Description"]
        self.factual_term3_desc_text.insert("1.0", text_insert_desc3)
        self.factual_text_term3_var.set(self.lesson_dict[0]["Factual_Term3"])
        self.factual_image3_var.set(self.lesson_dict[0]["Factual_Image3"])
        self.factual_term3_image_button.grid(row=11, column=0, pady=10)
        self.factual_image_label3.grid(row=11, column=3, pady=10)
        self.index = 2

    def create_application_edit_page(self, edit_lesson):


        self.apply_steps_label = ttk.Label(self.apply_activity_frame, text="Number of Steps?", style='Edit.TLabelframe.Label')
        self.selected_steps = tk.StringVar()
        self.selected_steps.set(str(self.lesson_dict[0]["Application_Steps_Number"]))
        print("sdasdas"+self.selected_steps.get())
        self.apply_steps_dropdown = tk.OptionMenu(self.apply_activity_frame, self.selected_steps, '0', '1', '2', '3', '4', '5', '6', '7', '8',
                                                  command=self.show_individual_steps)
        self.apply_steps_dropdown.configure(background="beige")
        self.apply_steps_dropdown["menu"].configure(background="beige")
        self.apply_steps_label.grid(row=0, column=0, pady=10,padx=5)
        self.apply_steps_dropdown.grid(row=0, column=1)

        self.number_of_steps = self.lesson_dict[0]['Application_Steps_Number']
        self.configure_steps(self.number_of_steps)

    def show_individual_steps(self,selected_number):

        for widget in self.apply_activity_steps_frame.winfo_children():
             widget.destroy()
        self.configure_steps(int(selected_number))




    def configure_steps(self,number_of_steps):
        self.step_text1 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text2 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text3 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text4 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text5 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text6 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text7 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_text8 = ttk.Entry(self.apply_activity_steps_frame)
        self.step_image_button1 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button2 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button3 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button4 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button5 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button6 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button7 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')
        self.step_image_button8 = ttk.Button(self.apply_activity_steps_frame, text='Add Image', style='Green.TButton')

        self.step1_image1 = StringVar()
        self.step2_image2 = StringVar()
        self.step3_image3 = StringVar()
        self.step4_image4 = StringVar()
        self.step5_image5 = StringVar()
        self.step6_image6 = StringVar()
        self.step7_image7 = StringVar()
        self.step8_image8 = StringVar()

        self.step1_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step1_image1,
                                     style='Edit.TLabelframe.Label')
        self.step2_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step2_image2,
                                     style='Edit.TLabelframe.Label')
        self.step3_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step3_image3,
                                     style='Edit.TLabelframe.Label')
        self.step4_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step4_image4,
                                     style='Edit.TLabelframe.Label')
        self.step5_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step5_image5,
                                     style='Edit.TLabelframe.Label')
        self.step6_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step6_image6,
                                     style='Edit.TLabelframe.Label')
        self.step7_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step7_image7,
                                     style='Edit.TLabelframe.Label')
        self.step8_label = ttk.Label(self.apply_activity_steps_frame, textvariable=self.step8_image8,
                                     style='Edit.TLabelframe.Label')

        steps = 1
        while steps < number_of_steps + 1:
            self.step_label = ttk.Label(self.apply_activity_steps_frame, text="Step Description",
                                        style='Edit.TLabelframe.Label')
            if steps == 1:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text1.grid(row=steps, column=1, padx=20)
                self.step_image_button1.grid(row=steps, column=2, padx=20)
                self.step1_label.grid(row=steps, column=4)
            if steps == 2:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text2.grid(row=steps, column=1, padx=20)
                self.step_image_button2.grid(row=steps, column=2, padx=20)
                self.step2_label.grid(row=steps, column=4)
            if steps == 3:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text3.grid(row=steps, column=1, padx=20)
                self.step_image_button3.grid(row=steps, column=2, padx=20)
                self.step3_label.grid(row=steps, column=4)
            if steps == 4:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text4.grid(row=steps, column=1, padx=20)
                self.step_image_button4.grid(row=steps, column=2, padx=20)
                self.step4_label.grid(row=steps, column=4)
            if steps == 5:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text5.grid(row=steps, column=1, padx=20)
                self.step_image_button5.grid(row=steps, column=2, padx=20)
                self.step5_label.grid(row=steps, column=4)
            if steps == 6:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text6.grid(row=steps, column=1, padx=20)
                self.step_image_button6.grid(row=steps, column=2, padx=20)
                self.step6_label.grid(row=steps, column=4)
            if steps == 7:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text7.grid(row=steps, column=1, padx=20)
                self.step_image_button7.grid(row=steps, column=2, padx=20)
                self.step7_label.grid(row=steps, column=4)
            if steps == 8:
                self.step_label.grid(row=steps, column=0, padx=20)
                self.step_text8.grid(row=steps, column=1, padx=20)
                self.step_image_button8.grid(row=steps, column=2, padx=20)
                self.step8_label.grid(row=steps, column=4)
            steps += 1
            self.apply_activity_steps_frame.grid(row=1,column=0,columnspan=2)

    def create_ip_edit_page(self, edit_lesson):
        pass

    def add_title_image(self):

        self.title_image_path_full, title_image_basename = Edit_Utils.add_file(Data_Flow.file_root)
        self.image_var.set(title_image_basename)
        pass

    def add_factual_image(self):

        self.factual_image_path_full, factual_image_basename = Edit_Utils.add_file(Data_Flow.file_root)
        self.factual_image_var.set(factual_image_basename)

    def add_title_video(self):

        self.title_video_path_full, title_video_basename = Edit_Utils.add_file(Data_Flow.file_root)
        self.video_var.set(title_video_basename)

    def next_page(self):
        if (self.index == 1):
            self.title_frame.grid_forget()
            self.create_factual_edit_page(self.to_edit_lesson)
            self.factual_frame.grid(row=0,column=0,pady=50,sticky=tk.NSEW)
            return
        if (self.index == 2):
            self.factual_frame.grid_forget()
            self.create_application_edit_page(self.to_edit_lesson)
            self.apply_activity_frame.grid(row=0, column=0, pady=50, sticky=tk.NSEW)

    def previous_page(self):
        pass

if __name__== "__main__":
        edit_app = tk.Tk()
        edit_app.title("Edit Learning Room Wizard")
        edit_app.selected_lessons = ""
        edit_app.geometry("600x600")
        edit_app.configure(background='beige')


        frame = MagicEditWizard(edit_app)
       # edit_app.rowconfigure(0,weight=1)
        edit_app.columnconfigure(0,weight=1)
        frame.grid(row=0,column=0,pady=20)
        edit_app.mainloop()
