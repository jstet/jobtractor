from jobtractor.processing import process_for_llm

def test_process_for_llm(orchard):
    processed = process_for_llm(orchard)
    assert isinstance(processed, str)
    assert len(processed) > 0
