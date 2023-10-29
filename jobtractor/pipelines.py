from jobtractor.loader import load
from jobtractor.helpers import greenhouse


def wikimedia():
    url = "https://wikimediafoundation.org/about/jobs/"
    html, final_url = load(url)
    jobs = greenhouse(html, "wikimedia")
    return jobs
    

        


