from boto3.session import Session
import boto3

ACCESS_KEY = 'AKIA4HTTGDLfadfsdfdsfg'
SECRET_KEY = 'Yl5hmy5H+ztNUKYuA+eorueorufdfa'

session = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY,
              region_name='cn-north-1')

s3 = session.resource('s3')
your_bucket = s3.Bucket('nlp')

for s3_file in your_bucket.objects.all():
    print(s3_file.key) # prints the contents of bucket


s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3.download_file('nlp', 'ltp_data_v3.4.0.zip', '/tmp/ltp_data_v3.4.0.zip')
