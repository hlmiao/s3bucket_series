import boto3
import datetime
import pprint
import json
import pytz

# Create an S3 client
s3 = boto3.client('s3', region_name='cn-north-1')

# Set the S3 bucket name
bucket_name = 'ad-hoc-analysis-202012'
tz = pytz.timezone('Asia/Shanghai')
# Set the start date for listing objects
start_date = datetime.datetime(2023, 11, 22, tzinfo=tz)
start_after = start_date.strftime('%Y-%m-%d %H:%M:%S')
print (start_after)

# Set the prefix for folder name
prefix = 'test001'

# Initialize the list of objects
object_list = []

# Use a paginator to iterate over all objects in the bucket
paginator = s3.get_paginator('list_objects_v2')
try:
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix, StartAfter=start_after):
        if 'Contents' not in page:
            break

    # Iterate over each object in the current page of results
    for obj in page['Contents']:
        # Add the object to the list if it was created after the start date
        if obj['LastModified'] <= start_date:
            # Convert UTC LastModified time to Shanghai timezone
            Shanghai_time = obj['LastModified'].astimezone(tz)
            obj['LastModified'] = Shanghai_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
            # Convert size to MB
            obj['Size'] = round(obj['Size'] / (1024 * 1024), 2)
            object_list.append(obj)
except Exception as e:
    print("Error:", e)

# Print the list of objects
pprint.pprint(object_list)

# Open the file for writing
with open('s3_objects.txt', 'w') as f:
    # Write the formatted output to the file
    for obj in object_list:
        f.write(f"Key: {obj['Key']}, Last Modified: {obj['LastModified']}, Size: {obj['Size']} MB\n")
