import customtkinter as ctk

def get_fonts():
    boldFont = ctk.CTkFont(family="Arial", size=40, weight="bold")
    buttonBoldFont = ctk.CTkFont(family="Arial", weight="bold")
    coursesBoldFont = ctk.CTkFont(family="Arial", size=20, weight="bold")
    popupBoldFont = ctk.CTkFont(family="Arial", size=15, weight="bold")
    
    return boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont