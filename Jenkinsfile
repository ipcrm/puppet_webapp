node {
  gitlabCommitStatus {
    stage 'Checkout'
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'WipeWorkspace']], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'cef3b072-1a13-4f79-9b93-35b06c9dfcf1', url: 'git@gitlab.inf.puppetlabs.demo:code_manager/flask_puppet.git']]])

    stage 'Install Dev Tools'
    sh '''
        PATH=$WORKSPACE/venv_python:bin:/usr/local/bin:$PATH
        test -d "venv_python" ] || virtualenv venv_python
        . venv_python/bin/activate
        pip install -r requirements.txt --download-cache=/tmp/$JOB_NAME
    '''

    stage 'Unit Testing'
    sh '''
        . venv_python/bin/activate
        python -m unittest discover  -v
    '''

    stage 'Build sdist'
    sh '''
        . venv_python/bin/activate
        python ./setup.py sdist
    '''

    stage 'Release sdist to Test'
    sh 'scp dist/*.tar.gz jenkins_scp@master.inf.puppetlabs.demo:/opt/tse-files/artifacts/flask_puppet.unstable.tar.gz'

    stage 'Deploy Test'
    sh '''/opt/puppetlabs/client-tools/bin/puppet-access login --username deploy --service-url https://master.inf.puppetlabs.demo:4433/rbac-api <<ANSWER
puppetlabs
ANSWER'''
    sh '/opt/puppetlabs/bin/puppet-job run Apps::Flask_puppet[dev]'

    stage 'Acceptance Test'
    sleep 10
    sh "curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://centos7a.pdx.puppetlabs.demo:6000/ |grep 200 &> /dev/null"

    stage 'Release Artifact to Stage'
    sh 'scp dist/*.tar.gz jenkins_scp@master.inf.puppetlabs.demo:/opt/tse-files/artifacts/flask_puppet.stable.tar.gz'
    archive 'dist/*.tar.gz'

    stage 'Deploy Stage'
    sh '''/opt/puppetlabs/client-tools/bin/puppet-access login --username deploy --service-url https://master.inf.puppetlabs.demo:4433/rbac-api <<ANSWER
puppetlabs
ANSWER'''
    sh '/opt/puppetlabs/bin/puppet-job run Apps::Flask_puppet[stage]'

    stage 'Acceptance Test'
    sleep 30
    sh "curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://centos7b.pdx.puppetlabs.demo:6000/|grep 200 &> /dev/null"
  }



}
