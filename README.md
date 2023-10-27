# WIP

Service that extracts job openings from various career pages.

(A combination) of different techniques are/will be used:

1. Use data the website retrieves from a CMS 
2. Rule based extraction with bs4, for example get all links that have a href that starts with /jobs.
3. LLMs (structured output) -> https://python.langchain.com/docs/use_cases/extraction#option-2-parsing

What technique will be used depends on the page. 

Goal is to run this on a daily basis and send the data to a database. Maybe it will be possible to assign ids to jobs and to detect whether a jobs is no longer offered.

## Strategies

### Rule Based Strategies 

#### Wikipedia

1. Look for links that contain grnh.se 
2. 




### Inspiration

https://www.reddit.com/r/MachineLearning/comments/12v0vda/p_i_built_a_tool_that_autogenerates_scrapers_for/

## Dev Setup

1. Clone Repo

2. Install Dependencies 
``` bash
poetry install
```

3. Install Playwright
```bash
poetry run playwright install
```