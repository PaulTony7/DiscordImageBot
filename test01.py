from PIL import Image, ImageFont, ImageDraw

my_img = Image.open('duda.jpg')
font = ImageFont.truetype('Roboto-Regular.ttf', 40)
text = 'Witam na otwarciu parasola'
image_edit = ImageDraw.Draw(my_img)
image_edit.text((15, 15), text, (255, 255, 255), font=font)
my_img.save('res.jpg')