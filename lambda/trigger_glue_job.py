"""
Lambda function triggered by S3 events.

Responsibilities:
- Capture uploaded CSV file details
- Trigger AWS Glue Visual ETL job
- Enable event-driven data onboarding
"""

import json
import boto3
import os

glue = boto3.client('glue')

GLUE_JOB_NAME = "csv-to-iceberg"

def lambda_handler(event, context):
    print("Lambda triggered by S3 event ✅")
    print("Event received:")
    print(json.dumps(event, indent=2))

    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        s3_path = f"s3://{bucket}/{key}"
        print(f"Starting Glue job for file: {s3_path}")

        response = glue.start_job_run(
            JobName=GLUE_JOB_NAME,
            Arguments={
                '--SOURCE_S3_PATH': s3_path
            }
        )

        print(f"Glue job started successfully 🚀")
        print(f"JobRunId: {response['JobRunId']}")

    except Exception as e:
        print("❌ Failed to start Glue job")
        print(str(e))
        raise e
