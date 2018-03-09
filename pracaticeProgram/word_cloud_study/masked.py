#coding=utf-8
#用图片做词云模板定制特定的词云

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

text = open('./txt/alice.txt').read()

alice_mask = np.array(Image.open('./img/alice_mask.png'))

stopwords = set(STOPWORDS)
stopwords.add('said')
#生成词云对象，并设置值
wc = WordCloud(background_color='white',max_font_size=2000,mask=alice_mask,stopwords=stopwords)
#生成词云
wc.generate(text)
#保存词云图
wc.to_file('./img/alice.png')

#展示效果
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(alice_mask,cmap=plt.cm.gray,interpolation='bilinear')
plt.axis('off')
plt.show()