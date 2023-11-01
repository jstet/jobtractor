from jobtractor.processing import process_for_llm, clean_html

def test_clean_html(wikimedia_html):
   
    result = clean_html(wikimedia_html)
    assert isinstance(result, str)

    html = """
    <html>
        <body>
            <h1>Title</h1>
            <p>Paragraph</p>
            <form>Form</form>
        </body>
    </html>
    """
    result = clean_html(html)
    assert isinstance(result, str)
    assert result == "Title\nParagraph"


def test_process_for_llm():
    text = "This is some sample text"
    chunk_size = 1000

    result = process_for_llm(text, chunk_size)

    assert isinstance(result, str)