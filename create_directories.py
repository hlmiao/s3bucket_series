import boto3
s3 = boto3.client('s3', 
                  region_name='cn-north-1', 
                  aws_access_key_id='afdfadfadfdfdsfsdfa', 
                  aws_secret_access_key='fadfadfawcjZCIdfdsfdsfdsfa')
# Create sub folders
# It's name of your folders
directory_name = "python" 
s3.put_object(Bucket='loganything',Key=(directory_name+'/'))
