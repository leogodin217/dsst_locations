import boto3

db = boto3.resource('dynamodb', 
                    region_name='us-west-2', 
                    endpoint_url='http://localhost:8000')

# Create the table, using only the id as the hash key
table = db.create_table(
    TableName='dsst_locations',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until we are finished
table.wait_until_exists()
print('Table created')