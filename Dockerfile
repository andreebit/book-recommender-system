FROM janlampe/gensim371
WORKDIR /code
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY code/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]