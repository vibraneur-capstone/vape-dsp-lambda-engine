args=("$@")
len=${#args[@]}

echo sam version:
sam --version

if [ "$len" == 0 ]; then
  echo No arguments provided... Existing...
  exit 1
elif [ "$1" == "package" ]; then
  echo packaging started
  sam package --template-file ./../dsp-engine-sam.yaml --s3-bucket vape-artifacts --output-template-file ./../packaged-dsp-sam.yaml
elif [ "$1" == "deploy" ]; then
  # --no-fail-on-empty-changeset
  sam deploy --template-file ./../packaged-dsp-sam.yaml --stack-name dsp-sam-test --region us-east-1 --capabilities CAPABILITY_IAM
else
  echo No valid arguments provided... Existing...
  exit 1
fi
