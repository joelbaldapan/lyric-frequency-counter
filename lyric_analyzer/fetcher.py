import os
from typing import TYPE_CHECKING

from dotenv import load_dotenv
from lyricsgenius import Genius

if TYPE_CHECKING:
    from lyricsgenius.types import Artist

# Load genius access token from .env
load_dotenv()
TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

# Set-up genius API
genius: Genius = Genius(TOKEN)
genius.remove_section_headers = True  # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False  # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"]  # Exclude songs with these words in their title


def get_artist_lyrics(artist_name: str, max_songs: int = 20) -> list[str]:
    """Search for the first `max_songs` popular songs that the artist appears on.

    Args:
        artist_name (str): The name of the artist to search for.
        max_songs (int, optional): The maximum number of songs to fetch. Defaults to 20.

    Returns:
        list[str]: A list of lyrics strings for the artist's songs.

    """
    artist: Artist | None = genius.search_artist(
        artist_name,
        max_songs=max_songs,
        sort="popularity",
        include_features=True,
    )

    if not artist:
        return []

    raw_lyrics_list = [song.lyrics for song in artist.songs]
    return clean_lyrics(raw_lyrics_list)


def clean_lyrics(lyrics_list: list[str]) -> list[str]:
    """Remove the first-line annotations that appear in every song.

    Args:
        lyrics_list (list[str]): List of lyrics strings.

    Returns:
        list[str]: List of cleaned lyrics strings with first-line annotations removed.

    """
    cleaned_lyrics_list = []
    for lyrics in lyrics_list:
        first_new_line = lyrics.index("\n")
        cleaned_lyrics_list.append(lyrics[first_new_line + 1 :])
    return cleaned_lyrics_list
