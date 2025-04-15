#import the json utility package
import json
#import the python math library
import math
#import the AWS SDK (for python the name is boto3)
import boto3
#import two packages to help us with dates and date formattting
from time import gmtime,strftime
#create dynamodb object using the AWS SDK
dynamodb =boto3.resource('dynamodb')
#use dynamodb object to select our table 
table =dynamodb.Table('mathsCalculation')
#store the current time in human readable format in a variable 
now = strftime("%a,%d %b %Y %H:%M:%S +0000",gmtime())
#define the lambda function where that the lambda service will use an entry point 
def lambda_handler(event,context):
    #extract the two numbers from the lambda services event object
    mathResult = math.pow(int (event["base"]),int(event["exponent"]))

    #write the result and time to the dynamo db table using the object we installed and save the response in a variable 

    responsible = table.put_item(
        Item ={
            "ID":str(mathResult),
            "LatestGreetingTime":now
        }
    )
    #return a properly formatted Json Object
    return{
        'statusCode':200,
        'body':json.dumps('your result is'+str(mathResult))
    }