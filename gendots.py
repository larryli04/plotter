from PIL import Image
import sys
from pathlib import Path

def luminosity(r: int, g: int, b:int) -> int:
    return (int) (0.2126*r + 0.7152*g + 0.0722*b)

n = len(sys.argv)
if(n == 2):
    filename = Path(sys.argv[1])
elif(n > 2):
    print("Too many arguments. Please only provide the filepath")
    exit(1)
else:
    print("Please provide a filepath")
    exit(1)
 

# from an image, generate a dotmap

im = Image.open(filename)
width, height = im.size
print(width, height)

# print(f"Opened file {filename.name} with width {width} and height {height}")

im = im.convert('RGBA')
out = [[0 for _ in range(width)] for _ in range(height)]

for x in range(width):
    for y in range(height):
        r, g, b, _ = im.getpixel((x, y));
        print(luminosity(r, g, b), end=' ')
    print()

