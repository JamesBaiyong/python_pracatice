# coding=utf-8

from wordcloud import WordCloud

# 读取制作词云文本
text = open('./txt/constitution.txt').read()

# 生成词云制作对象
wordcloud = WordCloud().generate(text)
wordcloud.to_file('./img/simple.png')

import matplotlib.pyplot as plt

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()



