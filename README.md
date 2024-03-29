# NotionAPI-Python
### ディレクトリ構造
```bash
.
├── Notion                     #ローカル用のディレクトリ
│   ├── EntryData.py           
│   ├── Notion_DB_Insert.py    
│   ├── __init__.py
│   └── settings　　　　　            ⭐️　.envファイル追加するディレクトリ
│       ├── __init__.py
│       └── config.py
│       └── .env              ⭐️　リポジトリにはあげてないので各自準備してください．
│          
├── Notion_GoogleColab        　　#GoogleColab用
│   ├── EntryData.py           
│   ├── Notion_DB_Insert.py    
│   ├── __init__.py
├── sample.json
├── demo.py
```

### 準備
- ローカルで動かす場合
  
Notionディレクトリ下のsettingsディレクトリ内に.envファイルを作って以下の内容を記述する．
```.env
NOTION_API_KEY = "APIキー"
DATABASE_ID = "データベースID"
```

- Google Colabで動かす場合
  
    - Notion_GoogleColab/EntryData.py内のDATABASE_IDにデータベースIDを設定<br>
    - Notion_GoogleColab/Notion_DB_Insert.py内のNOTION_API_KEYにAPIキーを設定<br>

### 環境構築

必要なパッケージはrequirements.txtに記載．

- venvの例
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Google Colabで動かす
    1. リポジトリの Notion_GoogleColabディレクトリをdriveにコピー
    2. 以下のコードを一番最初のセルで実行
```python
# driveのマウント
from google.colab import drive
drive.mount('/content/drive')
# %cd 以降にこのnotebookを置いているディレクトリを指定する．
%cd "現在のワーキングディレクトリを指定"

# 自作モジュールのインポート
from Notion_GoogleColab import Notion_DB_Insert
```

### 使い方
- ローカル，colabともに同様
- Notionディレクトリ内のNotion_DB_Insertモジュールのcreate_notion_entry関数を使用してデータベースに情報を追加
- 以下のコードコピーして送信データ型の部分の辞書のバリューの部分を登録したい内容に変える
```python
from Notion import Notion_DB_Insert       #ローカルの場合
from Notion_GoogleColab import Notion_DB_Insert       #GoogleColabの場合

# 送信データ型
entry_data = {
    "Model": "モデル名",
    "Public_LB": パブリックリーダーボードのスコア,
    "URL": "実行ファイルのURL",
    "Date": "year-manth-day",
    "Who": ["名前"],
    "CV_Score": バリデーションスコア,
    "実行ファイル名": "実行ファイル名"
}

# 関数呼び出し
Notion_DB_Insert.create_notion_entry(entry_data)   #Notion entry created successfully!　が出力されたら成功！

```
