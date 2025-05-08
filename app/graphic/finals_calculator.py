import customtkinter as ctk
from app.assets.ctk_assets.fonts import get_fonts


def display_finals_calculator(parent):
    global boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont
    boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont = get_fonts()
    
    calcFrame = ctk.CTkFrame(parent, width=300, height=275, corner_radius=20)
    calcFrame.pack(pady=20)
    calcFrame.pack_propagate(False)

    calcTitle = ctk.CTkLabel(master=calcFrame, text="Finals Calculator", font=coursesBoldFont)
    calcTitle.pack(pady=10)

    currentLabel = ctk.CTkLabel(master=calcFrame, text="Current Average:", font=popupBoldFont)
    currentLabel.pack()

    currentEntry = ctk.CTkEntry(master=calcFrame)
    currentEntry.pack()

    desiredLabel = ctk.CTkLabel(master=calcFrame, text="Desired Average:", font=popupBoldFont)
    desiredLabel.pack()

    desiredEntry = ctk.CTkEntry(master=calcFrame)
    desiredEntry.pack()

    weightLabel = ctk.CTkLabel(master=calcFrame, text="Final Evaluation Weight:", font=popupBoldFont)
    weightLabel.pack()

    weightEntry = ctk.CTkEntry(master=calcFrame)
    weightEntry.pack()

    submitButton = ctk.CTkButton(master=calcFrame, width=75, height=25, text="Submit", font=buttonBoldFont, fg_color="#858585", hover_color="#c3c0c0", command= lambda: handleSubmit())
    submitButton.pack(pady=15)