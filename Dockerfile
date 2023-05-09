FROM python:3.9

RUN mkdir -p  /app_course

COPY . /app_course

RUN python3 -m pip install -r /app_course/requirements.txt

EXPOSE 5000

CMD ["python","/app_course/app.py"]