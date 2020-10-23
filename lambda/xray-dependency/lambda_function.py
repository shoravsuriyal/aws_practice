import boto3

dynamodb= boto3.client('dynamodb')

from aws_xray_sdk.core import xray_recorder

from aws_xray_sdk.core import patch_all
patch_all()

@xray_recorder.capture('dynamodb')
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
    
    
    table_name = "SampleTable2"
    table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[{"AttributeName": "Name", "KeyType": "HASH"},{"AttributeName": "Age", "KeyType": "RANGE"}],
    
    AttributeDefinitions=[{"AttributeName": "Name", "AttributeType": "S"},{"AttributeName": "Age", "AttributeType": "N"}],
     
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    })
    
    '''

    dynamodb.put_item(TableName='SampleTable2', Item={"Name": {"S": "John"},"Age": {"N": "10"}})
    dynamodb.put_item(TableName='SampleTable2', Item={"Name": {"S": "Bob"},"Age": {"N": "45"}}) 
    #dynamodb.put_item(TableName='SampleTable', Item={"Name": {"S": "Taylor"},"Age": {"N": "32"}})



    dynamodb.get_item(TableName='SampleTable', Key={'Name':{'S':"John"},'Age':{'N':"10"}})

    
    #dynamodb.get_item(TableName='SampleTable2', Key={'Name':{'S':"John"},'Age':{'N':"10"}})

    #dynamodb.put_item(TableName='SampleTable',Key={'Name':{'S':'John'}})

    print 'I am executed successfully'
    return None






