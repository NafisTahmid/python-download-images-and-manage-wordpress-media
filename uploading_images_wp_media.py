import requests
import base64

user = "NafisT"
password = "R5fz sR55 pSEP l3Zx X6HT dLxK"
base_url = "https://localhost/PythonWordpress"
media_url = "/wp-json/wp/v2/media"
post_url = "/wp-json/wp/v2/posts"
url = f"{base_url}{media_url}"
post = f"{base_url}{post_url}"
credential = f"{user}:{password}"
token = base64.b64encode(credential.encode())
headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

file_path = open("ImagesTwo/dog_1.jpg", "rb")
files = {'file': file_path}
res = requests.post(url, headers=headers, files=files, verify=False)

# Post a feature image

id = res.json().get('id')
print(id)
data = {
    'title':'Feature image post',
    'status':'publish',
    'content':'Content for featured image',
    'featured_media':id
}
post_request = requests.post(post, json=data, headers=headers, verify=False)
print(post_request.text)