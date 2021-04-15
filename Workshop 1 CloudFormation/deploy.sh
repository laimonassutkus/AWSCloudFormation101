path="$1"
aws cloudformation deploy \
  --template-file "$path" \
  --stack-name WorkshopStack \
  --capabilities CAPABILITY_IAM
