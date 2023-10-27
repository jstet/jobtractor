from jobtractor.rb_extraction import extract_links

def test_extract_links(wikimedia_str):
    links = extract_links(wikimedia_str, rule=lambda href: href and "https://grnh.se" in href)
    print("\nLINKS\n",links)