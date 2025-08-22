# import pytest
from lambda_function import lambda_handler
from unittest.mock import patch, MagicMock
import json

@patch('urllib.request.urlopen')
@patch('boto3.resource')
def test_lambda_handler_success(mock_boto3_resource, mock_urlopen):
    # 模擬 API 回傳資料
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps({
        "rates": {"TWD": 32.5}
    }).encode('utf-8')
    mock_urlopen.return_value = mock_response

    # 模擬 DynamoDB 寫入
    mock_table = MagicMock()
    mock_dynamodb = MagicMock()
    mock_dynamodb.Table.return_value = mock_table
    mock_boto3_resource.return_value = mock_dynamodb

    # 呼叫 handler
    result = lambda_handler({}, {})

    # 驗證 response
    assert result["statusCode"] == 200
    body = json.loads(result["body"])
    assert "usd_to_twd" in body
    assert isinstance(body["usd_to_twd"], float)

    # 驗證 DynamoDB 寫入有被呼叫
    mock_table.put_item.assert_called_once()
