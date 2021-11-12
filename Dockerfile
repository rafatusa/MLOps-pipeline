FROM continuumio/anaconda3
COPY . /usr/app/
WORKDIR /usr/app/
RUN pip install -r requirements.txt
# CMD ["runipy", "model_jupyter.ipynb"]
CMD ["python", "model.py"]