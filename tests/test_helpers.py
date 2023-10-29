from jobtractor.helpers import greenhouse

def test_greenhouse(wikimedia):
    jobs = greenhouse(wikimedia, "wikimedia")
    assert isinstance(jobs, list)
    if len(jobs) > 0:
        assert isinstance(jobs[0], dict)