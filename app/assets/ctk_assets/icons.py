import customtkinter as ctk
from PIL import Image

def get_icons():
    backArrow = ctk.CTkImage(light_image=Image.open("app/assets/images/back.png"), size=(15, 15))
    crossIcon = ctk.CTkImage(light_image=Image.open("app/assets/images/cross.png"), size=(15, 15))

    return backArrow, crossIcon