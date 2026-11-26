import os

LINE = "Sorry, I heard 'order 400 tacos' instead of 'play soft jazz'. The tacos are already on their way. Please enjoy them."

assert "\n" not in LINE

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as out:
    print(LINE, file=out)
