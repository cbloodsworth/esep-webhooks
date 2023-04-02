make:
	zip my-deployment-package.zip lambda_function.py
	aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://my-deployment-package.zip
