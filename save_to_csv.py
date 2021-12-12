import csv


def save_file_to_csv(jobs_data):
    file = open("jobs.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)

    row_title = ["job_title", "company_name", "location", "apply_link"]

    writer.writerow(row_title)

    for job in jobs_data:
        writer.writerow(list(job.values()))
    return 0
