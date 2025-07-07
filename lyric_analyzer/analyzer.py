from fetcher import get_artist_lyrics

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

import matplotlib.pyplot as plt

nltk.download("stopwords")
lemmatizer = WordNetLemmatizer()


def combine_lyrics(lyrics_list: list[str]) -> str:
    """Combine a list of lyrics into a single string.

    Args:
        lyrics_list (list[str]): A list of lyric strings to be combined.

    Returns:
        str: A single string containing all lyrics joined by spaces.

    """
    return " ".join(lyrics_list)


def preprocess_lyrics(lyrics: str) -> list[str]:
    """Tokenize, remove stopwords, and lemmatize lyrics."""
    tokenized = word_tokenize(lyrics)
    stop_words = set(stopwords.words("english"))
    stop_words.update({",", "'s", "u", "'re", "'m", "'ll", "(", ")"})
    stop_words -= {"him"}
    filtered = [word for word in tokenized if word.lower() not in stop_words]
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
    return lemmatized


def get_word_frequencies(words: list[str]) -> list[tuple[str, int]]:
    """Return sorted word frequencies."""
    fdist = FreqDist(words)
    return fdist.most_common()


def plot_top_words(word_freqs: list[tuple[str, int]], top: int = 70):
    """Plot the top N most frequent words."""
    top_words = word_freqs[:top]
    words, counts = zip(*top_words)
    plt.figure(figsize=(25, 6))
    plt.bar(words, counts)
    plt.title(f"Top {top} Most Frequent Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    lyrics_list = get_artist_lyrics("The Itchyworms", 10)
    full_lyrics = combine_lyrics(lyrics_list)
    lemmatized_lyrics = preprocess_lyrics(full_lyrics)
    print(lemmatized_lyrics)
    sorted_freq = get_word_frequencies(lemmatized_lyrics)
    print(sorted_freq)
    plot_top_words(sorted_freq, top=20)