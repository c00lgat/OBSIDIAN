import boto3
from pprint import pprint as pp


client = boto3.client('ec2')

response = client.describe_instances(
    # Filters=[
    #     {
    #         'Subnet-Id': 'subnet-090d6373abcd8fa37'
    #     }
    # ]
)

for i in response['Reservations']:
    pp(i['Instances'][0]['InstanceId'])
    instance_id = i['Instances'][0]['InstanceId']
    tag_counter = 0
    for y in i['Instances'][0]['Tags']:
        tag = y
        if y['Key'] == 'Environment':
            tag_counter+=1
    if tag_counter == 0:
        termination_response = client.terminate_instances(
            InstanceIds = [instance_id]
        )
        print(termination_response)

