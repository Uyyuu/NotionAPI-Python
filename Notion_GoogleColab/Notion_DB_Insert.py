import requests
from . import EntryData

NOTION_API_KEY = ""

def create_notion_entry(entry_data):
    url = 'https://api.notion.com/v1/pages'
    headers = {
        'Notion-Version': '2022-06-28',
        'Authorization': 'Bearer ' + NOTION_API_KEY,
        'Content-Type': 'application/json',
    }

    # NotionDatabaseEntryクラスのインスタンス化
    entry = EntryData.NotionDatabaseEntry(**entry_data)

    # JSON形式への変換
    json_data = entry.to_json()

    # Notion APIにデータを作成するためのリクエスト
    response = requests.post(url, headers=headers, json=json_data)

    # レスポンスを確認
    if response.status_code == 200:
        print('Notion entry created successfully!')
    else:
        print(f'Error: {response.status_code}\n{response.json()}')

