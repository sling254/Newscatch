class NewsSource():
    def __init__(self, id, name, description, url, category, country):
        '''
        a Class to define NewsSource Object
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class NewsArticle():
    """
    NewsArticle class to define NewsArticle objects
    """

    def __init__(self,id,aurthor, title, description,url, image,date):
        self.id=id
        self.aurthor = aurthor
        self.title=title
        self.description=description
        self.url=url
        self.image=image
        self.date=date