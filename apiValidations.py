import requests

BASE_URL = "http://216.10.245.166/Library"

def get_books_by_author(author_name):
    response = requests.get(
        f"{BASE_URL}/GetBook.php",
        params={"AuthorName": author_name}
    )
    return response

def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"

def assert_content_type_json(response):
    assert "application/json" in response.headers["Content-Type"], \
        f"Expected JSON, got {response.headers['Content-Type']}"

def assert_response_time(response, max_ms=2000):
    actual_ms = response.elapsed.total_seconds() * 1000
    assert actual_ms < max_ms, \
        f"Response too slow: {actual_ms:.0f}ms (limit {max_ms}ms)"

def assert_book_exists(json_response, isbn, expected_book):
    found = False
    for book in json_response:
        if book["isbn"] == isbn:
            found = True
            assert book == expected_book, \
                f"Book mismatch for ISBN {isbn}: {book}"
            break
    assert found, f"Book with ISBN {isbn} not found in response"
#Purpose: Common assertion functions (status code checks, response field checks)

#What problem does it solve->
#Imagine you have a Library API — endpoints for adding books, fetching them, updating them, deleting them. Instead of manually clicking in Postman every time, your framework runs those tests automatically and gives you a nice report.

#Feature files → what to test (business language)
#stepImpl.py → how to test it (Python logic)
#utilities/ → configuration and reusable resources
#payLoad.py → test data
#apiValidations.py → assertion logic

#How to run:
#pip install -r requirements.txt
#behave
#For Allure reports: behave -f allure_behave.formatter:AllureFormatter -o AllureReports
#to see Report dashboard: allure serve AllureReports











