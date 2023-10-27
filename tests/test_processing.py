from jobtractor.processing import process

def test_process(orchard_loaded):
    processed = process(orchard_loaded)
    print(processed)