import os
from dotenv import load_dotenv
import boto3

load_dotenv()

# print("AWS_REGION =", os.getenv("AWS_REGION"))
# print("S3_BUCKET =", os.getenv("S3_BUCKET"))
# print("S3_KEY =", os.getenv("S3_KEY"))

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")

LOCAL_PATH = os.path.join("data", "downloaded.csv")
os.makedirs("data", exist_ok=True)

def main():
    s3 = boto3.client("s3", region_name=AWS_REGION)
    s3.download_file(S3_BUCKET, S3_KEY, LOCAL_PATH)
    print(f"Downloaded s3://{S3_BUCKET}/{S3_KEY} -> {LOCAL_PATH}")

if __name__ == "__main__":
    main()
