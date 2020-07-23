import requests #pip install requests or it aint gunna work yall

url = input("Enter url: ")
name = input("Enter name of file: ")
response = requests.get(url)
if response.status_code == 200:
    with open(f"{name}.mp3", 'wb') as f:
        f.write(response.content)
