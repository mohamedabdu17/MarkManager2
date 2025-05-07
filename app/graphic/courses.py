import customtkinter as ctk
from PIL import Image
from main import coursesBoldFont, buttonBoldFont, markColor
from app.logic.database_manager import fetchCourses
from app.logic.terms import get_current_semester
from assessments import display_assessments

def display_courses(parent, font):
    courses = fetchCourses()
    if not courses:
        noCoursesLabel = ctk.CTkLabel(parent, text="No courses available", font=font)
        noCoursesLabel.pack(pady=225)
    else:
        for course in courses:
            code, title, average, semester, letterGrade, gpa = course  # Unpacks tuple returned from fetchCourses()
            if semester == get_current_semester():
                courseFrame = ctk.CTkFrame(master=parent, height=100, corner_radius=20, fg_color="#333333")
                courseFrame.pack(fill="x", padx=10, pady=10)
                courseFrame.pack_propagate(False)

                markLabel = ctk.CTkLabel(master=courseFrame, text=f"{average}% ({letterGrade})", font=coursesBoldFont)
                markLabel.pack(side="right", padx=15)

                courseLabel = ctk.CTkLabel(master=courseFrame, text=f"{code} - {title}", font=coursesBoldFont)
                courseLabel.pack(pady=15, padx=15, anchor="nw")

                openCourseButton = ctk.CTkButton(master=courseFrame, text="Open Course", font=buttonBoldFont,
                                                 fg_color="#858585", hover_color="#c3c0c0",
                                                 command=lambda courseCode=code: display_assessments(courseCode))
                openCourseButton.pack(padx=15, anchor="sw")

                markColor(markLabel, average)