export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv local 2.7.10

REL_NAME=$(python ./setup.py --version)


echo "Build Success"
echo "Creating github release"

API_JSON=$(printf '{"tag_name":"%s","target_commitish":"%s","name":"%s","body":"Release of version %s","draft":false,"prerelease":false}' $REL_NAME $DISTELLI_RELBRANCH $REL_NAME $REL_NAME)
REL_ID=$(curl -s -f -k -X POST -H "Content-Type: application/json" "https://api.github.com/repos/$GITHUB_USERNAME/$GITHUB_APPNAME/releases?access_token=$GITHUB_TOKEN" -d "$API_JSON"|./jq '.["id"]'|tr -d '\n')

echo "Uploading artifact to github release"
ARCHIVE=$(find . -name '*.tar.gz')
GH_ASSET="https://uploads.github.com/repos/$GITHUB_USERNAME/$GITHUB_APPNAME/releases/$REL_ID/assets?name=$(basename $ARCHIVE)&access_token=$GITHUB_TOKEN"
echo $GH_ASSET
echo $ARCHIVE
curl --data-binary @"${ARCHIVE}" --header "Content-Type: application/x-gzip" $GH_ASSET
