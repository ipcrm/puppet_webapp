echo "Build Success"
echo "Creating github release"
API_JSON=$(printf '{"tag_name":"%s","target_commitish":"%s","name":"%s","body":"Release of version %s","draft":false,"prerelease":false}' $DISTELLI_BUILDNUM $DISTELLI_RELBRANCH $DISTELLI_BUILDNUM $DISTELLI_BUILDNUM)
REL_ID=$(curl -s -f -k -X POST -H "Content-Type: application/json" "https://api.github.com/repos/$GITHUB_USERNAME/$GITHUB_APPNAME/releases?access_token=$GITHUB_TOKEN" -d "$API_JSON"|./jq '.["id"]'|tr -d '\n')

echo "Uploading artifact to github release"
ARCHIVE=$(find . -name '*.tar.gz')
GH_ASSET="https://uploads.github.com/repos/$GITHUB_USERNAME/$GITHUB_APPNAME/releases/$REL_ID/assets?name=$(basename $ARCHIVE)&access_token=$GITHUB_TOKEN"
echo $GH_ASSET
echo $ARCHIVE
curl --data-binary @"${ARCHIVE}" --header "Content-Type: application/x-gzip" $GH_ASSET
