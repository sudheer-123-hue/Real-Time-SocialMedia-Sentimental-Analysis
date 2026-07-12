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
    "EntityPath=trends-hub"
)

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING
)

# ==========================================
# Read CSV
# ==========================================

df = pd.read_csv(r"C:\Twitter_project_rev\bronze_trends_raw.csv")

print("Starting Trends Producer...")

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
        "trend_timestamp": row["trend_timestamp"],
        "topic_category": row["topic_category"],
        "country": row["country"],
        "tweet_volume": row["tweet_volume"],
        "mention_count": row["mention_count"],
        "retweet_count": row["retweet_count"],
        "trend_score": row["trend_score"],
        "sentiment_index": row["sentiment_index"],
        "impressions": row["impressions"],
        "engagement_count": row["engagement_count"]
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

print(f"Successfully sent {record_count} records to Trends Event Hub.")
