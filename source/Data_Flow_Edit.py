import os
import sqlite3
import sys
import traceback
from logging.handlers import RotatingFileHandler
from tkinter import messagebox
import logging

import assessment_generate
from snapshot_view import SnapshotView

LESSON_ID = 5

logger = logging.getLogger("MagicLogger")


file_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
db = file_root + os.path.sep + "MagicRoom.db"


saved_canvas = ""



def get_Lessons():
 try:
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    sql = "select Lesson_ID, Lesson_Title from Magic_Science_Lessons"
    cur.execute(sql)
    rows = cur.fetchall()
    list_lessons = []
    for element in rows:
        list_lessons.append(element)
    connection.commit()
    connection.close()
    return list_lessons
 except sqlite3.OperationalError:
     messagebox.showerror("DB Error", "Cannot Connect to Database")
     logger.exception("get_lessons() met with an error")


def select_lesson_data(lessonid):
    try:
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        sql = "select * from Magic_Science_Lessons where Lesson_ID =?"
        cur.execute(sql,(lessonid,))
        lesson_dict = [dict((cur.description[i][0], value) \
                  for i, value in enumerate(row)) for row in cur.fetchall()]
        cur.connection.close()
        return lesson_dict
    except sqlite3.OperationalError:
        messagebox.showerror("Database Issue", "Issue with database connection")
        logger.exception("Select Lesson Data met with an error")

def save_all_data(data_collector,lesson_file_manager,self):
    connection = sqlite3.connect(db)
    try:
        print(data_collector)

        cur = connection.cursor()
        for key, values in data_collector.items():
            print(key)
            print(values)
            if values is not None and isinstance(values,str):
                values = values.strip()
            sql = "update Magic_Science_Lessons set {} = ? where Lesson_ID = ?".format(key)
            cur.execute(sql, (values, LESSON_ID))

        connection.commit()
    except (sqlite3.OperationalError ):
        messagebox.showerror("Error Connecting to DB", "Saving the Information met with an error")
        connection.set_trace_callback(print)
        logger.exception("Saving data met with an error")

    try:

        snapshot = SnapshotView(self,LESSON_ID,lesson_file_manager.lesson_dir+os.path.sep+"notes_"+str(LESSON_ID)+".pdf")
    except:
        messagebox.showerror("Notes Generation","There was an error during notes generation")
        logger.exception("Notes generation met with an error")
    try:
        assessment = assessment_generate.generate_ip_paper(LESSON_ID,lesson_file_manager.lesson_dir+os.path.sep+"ip_"+str(LESSON_ID)+".pdf",db)
    except:
        messagebox.showerror("Assessment Generation", "There was an error during assessments/points generation",parent=self)
        logger.exception("Assessment generation met with an error")


    else:
        messagebox.showinfo("Content Created",
                            "Content created for you to view in the interactive player. \nNotes and Assessments modifield\n"
                            "This window shall close now",parent=self)
        logger.info("Lesson Record Modified")
        self.destroy()

#get_Title()

