import unittest
from app.models import News, Articles


class TestNews(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("axios","Axios","Axios are a new media company delivering vital, trustworthy news and analysis in the most efficient, illuminating and shareable ways possible.","https://www.axios.com","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))




class TestArticles(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("techcrunch","TechCrunch","Brave, a maker of a pro-privacy browser","https://techcrunch.com/2020/04/27/brave-accuses-european-governments-of-gdpr-resourcing-failure/", "https://techcrunch.com/wp-content/uploads/2018/04/gettyimages-936469236.jpg?w=600","2020-04-27T12:01:46Z","Brave, a maker of a pro-privacy browser, has lodged complaints with the European Commission against 27 EU Member States for under resourcing their national data protection watchdogs.\r\nIt’s asking the European Union’s executive body to launch an infringement p… [+8721 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
