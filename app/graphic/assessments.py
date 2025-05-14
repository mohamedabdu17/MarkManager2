import customtkinter as ctk
from config import frame_color, button_fg, button_hover
from utils import mark_color
from app.assets.ctk_assets.fonts import get_fonts
from app.assets.ctk_assets.icons import get_icons
from app.logic.database_manager import fetchAssessments

def display_assessments(parent, code):
    global boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont
    global backArrow, crossIcon
    
    boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont = get_fonts()
    backArrow, crossIcon = get_icons()

    for i in parent.winfo_children(): # Clear the parent frame before displaying assessments
        i.destroy()
    
    from app.graphic.courses import display_courses
    backButton = ctk.CTkButton(master=parent, image=backArrow, text="", font=buttonBoldFont, 
                               fg_color=button_fg, hover_color=button_hover, command=lambda: display_courses(parent))
    backButton.place(relx=0.01, rely=0.01, relwidth=0.05, relheight=0.05)

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