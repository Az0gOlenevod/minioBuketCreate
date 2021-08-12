import json
from minio import Minio
minio_url = '127.0.0.1:9000'
project_name = 'xyi'
access_key= '123456789'
privat_key='123456789'


def CreateBucket(project_name, minio_url):
    policy_read_only = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetBucketLocation",
                "Resource": f"arn:aws:s3:::{project_name}"
            },
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:ListBucket",
                "Resource": f"arn:aws:s3:::{project_name}"
            },
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{project_name}/*"
            }
        ]
    }
    minioClient = Minio(minio_url,
                    access_key=access_key,
                    secret_key=privat_key,
                    secure=False)
    minioClient.make_bucket(project_name)
    minioClient.set_bucket_policy(project_name, json.dumps(policy_read_only))



CreateBucket (project_name,minio_url)