import urllib.request, json 
from .models import News



api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    news_url = base_url.format(api_key)
    with urllib.request.urlopen(news_url) as url:
        get_news_data = url.read()
        py_readable_urlData = json.loads(get_news_data) 
        news_results = None
        if py_readable_urlData['articles']:
            news_list = py_readable_urlData['articles']
            news_results = process_results(news_list)
    return news_results

        
        




def process_results(url_list):
    url_results = []
    for url_item in url_list:
        title = url_item.get('title')
        description = url_item.get('description')
        urlToImage = url_item.get('urlToImage')
        content = url_item.get('content')
        publishedAt = url_item.get('publishedAt') 

        if urlToImage:
            news_object = News(title, description, urlToImage, content, publishedAt)
            url_results.append(news_object)

    return(url_results)     

