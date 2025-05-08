# Alexa Dialog to Web Service

⚠️ **WARNING** ⚠️
This code has been automatically generated and has not been tested in production. It is provided "as is" without any warranty of functionality. It is strongly recommended to:
- Test the code in a development environment before deployment
- Verify the security of endpoints and configurations
- Adapt the code according to your specific needs
- Perform thorough testing before any production use

This project contains an Alexa Lambda function that captures user dialogue and transmits it to a web endpoint. The endpoint's response is then returned to the user.

## Prerequisites

- Python 3.8 or higher
- An Amazon Developer account
- An AWS account
- A functional web endpoint

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file at the root of the project with the following variables:
```
WEB_ENDPOINT=your_endpoint_url
```

## Alexa Configuration

1. Create a new Alexa skill in the [Alexa Developer Console](https://developer.amazon.com/alexa)
2. Configure the `DialogIntent` with the following slot:
   - Slot name: `dialog`
   - Type: `AMAZON.SearchQuery`
3. Configure the Lambda in AWS:
   - Create a new Lambda function
   - Copy the content of `lambda_function.py`
   - Configure Python 3.8 runtime
   - Add necessary environment variables
4. Link the Lambda to your Alexa skill

## Alexa Configuration Files

The project contains two main configuration files for the Alexa skill:

### 1. interaction-model.json
This file defines the skill's interaction model:
- Invocation name ("mon assistant")
- `DialogIntent` with its `dialog` slot
- Sample utterances for the intent
- System intents (Help, Cancel, Stop)

### 2. skill-package/skill.json
This file contains the skill manifest:
- Skill metadata (name, description, etc.)
- Lambda endpoint configuration
- Publishing information

To use these files:
1. In the Alexa Developer Console, go to "Build"
2. For the interaction model:
   - Click on "JSON Editor"
   - Copy the content of `interaction-model.json`
3. For the manifest:
   - Go to "Skill Information"
   - Update information according to your configuration
   - Replace `REGION`, `ACCOUNT_ID`, and `FUNCTION_NAME` in the endpoint URI

## Project Structure

- `lambda_function.py`: Main Lambda function code
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (to be created)
- `interaction-model.json`: Alexa interaction model
- `skill-package/skill.json`: Skill manifest

## Request/Response Format

### Request to web endpoint
```json
{
    "dialog": "user text"
}
```

### Expected endpoint response
```json
{
    "response": "response to return to user"
}
```

## Deployment

1. Create a ZIP file containing:
   - `lambda_function.py`
   - All files from the `site-packages` directory after installing dependencies
2. Upload the ZIP to your AWS Lambda function
3. Configure environment variables in the AWS console 