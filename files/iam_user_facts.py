import boto3

client = boto3.client('iam')

usernames = []

response = client.list_users(MaxItems=1)
usernames = usernames + list(map(lambda user_details: user_details['UserName'], response['Users']))

while (response['IsTruncated']):
    response = client.list_users(MaxItems=1, Marker=response['Marker'])
    usernames = usernames + list(map(lambda user_details: user_details['UserName'], response['Users']))

print(usernames)
