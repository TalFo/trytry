import os
import datetime
import subprocess

end_date = datetime.date(2010, 12, 31)
start_date = datetime.date(2010, 1, 1)
delta = datetime.timedelta(days=2)

while start_date <= end_date:
    # print(start_date)
    date = f"{start_date} 17:18:43 +0200"
    print(date)
    os.environ['GIT_AUTHOR_DATE'] = date
    os.environ['GIT_COMMITTER_DATE'] = date
    start_date += delta
    out1 = subprocess.run('echo try >> try.txt', shell=True, capture_output=True)
    out2 = subprocess.run('git add .', shell=True, capture_output=True)
    print(out2)
    out3 = subprocess.run('git commit -m "try"', shell=True, capture_output=True)
    print(out3)
    out4 = subprocess.run('git push', shell=True, capture_output=True)
    print(out4)
