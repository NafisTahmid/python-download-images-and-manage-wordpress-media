import requests
import base64

media_url = "https://localhost/PythonWordpress/wp-json/wp/v2/media"
user = "NafisT"
password = "R5fz sR55 pSEP l3Zx X6HT dLxK"
credential = f"{user}:{password}"
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

with open("Images/3.jpg", "rb") as file_path:
    files = {'file': file_path}
    res = requests.post(media_url, files=files, headers=headers, verify=False)
    print(res.status_code)
