import Image
import ImageDraw

img = Image.open("grass.png")
draw = ImageDraw.Draw(img)
texto = "sapoha pega mesmo spoakspoakpsokaop"
pos = 50,50
draw.text(pos, texto)
img.save("foto_exemplo.jpg")