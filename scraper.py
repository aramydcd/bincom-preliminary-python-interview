import re
from collections import Counter

# ==============================
#  DATA EXTRACTION & CLEANING
# ==============================

html_content = """
MONDAY: GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
TUESDAY: ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE
WEDNESDAY: GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE
THURSDAY: BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
FRIDAY: GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE
"""

# Find all words
raw_data = re.findall(r'\b[A-Z]+\b', html_content)

days = {'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY'}

# Extract the color value and Normalize spelling errors
colors = [
    "BLUE" if word == "BLEW" else
    "ASH" if word == "ARSH" else
    word
    for word in raw_data if word not in days
]

# Frequency Dictionary
color_freq = Counter(colors)