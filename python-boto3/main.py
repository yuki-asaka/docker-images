import boto3


def list_s3():
    s3 = boto3.client('s3')
    res = s3.list_buckets()
    for bucket in res.get('Buckets', []):
        print(bucket.get('Name'))


if __name__ == '__main__':
    list_s3()
