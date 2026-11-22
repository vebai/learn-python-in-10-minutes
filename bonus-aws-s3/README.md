# Optional Bonus — Automate AWS with Python

Use this exercise to upload the Employee Directory JSON to a private S3 bucket, verify it, and remove the object.

## Preparation

1. Install Boto3 using `python -m pip install boto3` and configure the AWS CLI.
2. Sign in with a named AWS CLI profile or IAM Identity Center (SSO); do not put access keys in files.
3. Run `aws sts get-caller-identity` and confirm your AWS account and Region.
4. Use a private practice S3 bucket you control. AWS charges may apply.
5. Copy `employees.json` from the Chapter 7 project into this folder.
6. Replace `BUCKET` in **both** Python programs with your practice bucket name.

[.env.example](.env.example) illustrates optional AWS shell settings. The Python scripts **do not read .env files automatically**, and `S3_BUCKET_NAME` does not replace the `BUCKET` constant.

## Run the exercise

```bash
python upload_to_s3.py
python cleanup_s3.py
```

Verify the uploaded object in S3 before cleanup, then verify it is gone. Never commit credentials.

## Files

- `upload_to_s3.py`
- `cleanup_s3.py`
- `.env.example` — optional settings reference

More short examples and sample output: [Additional examples](additional-excerpts.md).
