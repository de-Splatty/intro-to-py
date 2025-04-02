# json data
data = {
    "name": "Bruce Lee",
    "dob": "2000-10-10",
    "email": "BL@gmail.com",
    "school": {
        "name": "MHS",
        "County": "Kiambu",
        "KCSE":{
            "mean score": "B+",
            "students": 610
        }
    }
}

print(data["dob"])
county = data["school"]["County"]
print(county)

print(data["school"]["KCSE"]["mean score"])