import boto3

dynamodb= boto3.client('dynamodb')

table = boto3.resource('dynamodb').Table('SampleTable')

pipeline = boto3.client('codepipeline')

sqs=boto3.client('sqs')

queue_url='https://sqs.us-east-2.amazonaws.com/496585200392/xray-sdk'

num=10

from boto3.dynamodb.conditions import Key

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



    result=dynamodb.get_item(TableName='SampleTable', Key={'Name':{'S':"John"},'Age':{'N':"10"}},ConsistentRead=True)
    

    #getsqsdata=table.query(KeyConditionExpression=Key('Name').eq('John')) 
    

    #### Time Consuming code 

    d= table.scan()
    def getsqsdata(k,d):

        if k in d:

            return d[k]

        for v in d.values():

            if isinstance(v,dict):

                res=getsqsdata(k,v)

                if res is not None:

                    return res
        return None

    #### 

    print type(getsqsdata)
    
    print "==========================="

    print getsqsdata

    print "========End Of Data========"

    
     
    response= sqs.send_message(
        
        QueueUrl=queue_url,
        MessageAttributes={
            'Name':{
                'DataType':'String',
                
                'StringValue':getsqsdata['Items'][0]['Name'],
                
            },
            
            'Age':{
                'DataType':'String',
                
                'StringValue':str(getsqsdata['Items'][-1]['Age']),
                
            }},
            
            MessageBody=('Pushing the data to sqs')
    
        )
    
    response1 = pipeline.put_job_success_result(jobId=event['CodePipeline.job']['id'])    

    #dynamodb.get_item(TableName='SampleTable2', Key={'Name':{'S':"John"},'Age':{'N':"10"}})

    #dynamodb.put_item(TableName='SampleTable',Key={'Name':{'S':'John'}})

    print 'I am executed successfully'
    return response






