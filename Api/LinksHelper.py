from Links.models import Link
from .Errors import *
from django.conf import settings
from random import choice
from string import ascii_letters, digits
from datetime import datetime

# Try to get the value from the settings module, i have not set MAXIMUM_URL_CHARS but u can:D
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits

class LinksHelper:

    def __init__(self, url):
        self.url= url
        
    """
        Creates a random string with the predetermined size
    """
    def create_random_code(self, chars=AVAIABLE_CHARS):
        return "".join(
            [choice(chars) for _ in range(SIZE)]
        )

    """
        Create short url for long url + insert to db
        Return url short
    """
    def CreateShort(self):
        try:
            #create new code
            code = self.create_random_code()
            #create our link object
            new_link = Link(long_url=self.url,short_url=code,created=datetime.now())
            print(f' NEW LINK {new_link}')
            
            #save our link to db
            new_link.save()
            
            #return tp user his short
            return new_link.short_url
            
        except Exception as e:
            Error_msg = str(e)
            raise Exception(f'{SHORTLINK_GENERATE_ERROR}, more info: {Error_msg}')
    
    """
        Getting url code and checking if exist in our db if we have it
        add clicks to link + save
        return to user full link to redirect to
    """
    def ProccessCode(self):
        #Check if code exist in our db
        try:
            url = Link.objects.get(short_url__exact=self.url)
        except Link.DoesNotExist:
            raise KeyError(INVALID_CODE)
        
        #add clicks
        url.clicks += 1
        #save changes
        url.save()
        #print url stats
        print(url)
        #return full url to user
        return url.long_url