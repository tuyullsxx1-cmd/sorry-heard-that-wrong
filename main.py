import os

LINE = "Sorry, I heard 'order 400 tacos' instead of 'play soft jazz'. The tacos are already on their way. Please enjoy them."

assert "\n" not in LINE
# print() supplies the single trailing newline the format requires.
assert len(LINE) <= 140
# The apology must name the wrong order: the tacos are the punchline.
assert "tacos" in LINE

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as out:
    print(LINE, file=out)
