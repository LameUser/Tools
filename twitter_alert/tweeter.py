import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_latest_tweet(twitter_handle):
    url = f"https://twitter.com/{twitter_handle}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the latest tweet
        tweet_container = soup.find('div', {'data-testid': 'tweet'})
        if tweet_container:
            tweet_text = tweet_container.find('div', {'lang': True}).text.strip()
            timestamp = tweet_container.find('time')['datetime']
            return tweet_text, timestamp

        return None, None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching tweets: {e}")
        return None, None

if __name__ == "__main__":
    twitter_handle = input("Enter the Twitter handle (without @): ").strip()
    last_tweet_timestamp = None

    print(f"Monitoring tweets from @{twitter_handle}...\n")

    while True:
        tweet, timestamp = get_latest_tweet(twitter_handle)
        if tweet and timestamp != last_tweet_timestamp:
            print(f"\n[{datetime.now()}] New tweet detected from @{twitter_handle}:\n{tweet}\n")
            last_tweet_timestamp = timestamp
        else:
            print(f"[{datetime.now()}] No new tweets from @{twitter_handle}.")
        time.sleep(60)  # Check every minute
