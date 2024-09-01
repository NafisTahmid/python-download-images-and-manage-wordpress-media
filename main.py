from requests import get
api = "45739691-464a345be12be1b4273e71c59"
kw = input("Please enter a text: ").replace(' ', '+')
url = f"https://pixabay.com/api/?key={api}&q={kw}_type=photo&pretty=true"
res = get(url)
data = res.json()
hits = data.get('hits')
image_id = 0
for image in hits:
    image_url = image.get('webformatURL')
    image_res = get(image_url)
    if image_res.status_code == 200:
        with open(f"Images/downloaded_image_{image_id}.jpg", "wb") as file:
            file.write(image_res.content)
            image_id += 1
