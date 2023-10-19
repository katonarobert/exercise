#!/bin/sh

install_requirements()
{
  echo "\n*** Installing all requirements ***\n"
  python3 -m pip install -r requirements.txt
}

help_with_allure()
{
  echo "\n****************************************************************************"
  echo "***  To be able to view the allure report, please install allure         ***"
  echo "***  MacOS: 'brew install allure', Linux: 'sudo apt-get install allure'  ***"
  echo "***  Then use: allure serve ./allure_reports                             ***"
  echo "***  Visit: https://docs.qameta.io/allure-report/                        ***"
  echo "****************************************************************************\n"
}

# Get arguments
while getopts "had" opt; do
  case $opt in
    a)
      # Install requirements
      install_requirements

      # Run the API tests
      echo "\n*** Running the tests with allure reporting ***\n"
      ALLURE_REPORT_FOLDER="./allure_reports"
      behave -f allure_behave.formatter:AllureFormatter -o $ALLURE_REPORT_FOLDER ./features

      # Run the performance tests
      echo "\n*** Running the performance tests with html reporting ***\n"
      locust --headless --host localhost --run-time 10s --users 3 --spawn-rate 1 --html locust_reports/report__$(date +"%Y-%m-%dT%H:%M:%S").html --locustfile locustfiles/api.py

      # Help printout
      help_with_allure
      exit 0
      ;;

    d)
      echo "\n*** Running the tests in a docker container ***\n" 
      docker build -t swapi .
      docker run --rm -it -p 80:80/tcp swapi:latest
      docker rmi swapi
      exit 0
      ;;

    h)
      echo "\nUsage:\n"
      echo "'./test.sh -a' : to run locally with allure and locust reporting"
      echo "'./test.sh -d' : to run the tests in a docker container. Make sure that docker deamon is running. (Note, there is no report generation)" 
      echo "'./test.sh'    : to run locally without allure reporting\n"
      echo "Please note that flags can only be used separately. Only the first flag will be executed.\n" >&2
      exit 0
      ;;

    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Install requirements
install_requirements

# Run the API tests
echo "\n*** Running the tests without allure reporting ***\n"
behave

# Run the performance tests
echo "\n*** Running the performance tests without html reporting ***\n"
locust --headless --host localhost --run-time 10s --users 3 --spawn-rate 1 --print-stats --locustfile locustfiles/api.py
