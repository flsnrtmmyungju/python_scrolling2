"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, request,redirect
app = Flask("WebScrapper") 
from scrapper import get_jobs


# @는 데코레이터 : 해당 url로 접속요청들어오면 바로아래있는 "함수만"찾음 함수아니면 에러
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  job = request.args.get('job',str)
  if job:    
    job= job.lower()
    jobs= get_jobs(job)
    print("jobs",jobs)
  else:
    redirect("/")
  return render_template("search.html",searchingBy=job)



# 0.0.0.0은 리플에서실행하려고 적어둔거(리플이 공개하려는걸 알아차림)
app.run(host="0.0.0.0")