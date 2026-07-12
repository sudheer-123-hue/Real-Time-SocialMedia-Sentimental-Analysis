from azure.eventhub import EventHubProducerClient, EventData
import pandas as pd
import json

# ==========================================
# Event Hub Connection String
# ==========================================

CONNECTION_STRING = (
    "Endpoint=sb://eh-social-media.servicebus.windows.net/;"
    "SharedAccessKeyName=sudheer;"
    "SharedAccessKey=1IhrynvVGzNbhQLyvqMUxuT7QdTRHRh57+AEhJK7+eQ=;"
    "EntityPath=valid-tweets-hub"
)

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING
)

# ==========================================
# Read CSV
# ==========================================

df = pd.read_csv(r"C:\Twitter_project_rev\bronze_valid_tweets_raw.csv")

print("Starting Valid Tweets Producer...")

# ==========================================
# Create Batch
# ==========================================

batch = producer.create_batch()

record_count = 0

# ==========================================
# Send Events
# ==========================================

for _, row in df.iterrows():

    event = {
        "tweet_id": row["tweet_id"],
        "topic_category": row["topic_category"],
        "tweet_text": row["tweet_text"],
        "tweet_timestamp": row["tweet_timestamp"],
        "impressions": row["impressions"],
        "likes": row["likes"],
        "retweets": row["retweets"],
        "replies": row["replies"],
        "engagement_count": row["engagement_count"],
        "sentiment_score": row["sentiment_score"]
    }

    event_json = json.dumps(event, default=str)

    try:
        batch.add(EventData(event_json))
        record_count += 1

    except ValueError:
        producer.send_batch(batch)
        print(f"{record_count} records sent...")

        batch = producer.create_batch()
        batch.add(EventData(event_json))
        record_count += 1

# ==========================================
# Send Remaining Records
# ==========================================

if len(batch) > 0:
    producer.send_batch(batch)

producer.close()

print(f"Successfully sent {record_count} records to Valid Tweets Event Hub.")
