from jobtractor.loader import load

def test_load():
    doc, final_url = load("https://climeworks.com/careers-search")
    assert len(doc) > 0
    assert isinstance(doc, str)
    # save to file
    with open("tests/fixtures/html/climeworks_11_01.txt", "w") as f:
        f.write(doc)

