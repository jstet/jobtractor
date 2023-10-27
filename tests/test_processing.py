from jobtractor.processing import process

def test_process_rule_based(orchard_loaded):
    processed = process(orchard_loaded)
    print(processed)