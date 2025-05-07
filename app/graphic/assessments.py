import customtkinter as ctk
from PIL import Image
from constants import markColor
from app.logic.database_manager import fetchAssessments, fetchCourses
from main import coursesBoldFont, boldFont, contentFrame

def display_assessments(code):
    assessments = fetchAssessments(code)
    if not assessments:
        noEvalLabel = ctk.CTkLabel(master=contentFrame, text="No assessments available", font=boldFont)
        noEvalLabel.pack(pady=225)
    else:
        dividerText = "Name".ljust(93) + "Weight".ljust(20) + "Grade"
        nameLabel = ctk.CTkLabel(master=contentFrame, text=dividerText, font=coursesBoldFont)
        nameLabel.pack(padx=10)
        for assess in assessments:
            name, mark, weight = assess

            assessFrame = ctk.CTkFrame(master=contentFrame, height=100, corner_radius=20, fg_color="#333333")
            assessFrame.pack(fill="x",pady=10, padx=10)

            markLabel = ctk.CTkLabel(master=assessFrame, text=f"{mark}%", font=coursesBoldFont)
            markLabel.pack(side="right", padx=15)

            weightLabel = ctk.CTkLabel(master=assessFrame, text=f"{weight}%", font=coursesBoldFont)
            weightLabel.pack(side="right", padx=80)

            courseLabel = ctk.CTkLabel(master=assessFrame, text=f"{name}", font=coursesBoldFont)
            courseLabel.pack(pady=15, padx=15, anchor="nw")

            markColor(markLabel, mark)