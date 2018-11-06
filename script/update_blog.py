#coding=utf-8
import os

blog_path = 'blog_obj_path'
os.chdir(blog_path)

title = raw_input("Enter blog's title:")
comd="hexo new "+title
os.system(comd)
file = r'%s\source\_posts'%blog_path
os.startfile(file)

raw_input("Waiting .....")
print("start update")
os.chdir(blog_path)
os.system("hexo g")
os.system("xcopy public\*.* .deploy\jamesbaiyong.github.io\ /s/h/y")
os.chdir("%s\.deploy\jamesbaiyong.github.io"%blog_path)
os.system("git add .")
os.system("git commit -m\'update\'")
os.system("git push")

raw_input("Look .....")