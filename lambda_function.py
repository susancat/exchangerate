import json
import urllib.request
import boto3
from datetime import datetime
from decimal import Decimal


def lambda_handler(event, context):
    # call API
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    # fetch the exchange rate and date
    usd_to_twd = data['rates'].get('TWD')
    hkd_to_twd = data['rates'].get('TWD') / data['rates'].get('HKD')

    # write to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ExchangeRateTable')
    timestamp = datetime.utcnow().isoformat()

    table.put_item(Item={
        'timestamp': timestamp,
        'usd_to_twd': Decimal(str(usd_to_twd)),
        'hkd_to_twd': Decimal(str(hkd_to_twd))
    })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'usd_to_twd': usd_to_twd,
            'hkd_to_twd': round(hkd_to_twd, 4),
            'timestamp': timestamp
        })
    }
