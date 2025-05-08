import customtkinter as ctk
from config import GPA_SCALE

def mark_color(markLabel, average):
    if average is None:
        markLabel.configure(text="No Marks Available")
    elif 100 >= average >= 90:
        markLabel.configure(text_color="#3d7dcc")
    elif 90 >= average >= 80:
        markLabel.configure(text_color="#92c91c")
    elif 80 >= average >= 70:
        markLabel.configure(text_color="#4d9e3a")
    elif 70 >= average >= 60:
        markLabel.configure(text_color="#c98a1c")
    elif 60 >= average >= 50:
        markLabel.configure(text_color="#c91c1c")
    elif 49 <= average:
        markLabel.configure(text_color="gray")

def update_GPA_SCALE(new_scale: list[dict]):
    GPA_SCALE.clear()
    GPA_SCALE.extend(new_scale)
