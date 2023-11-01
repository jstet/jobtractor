from dagster import build_op_context
from jobtractor.strategies import rb_by_link_llm_text_extract_single

def test_rb_by_link_llm_text_extract_single(wikimedia_organization):
    print("\n\n\n", wikimedia_organization)
    # Call the op under test
    result = rb_by_link_llm_text_extract_single(build_op_context(), wikimedia_organization)

    # Perform assertions on the result
    assert isinstance(result, list)
    for job in result:
        assert isinstance(job, dict)
        assert "job_data" in job
        assert "meta" in job