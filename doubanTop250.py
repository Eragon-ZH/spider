#doubanTop250 V2.0
import requests
import time
import random
from bs4 import BeautifulSoup
import re

def getHTMLText(url,code = 'utf-8'):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
	#据说可以避免HttpConnectionPool:Max retries exceeded with url的问题
	requests.adapters.DEFAULT_RETRIES = 5  
	text = requests.get(url,headers = headers)
	text.encoding = code
	# print(text.text)
	print(text.status_code)
	return text.text


def soup(html):
	soup = BeautifulSoup(html,'html.parser')
	movie_list_soup = soup.find('ol',attrs = {'class':'grid_view'})
	movie_list = []
	directer_list = []
	score_list = []
	quote_list = []
	people_list = []
	date_list = []
	for movie_li in movie_list_soup.find_all('li'):
		title = movie_li.find('div',attrs = {'class':'hd'})
		movie_name = title.find('span',attrs = {'class':'title'}).getText()
		detiles = movie_li.find('div',attrs = {'class':'bd'})
		#去掉...再按照/进行划分
		#directer的一堆复杂操作都是对字符串进行格式化
		directer = ''.join(''.join(detiles.find('p').getText().split()).rsplit('...'))
		date = re.findall(r'\d{4}',directer)
		directer = re.sub(r'\d{4}','',directer)
		#为了输出对齐去掉了人员的英文名，结果还是对不齐
		directer = re.sub(r'[a-zA-Z]*','',directer)
		directer = directer.rsplit('/',2)
		directer[0] = re.sub(r'/$','',directer[0])
		
		score = detiles.find('div',attrs = {'class':'star'}).find('span',attrs = {'class':'rating_num'}).getText()
		peoplesoup = detiles.find('div',attrs = {'class':'star'})
		people = re.findall(r'\d{4,7}',peoplesoup.getText())
		quote  = detiles.find('p',attrs = {'class':'quote'})
		if quote:
			quote = quote.find('span',attrs = {'class':'inq'}).getText()
		#说的就是你，小萝莉的猴神大叔还有聚焦
		else:
			quote = '豆瓣没写我有什么办法'
		movie_list.append(movie_name)
		directer_list.append(directer)
		date_list.append(date)
		score_list.append(score)
		quote_list.append(quote)
		people_list.append(people)
		# print(date)
		# print(directer)
		# print(score)
		# print(quote)
		# print(people)
	#获取下一页的地址
	next_page = soup.find('span',attrs = {'class':'next'}).find('a')
	if next_page:
		return movie_list,directer_list,date_list,quote_list,people_list,score_list,'http://movie.douban.com/top250' + next_page['href']
	return movie_list,directer_list,date_list,quote_list,people_list,score_list,None
		
def main():
	url = 'http://movie.douban.com/top250/'
	K = 1
	while url:
		text = getHTMLText(url)
		# print(text[:100])
		movie_list,directer_list,date_list,quote_list,people_list,score_list,url = soup(text)
		#我知道这个输出很智障但这样也对不齐妈个鸡
		tplt = '{0:{9}<5}\t{1:{10}<10}\t{2:{11}<35}\t{3:{12}<10}\t{4:{13}<10}\t{5:{14}<5}\t{6:{15}<30}\t{7:{16}<10}\t{8:{17}<5}'
		print(movie_list)
		print('\n')
		with open('G:/python/doubanTop250 2.0.txt', 'a', encoding='utf-8') as f:
			for i in range(len(movie_list)):
				f.write(tplt.format(K+i,movie_list[i],directer_list[i][0],directer_list[i][1],directer_list[i][2],date_list[i][0],quote_list[i],people_list[i][0],score_list[i],chr(12288),chr(12288),chr(12288),chr(12288),chr(12288),chr(12288),chr(12288),chr(12288),chr(12288))+'\n')
		K += 25
		#第一次没有sleep而且循环写错了同一个页面连续访问上百次被豆瓣封了IP......
		time.sleep(random.uniform(1,8))
main()