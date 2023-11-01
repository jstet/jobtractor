from jobtractor.rb_extraction import extract_by_links

def test_extract_by_links(wikimedia):
    links = extract_by_links(wikimedia, rule=lambda href: href and "https://grnh.se" in href)
    assert isinstance(links, list)
    assert len(links) > 0
    assert isinstance(links[0], dict)


