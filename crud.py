import boto3

class DataBase:
    def __init__(self, db, tablename: str):
        self. db = db
        self.table = db.Table(tablename)
        self.tablename = tablename
        self.client = boto3.client('dynamodb')
    
    def create(self, reduction, url):
        self.client.put_item(
            TableName = self.tablename, 
            Item = { 
                'Reduction': { 'S': reduction }, 
                'URL': { 'S': url }
            })
    
    def read(self, reduction):
        return self.table.get_item(Key={"Reduction": reduction})