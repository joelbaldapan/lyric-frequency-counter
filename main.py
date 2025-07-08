from lyric_analyzer.fetcher import get_artist_lyrics
from lyric_analyzer.analyzer import analyze_lyrics, plot_top_words


def main():
    while True:
        artist = input("Name of artist (or 'q' to quit): ").strip()
        if artist.lower() == 'q':
            break

        try:
            num_songs = int(input("How many songs to look up: ").strip())
            top_n = int(input("How many most frequent words: ").strip())
        except ValueError:
            print("Please enter valid numbers.")
            continue

        lyrics_list = get_artist_lyrics(artist, num_songs)
        if not lyrics_list:
            print("No lyrics found.")
            continue
        sorted_freq = analyze_lyrics(lyrics_list)
        print(sorted_freq[:top_n])
        plot_top_words(sorted_freq, top=top_n)


if __name__ == "__main__":
    main()