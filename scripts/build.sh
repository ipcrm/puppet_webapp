tox
sonar-scanner -Dsonar.login=$SONAR_LOGIN -Dsonar.projectVersion=$(python ./setup.py --version)
sleep 5
QG=$(curl -s https://sonarcloud.io/api/qualitygates/project_status\?projectKey\=ipcrm-puppet_webapp|./jq .[].status)

if [ $QG != '"OK"' ]; then
  echo "Failed SonarCube Quality Gate!"
  exit 10
fi

python ./setup.py sdist
