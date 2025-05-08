from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

origins = [
    "http://localhost:3000",  # React app running on localhost
    "http://127.0.0.1:3000",
    "https://csv-dashboard-navy.vercel.app/",  # React app running on localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://csv-dashboard-navy.vercel.app/"],
    allow_credentials=True,  # Allows all origins
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# @app.get("/")
# def read_root():
#     return {"message": "Hello World, made by FastAPI with CORS"}


@app.get("/api/summary")
def get_summary():
    data = []
    total = 0
    count = 0

    with open("data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            month = row["month"]
            value = int(row["value"])
            total += value
            count += 1
            data.append({"month": month, "value": value})

    average = total / count if count > 0 else 0

    return {"data": data, "total": total, "average": average}
