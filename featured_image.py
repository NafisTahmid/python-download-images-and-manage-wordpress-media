import requests
import base64

base_url = "https://localhost/PythonWordpress/wp-json"
media_url =f"{base_url}/wp/v2/media"
post_url = f"{base_url}/wp/v2/posts"
user = "NafisT"
password = "R5fz sR55 pSEP l3Zx X6HT dLxK"
credential = f"{user}:{password}"
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

file_path = open("Images/2.jpg", "rb")
files = {'file':file_path}
res = requests.post(media_url, files=files, headers=headers, verify=False)
media_id = res.json().get('id')
data = {
    'title':'This is Awesome title',
    'status':'publish',
    'content':'Post content',
    'featured_media': media_id
}
response = requests.post(post_url, json=data, headers=headers, verify=False)
print(response.text)