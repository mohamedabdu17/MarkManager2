import customtkinter as ctk
from config import APP_NAME, DEFAULT_WINDOW_SIZE
from app.logic.term_manager import handle_semesters
from app.assets.ctk_assets.fonts import get_fonts
from app.graphic.courses import display_courses
from app.graphic.finals_calculator import display_finals_calculator

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        handle_semesters("init")
        
        self.title(APP_NAME)
        self.geometry(DEFAULT_WINDOW_SIZE)

        boldFont, buttonBoldFont, coursesBoldFont, popupBoldFont = get_fonts() # Load fonts

        contentFrame = ctk.CTkScrollableFrame(self, corner_radius=20) 
        contentFrame.place(relx=0.30, rely=0.01, relwidth=0.69, relheight=0.98)

        optionsFrame = ctk.CTkFrame(self, corner_radius=20)
        optionsFrame.place(relx=0.01, rely=0.01, relwidth=0.275, relheight=0.98)

        optionsTitle = ctk.CTkLabel(master=optionsFrame, text="Options", font=boldFont)
        optionsTitle.pack(pady=20)

        display_courses(contentFrame)
        display_finals_calculator(optionsFrame)

if __name__ == "__main__":
    app = App()
    app.mainloop()