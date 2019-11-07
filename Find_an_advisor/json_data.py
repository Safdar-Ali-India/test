import json


    advisor = {
        "item": {
            "advisors": [
    
                {
                    "id": 1,
                    "Name": "Mukesh Bhardwaj",
                    "Gender": "Male",
                    "city": "Rampur",
                    "Experience": "7",
                    "state": "Uttar Pradesh",
                    "pin": 244901,
                    "specialization": ["ETFS"]
    
                },
                {
                    "id": 2,
                    "Name": "Aniska Sexsena",
                    "Gender": "Female",
                    "city": "Haridwar",
                    "Experience": "8",
                    "state": "Uttarakhand",
                    "pin": 24400901,
                    "specialization": ["Bonds"]
                },
                {
                    "id": 3,
                    "Name": "Dharmendra Singh",
                    "Gender": "Male",
                    "city": "Rampur",
                    "Experience": "5",
                    "state": "Uttar Pradesh",
                    "pin": 244924,
                    "specialization": ["Mutual Fund", "Equity"]
    
                },
                {
                    "id": 4,
                    "Name": "Rahul Singh",
                    "Gender": "Male",
                    "city": "Moradabad",
                    "Experience": "5",
                    "state": "Uttar Pradesh",
                    "pin": 244001,
                    "specialization": ["Equity", "ETFS"]
                },
    
            ]
        }
    }
input_data = {"age": "Uder 30",
              "Marital_status": "Single",
              'experience': 5,
              "anual_income": "10c-20c",
              "total_saving": "40c-80c",
              "own_b": "yes", "wwfa": "no",
              "looking_for": "Both",
              "tlooking_for": "OTP",
              "State": "Uttar Pradesh",
              "City": "Rampur",
              "pin":244924,
              "goals": ["Prepare for retirement", "Save for kid's college",
                        "Access to alternative investments", "Diversify concentrated wealth",
                        "Manage my inheritance"],
              "specialization":["Equity"]}

with open('output.json', 'w') as json_file:
    json.dump(advisor, json_file)
with open('data1.json', 'w') as json_file:
    json.dump(input_data, json_file)
    