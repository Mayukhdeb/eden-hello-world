# set base image (host OS)
FROM python:3.8

# copy the content of the local src directory to the working directory
WORKDIR /usr/local/
COPY . .

# install dependencies
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN sh setup.sh

# the line below is commented out because: https://stackoverflow.com/questions/49323225/expose-all-ports-for-a-docker-image/49323975
# EXPOSE 5656  

# command to run on container start
# CMD ["python","server.py","--use-gpu","(use-gpu)","--num-workers","(num-workers)","--port","(port)", "--logfile","(logfile)"]
ENTRYPOINT ["python","server.py"]