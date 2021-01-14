######Delete s3 bucket files with multiple conditions in Python 3.x ######
###Examples
###{'Key': 'crawler.pdf'}
###{'Key': 'crawler.txt'}
###{'Key': 'test001/Report.pdf'}
###{'Key': 'test001/test002/Report.pdf'}
###{'Key': 'test001/test002/crawler.pdf'}
###{'Key': 'test001/test002/crawler.txt'}


import boto3
import datetime
from datetime import timedelta

s3 = boto3.client('s3', region_name='cn-north-1')
response = s3.list_objects_v2(Bucket='your-bucket-name')

keys_to_delete = [{'Key': object['Key']}
                  for object in response['Contents']
                  if object['LastModified'] > datetime.datetime.now().astimezone() - timedelta(days=7) #### check the day differ over 7 days
                     and ('crawler' in object['Key'] or 'Report' in object['Key']) ### Apply lifecycle rules with wildcards such as *crawler* and *Report* 
                 ]

print(*keys_to_delete, sep="\n") ###Print is a function in Python 3.x

input("Confirm the Deleter files name and Press Enter to continue...")

s3.delete_objects(Bucket='your-bucket-name', Delete={'Objects': keys_to_delete})
