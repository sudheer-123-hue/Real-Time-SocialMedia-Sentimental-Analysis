# 🚀 Real-Time Social Media Sentiment Analysis Platform

> End-to-End Azure Data Engineering Project using Azure Event Hub, Azure Data Lake Storage Gen2, Azure Databricks, dbt, Apache Airflow, Power BI and Slack Notifications.

---

# 📌 Project Overview

This project implements a complete real-time Social Media Sentiment Analysis Platform using the Medallion Architecture (Bronze → Silver → Gold).

The pipeline ingests streaming social media data through Azure Event Hub, processes it using Azure Databricks Structured Streaming, transforms it into analytics-ready datasets using dbt, stores business-ready Delta tables in Azure Data Lake Storage Gen2, orchestrates workflows using Databricks Jobs/Airflow, and delivers insights through Power BI dashboards.

The project also includes:

- Real-time streaming
- Medallion Architecture
- Delta Lake
- Unity Catalog
- dbt Gold Layer
- Logging
- Exception Handling
- Data Quality Testing
- Slack Notifications
- ADLS Gen2 Storage
- Star Schema Data Warehouse

---

# 🏗️ High Level Architecture

![High Level Architecture](architecture/high_level_architecture.png)

---

# 🔧 Low Level Design

![Low Level Design](architecture/low_level_design.png)

---

# ⭐ Star Schema

![Star Schema](architecture/star_schema.png)

---

# 📋 List of Tables

![Tables](architecture/list_of_tables.png)

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Cloud | Microsoft Azure |
| Streaming | Azure Event Hub |
| Storage | Azure Data Lake Storage Gen2 |
| Processing | Azure Databricks |
| Data Lake | Delta Lake |
| Transformation | PySpark |
| Data Modeling | dbt |
| Catalog | Unity Catalog |
| Workflow | Databricks Workflows |
| Orchestration | Apache Airflow |
| Reporting | Power BI |
| Notifications | Slack |
| Testing | dbt Tests, PyTest |
| Language | Python, SQL |

---

# 📂 Project Structure

```
Real-Time-Social-Media-Sentiment-Analysis
│
├── architecture/
│   ├── high_level_architecture.png
│   ├── low_level_design.png
│   ├── star_schema.png
│   └── list_of_tables.png
│
├── notebooks/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── common/
│
├── dbt/
│   ├── models/
│   ├── tests/
│   ├── seeds/
│   └── dbt_project.yml
│
├── airflow/
│
├── datasets/
│
├── dashboards/
│
├── screenshots/
│
├── docs/
│
└── README.md
```

---

# 📊 Dataset

The project processes real-time social media streaming data.

### Source Files

- Tweets
- User Metadata
- Sentiment Scores
- Trending Topics
- Valid Tweets
- External News Feeds

### Main Attributes

- Tweet ID
- User ID
- Username
- Tweet Text
- Sentiment Score
- Topic
- Timestamp
- Likes
- Replies
- Retweets
- Impressions
- Country
- Language

---

# 🏛 Medallion Architecture

## Bronze Layer

Raw streaming data from Azure Event Hub.

Tables

- bronze_tweets_raw
- bronze_user_metadata_raw
- bronze_sentiment_raw
- bronze_trends_raw
- bronze_valid_tweets_raw

Features

- Raw ingestion
- Append only
- Schema inference
- Delta Format
- Streaming Checkpoints

---

## Silver Layer

Business validated data.

Tables

- silver_tweets
- silver_user_metadata
- silver_sentiment
- silver_trends
- silver_valid_tweets

Transformations

- Duplicate Removal
- Null Handling
- Data Cleansing
- Standardization
- Business Rules
- Data Quality Validation
- Logging
- Exception Handling

---

## Gold Layer (dbt)

Business-ready analytics layer.

Dimension Tables

- dim_user
- dim_topic
- dim_date
- dim_sentiment

Fact Table

- fact_socialmedia

Aggregate Tables

- daily_socialmedia
- topic_summary
- country_summary

KPI Table

- executive_dashboard

---

# ⭐ Star Schema

One Fact Table

- fact_socialmedia

Dimension Tables

- dim_user
- dim_topic
- dim_date
- dim_sentiment

---

# 🔄 Pipeline Flow

```
Twitter / Social Media

        │

Azure Event Hub

        │

Azure Databricks Bronze

        │

Azure Databricks Silver

        │

dbt Gold Models

        │

Delta Tables

        │

Azure Data Lake Storage Gen2

        │

Power BI Dashboard

        │

Slack Notifications
```

---

# 📈 Dashboards

The Power BI dashboard provides:

- Executive KPI Dashboard
- Daily Sentiment Analysis
- Country-wise Analysis
- Topic-wise Analysis
- User Engagement
- Positive vs Negative Sentiment
- Trending Topics
- Tweet Volume
- Top Countries
- Executive Summary

---

# 📦 Workflow

Databricks Workflow

```
Bronze

↓

Silver

↓

dbt Gold

↓

Export Gold to ADLS

↓

Slack Notification
```

---

# ✅ Data Quality

Implemented using

- dbt Tests
- PyTest
- Schema Validation
- Null Checks
- Duplicate Checks
- Data Reconciliation
- Business Rule Validation

---

# 📝 Logging & Monitoring

Implemented

- Application Logging
- Exception Handling
- Delta Logging Tables
- Databricks Job Logs
- Slack Alerts
- Pipeline Monitoring

---

# 📁 Storage

Azure Data Lake Storage Gen2

Containers

- raw
- silver
- gold
- logs

Data Format

- Delta Lake

---

# 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/Real-Time-Social-Media-Sentiment-Analysis.git
```

### Open Azure Databricks

Import all notebooks.

### Configure

- Azure Event Hub
- ADLS Gen2
- Unity Catalog
- Storage Credentials
- External Locations

### Execute Pipeline

Run in order

1. Bronze Streaming
2. Silver Processing
3. dbt

```
dbt deps
dbt seed
dbt run
dbt test
```

4. Export Gold to ADLS

5. Execute Databricks Workflow

---

# 🎯 Project Outcomes

✔ Real-time streaming pipeline

✔ End-to-End Azure Data Engineering Solution

✔ Medallion Architecture

✔ Delta Lake

✔ Unity Catalog

✔ dbt Transformations

✔ Star Schema

✔ Automated Data Quality Checks

✔ Logging & Exception Handling

✔ Slack Notifications

✔ Power BI Reporting

✔ Databricks Workflows

✔ ADLS Gen2 Storage

---

# 👥 Team Members

- Dara Naga Sai Sudheer
- Mallikarjun
- Chandrika
- Santhosh
- Suhan

---

# 👨‍💻 Author

**Dara Naga Sai Sudheer**

Azure Data Engineer | PySpark | Azure Databricks | Delta Lake | dbt | SQL | Python
