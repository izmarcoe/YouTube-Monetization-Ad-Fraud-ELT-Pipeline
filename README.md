# YouTube-Monetization-Ad-Fraud-ELT-Pipeline

1. Case Study Overview
* **Problem:** YouTube processes billions of daily video view events and ad impressions. Before paying creators or billing advertisers, the platform must filter out invalid bot traffic, handle schema drift from messy JSON payloads, and calculate accurate daily creator revenue (RPM) within strict SLAs.
* **Solution:** A hybrid-cloud ELT pipeline. Dockerized Apache Airflow extracts raw data from the YouTube API and simulated ad-click logs, landing them into AWS S3. Airflow then triggers Databricks (Apache Spark) to process the data through a Medallion Architecture (Bronze, Silver, Gold) stored as Delta Lake tables.
