import sqlite3, os
import random, sys
import configparser
import traceback
from pathlib import Path
from tkinter import StringVar,messagebox

import assessment_generate
from snapshot_view import SnapshotView
import Lesson_File_Manager

LESSON_ID = 5

config = configparser.RawConfigParser()
two_up = Path(__file__).parents[2]
imageroot = ""
videoroot = ""


print(str(two_up)+'/magic.cfg')
try:
    config.read(str(two_up)+'/magic.cfg')
    db = config.get("section1",'file_root')+os.path.sep+'MagicRoom.db'
    file_root = config.get("section1",'file_root')
except configparser.NoSectionError:
    messagebox.showerror("Configuration Error", "No Section found or Configuration File Missing")
    sys.exit()

saved_canvas = ""
imageroot=file_root+os.path.sep+"Lessons"+os.path.sep+"Lesson"+str(LESSON_ID)+os.path.sep+"images"
videoroot=file_root+os.path.sep+"Lessons"+os.path.sep+"Lesson"+str(LESSON_ID)+os.path.sep+"videos"



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
     sys.exit()

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


def save_all_data(data_collector,lesson_file_manager):
    connection = sqlite3.connect(db)
    try:
        print(data_collector)

        cur = connection.cursor()
        for key, values in data_collector.items():
            print(key)
            print(values)
            sql = "update Magic_Science_Lessons set {} = ? where Lesson_ID = ?".format(key)
            cur.execute(sql, (values, LESSON_ID))

        connection.commit()
    except (sqlite3.OperationalError ):
        messagebox.showerror("Error Connecting to DB", "Saving the Information met with an error")
        connection.set_trace_callback(print)
        traceback.print_exc()

    try:
         snapshot = SnapshotView(None,LESSON_ID,lesson_file_manager.lesson_dir+os.path.sep+"notes_"+str(LESSON_ID)+".pdf")
    except:
        messagebox.showerror("Notes Generation","There was an error during notes generation")
        traceback.print_exc()
    try:
        assessment = assessment_generate.generate_ip_paper(LESSON_ID,lesson_file_manager.lesson_dir+os.path.sep+"ip_"+str(LESSON_ID)+".pdf",db)
    except:
        messagebox.showerror("Assessment Generation", "There was an error during assessments/points generation")
        traceback.print_exc()


    else:
        messagebox.showinfo("Content Created",
                            "Content created for you to view in the interactive player. \n Notes and Assessments modifield")

#get_Title()

