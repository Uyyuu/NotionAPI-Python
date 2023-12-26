from Notion import Notion_DB_Insert

# データの作成
entry_data = {
    "Model": "test Model",
    "Public_LB": 98.5,
    "URL": "https://test.com",
    "Date": "2023-01-01",
    "Who": ["臼井"],
    "CV_Score": 97.8,
    "実行ファイル名": "test_file.txt"
}

# 関数呼び出し
Notion_DB_Insert.create_notion_entry(entry_data)