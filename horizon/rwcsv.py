import boto3
import io
from io import BytesIO
import pandas as pd

# Load AWS S3 credentials
session = boto3.Session(profile_name='default')
s3 = session.resource('s3')

# Select the S3 bucket and file
bucket = s3.Bucket('horzion-bucket')
key = 'list/namelist.csv'

# Read the CSV file from S3
csv_obj = s3.Object(bucket.name, key)
body = csv_obj.get()['Body'].read()

# Convert the CSV data to Pandas DataFrame
import pandas as pd
df = pd.read_csv(BytesIO(body), encoding='utf8')
print(df.head())
