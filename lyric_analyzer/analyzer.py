import matplotlib.pyplot as plt
import nltk
from fetcher import get_artist_lyrics
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
lemmatizer = WordNetLemmatizer()

REMOVE_STOP_WORDS = {"him"}
ADD_STOP_WORDS = {",", "'s", "u", "'re", "'m", "'ll", "(", ")"}


def combine_lyrics(lyrics_list: list[str]) -> str:
    """Combine a list of lyrics into a single string.

    Args:
        lyrics_list (list[str]): A list of lyric strings to be combined.

    Returns:
        str: A single string containing all lyrics joined by spaces.

    """
    return " ".join(lyrics_list)


def preprocess_lyrics(lyrics: str) -> list[str]:
    """Tokenize, remove stopwords, and lemmatize lyrics.

    Args:
        lyrics (str): The lyrics text to preprocess.

    Returns:
        list[str]: A list of lemmatized words after tokenization and stopword removal.

    """
    """Tokenize, remove stopwords, and lemmatize lyrics."""
    tokenized = word_tokenize(lyrics)

    stop_words = set(stopwords.words("english"))
    stop_words.update(ADD_STOP_WORDS)
    stop_words -= REMOVE_STOP_WORDS

    filtered = [word for word in tokenized if word.lower() not in stop_words]
    return [lemmatizer.lemmatize(word) for word in filtered]


def get_word_frequencies(words: list[str]) -> list[tuple[str, int]]:
    """Create a frequency distribution of the words.

    Args:
        words (list[str]): A list of words to analyze.

    Returns:
        list[tuple[str, int]]: A list of tuples where each tuple contains a word and its frequency,
            sorted by frequency in descending order.

    """
    fdist = FreqDist(words)
    return fdist.most_common()


def plot_top_words(word_freqs: list[tuple[str, int]], top: int = 70) -> None:
    """Plot a bar chart of the top N most frequent words from a list of word-frequency tuples.

    Args:
        word_freqs (list[tuple[str, int]]): A list of tuples where each tuple contains a word and its
            corresponding frequency, sorted in descending order of frequency.
        top (int, optional): The number of top words to display in the plot. Defaults to 70.

    """
    top_words = word_freqs[:top]
    words, counts = zip(*top_words, strict=False)
    plt.figure(figsize=(25, 6))
    plt.bar(words, counts)
    plt.title(f"Top {top} Most Frequent Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # tests
    lyrics_list = get_artist_lyrics("The Itchyworms", 10)
    full_lyrics = combine_lyrics(lyrics_list)
    lemmatized_lyrics = preprocess_lyrics(full_lyrics)
    print(lemmatized_lyrics)
    sorted_freq = get_word_frequencies(lemmatized_lyrics)
    print(sorted_freq)
    plot_top_words(sorted_freq, top=20)
