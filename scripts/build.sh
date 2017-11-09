export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv local 2.7.10 3.3.6 3.4.3 3.5.0
tox
python ./setup.py sdist
