from . import settings

class NotionDatabaseEntry:
    def __init__(self, Model, Public_LB, URL, Date, Who, CV_Score, 実行ファイル名):
        self.Model = Model
        self.Public_LB = Public_LB
        self.URL = URL
        self.Date = Date
        self.Who = Who
        self.CV_Score = CV_Score
        self.実行ファイル名 = 実行ファイル名

    def to_json(self):
        return {
            "parent": {"database_id": settings.config.db_id},
            "properties": {
                "Model": {"rich_text": [{"text": {"content": self.Model}}]},
                "Public LB": {"number": self.Public_LB},
                "URL": {"url": self.URL},
                "Date": {"date": {"start": self.Date}},
                "Who": {"multi_select": [{"name": name} for name in self.Who]},
                "CV Score": {"number": self.CV_Score},
                "実行ファイル名": {"title": [{"text": {"content": self.実行ファイル名}}]}
            }
        }