########################
# googleplaylib.py
# 2017.1.4
########################

def get_value(soup_) :
    if len(soup_) == 1 :
        str_ = soup_[0].get_text()
        # error processing
        str_ = str_.replace("\xa0", " ")
        return str_.strip()
    elif len(soup_) > 1 :
        items = []        
        for i in range(len(soup_)) :
            item = soup_[i].get_text()
            items.append(item.strip())
        return "|".join(items)
    else :
        return None

import urllib.request
from bs4 import BeautifulSoup

def url_connect(url) :
    try :    
        res = urllib.request.urlopen(url)
        soup = BeautifulSoup(res.read(), "lxml")
        if url.find("?id=") > 0 :
            app_id = url.split("?id=")[1].split('&')[0]
        elif url.find("&id=") > 0 :
            app_id = [q for q in url.split('&')[1:] if q.find("id=")>-1][0][3:]
        else :        
            app_id = None
        return soup, app_id
    except urllib.error.HTTPError as err:
        print(">>> Error Code :", err.code,",\tNot valid URL Link:\n", url)
        return None, err.code

def get_primary_info(soup) :  
    DIC = {}
    title_soup = soup.find_all('div',attrs={'class':'id-app-title'})
    DIC['title'] = get_value(title_soup)
    dev_soup = soup.find_all('a', attrs={'class':'document-subtitle primary'})
    DIC['developer'] = get_value(dev_soup)
    catg_soup = soup.find_all('a', attrs={'class':'document-subtitle category'})
    DIC['category'] = get_value(catg_soup)
    desc_soup = soup.find_all('div',attrs={'jsname':'C4s9Ed'})
    DIC['description'] = get_value(desc_soup)
    return DIC
    
def get_secondary_info(soup) :
    DIC = {}
    score_soup = soup.find_all('div', attrs={'class':'score'})    
    DIC['score'] = get_value(score_soup)  
    review_n_soup = soup.find_all('span', attrs={'class':'reviews-num'})
    DIC['review_num'] = get_value(review_n_soup)
    update_soup = soup.find_all('div', attrs={'itemprop':'datePublished'})
    DIC['updated_date'] = get_value(update_soup)
    down_soup = soup.find_all('div', attrs={'itemprop':'numDownloads'})
    DIC['download_volumn'] = get_value(down_soup)
    contents_soup = soup.find_all('div', attrs={'itemprop':'contentRating'})
    DIC['contents_rating'] = get_value(contents_soup)
    return DIC 
"""
def print_info(dic0, dic1) :
    print("\ntitle:\t", dic0["title"], "\ndeveloper:\t", dic0["developer"],
      "\ncategory:\t", dic0["category"])
    for k, v in dic1.items() :
        print(" ", k, ":\t", v)
    print("description:\n", dic0["description"])
    return None
"""



