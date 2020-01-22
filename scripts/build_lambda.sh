#!/bin/bash

# access arguments
args=("$@")
len=${#args[@]}

dist_name="dsp-aws-lambda-dist.zip"
dep_target_path="external_libraries"
numpy="numpy"
numpy_info="numpy*"

if [ "$len" == 0 ]; then
  echo Default goal to package
  goal="package"
else
  goal=$1
fi

echo "build start"

sleep 1

rm $dist_name
rm -rf $dep_target_path

printf "\nInstall dependency \n"
sleep 3

python3 -m pip install -r requirements.txt --target $dep_target_path

printf "\nPackaging dependency \n"
sleep 3

cd $dep_target_path || exit

# remove redundant dependencies (deps will be imported from aws layers)
if [ "$goal" == "aws" ]; then
  rm -rf $numpy
  rm -rf $numpy_info
fi

#zip -g -r $dist_name $dep_target_path/*

zip -r9 ${OLDPWD}/$dist_name .

cd ${OLDPWD} || exit

printf "\nPackaging project modules \n"
sleep 3
zip -g -r $dist_name src/*

printf "\nCleaning up \n"
rm -rf $dep_target_path

printf "\nFinished Building \n"
