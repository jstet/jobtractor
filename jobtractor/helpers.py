from datetime import datetime
from dagster import op
import re

@op
def filter_jobs(links):
    return [link for link in links if "data" in link["text"].lower()]

@op
def add_meta(final_url, html, id_extract_re):
    """
    Adds metadata to the job object.

    Args:
        job (dict): The job object to add metadata to.
        url (str): The URL of the job.
        html (str): The HTML content of the job.
        company_job_id (str): The ID of the job in the company database.

    Returns:
        dict: The job object with added metadata.
    """
    dct = {}
    dct["company_job_id"] = re.search(fr"{id_extract_re}", final_url).group(1)
    dct["html"] = html
    dct["url"] = final_url
    dct["extracted_at"] = datetime.now()
    return dct


