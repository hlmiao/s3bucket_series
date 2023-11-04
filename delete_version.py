### Deleting latest version of multiple object ###

import boto3
 
s3Client = boto3.client('s3',region_name="cn-north-1")
sourceBucket = ""
prefix=""
 
NextKeyMarker = "start"
NextVersionIdMarker = "start"
 
while(NextKeyMarker!="" and NextVersionIdMarker!=""):
    objects = []
    if NextKeyMarker == "start" and NextVersionIdMarker == "start":
        result = s3Client.list_object_versions(Bucket=sourceBucket,Prefix=prefix)
    else:
        result = s3Client.list_object_versions(Bucket=sourceBucket,KeyMarker=NextKeyMarker,VersionIdMarker=NextVersionIdMarker)
 
    if "DeleteMarkers" in result.keys():
        deleteMarkers = result["DeleteMarkers"]
        # print(len(deleteMarkers))
        for delete_marker in deleteMarkers:
            if delete_marker["IsLatest"] == True:
            	object_key = delete_marker["Key"]
				object_VersionID = delete_marker["VersionId"]
                objects.append({"Key":object_key,"VersionId":object_VersionID})
   
    print(objects)
 
    response = s3Client.delete_objects(Bucket=sourceBucket,Delete={"Objects":objects})
 
    print(response)
 
    if result['IsTruncated']:
        # print(result["NextKeyMarker"])
        NextKeyMarker = result["NextKeyMarker"]
        # print(result["NextVersionIdMarker"])
        NextVersionIdMarker = result["NextVersionIdMarker"]
    else:
        NextKeyMarker = ""
        NextVersionIdMarker = ""
