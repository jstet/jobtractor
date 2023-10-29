import requests

def load(url, avoid_url: str = None):
    response = requests.get(url)
    response.raise_for_status()  

    html = response.text

    # Check if the request was redirected to the specified URL
    if response.url != url and response.url == avoid_url:
        raise ValueError("The request was redirected to the URL specified to be avoided.")

    return html