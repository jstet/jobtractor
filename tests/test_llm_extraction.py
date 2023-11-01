from jobtractor.llm_extraction import text_extract_single
from jobtractor.models import Job

def test_text_extract_single():
    content = "We are looking for a Data Engineer in Zurich. You should have at least 200 years work experience."

    expected_job = Job(
        job_name='Data Engineer',
        job_location='Zurich',
        job_required_years_work_experience=200
    )

    result = text_extract_single(content)

    assert isinstance(result, Job)
    assert result == expected_job
    print(result)