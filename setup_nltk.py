import shutil
import os

# Common folders where punkt might exist
paths = [
    'nltk_data/tokenizers/punkt',
    os.path.expanduser('~/nltk_data/tokenizers/punkt'),
    os.path.join(os.getenv("APPDATA", ""), 'nltk_data/tokenizers/punkt'),
    'C:/nltk_data/tokenizers/punkt'
]

for path in paths:
    if os.path.exists(path):
        print("Deleting:", path)
        shutil.rmtree(path)
