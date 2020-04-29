import sqlite3, os
import random, sys
import configparser
from pathlib import Path
from tkinter import StringVar,messagebox
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


#get_Title()
