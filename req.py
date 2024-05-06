import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/image-to-video",
    headers={
        "authorization": "sk-Gfy80IdUTb3rHcqnFcBhIblmPyEMjCvjyTpmQx9f7JfDyfx7"
    },
    files={
        "image": open("./images/train.png", "rb")
    },
    data={
        "seed": 0,
        "cfg_scale": 1.8,
        "motion_bucket_id": 127
    },
)

if response.status_code == 200:
    print("Hura")
else:
    print("Err: ", response.json())

print("Generation ID:", response.json().get('id'))