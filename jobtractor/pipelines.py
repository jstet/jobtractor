from jobtractor.loader import load
from jobtractor.helpers import greenhouse


def wikimedia():
    url = "https://wikimediafoundation.org/about/jobs/"
    html, final_url = load(url)
    jobs = greenhouse(html, "wikimedia")
    return jobs


def climeworks():
    url = "https://climeworks.com/careers-search"
    html, final_url = load(url)
    jobs = greenhouse(html, "climeworks")
    return jobs


    

        


