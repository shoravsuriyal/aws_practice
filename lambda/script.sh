aws lambda invoke --function-name function_1 out.txt
aws iam create-role --role-name lambda-dynamodb --assume-role-policy-document file://trust-policy.json
aws lambda create-function --function-name function_1 --runtime python2.7 --zip-file fileb://function.zip --handler lambda_handler.lambda_handler --role arn:aws:iam::496585200392:role/lambda-dynamodb
aws lambda delete-function --function-name function_1
zip function.zip lambda_handler.py
