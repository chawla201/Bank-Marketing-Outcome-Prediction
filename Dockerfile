# start from python base image
FROM python:3.11

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# add python code and models
COPY ./app/ /code/app/

# specify default commands
CMD ["fastapi", "run", "app/app.py", "--port", "80"]
