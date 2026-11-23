import os

# One-Line Roast: The Gadget You Use Every Day (make.fun, program/v1)
# The entry is a single line, 1-200 characters, written to /output/entry.txt.

LINE = (
    "My wireless earbuds survive firmware updates, rainstorms and the washing "
    "machine — but not the 40 seconds it takes me to walk to the kitchen."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
