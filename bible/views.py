import os
import json
from django.conf import settings
from django.http import Http404
from django.shortcuts import render


BOOKS = [
    {'name': 'Genesis', 'abbr': 'Gen', 'filename': 'genesis.json'},
    {'name': 'Exodus', 'abbr': 'Exo', 'filename': 'exodus.json'},
    {'name': 'Leviticus', 'abbr': 'Lev', 'filename': 'leviticus.json'},
    {'name': 'Numbers', 'abbr': 'Num', 'filename': 'numbers.json'},
    {'name': 'Deuteronomy', 'abbr': 'Deu', 'filename': 'deuteronomy.json'},
    {'name': 'Joshua', 'abbr': 'Jos', 'filename': 'joshua.json'},
    {'name': 'Judges', 'abbr': 'Jdg', 'filename': 'judges.json'},
    {'name': 'Ruth', 'abbr': 'Rut', 'filename': 'ruth.json'},
    {'name': '1 Samuel', 'abbr': '1Sa', 'filename': '1samuel.json'},
    {'name': '2 Samuel', 'abbr': '2Sa', 'filename': '2samuel.json'},
    {'name': '1 Kings', 'abbr': '1Ki', 'filename': '1kings.json'},
    {'name': '2 Kings', 'abbr': '2Ki', 'filename': '2kings.json'},
    {'name': '1 Chronicles', 'abbr': '1Ch', 'filename': '1chronicles.json'},
    {'name': '2 Chronicles', 'abbr': '2Ch', 'filename': '2chronicles.json'},
    {'name': 'Ezra', 'abbr': 'Ezr', 'filename': 'ezra.json'},
    {'name': 'Nehemiah', 'abbr': 'Neh', 'filename': 'nehemiah.json'},
    {'name': 'Esther', 'abbr': 'Est', 'filename': 'esther.json'},
    {'name': 'Job', 'abbr': 'Job', 'filename': 'job.json'},
    {'name': 'Psalms', 'abbr': 'Psa', 'filename': 'psalms.json'},
    {'name': 'Proverbs', 'abbr': 'Pro', 'filename': 'proverbs.json'},
    {'name': 'Ecclesiastes', 'abbr': 'Ecc', 'filename': 'ecclesiastes.json'},
    {'name': 'Song of Solomon', 'abbr': 'Son', 'filename': 'songofsolomon.json'},
    {'name': 'Isaiah', 'abbr': 'Isa', 'filename': 'isaiah.json'},
    {'name': 'Jeremiah', 'abbr': 'Jer', 'filename': 'jeremiah.json'},
    {'name': 'Lamentations', 'abbr': 'Lam', 'filename': 'lamentations.json'},
    {'name': 'Ezekiel', 'abbr': 'Eze', 'filename': 'ezekiel.json'},
    {'name': 'Daniel', 'abbr': 'Dan', 'filename': 'daniel.json'},
    {'name': 'Hosea', 'abbr': 'Hos', 'filename': 'hosea.json'},
    {'name': 'Joel', 'abbr': 'Joe', 'filename': 'joel.json'},
    {'name': 'Amos', 'abbr': 'Amo', 'filename': 'amos.json'},
    {'name': 'Obadiah', 'abbr': 'Oba', 'filename': 'obadiah.json'},
    {'name': 'Jonah', 'abbr': 'Jon', 'filename': 'jonah.json'},
    {'name': 'Micah', 'abbr': 'Mic', 'filename': 'micah.json'},
    {'name': 'Nahum', 'abbr': 'Nah', 'filename': 'nahum.json'},
    {'name': 'Habakkuk', 'abbr': 'Hab', 'filename': 'habakkuk.json'},
    {'name': 'Zephaniah', 'abbr': 'Zep', 'filename': 'zephaniah.json'},
    {'name': 'Haggai', 'abbr': 'Hag', 'filename': 'haggai.json'},
    {'name': 'Zechariah', 'abbr': 'Zec', 'filename': 'zechariah.json'},
    {'name': 'Malachi', 'abbr': 'Mal', 'filename': 'malachi.json'},
    {'name': 'Matthew', 'abbr': 'Mat', 'filename': 'matthew.json'},
    {'name': 'Mark', 'abbr': 'Mar', 'filename': 'mark.json'},
    {'name': 'Luke', 'abbr': 'Luk', 'filename': 'luke.json'},
    {'name': 'John', 'abbr': 'Joh', 'filename': 'john.json'},
    {'name': 'Acts', 'abbr': 'Act', 'filename': 'acts.json'},
    {'name': 'Romans', 'abbr': 'Rom', 'filename': 'romans.json'},
    {'name': '1 Corinthians', 'abbr': '1Co', 'filename': '1corinthians.json'},
    {'name': '2 Corinthians', 'abbr': '2Co', 'filename': '2corinthians.json'},
    {'name': 'Galatians', 'abbr': 'Gal', 'filename': 'galatians.json'},
    {'name': 'Ephesians', 'abbr': 'Eph', 'filename': 'ephesians.json'},
    {'name': 'Philippians', 'abbr': 'Php', 'filename': 'philippians.json'},
    {'name': 'Colossians', 'abbr': 'Col', 'filename': 'colossians.json'},
    {'name': '1 Thessalonians', 'abbr': '1Th', 'filename': '1thessalonians.json'},
    {'name': '2 Thessalonians', 'abbr': '2Th', 'filename': '2thessalonians.json'},
    {'name': '1 Timothy', 'abbr': '1Ti', 'filename': '1timothy.json'},
    {'name': '2 Timothy', 'abbr': '2Ti', 'filename': '2timothy.json'},
    {'name': 'Titus', 'abbr': 'Tit', 'filename': 'titus.json'},
    {'name': 'Philemon', 'abbr': 'Phm', 'filename': 'philemon.json'},
    {'name': 'Hebrews', 'abbr': 'Heb', 'filename': 'hebrews.json'},
    {'name': 'James', 'abbr': 'Jam', 'filename': 'james.json'},
    {'name': '1 Peter', 'abbr': '1Pe', 'filename': '1peter.json'},
    {'name': '2 Peter', 'abbr': '2Pe', 'filename': '2peter.json'},
    {'name': '1 John', 'abbr': '1Jo', 'filename': '1john.json'},
    {'name': '2 John', 'abbr': '2Jo', 'filename': '2john.json'},
    {'name': '3 John', 'abbr': '3Jo', 'filename': '3john.json'},
    {'name': 'Jude', 'abbr': 'Jud', 'filename': 'jude.json'},
    {'name': 'Revelation', 'abbr': 'Rev', 'filename': 'revelation.json'}
]

# Preprocess BOOKS to create a mapping from book names to their data
BOOKS_BY_NAME = {book['name'].lower(): book for book in BOOKS}
BOOKS_BY_ABBR = {book['abbr'].lower(): book for book in BOOKS}


# Create your views here.
def bible(request, book_name=None, chapter_number=None):
    # Get all books
    books = BOOKS

    # Initialize variables
    current_book = None
    bible_text = None
    chapters = []
    selected_chapter = None

    if book_name:
        # Normalize the book name
        book_name_lower = book_name.strip().lower()

        # Find the book dictionary using the mappings
        book = BOOKS_BY_NAME.get(book_name_lower) or BOOKS_BY_ABBR.get(book_name_lower)
        if not book:
            raise Http404("Book not found")

        json_filename = book.get('filename')
        if not json_filename:
            raise Http404("Filename for the book not found")

        # Construct the path to the JSON file
        json_path = os.path.join(settings.BASE_DIR, 'bible', 'static', 'assets', json_filename)

        # Ensure the file exists before attempting to open it
        if not os.path.exists(json_path):
            raise Http404("Book content file not found")

        try:
            with open(json_path, 'r', encoding="utf-8") as f:
                full_bible_text = json.load(f)
            current_book = book['name']
        except (IOError, json.JSONDecodeError):
            return render(request, 'error.html', {'message': 'Error loading book content.'})

        # Get the list of chapters
        chapters = list(range(1, len(full_bible_text) + 1))

        # Process the chapters and verses
        if chapter_number:
            # If a chapter number is provided, get only that chapter
            if 1 <= chapter_number <= len(full_bible_text):
                selected_chapter = chapter_number
                chapter_data = full_bible_text[chapter_number - 1]
                verses = []
                for verse in chapter_data:
                    if not verse or not isinstance(verse, str):
                        continue
                    parts = verse.strip().split(' ', 1)
                    if len(parts) > 1:
                        verse_number = parts[0]
                        verse_text = parts[1]
                    else:
                        verse_number = ''
                        verse_text = parts[0]
                    verses.append({'number': verse_number, 'text': verse_text})
                bible_text = [{'chapter_number': chapter_number, 'verses': verses}]
            else:
                raise Http404("Chapter not found")
        else:
            # If no chapter is selected, process all chapters
            bible_text = []
            for idx, chapter_data in enumerate(full_bible_text):
                verses = []
                for verse in chapter_data:
                    if not verse or not isinstance(verse, str):
                        continue
                    parts = verse.strip().split(' ', 1)
                    if len(parts) > 1:
                        verse_number = parts[0]
                        verse_text = parts[1]
                    else:
                        verse_number = ''
                        verse_text = parts[0]
                    verses.append({'number': verse_number, 'text': verse_text})
                bible_text.append({'chapter_number': idx + 1, 'verses': verses})

    context = {
        "books": books,
        "current_book": current_book,
        "bible_text": bible_text,
        "chapters": chapters,
        "selected_chapter": selected_chapter,
    }
    return render(request, "bible.html", context)