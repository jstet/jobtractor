from dagster import build_op_context
from jobtractor.strategies import rb_by_link_llm_text_extract_single
from jobtractor.models import Organization, JobObjects

def test_rb_by_link_llm_text_extract_single(wikimedia_organization, climeworks_organization):
    wikimedia_organization= Organization(**wikimedia_organization)
    result = rb_by_link_llm_text_extract_single(build_op_context(), wikimedia_organization)
    assert isinstance(result, JobObjects)

    climeworks_organization= Organization(**climeworks_organization)
    result = rb_by_link_llm_text_extract_single(build_op_context(), climeworks_organization)
    assert isinstance(result, JobObjects)

 
    
    
