import uuid
import requests
from dotenv import load_dotenv

load_dotenv()
    
AUTH_KEY = os.getenv("GIGACHAT_AUTH_KEY")
    
url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "RqUID": str(uuid.uuid4()),
    "Authorization": f"Basic {AUTH_KEY}",
}
    
data = {
    "scope": "GIGACHAT_API_PERS"
}
    
response = requests.post(url, headers=headers, data=data, verify=False)
    
print(response.json())