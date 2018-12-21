from PIL import Image
import os
src = "./data"
dst = "./resized_black/"

for each in os.listdir(src):
    png = Image.open(os.path.join(src,each))
    # print each
    if png.mode != 'RGB':
        png.load() # required for png.split()
        background = Image.new("RGB", png.size, (0,0,0))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
        background.convert('RGB')
        background.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
    else:
        png = png.convert('RGB')
        png.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
