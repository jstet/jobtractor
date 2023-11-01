from dagster import op
from jobtractor.loader import load
from jobtractor.helpers import filter_jobs, add_meta
from jobtractor.rb_extraction import extract_by_links
from jobtractor.llm_extraction import text_extract_single
from jobtractor.processing import clean_html, process_for_llm
import requests

@op()
def rb_by_link_llm_text_extract_single(context, organization):
    """
    Extracts job data from a given organization's career page.

    Args:
        context (object): The context object containing information about the execution context.
        organization (dict): The organization dictionary containing information about the organization.

    Returns:
        list: A list of dictionaries containing job data and metadata for each job.
    """
    html = load(organization["career_url"])
    print(html)
    links = extract_by_links(html, rule=lambda href: href and organization["jobs_url"] in href, base_url=organization["jobs_base_url"] if organization["jobs_base_url"] else None) 
    links = filter_jobs(links)

    jobs = []
    for link in links:
        url = link["url"]
        context.log.info(f"Trying: {url}")
        try:
            html, final_url = load(url, forward_url=organization["career_forward_url"])
        except ValueError as e:
            context.log.info(f"Error: {e}. Job is probably no longer open")
            continue
        except requests.HTTPError as e:
            context.log.info(f"Error: {e}. Job is probably no longer open")
            continue
        text = clean_html(html)
        content = process_for_llm(text, chunk_size=1500)
        job = {}
        job["job_data"] = text_extract_single(content)  
        job["meta"] = add_meta(final_url, html, organization["id_extract_re"])  
        jobs.append(job)
    return jobs