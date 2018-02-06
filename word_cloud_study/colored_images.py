#coding=utf-8
#采用图片的配色方案制作词云

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image

text = open('./txt/alice.txt').read()

alice_coloring= np.array(Image.open('./img/alice_color.png'))

stopwords=set(STOPWORDS)
stopwords.add('said')

wc = WordCloud(background_color='white',max_words=2000,mask=alice_coloring,stopwords=stopwords,max_font_size=40,random_state=42)
wc.generate(text)

imge_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.figure()

plt.imshow(wc.recolor(color_func=imge_colors),interpolation='bilinear')
wc.to_file('./img/alice_colored.png')
plt.axis('off')
plt.figure()

plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()