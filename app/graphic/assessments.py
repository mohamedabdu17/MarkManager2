import customtkinter as ctk
from config import frame_color
from utils import mark_color
from app.assets.ctk_assets.fonts import get_fonts
from app.logic.database_manager import fetchAssessments

def display_assessments(parent, code):
    global boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont
    boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont = get_fonts()
    for i in parent.winfo_children(): # Clear the parent frame before displaying assessments
        i.destroy()

    assessments = fetchAssessments(code)
    if not assessments:
        noAssessLabel = ctk.CTkLabel(master=parent, text="No assessments available", font=boldFont)
        noAssessLabel.pack(pady=225)
    else:
        dividerText = "Name".ljust(93) + "Weight".ljust(20) + "Grade"
        nameLabel = ctk.CTkLabel(master=parent, text=dividerText, font=coursesBoldFont)
        nameLabel.pack(padx=10)
        for assessment in assessments:
            name, mark, weight = assessment # Unpacks tuple returned from fetchAssessments()

            assessFrame = ctk.CTkFrame(master=parent, height=100, corner_radius=20, fg_color=frame_color)
            assessFrame.pack(fill="x",pady=10, padx=10)

            markLabel = ctk.CTkLabel(master=assessFrame, text=f"{mark}%", font=coursesBoldFont)
            markLabel.pack(side="right", padx=15)

            weightLabel = ctk.CTkLabel(master=assessFrame, text=f"{weight}%", font=coursesBoldFont)
            weightLabel.pack(side="right", padx=80)

            courseLabel = ctk.CTkLabel(master=assessFrame, text=f"{name}", font=coursesBoldFont)
            courseLabel.pack(pady=15, padx=15, anchor="nw")

            mark_color(markLabel, mark)