#coding=utf-8
#用中文文本做词云

import jieba
from wordcloud import  WordCloud
import matplotlib.pyplot as plt

#读取中文文本，并对其做分词
zh_text=open("./txt/coder.txt").read()
mytext=" ".join(jieba.cut(zh_text))

wordcloud = WordCloud(font_path="./font/simsun.ttf").generate(mytext)

plt.imshow(wordcloud,interpolation="bilinear")
wordcloud.to_file('./img/simple_zh.png')
plt.axis("off")
plt.show()