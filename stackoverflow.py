import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


# Step 1. Get page
# Step 2. Make request
# Step 3. Extract Jobs


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "s-pagination"})
    pages = pagination.find_all("a")
    last_page = pages[-2].get_text().strip()
    return int(last_page)


def get_job_info():
    pass


def get_jobs(last_page):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_cards = soup.find_all("div", {"class": "-job"})

        for job_card in job_cards:
            print(job_card["data-jobid"])


def operate_model():

    last_page = get_last_page()
    jobs = get_jobs(last_page)

    return []
