import nltk 
import ssl
def download1():
    try:
        _create_unverified_https_content = ssl._create_default_https_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_content

    nltk.download()
