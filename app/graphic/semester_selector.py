import customtkinter as ctk
from app.assets.ctk_assets.fonts import get_fonts
from app.logic.term_manager import handle_semesters, get_current_semester, get_semesters

def display_semester_selector(parent):
    boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont = get_fonts() # Load fonts
    semDropdown = ctk.CTkOptionMenu(master=parent, values=get_semesters(), font=buttonBoldFont, fg_color="#858585",
                                    button_color="#626262", button_hover_color="#c3c0c0", command=handle_semesters)
    semDropdown.place(relx=0.035, rely=0.04)
    semDropdown.set(get_current_semester()) # Set the current semester as the default value