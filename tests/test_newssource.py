import unittest
from app.model import NewsSource

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsSource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = NewsSource('ntv-jioni','Uhuru President','Breaking Political news.','https://ntv.nation.co.ke/ke/news/politics','politics','ke')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'ntv-jioni')
        self.assertEquals(self.new_source.name,'Uhuru President')
        self.assertEquals(self.new_source.description,'Breaking Political news.')
        self.assertEquals(self.new_source.url,'https://ntv.nation.co.ke/ke/news/politics')
        self.assertEquals(self.new_source.category,'politics')
        self.assertEquals(self.new_source.country,'ke')