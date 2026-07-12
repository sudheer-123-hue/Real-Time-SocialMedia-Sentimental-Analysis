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
    "EntityPath=user-metadata-hub"
)

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STRING
)

# ==========================================
# Read CSV
# ==========================================

df = pd.read_csv(r"C:\Twitter_project_rev\bronze_user_metadata_raw.csv")

print("Starting User Metadata Producer...")

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
        "user_id": row["user_id"],
        "country": row["country"],
        "topic_category": row["topic_category"],
        "account_created_date": row["account_created_date"],
        "followers_count": row["followers_count"],
        "following_count": row["following_count"],
        "likes_count": row["likes_count"],
        "shares_count": row["shares_count"],
        "posts_count": row["posts_count"],
        "verified": row["verified"]
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

print(f"Successfully sent {record_count} records to User Metadata Event Hub.")
