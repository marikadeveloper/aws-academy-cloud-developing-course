# upload a css file to the bucket
import boto3

S3API = boto3.client("s3", region_name="us-east-1")
bucket_name = " samplebucket"
filename = "/resources/website/core.css"
S3API. upload__file(filename, bucket_name, "core.css", ExtraArgs={ 'ContentType': "text/css", "CacheControl": "max-age=0" })