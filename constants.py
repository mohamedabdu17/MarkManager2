# This file contains constants used in the application.
# It includes the application name, version, and file paths for icons and images.
# The constants are used throughout the application to maintain consistency and avoid hardcoding values.
# Constants for the application
import customtkinter as ctk
from PIL import Image

APP_NAME = "MarkManager"
DEFAULT_WINDOW_SIZE = "1280x720"

# GRAPHIC ASSETS
def markColor(markLabel, average):
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
        markLabel.configure(text_color="c91c1c")