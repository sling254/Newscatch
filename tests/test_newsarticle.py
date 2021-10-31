import unittest
from app.model import NewsArticle
class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = NewsArticle('The Nairobian','David Ndii','Four things we must stop doing','Four things we must stop doing before 2022.','https://www.standardmedia.co.ke/thenairobian/author/nancy-roxanne','image.jpg','2022-06-07T06:13:47Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticle))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'The Nairobian')
        self.assertEquals(self.new_article.aurthor,'David Ndii')
        self.assertEquals(self.new_article.title,'Four things we must stop doing')
        self.assertEquals(self.new_article.description,'Four things we must stop doing before 2022.')
        self.assertEquals(self.new_article.url,'https://www.standardmedia.co.ke/thenairobian/author/nancy-roxanne')
        self.assertEquals(self.new_article.image,'image.jpg')
        self.assertEquals(self.new_article.date,'2022-06-07T06:13:47Z')