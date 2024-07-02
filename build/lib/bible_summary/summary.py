import json
import random
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

CATEGORIES = {
    'NT': ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    'OT': ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Songs", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"],
    'Historical Books': ["Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther"],
    'Poetic Books': ["Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Songs"],
    'Prophets': ["Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"],
    'Major Prophets': ["Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel"],
    'Minor Prophets': ["Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"],
    'Gospels': ["Matthew", "Mark", "Luke", "John"],
    'Letters': ["Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude"]
}

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

def get_random_chapter(book=None, include_summary=True):
    if book:
        book = book.title()
        if book in BOOKS:
            chapter = random.choice(list(BOOKS[book].keys()))
            if include_summary:
                return chapter, BOOKS[book][chapter]
            return chapter
        return "Book not available."
    else:
        book = random.choice(list(BOOKS.keys()))
        chapter = random.choice(list(BOOKS[book].keys()))
        if include_summary:
            return book, chapter, BOOKS[book][chapter]
        return book, chapter

def get_random_category_chapter(category, include_summary=True):
    category = category.title()
    if category in CATEGORIES:
        book = random.choice(CATEGORIES[category])
        chapter = random.choice(list(BOOKS[book].keys()))
        if include_summary:
            return book, chapter, BOOKS[book][chapter]
        return book, chapter
    return "Category not available."

def get_max_chapters(book):
    book = book.title()
    if book in BOOKS:
        return len(BOOKS[book])
    return "Book not available."

def get_summary_range(book, start_chapter, end_chapter):
    book = book.title()
    if book in BOOKS:
        summaries = {}
        for chapter in range(start_chapter, end_chapter + 1):
            chapter_str = str(chapter)
            if chapter_str in BOOKS[book]:
                summaries[chapter_str] = BOOKS[book][chapter_str]
        return summaries
    return "Book not available."

def get_all_chapters_summary(book):
    book = book.title()
    if book in BOOKS:
        return BOOKS[book]
    return "Book not available."

def search_summaries(keyword, book=None):
    keyword = keyword.lower()
    results = {}
    books_to_search = [book.title()] if book else BOOKS.keys()

    for book in books_to_search:
        if book in BOOKS:
            for chapter, summary in BOOKS[book].items():
                if keyword in summary.lower():
                    if book not in results:
                        results[book] = {}
                    results[book][chapter] = summary
    return results if results else "No matches found."

def get_categories():
    return list(CATEGORIES.keys())

def get_random_chapter_by_category(category, include_summary=True):
    category = category.title()
    if category in CATEGORIES:
        book = random.choice(CATEGORIES[category])
        chapter = random.choice(list(BOOKS[book].keys()))
        if include_summary:
            return book, chapter, BOOKS[book][chapter]
        return book, chapter
    return "Category not available."

def get_total_chapters():
    total_chapters = sum(len(chapters) for chapters in BOOKS.values())
    return total_chapters

def get_total_books():
    return len(BOOKS)


