########################
# crawler_test.py
# 2017.1.4
########################

from GooglePlayApp import GooglePlayApp

url = "https://play.google.com/store/apps/details?id=com.imagedrome.jihachul"
test = GooglePlayApp(url)
test()

url_samples = [
"https://play.google.com/store/apps/details?id=com.idincu.ovey.android",
"https://play.google.com/store/apps/details?id=com.ykikisoft.lj.savvy_sister",
"https://play.google.com/store/apps/details?id=com.quickhero.client"
]
entities = [GooglePlayApp(url) for url in url_samples]
for entity in entities :
	entity()

