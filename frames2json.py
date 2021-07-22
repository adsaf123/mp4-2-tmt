import json
from PIL import Image

to_json = [[["" for i in range(24)] for j in range(32)] for k in range(6569)]

for i in range(6569):
    img = Image.open("mini/" + str(i) + ".jpg")
    for x in range(32):
        for y in range(24):
            col = img.getpixel((x, y))
            to_json[i][x][y] = '#%02x%02x%02x' % col

file = open("precomp.js", "w")
file.write("var images = JSON.parse(\'" + json.dumps(to_json) + "\')")

print("Done")