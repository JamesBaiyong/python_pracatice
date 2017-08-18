#coding=utf-8
from PIL import Image,ImageFilter

im = Image.open('D:\\macos06.jpg')
w,h=im.size
im.thumbnail((w//2,h//2))
im.save('D:\\macos07.jpg','jpeg')

#模糊效果
im2=im.filter(ImageFilter.BLUR)
im2.save('D:\\macos08.jpg','jpeg')