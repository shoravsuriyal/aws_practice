import boto3

dynamodb= boto3.client('dynamodb')


def lambda_handler(event,cotext):
    
    #response = dynamodb.delete_table(TableName='SampleTable')
    '''
    table_name = "SampleTable"
    table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[{"AttributeName": "Name", "KeyType": "HASH"},{"AttributeName": "Age", "KeyType": "RANGE"}],
    
    AttributeDefinitions=[{"AttributeName": "Name", "AttributeType": "S"},{"AttributeName": "Age", "AttributeType": "N"}],
     
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    })
    '''
    #dynamodb.put_item(TableName='SampleTable', Item={"Name": {"S": "John"},"Age": {"N": "10"}})
    #dynamodb.put_item(TableName='SampleTable', Item={"Name": {"S": "Bob"},"Age": {"N": "45"}}) 
    #dynamodb.put_item(TableName='SampleTable', Item={"Name": {"S": "Taylor"},"Age": {"N": "32"}})

    with xray_recorder.in_segment('Dynamodb') as segment:
    # Add metadata or annotation here if necessary
    segment.put_metadata('key', dict, 'namespace')
    with xray_recorder.in_subsegment('Table-get-operation') as subsegment:
        subsegment.put_annotation('key', 'value')
        # Do something here
        response = dynamodb.get_item(TableName='SampleTable', Key={'Name':{'S':"John"},'Age':{'N':"10"}})

    #dynamodb.put_item(TableName='SampleTable',Key={'Name':{'S':'John'}})

    print 'I am executed successfully'
    return response






