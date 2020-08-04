import boto3
import boto3.session
import time
awsAccessKey = "#############"
awsSecretAccessKey = "###################"
region = "cn-north-1"
s3BucketName = 'yourbucketname'
oldFolderKey = 'source'
newFolderKey = 'target'

session = boto3.Session(aws_access_key_id=awsAccessKey, aws_secret_access_key=awsSecretAccessKey, region_name=region)
s3 = session.resource('s3')
bucket = s3.Bucket(s3BucketName)
for object in bucket.objects.filter(Prefix=oldFolderKey):
    srcKey = object.key
    if not srcKey.endswith('/'):
        fileName = srcKey.split('/')[-1]
        destFileKey = newFolderKey + '/' + fileName + '.' + time.strftime('%Y%m%d')
        copySource = s3BucketName + '/' + srcKey
        s3.Object(s3BucketName, destFileKey).copy_from(CopySource=copySource)
        #s3.Object(s3BucketName, srcKey).delete()
