'''
统计说说词频并绘制词云
'''
import jieba
import wordcloud

w = wordcloud.WordCloud(width=1000,font_path='msyh.ttc',height=700,max_words=200)

f = open("content.txt","rb")
text = f.read()
f.close()

words = jieba.lcut(text)  #分割成词语
w.generate(' '.join(words)) #空格隔开并赋给词云w

w.to_file('shuoshuo.png')
