import requests

API_URL = "http://tldr.pythonanywhere.com/api/tldr"


def tldrify(url:str=None, text:str=None, filename:str=None, ratio:float=None, words:int=None) -> str:
    """
    Returns a string summary of the input data via TLDR platform (http://tldr.pythonanywhere.com)
    Note that input text MUST be longer than once sentence to summarize
    
    Please use one of the following:
    :param url: The URL of the page to summarize. Note that this is not available at this time!
    :param text: The string text to summarize. 
    :param filename: The path of the file to summarize. Note that this must be .pdf, .txt, .docx, or .pptx
    
    And one of the following:
    :param ratio: The percent to shrink the data to (ex, 5 reduces the text to 5% of what it is)
    :param words: The approximate word count of the resultant data
    :return: A string summary of the data
    """
    data = {}
    files = {}

    if url is not None:
        data["url"] = url
        raise NotImplementedError("The URL Summaries Are Not Available At This Time!")
    elif text is not None:
        data["text"] = text
    elif filename is not None:
        files["file"] = open(filename, 'rb')
    else:
        raise TypeError("Please specify a data input source (url, text, or filename)")

    if ratio is not None:
        data["ratio"] = ratio
    elif words is not None:
        data["words"] = words
    else:
        raise TypeError("Please specify a summary amount (ratio or words)")

    r = requests.post(API_URL, data=data, files=files)
    if r.status_code == 200:
        return r.text

    if r.status_code == 409:
        raise ValueError(r.text)

    raise IOError("The Summarization Server Returned HTTP Status Code '{}', With The Message:\n{}".format(
        r.status_code, r.text
    ))
