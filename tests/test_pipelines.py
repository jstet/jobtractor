from jobtractor.pipelines import wikimedia


def test_run():
    res = wikimedia()
    assert isinstance(res, list)
    assert len(res) > 0
    print(res[0]["company_job_id"])
    

