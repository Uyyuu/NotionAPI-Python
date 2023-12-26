import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("NOTION_API_KEY")
db_id = os.getenv("DATABASE_ID")