# This file contains constants used in the application.
# It includes the application name, version, and file paths for icons and images.
# The constants are used throughout the application to maintain consistency and avoid hardcoding values.
# Constants for the application
import customtkinter as ctk
from PIL import Image

APP_NAME = "MarkManager"
APP_VERSION = "1.0.0"
DEFAULT_WINDOW_SIZE = "1280x720"

# GRAPHIC
button_fg = "#858585"
button_hover = "#c3c0c0"
frame_color = "#333333"

# BACKEND
GPA_SCALE = [
    {"min": 90, "max": 100, "letter": "A+", "gpa": 4.33},
    {"min": 85, "max": 89,  "letter": "A",  "gpa": 4.00},
    {"min": 80, "max": 84,  "letter": "A-", "gpa": 3.67},
    {"min": 77, "max": 79,  "letter": "B+", "gpa": 3.33},
    {"min": 73, "max": 76,  "letter": "B",  "gpa": 3.00},
    {"min": 70, "max": 72,  "letter": "B-", "gpa": 2.67},
    {"min": 67, "max": 69,  "letter": "C+", "gpa": 2.33},
    {"min": 63, "max": 66,  "letter": "C",  "gpa": 2.00},
    {"min": 60, "max": 62,  "letter": "C-", "gpa": 1.67},
    {"min": 57, "max": 59,  "letter": "D+", "gpa": 1.33},
    {"min": 53, "max": 56,  "letter": "D",  "gpa": 1.00},
    {"min": 50, "max": 52,  "letter": "D-", "gpa": 0.67},
    {"min": 0,  "max": 49,  "letter": "F",  "gpa": 0.00}
]

