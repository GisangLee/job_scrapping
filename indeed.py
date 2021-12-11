import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    results = requests.get(URL)

    soup = BeautifulSoup(results.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def get_job_info(html):

    job_title = html.find("span", title=True).string

    company_name = html.find("span", {"class": "companyName"}).string

    location = html.select_one("pre>div").text
    job_id = html["data-jk"]

    return {
        "job_title": job_title,
        "company_name": company_name,
        "location": location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3",
    }


def get_jobs(last_page):
    print("============================ 웹 크롤링 작동 중 ==========================")
    jobs = []
    for page in range(last_page):
        print(f"==================== 페이지 {page+1}============================")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_cards = soup.find_all("a", {"class": "tapItem"})

        for job_card in job_cards:
            job = get_job_info(job_card)
            jobs.append(job)
    return jobs


def operate_model():
    last_page = get_last_page()
    jobs = get_jobs(last_page)
    return jobs
