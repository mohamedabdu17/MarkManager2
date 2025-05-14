import customtkinter as ctk
from config import button_fg, button_hover, frame_color
from utils import mark_color
from app.assets.ctk_assets.fonts import get_fonts
from app.assets.ctk_assets.icons import get_icons
from app.graphic.semester_selector import display_semester_selector
from app.logic.database_manager import fetchCourses
from app.logic.term_manager import get_current_semester

def display_courses(parent):
    global boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont
    global backArrow, crossIcon
    boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont = get_fonts()
    backArrow, crossIcon = get_icons()
    for i in parent.winfo_children():
        i.destroy()

    display_semester_selector(parent)

    coursesTitle = ctk.CTkLabel(master=parent, text="Courses", font=boldFont)
    coursesTitle.pack(pady=20)

    courses = fetchCourses()
    if not courses:
        noCoursesLabel = ctk.CTkLabel(parent, text="No courses available", font=boldFont)
        noCoursesLabel.pack(pady=225)
    else:
        for course in courses:
            code, title, average, semester, letterGrade, gpa = course  # Unpacks tuple returned from fetchCourses()
            if semester == get_current_semester():
                courseFrame = ctk.CTkFrame(parent, height=100, corner_radius=20, fg_color=frame_color)
                courseFrame.pack(fill="x", padx=10, pady=10)
                courseFrame.pack_propagate(False)

                markLabel = ctk.CTkLabel(master=courseFrame, text=f"{average}% ({letterGrade})", font=coursesBoldFont)
                mark_color(markLabel, average)
                markLabel.pack(side="right", padx=15)

                courseLabel = ctk.CTkLabel(master=courseFrame, text=f"{code} - {title}", font=coursesBoldFont)
                courseLabel.pack(pady=15, padx=15, anchor="nw")

                from app.graphic.assessments import display_assessments
                openCourseButton = ctk.CTkButton(master=courseFrame, text="Open Course", font=buttonBoldFont,
                                                 fg_color=button_fg, hover_color=button_hover,
                                                 command=lambda courseCode=code: display_assessments(parent, courseCode))
                openCourseButton.pack(padx=15, anchor="sw")
                
def display_course_options(parent):
    addCourseButton = ctk.CTkButton(parent, text="Add Course", font=buttonBoldFont,
                                     fg_color=button_fg, hover_color=button_hover,
                                     command=lambda: add_course())
    addCourseButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.05)

    editCoursesButton = ctk.CTkButton(parent, text="Edit Course", font=buttonBoldFont,
                                     fg_color=button_fg, hover_color=button_hover,
                                     command=lambda: edit_course())
    editCoursesButton.place(relx=0.85, rely=0.05, relwidth=0.25, relheight=0.05)
    
def add_course():
    pass

def remove_course():
    pass

def edit_course():
    pass