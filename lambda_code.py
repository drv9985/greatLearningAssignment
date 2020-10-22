import json

def lambda_handler(event, context):
    # TODO implement
    
    data = {
        "name" : "great_learning",
        "type" : "assignment",
        "service" : "AWS Lambda and ALB"
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(data)
    }
