from indeed import operate_model as get_indeed_jobs
from stackoverflow import operate_model as get_so_jobs
from save_to_csv import save_file_to_csv

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()

jobs = so_jobs + indeed_jobs
save_file_to_csv(jobs)
