args=("$@")
len=${#args[@]}

if [ "$len" == 0 ]; then
  echo Default build for develop branch
  branch="develop"
else
  branch=$1
fi

aws codebuild start-build \
--project-name dsp-lambda-engine \
--timeout-in-minutes-override 10 \
--source-version $branch \
--region us-east-1 \
--artifacts-override type=S3,overrideArtifactName=true,encryptionDisabled=false,location=vape-artifacts,packaging=NONE \
