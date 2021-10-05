# lightweight python
FROM python:3.7-slim

RUN apt-get update

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN ls -la $APP_HOME/

# Install dependencies
RUN pip install -r requirements.txt

RUN pip install lark --upgrade

# Run the streamlit on container startup
CMD [ "streamlit", "run","imgwebapp.py" ]
