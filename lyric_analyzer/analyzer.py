from fetcher import get_artist_lyrics
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")

def combine_lyrics(lyrics_list: list[str]) -> str:
    """Combine a list of lyrics into a single string.

    Args:
        lyrics_list (list[str]): A list of lyric strings to be combined.

    Returns:
        str: A single string containing all lyrics joined by spaces.

    """
    return " ".join(lyrics_list)


if __name__ == "__main__":
    lyrics_list = get_artist_lyrics("Bruno Mars", 2)
    full_lyrics = combine_lyrics(lyrics_list)

    tokenized_lyrics = word_tokenize(full_lyrics)
    stop_words = set(stopwords.words("english"))

    filtered_lyrics = [word for word in tokenized_lyrics if word.lower() not in stop_words]
    
    
    print(filtered_lyrics)

    
