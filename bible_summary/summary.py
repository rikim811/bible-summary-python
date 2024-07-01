import json
import pkg_resources

def _load_books():
    books = {}
    resource_package = __name__
    resource_path = 'data/'  # Do not use os.path.join()

    for resource in pkg_resources.resource_listdir(resource_package, resource_path):
        if resource.endswith('.json'):
            full_path = pkg_resources.resource_filename(resource_package, f'{resource_path}{resource}')
            with open(full_path, 'r', encoding='utf-8') as f:
                book_data = json.load(f)
                books.update(book_data)
    return books

BOOKS = _load_books()

def get_summary(book, chapter):
    book = book.title()
    if book in BOOKS and chapter in BOOKS[book]:
        return BOOKS[book][chapter]
    else:
        return "Summary not available."

def get_books():
    return list(BOOKS.keys())

def get_chapters(book):
    book = book.title()
    if book in BOOKS:
        return list(BOOKS[book].keys())
    else:
        return "Book not available."
