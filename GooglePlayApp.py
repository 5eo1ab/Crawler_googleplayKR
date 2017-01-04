########################
# GooglePlayApp.py
# 2017.1.4
########################

import googleplaylib as lib

class GooglePlayApp :

	def __init__(self, url) :
		soup, app_id = lib.url_connect(url)
		dic_p = lib.get_primary_info(soup)
		dic_s = lib.get_secondary_info(soup)
		self.appid = app_id
		self.title = dic_p['title']
		self.developer = dic_p['developer']
		self.category = dic_p['category']
		self.description = dic_p['description']
		self.score = dic_s['score']
		self.review_num = dic_s['review_num']
		self.updated_date = dic_s['updated_date']
		self.download_volumn = dic_s['download_volumn']
		self.contents_rating = dic_s['contents_rating']

	def __call__(self) :
		print("AppID:\t{0}\nTitle:\t{1}\ndeveloper:\t{2}\ncategory:\t{3}\n".format(self.appid, self.title, self.developer, self.category))
		print("score:\t{0}\nreview_num:\t{1}\nupdated_date:\t{2}\ndownload_volumn:\t{3}\ncontents_rating:\t{4}\n".format(self.score, self.review_num,self.updated_date,self.download_volumn,self.contents_rating))
		print("description:\n{0}".format(self.description))
