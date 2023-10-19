
# Coding Exercise

## Overview

```
exercise/
|   test.sh: tests can be started by running test.sh
│   README.md: exercise description
│   TESTME.md: implementation description
│   requirements.txt: file containing the required pip packages
│   Dockerfile: docker file to build docker image
│   pyproject.toml: project toml file
│
└───resources/ : directory containing class implementations
└───schemas/ : directory containing schemas to validate responses against
└───features/ : directory containing feature files
│   └───steps/ : directory containing step implementations
└───allure_reports/ : directory containing generated allure reports
└───locust_reports/ : directory containing generated locust html reports
└───locustfiles/ : directory containing locust files (only api.py was added so far)
```

## Overview

To run the tests, please use the `./test.sh` file. It would go through the feature files and then run a proof-of-concept performance test (ca. 10-15 requests per run).
Two additional optional flags were added.

### Run it with Allure Reporting

To generate allure reports, please use the `./test.sh -a` command.
It would generate an Allure report under `./allure_reports` folder.
The performance test would also generate an html report under `./locust_reports` folder.

### Run it using Docker

To run the tests in a Docker container, please use the `./test.sh -d` command.
It requires Docker daemon to run in the background (I, myself quickly used MacOS Docker Desktop running in the background).
It would generate an image, install requirements, then run the tests and print the results on stdout.

## Implementation

- I used my Mac Mini and VSCode to implement the tests.
- To decrease the number of API requests (respecting rate limiting), I decided to create 1 `Scenario Outline` for each search category and then verify the result endpoints and detailed endpoints for each search phrase.
- I created 1 base class and extended it for each categories. I tried to keep the special cases to a minimum and tried to reuse code as much as possible, while keeping in mind the KISS principle.
- For some reason I was unable to query the schemas under `swapi.dev/api/<resource>/schema`, so I decided to create my own schemas under `./schemas` directory.
- After implementing the Docker support, I could have parallelize the docker runs to save time, but I decided to leave it as one run.
- I wanted to add a proof-of-concept performance test too, while making sure not to cause rate-limiting to kick in.
- To adhere to the assignment description I added a simple `./test.sh` option to run the tests locally. Then I added two optional flags (flags should only be used separately). So now `./test.sh -a` can be used to generate allure report, and `./test.sh -d` can be used to run the tests in a docker container.
