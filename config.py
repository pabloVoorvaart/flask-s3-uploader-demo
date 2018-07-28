import boto3, os

SECRET_KEY = os.environ.get('BUCKET_NAME') or ("FLASK_SECRET_KEY")
BUCKET_NAME = os.environ.get('BUCKET_NAME')
S3 = boto3.resource(
    's3',
    aws_access_key_id=os.environ.get('ACCES_KEY'),
    aws_secret_access_key=os.environ.get('SECRET_KEY'),
    region_name=os.environ.get('REGION_NAME'),
    )
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
