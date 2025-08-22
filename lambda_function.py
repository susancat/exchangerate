import json
import urllib.request
import boto3
from datetime import datetime
from decimal import Decimal


def lambda_handler(event, context):
    # call API
    url = 'https://open.er-api.com/v6/latest/USD'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    # fetch the exchange rate and date
    rate = data["rates"]["TWD"]
    today = datetime.utcnow().strftime('%Y-%m-%d')

    # write to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ExchangeRates')

    table.put_item(Item={
        'date': today,
        'usd_to_twd': Decimal(str(rate))  # 👈 use Decimal to convert float
    })

    print(f"Wrote USD→TWD {rate} for {today} to DynamoDB")

    return {
        'statusCode': 200,
        'body': json.dumps({'date': today, 'usd_to_twd': float(rate)})
    }
