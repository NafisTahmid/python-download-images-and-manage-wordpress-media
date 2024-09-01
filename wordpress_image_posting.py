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


def media_code(image_path, alter_text):

    file_open = open(image_path, "rb")
    files = {'file':file_open}
    res = requests.post(media_url, files=files, headers=headers, verify=False)
    media_data = res.json()
    media_id = media_data.get('id')
    media_src = media_data.get('guid').get('rendered')
    code = f'<!-- wp:image {{"{media_id},"sizeSlug":"full","linkDestination":"none","align":"center"}} --><figure class="wp-block-image aligncenter size-full"><img src="{media_src}" alt="{alter_text}" class="wp-image-{media_id}"/></figure><!-- /wp:image -->'
    return code, media_id

image_one_url, image_one_id = media_code("Images/1.jpg", "First image")
image_two_url, image_two_id = media_code("Images/2.jpg", "Second image")
paragraph = f"<!-- wp:paragraph --><p>This is the paragraph</p><!-- /wp:paragraph -->"
content = image_one_url + paragraph + image_two_url
   
data = {
    'title':'This is Awesome title',
    'status':'publish',
    'content':content,
    'featured_media': image_two_id
}
response = requests.post(post_url, json=data, headers=headers, verify=False)
print(response.text)