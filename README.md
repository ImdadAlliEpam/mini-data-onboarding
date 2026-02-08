# mini-data-onboarding

## Overview
This project demonstrates a self-service, event-driven data onboarding
platform on AWS that converts CSV files into Apache Iceberg tables
queryable via Athena.

## Architecture
S3 (Source) → Lambda → Glue Visual ETL → Iceberg → Athena

## Components
- AWS S3 (source & sink)
- AWS Lambda (orchestration)
- AWS Glue Visual ETL (processing)
- Apache Iceberg
- AWS Glue Data Catalog
- Amazon Athena

## Implementation Notes
- Glue job was created using Visual ETL
- Generated Spark script is version-controlled under `glue/`
- Lambda source code is available under `lambda/`

## Setup Steps
1. Create S3 buckets and folders
2. Create Glue Visual ETL job
3. Create Lambda function and IAM role
4. Configure S3 event notifications
5. Query data using Athena

## Error Handling
- Lambda uses try/except with CloudWatch logging
- Glue job failures visible in Glue Job Runs & CloudWatch

## Improvements
- Terraform for IaC
- CI/CD for Lambda & Glue
- Schema validation
- Data quality rules expansion
