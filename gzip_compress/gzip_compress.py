import json
import pprint
import boto3
import botocore
import tempfile
import os
import subprocess
import fnmatch
import gzip

def lambda_handler(event, context):
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    for r in event.get('Records'):
        #pprint.pprint(r)
        bucketName = r.get('s3').get('bucket').get('name')
        objectKey = r.get('s3').get('object').get('key')
        etag = r.get('s3').get('object').get('eTag')
        print ("Retreiving object :")
        print (" bucketname = " + bucketName)
        print (" objectKey = " + objectKey)
        uploadedMeta = client.head_object(Bucket=bucketName, Key=objectKey, IfMatch=etag)
        contentEncoding = uploadedMeta.get('ContentEncoding', None)
        size = uploadedMeta.get('ContentLength', 0)
        print (" Current encoding = " + str(contentEncoding))
        print (" Size = " + str(size))
        
        tmp_in = tempfile.mkdtemp()+'.orig'
        tmp_out = tmp_in + '.gz' # must be .gz because it is gzip default file creation
        new_objectKey = objectKey + '.gz' # name in S3
        print("Download content to " + tmp_in + " and gzip it to " + tmp_out)
        s3.Bucket(bucketName).download_file(objectKey, tmp_in)
        print("GZipping file")
        print (subprocess.check_output(['gzip', '-v', '-f', '-9', tmp_in])) #  gzip command create .gz file
        statinfo = os.stat(tmp_out)
        newsize = statinfo.st_size
        print ("New gzipped file = " + str(statinfo.st_size))
        print ("Uploading gzipped S3 file to another bucket")
        
        bucketNamebk = 'tizhong-compression-bk' #  backup s3 bucket name
        s3.Object(bucketNamebk, objectKey).upload_file(
            Filename=tmp_out)

        # remove local file
        os.remove(tmp_out) 
    return {
        'statusCode': 200,
        'body': 'It works'
    }
