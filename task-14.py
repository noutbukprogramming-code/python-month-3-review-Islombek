import json

talaba = {
    "ism": "Ali",
    "yosh": 18,
    "ball": 90
}


with open("talaba.json", "w") as f:
    json.dump(talaba, f, indent=4)


with open("student.json", "r") as f:
    talaba = json.load(f)


print(f"Ism: {talaba["ism"]}")
print(f"Yosh: {talaba["yosh"]}")
print(f"Ball: {talaba["ball"]}")