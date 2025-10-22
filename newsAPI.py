from typing import final

import main_functions
import requests
from dotenv import load_dotenv
import os

from main_functions import save_to_file

load_dotenv()

news_key = os.getenv("NEWS_KEY")

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="

final_url = url + news_key

response = requests.get(final_url).json()

save_to_file(response,"news.json")