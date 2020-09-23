# Ionic Icon helper to overwrite old icons with the required sizes.

import sys
import os
from PIL import Image
from copy import copy

input_image = sys.argv[1]
output_folder = sys.argv[2]

icon = Image.open(input_image).convert("RGBA")

for _, _, files in os.walk("./"):
    for item in files:
        if not item.endswith("png"):
            continue
        item = str(item)
        print(item)

        prefix = "icon-"
        try:
            _, rest = item.split(prefix, 1)
        except ValueError:
            _, rest = item.split(prefix.rstrip("-"), 1)

        size, _ = rest.split(".png")

        if "@" in size:
            pixels, zoom = size.split("@")

            if pixels == 'small':
                pixels = 29
            elif pixels == '':
                pixels = 57
            else:
                pixels = float(pixels)

            zoom = int(zoom.rstrip("x"))
        else:
            try:
                pixels = float(size)
            except ValueError:
                pixels = 29
            zoom = 1

        pixels = int(pixels * zoom)
        print(pixels)

        resized_icon = copy(icon)

        resized_icon = resized_icon.resize((pixels, pixels), Image.BILINEAR)

        output = os.path.join(output_folder, item)
        print("Writing to ", output)
        resized_icon.save(output)



