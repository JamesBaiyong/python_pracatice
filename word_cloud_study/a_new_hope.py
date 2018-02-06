#coding=utf-8
#自定义词云的色彩

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud,STOPWORDS

#自定义词云颜色函数
def gtey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
	return 'hsl(0,0%%,%d%%)' % random.randint(60,100)

mask = np.array(Image.open('./img/stormtrooper_mask.png'))
text = open('./txt/a_new_hope.txt').read()

text=text.replace('HAN','Bai')
text=text.replace('LUKE','Yong')

stopword=set(STOPWORDS)
stopword.add('int')
stopword.add('ext')

wc = WordCloud(max_words=1000,mask=mask,stopwords=stopword,margin=10,random_state=1).generate(text)
default_colors=wc.to_array()
plt.title('Custom colors')
plt.imshow(wc.recolor(color_func=gtey_color_func,random_state=3),interpolation='bilinear')
wc.to_file('./img/a_new_hope_CustomColors.png')
plt.axis('off')
plt.figure()

wc = WordCloud(max_words=1000,mask=mask,stopwords=stopword,margin=10,random_state=1).generate(text)
plt.title('Default colors')
plt.imshow(default_colors,interpolation='bilinear')
wc.to_file('./img/a_new_hope_DefaultColors.png')
plt.axis('off')
plt.show()
