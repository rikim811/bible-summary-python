# Bible Summary

A Python package for summarizing Bible books, chapters, and providing various utilities to access Bible summaries.

## Features

- Get summary of a specific book and chapter
- Get a list of all books available
- Get a list of chapters in a specific book
- Get a random chapter summary or chapter number from a specific book or from the entire Bible
- Get a random chapter summary or chapter number from a specific category
- Get the number of chapters in a specific book
- Get a list of all categories
- Get a random chapter summary including a specific verse reference
- Get all books in a specified testament (NT or OT)
- Search for chapters that contain a specific keyword
- Get the total number of chapters in the Bible
- Get the total number of books in the Bible

## Installation

You can install the package using pip:

```bash
pip install bible-summary
```

## Importing the Package
```python
import bible_summary
```

## Get Summary of a Specific Book and Chapter
```python
summary = bible_summary.get_summary("Genesis", "1")
print(summary)
```

## Get List of All Books Available
```python
books = bible_summary.get_books()
print(books)
```

## Get List of Chapters in a Specific Book
```python
chapters = bible_summary.get_chapters("Genesis")
print(chapters)
```

## Get a Random Chapter Number without Summary
```python
random_chapter = bible_summary.get_random_chapter("Genesis", False)
print(f"Random Chapter in Genesis (No Summary): {random_chapter}")
```

## Get List of Categories
```python
categories = bible_summary.get_categories()
print(categories)
```

## Get Random Chapter by Category
```python
random_book, random_chapter, random_summary = bible_summary.get_random_category_chapter("Gospels")
print(f"Random Chapter in Gospels: {random_book} {random_chapter}")
print(f"Summary: {random_summary}")
```

## Get Chapters by Keyword
```python
chapters_with_keyword = bible_summary.get_chapters_by_keyword("creation")
print(chapters_with_keyword)
```


This `README.md` provides a clear and concise overview of the package's features, installation instructions, usage examples, and additional functionalities. Feel free to adjust the content to better fit your specific requirements or preferences.
