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


def get_job_info(html):
    title_div = html.find("div", {"class": "flex--item fl1"})

    job_title = title_div.find("h2").find("a", {"class": "s-link"})["title"]

    company_name, location = title_div.find("h3", {"class": "mb4"}).find_all(
        "span", recursive=False
    )

    company_name = company_name.get_text(strip=True)
    location = location.get_text(strip=True)

    job_id = html["data-jobid"]
    apply_link = f"https://stackoverflow.com/jobs/{job_id}"

    return {
        "job_tilte": job_title,
        "company_name": company_name,
        "location": location,
        "apply_link": apply_link,
    }


def get_jobs(last_page):
    print("======================== SO 스크래퍼 작동 중 =========================")

    jobs = []

    for page in range(last_page):
        print(f" Page : {page} =====================================")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_cards = soup.find_all("div", {"class": "-job"})

        for job_card in job_cards:
            job = get_job_info(job_card)
            jobs.append(job)
    return jobs


def operate_model():

    last_page = get_last_page()
    jobs = get_jobs(last_page)

    return jobs
