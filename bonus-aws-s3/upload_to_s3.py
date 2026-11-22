from pathlib import Path

import boto3
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError, NoCredentialsError

BUCKET = "your-lab-bucket-name"
KEY = "python-bonus/employees.json"
FILE = Path("employees.json")

if not FILE.is_file():
    raise SystemExit("employees.json was not found.")

s3 = boto3.client("s3")

try:
    s3.upload_file(str(FILE), BUCKET, KEY)
    result = s3.head_object(Bucket=BUCKET, Key=KEY)
except (S3UploadFailedError, ClientError, NoCredentialsError) as error:
    raise SystemExit(f"AWS operation failed: {error}")

if result["ContentLength"] != FILE.stat().st_size:
    raise SystemExit("Verification failed: file sizes differ.")

print(f"Verified s3://{BUCKET}/{KEY}")
print(f"Object size: {result['ContentLength']} bytes")
