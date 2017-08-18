
python词云
==========

本词云练习是按照[官方库](https://github.com/amueller/word_cloud)案例做的，基本上就是了解熟悉一下整个库的使用方式方法。

### 安装

#### pip安装

```` 
pip install wordcloud
````

#### whl文件安装

下载[.whl文件](http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)，使用pip install 安装,会自动安装依赖

### 案例

#### 简单生成词云

文件[simple.py](./simple.py)生成一个简单的词云案例

![简单生成词云](img/simple.png)

文件[simple_zh.py](./simple_zh.png)生成一个显示中文的默认词云

![中文词云](/img/simple_zh.png)

文件[masked.py](./masked.py)生成一个有固定图案的词云

![有图案的词云](/img/alice.png)

文件[colored_images.py](./colored_images.py)使用给定图片的配色方案制作词云

![有配色方案的词云](/img/alice_colored.png)

文件[a_new_hope.py](./a_new_hope.py)制作自定义词云的色彩

![自定义词云色彩](/img/a_new_hope_CustomColors.png)
