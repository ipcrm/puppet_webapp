mkdir reports
sudo pip install tox
sudo pip install pylint
wget -q https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O jq
chmod +x jq
curl -s -L -o sonar.zip 'https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip'
unzip -d /var/tmp/sonar sonar.zip
chmod +x /var/tmp/sonar/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner
sudo ln -s /var/tmp/sonar/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner
