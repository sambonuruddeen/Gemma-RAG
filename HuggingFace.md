# Obtaining Hugging Face API Access Token

Hugging Face provides an API that allows you to access their models and services. To use the API, you need to obtain an access token. Follow these steps to get your Hugging Face API access token and save it:

## 1. Sign Up on Hugging Face:

If you don't have a Hugging Face account, sign up at [Hugging Face](https://huggingface.co/). 

## 2. Log In:

Log in to your Hugging Face account.

## 3. Go to Profile Section:

Navigate to the your Hugging Face account dashboard.

## 4. Generate API Token:

Click on `Access Tokens` and then select "Generate Token" button. This will create an access token for you.

## 5. Copy Access Token:

Copy the generated access token. It will look like a long string of characters.

## 6. Save in .env File:

Create a `.env` file in the root directory of your project (if not already present). Add the following line, replacing `<your_access_token>` with the copied access token:

```env
HF_KEY=<your_access_token>
