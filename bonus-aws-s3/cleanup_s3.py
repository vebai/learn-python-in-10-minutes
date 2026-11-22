import boto3
from botocore.exceptions import ClientError

BUCKET = "your-lab-bucket-name"
KEY = "python-bonus/employees.json"

s3 = boto3.client("s3")

try:
    s3.delete_object(Bucket=BUCKET, Key=KEY)
except ClientError as error:
    raise SystemExit(f"Cleanup failed: {error}")

print(f"Delete requested for s3://{BUCKET}/{KEY}")
print("Verify in the AWS Console that the object no longer appears.")
