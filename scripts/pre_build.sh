curl -s -o jq 'https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64'
chmod +x jq
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv install 2.7.10
pyenv local 2.7.10
pip install -r requirements.txt
pip install discover
