# coding=utf-8
from boto3.session import Session
import csv

# DynamoDB接続情報
session = Session(aws_access_key_id='YOUR_ACCESS_KEY_ID',
                  aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
                  region_name='YOUR_REGION_NAME')
conn = session.resource('dynamodb')

# DynamoDBテーブル情報
table = conn.Table('TABLE_NAME')


if __name__ == '__main__':

    # CSVファイル読込み
    csv_object = csv.reader(open('csv file path', 'rb'))
    data = [ v for v in csv_object]

    # バッチ書込み
    count = len(data)/25
    for j in range(count):
        with table.batch_writer() as batch:
            for i in range(25):
                batch.put_item(
                    Item={
                        'col_name_1': data[i+j*25][0],
                        'col_name_2': data[i+j*25][1],
                        'col_name_3': data[i+j*25][2]
                    }
                )
