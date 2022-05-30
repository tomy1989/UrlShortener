from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serizalizers import PostLinkSerizalizer
from urllib.parse import urlparse, urljoin
from .Errors import *
import logging
from .LinksHelper import LinksHelper
logger = logging.getLogger(__name__)

#this base url django start
BASE_URL = 'http://127.0.0.1:8000/s/'

"""
    Checking given url if in valid schema
"""
def validate_url_schema(url):
    #using urlparse
    parsed_url = urlparse(url)
    res = bool(parsed_url.scheme)
    if(not res):
        raise Exception(WRONG_INPUT_URL)


@api_view(['POST'])
def create_short(request):
    """_summary_
    view getting POST req and creating for link a short link
    Args:
        requests (_type_): _description_
    """
    try:
        serializer = PostLinkSerizalizer(data=request.data)
        #checking dat we got valid format
        if serializer.is_valid():
            print(f'our data {serializer.data}')
        else:
            return Response({'Error': WRONG_REQ_FORMAT}, status=status.HTTP_400_BAD_REQUEST)
        url = serializer.data['url']
        #checking if url given in corrent schema
        validate_url_schema(url)
        #setting our helper
        link_helper = LinksHelper(url)
        #creatin link
        url_short = link_helper.CreateShort()
        #join links
        user_url = urljoin(BASE_URL, url_short)
        #return to user his new link
        return Response({'Here you are!': user_url})
    
    except Exception as e:
        Error_msg = str(e)
        logger.error(f'Got Error, more details: {Error_msg}')
        return Response({'Error': Error_msg}, status=status.HTTP_400_BAD_REQUEST)

    
"""
    Getting short link code and proccess it
    getting code full url + redirect to the full url

Returns:
    redirect or error info if there an error
"""
@api_view(['GET'])
def create_redirect(request, code):
     
    try:
        #setting our helper with code
        link_helper = LinksHelper(code)
        #get full url from code if exists
        full_url = link_helper.ProccessCode()
        #user redirect
        return redirect(full_url)
        
        
    except Exception as e:
        Error_msg = str(e)
        logger.error(f'Got Error, more details: {Error_msg}')
        return Response({'Error': Error_msg}, status=status.HTTP_400_BAD_REQUEST)