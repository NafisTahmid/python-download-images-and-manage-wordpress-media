import requests
api = "45739691-464a345be12be1b4273e71c59"
kw = input("Please enter image name: ").replace(' ', '+')
url = f'https://pixabay.com/api/?key={api}&q={kw}&image_type=photo'
res = requests.get(url)
data = res.json()
hits = data.get('hits')
image_number = 0

for image in hits:
    image_url = image.get('webformatURL')
    res = requests.get(image_url)
    if res.status_code == 200:
        with open(f"imagesTwo/image_{image_number}.jpg", "wb") as file:
            file.write(res.content)
            image_number += 1
