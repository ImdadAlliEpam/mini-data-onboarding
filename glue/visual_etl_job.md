---
noteId: "01c72930050911f1a634578e04098deb"
tags: []

---

# Glue Visual ETL Job: csv-to-iceberg

## Job Type
AWS Glue Visual ETL (Spark)

## Source
- S3 Path: s3://epam-demo-source/source/
- Format: CSV

## Transformations
- SelectFields: order_id, order_date, order_customer_id, order_status

## Target
- Format: Apache Iceberg
- Database: onboarding_db
- Table: orders
- Warehouse Path: s3://epam-demo-sink/sink/onboarding_db/orders

## Write Strategy
- Create table if not exists
- Append data for subsequent files

## Trigger
- Event-driven via S3 → Lambda
