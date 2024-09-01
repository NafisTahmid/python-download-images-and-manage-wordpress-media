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

def upload_image(image_url, alt_text):
    file_open = open(image_url, "rb")
    files = {'file':file_open}
    res = requests.post(media_url, files=files, headers=headers, verify=False)
    media_data = res.json()
    id = media_data.get('id')
    source = media_data.get('guid').get('rendered')

    code = f'<!-- wp:image {{"id":{id},"sizeSlug":"full","linkDestination":"none","align":"center"}} --><figure class="wp-block-image aligncenter size-full"><img src="{source}" alt="{alt_text}" class="wp-image-{id}"/></figure><!-- /wp:image -->'
    return code, id

image_one_url, image_one_id = upload_image("ImagesTwo/image_2.jpg", "second image")
image_two_url, image_two_id = upload_image("ImagesTwo/image_3.jpg", "third image")
paragraph = f'<!-- wp:paragraph --><p>Our faithful canine companions</p><!-- /wp:paragraph -->'
content = image_one_url + paragraph + image_two_url
data = {
    'title':'Dog: A faithful animal',
    'content': content,
    "status":'publish',
    'featured_media':image_two_id
}
res = requests.post(post_url, json=data, headers=headers, verify=False)
print(res.status_code)