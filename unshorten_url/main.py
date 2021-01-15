import http.client
import urllib.parse

def unshorten_url(url):
    """
    docstring
    """
    parsed = urllib.parse.urlparse(url)
    h = http.client.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status//100 == 3 and response.getheader('Location'):
        return response.getheader('Location')        
    else:
        return url




