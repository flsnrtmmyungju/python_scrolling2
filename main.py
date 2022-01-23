import os
from flask import Flask, render_template, request,redirect,send_file
from soScrapper import get_so_jobs
from wrScrapper import get_wr_jobs
from rtScrapper import get_rt_jobs
from exporter import save_to_file
os.system('clear')
app = Flask("WebScrapper") 
db={}

# @는 데코레이터 : 해당 url로 접속요청들어오면 바로아래있는 "함수만"찾음 함수아니면 에러
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  job = request.args.get('job')
  if job:    
    job= job.lower()
    existingJobs = db.get(job)
    if existingJobs :
      jobs = existingJobs
    else:
      so_jobs = get_so_jobs(job)
      wr_jobs = get_wr_jobs(job)
      rt_jobs = get_rt_jobs(job)
      jobs= so_jobs+wr_jobs+rt_jobs      
      db[job]=jobs
      print(f"stackoverflow: {len(so_jobs)}건")
      print(f"weworkremotely: {len(wr_jobs)}건")
      print(f"remoteok: {len(rt_jobs)}건")
  else:
    redirect("/")
  # return render_template("search.html",searchingBy=job,so_len=len(so_jobs),wr_len=len(wr_jobs),rt_len=len(rt_jobs),so_jobs=so_jobs,wr_jobs=wr_jobs,rt_jobs=rt_jobs,)
  return render_template("search.html",searchingBy=job, jobsLen = len(jobs),jobs = jobs)
  

@app.route("/export")
def export():
  try:
    word = request.args.get('word')    
    if not word:
      raise Exception();
    word= word.lower() 
    jobs = db.get(word)
    if not jobs:
      raise Exception();
    save_to_file(jobs)
    # attachment_filename='저장할 파일이름'
    return send_file("jobs.csv", attachment_filename='jobs.csv', as_attachment=True)
  except:
    return redirect("/")

# 0.0.0.0은 리플에서실행하려고 적어둔거(리플이 공개하려는걸 알아차림)
app.run(host="0.0.0.0")
