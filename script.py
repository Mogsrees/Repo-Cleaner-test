import requests
import boto3 
import os

data = ['dlfe123', 'efad786', '864pws', '8hgyfs']

url = 'http://corey-awesome-website.com'
usr = 'corey@accenture.com'
pwd = os.environ['ENV_PASS']

resp = requests.post(url, data=data, auth=(usr, pwd))


s3_client = boto3.client('s3', 
				aws_access_key_id='AKEQIEDKFDAW', 
				aws_secret_acces_key='0-314dfaDAFDFAS', 
				region_name='eu-west-1')

s3_client.get_bucket_policy(
				Bucket='arn:aws:s3:::corey-s3bucket'
)
