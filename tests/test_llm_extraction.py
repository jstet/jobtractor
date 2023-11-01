from jobtractor.llm_extraction import text_extract_single
from jobtractor.models import JobData

def test_text_extract_single(wikimedia_data_engineer_str, climeworks_data_analyst_str):
    content = "We are looking for a Data Engineer (80%) in Zurich. You should have at least 200 years work experience."

    expected_job = JobData(
        job_name='Data Engineer',
        job_location='Zurich',
        job_required_years_work_experience=200
    )

    result = text_extract_single(content)
    

    assert isinstance(result, JobData)
    assert result == expected_job

    expected_job = JobData(
        job_name='Senior Data Engineer',
        job_location='Remote',
        job_required_years_work_experience=5
    )

    result = text_extract_single(wikimedia_data_engineer_str)
    assert isinstance(result, JobData)
    assert result == expected_job

    expected_job = JobData(
        job_name='Data Operations Specialist',
        job_location='Zurich',
        job_required_years_work_experience=5
    )

    result = text_extract_single(climeworks_data_analyst_str)
    print(result)
    assert isinstance(result, JobData)
    assert result == expected_job




    