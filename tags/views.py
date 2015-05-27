from django.shortcuts import render
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
from collections import Counter

from .forms import TagsForm

import logging
import operator
import requests
import re
#logger = logging.getLogger(__name__)

def getPageSource (webURL):
    try:
        response = requests.get(webURL, timeout=20)
        contentType = response.headers.get('content-type')
        #logger.debug("content type: "+contentType)
        if re.match('text/html', contentType):
            return (response.text, None)
        else:
            return (None, 'Not a valid HTML page')
    except ConnectionError as e:
        #logger.debug("Connection Error: "+str(e.args[0].reason))
        return (None, str(e.args[0]))

def index(request):
    if request.method == 'POST':
        # create a form instance
        form = TagsForm(request.POST)
        # check whether form is valid:
        if form.is_valid():
            messages = []
            tags = []
            inputUrl= form.cleaned_data['inputUrl']
            try:
                (inputSource, errorMessage) = getPageSource(inputUrl)
                if inputSource:
                    tagList = list()
                    #Parse HTML and get tags
                    soup = BeautifulSoup(inputSource)
                    tagList = [tag.name for tag in soup.find_all(True)]
                    tags = Counter(tagList)
                    #logger.debug(dict(tags))
                    #Sort tag count, starting from highest to lowest
                    tags = sorted(tags.items(), key = operator.itemgetter(1), reverse=True)
                    return render(request, 'tags.html', {'form': form, 'tags': tags, 'messages':messages, 'source': inputSource})
                else:
                    messages = [errorMessage]
                    return render(request, 'tags.html', {'form': form, 'tags': tags, 'messages':messages })
            except Exception, e:
                messages = [str(e)]
                #logger.debug("URL fetch error[" + repr(e) + "]")
                return render(request, 'tags.html', {'form': form, 'tags': tags, 'messages':messages})
        else:
            return render(request, 'tags.html', {'form': form})

    #If not POST
    else:
        form = TagsForm()

    return render(request, 'tags.html', {'form': form})
