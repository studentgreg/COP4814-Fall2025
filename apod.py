import main_functions
import requests
from dotenv import load_dotenv
import os

from main_functions import save_to_file

load_dotenv()

# NASA's API url
url = "https://api.nasa.gov/planetary/apod?api_key="

# Read your NASA API key
api_key = os.getenv("NASA_KEY")

#Build the final API url
final_url = url + api_key

#Make the API request
response = requests.get(final_url).json()

#Serialize the result to a JSON document
save_to_file(response,"apod.json")

#Deserialize the recently create JSON document

#What is the type of the object deserialized?

#What are its keys?

#Access some of their values passing their keys