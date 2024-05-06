import requests

generation_id = "27400e0d0c69c211b8f37062b96deba347a7f3e989d278c78c7ea14cb2e205b9"

response = requests.request(
    "GET",
    f"https://api.stability.ai/v2beta/image-to-video/result/{generation_id}",
    headers={
        'accept': "video/*",  # Use 'application/json' to receive base64 encoded JSON
        'authorization': "sk-Gfy80IdUTb3rHcqnFcBhIblmPyEMjCvjyTpmQx9f7JfDyfx7"
    },
)

if response.status_code == 202:
    print("Generation in-progress, try again in 10 seconds.")
elif response.status_code == 200:
    print("Generation complete!")
    with open("./videos/video1.mp4", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))