import customtkinter as ctk
from constants import *
from app.graphic.courses import display_courses
from app.logic.terms import handle_semesters

boldFont = ctk.CTkFont(family="Arial", size=40, weight="bold")
buttonBoldFont = ctk.CTkFont(family="Arial", weight="bold")
coursesBoldFont = ctk.CTkFont(family="Arial", size=20, weight="bold")
popupBoldFont = ctk.CTkFont(family="Arial", size=15, weight="bold")

backArrow = ctk.CTkImage(light_image=Image.open("app/assets/back.png"), size=(15, 15))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        handle_semesters("init")
        
        self.title(APP_NAME)
        self.geometry(DEFAULT_WINDOW_SIZE)

        contentFrame = ctk.CTkScrollableFrame(self, corner_radius=20)
        contentFrame.place(relx=0.30, rely=0.01, relwidth=0.69, relheight=0.98)

        optionsFrame = ctk.CTkFrame(self, corner_radius=20)
        optionsFrame.place(relx=0.01, rely=0.01, relwidth=0.275, relheight=0.98)

        coursesTitle = ctk.CTkLabel(master=contentFrame, text="Courses", font=boldFont)
        coursesTitle.pack(pady=20)

        optionsTitle = ctk.CTkLabel(master=optionsFrame, text="Options", font=boldFont)
        optionsTitle.pack(pady=20)

        display_courses(contentFrame, coursesBoldFont)



if __name__ == "__main__":
    app = App()
    app.mainloop()