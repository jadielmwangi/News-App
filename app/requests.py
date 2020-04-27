import urllib.request,json
from .models import News, Articles

# import requests
# from flask import request
 
#Getting api key
api_key = None

#getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url + api_key
    # with urllib.request.urlopen(get_news_url) as url:

    with urllib.request.urlopen(get_news_url) as url:
     get_news_response = request.get(get_news_url).json()

    if get_news_response['sources']:
        news_result_list = get_news_response['sources']
        news_result = process_result(news_result_list)

        return news_result

def process_result(news_result_list):
    news_result= []
    for news_item in news_result_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_object = News(id, name, description,url,category,language,country)
            news_result.append(news_object)
    return news_result

#get articles
def get_article(id):
    get_article_url = article_base_url.format(id,api_key)
    
    get_article_response = request.get(get_article_url).json()
    if get_article_response['articles']:
        articles_result_list = get_article_response['articles']
        articles_result = process_article(articles_result_list)

        return articles_result

def process_article(article_list):
    articles_result= []
    for article in article_list:
            id = article.get('id')
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')
            content = article.get('content')
            if urlToImage:
                article_result = Articles(id, author,title, description,url,urlToImage,publishedAt,content)
                articles_result.append(article_result)
    return articles_result

def search_news(name):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(name,api_key)
    search_news_response = request.get(search_movie_url).json()

    if search_news_response['articles']:
        search_news_list = search_news_response['articles']
        search_news_result = process_article(search_news_list) 

    return search_news_result  