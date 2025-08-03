import tweepy
import sqlite3

# Twitter API credentials (replace with your own)
bearer_token = "YOUR_TWITTER_BEARER_TOKEN"

client = tweepy.Client(bearer_token=bearer_token)

# Search for recent tweets about "sanctions"
query = "sanctions"
tweets = client.search_recent_tweets(query=query, max_results=10)

# Store tweets in SQLite
conn = sqlite3.connect("tweets.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS tweets (id TEXT, text TEXT)""")

for tweet in tweets.data:
    c.execute("INSERT INTO tweets (id, text) VALUES (?, ?)", (tweet.id, tweet.text))

conn.commit()
conn.close()
print("Tweets ingested!")
