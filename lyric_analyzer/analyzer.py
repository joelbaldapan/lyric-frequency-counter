from fetcher import get_artist_lyrics

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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


if __name__ == "__main__":
    lyrics_list = get_artist_lyrics("Taylor Swift", 70)
    full_lyrics = combine_lyrics(lyrics_list)

    tokenized_lyrics = word_tokenize(full_lyrics)
    stop_words = set(stopwords.words("english"))
    stop_words.update({",", "'s", "u", "'re", "'m", "'ll", "(", ")"})
    stop_words -= {"him"}

    filtered_lyrics = [word for word in tokenized_lyrics if word.lower() not in stop_words]
    # filtered_lyrics = tokenized_lyrics

    lemmatized_lyrics = [lemmatizer.lemmatize(word) for word in filtered_lyrics]
    
    print(lemmatized_lyrics)

    fdist = FreqDist(lemmatized_lyrics)
    sorted_freq = fdist.most_common()

    print(sorted_freq)

    top = 70
    top_words = fdist.most_common(top)
    words, counts = zip(*top_words)

    plt.figure(figsize=(25, 6))
    plt.bar(words, counts)
    plt.title(f"Top {top} Most Frequent Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
        
