# Lyric Frequency Counter

A Python app that fetches song lyrics for a given artist and analyzes the frequency of words or phrases in their songs.

## Features

- Fetches lyrics using the Genius API.
- Analyzes word frequency in song lyrics.
- Visualizes the most frequent words with a bar chart.
- Customizable number of songs and top frequent words to display.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/joelbaldapan/lyric-frequency-counter
   cd lyric-frequency-counter
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Create a Genius API account:**

   - Create an account at the [Genius API developer portal](https://genius.com/developers)
   - Copy your access token.

4. **Set up environment file:**

   - Copy the `.env.example` file in the project root and rename it to `.env`

   ```sh
   cp .env.example .env
   ```

   - In your newly created `.env` file, replace `YOUR_TOKEN_HERE` with your Genius API access token:

   ```
   GENIUS_ACCESS_TOKEN=YOUR_TOKEN_HERE
   ```

## Usage

Run the main script:

```sh
python main.py
```

You will be prompted to enter:

- The artist's name
- The number of songs to analyze
- The number of top frequent words to display

The app will fetch lyrics, analyze word frequencies, print the most frequent words, and display a bar chart.

## Example

```
Name of artist (or 'q' to quit): Coldplay
How many songs to look up: 10
How many most frequent words: 20
[('love', 42), ('life', 35), ...]
```

A bar chart of the top 20 words will be displayed.
