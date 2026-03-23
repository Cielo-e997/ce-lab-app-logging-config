# Lab M6.01 - Deploy Application with Logging Configuration

## Overview
This project shows how to configure structured logging in a Flask application and send logs to AWS CloudWatch Logs for centralized monitoring and analysis.

## Architecture
- Application: Flask API with structured JSON logging
- Agent: CloudWatch Logs Agent shipping logs to CloudWatch
- Analysis: CloudWatch Logs Insights queries

## Setup & Deployment
1. Created the Flask application with structured JSON logging
2. Installed the required dependencies
3. Installed and configured the CloudWatch Logs Agent
4. Configured the agent to collect application logs
5. Created and attached the IAM role with CloudWatch permissions
6. Verified that logs were delivered to CloudWatch Logs
7. Set the retention policy to 30 days

## How to Verify Logs Are Working
- Start the application
- Send requests to the available endpoints
- Confirm that logs are generated
- Check that the log group `/aws/application/api` exists in CloudWatch Logs
- Verify that the log streams contain data
- Run queries in CloudWatch Logs Insights

## Screenshots
The repository includes screenshots of:
- CloudWatch log group created
- Log streams with data
- Logs Insights query results
- Application running

## Challenges & Solutions
One challenge was making sure the EC2 instance had the correct permissions to send logs to CloudWatch. This was solved by creating the required IAM policy and attaching an IAM role to the instance. Another important step was confirming that the CloudWatch Agent configuration pointed to the correct log file path so logs could be collected properly.
