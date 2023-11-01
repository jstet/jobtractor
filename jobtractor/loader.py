import requests
from dagster import op

@op()
def load(url, forward_url: str = None):
    """
    Load the content of a web page from a given URL. Some organization don't respond with 404 if you navigate to a non existing job page but redirect to some general jobs page. We cant forbid forwarding in general, because some urls specified on career pages are shortened urls.

    Parameters:
        url (str): The URL of the web page to load.
        forward_url (str): The URL to be avoided if the request is redirected.

    Returns:
        tuple: A tuple containing the HTML content of the web page and the final URL after any redirection.
        
    Raises:
        ValueError: If the request is redirected to the specified URL to be avoided.
    """
    response = requests.get(url)
    response.raise_for_status()  

    html = response.text

    # Check if the request was redirected to the specified URL
    if response.url != url and response.url == forward_url:
        raise ValueError("The request was redirected to the URL specified to be avoided.")

    return html, response.url