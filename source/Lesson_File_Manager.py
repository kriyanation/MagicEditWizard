import logging
import os, sys

import traceback

from shutil import copyfile

logger = logging.getLogger("MagicLogger")

class LessonFileManager():
    def __init__(self,file_root,edit_lesson):
        print(file_root)
        self.image_path = file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(edit_lesson)+ os.path.sep + "images"
        self.video_path = file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(edit_lesson)+ os.path.sep + "videos"
        self.lesson_dir = file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(edit_lesson)
    def add_image_file(self,filepath):
        try:
            copyfile(filepath,self.image_path+os.path.sep+os.path.basename(filepath))
        except (IOError, OSError):
            print("Image File could not be copied")
            logger.exception("Image file could not copied edit screen")


    def add_video_file(self,filepath):
        try:
            copyfile(filepath, self.video_path + os.path.sep + os.path.basename(filepath))
        except (IOError, OSError):
            print("Video File could not be copied")
            logger.exception("Video file could not copied edit screen")

