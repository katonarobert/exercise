FROM docker/getting-started

# Add GCC
RUN apk add build-base

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add python3-dev libffi-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Setting up workdir
WORKDIR /usr/src/app

# Copy code
COPY . .

# Run tests
CMD [ "./test.sh" ]
