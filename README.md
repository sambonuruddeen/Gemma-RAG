# RAG-based QA system from PDF documents using Gemma

## Project Setup Guide
This guide is written and tested on a linux (Ubuntu) virtual machine.

**Prerequisites:** Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/). 

## Installation

### Step 1: Install `pip`

If you don't have `pip` installed, follow these steps:

```bash
# On Unix/macOS
sudo apt-get install python3-pip

# On Windows
python -m ensurepip --default-pip
```

### Step 2: Install `venv`
Now, let's install venv to create a virtual environment for your project:

```bash
# On Unix/macOS/Windows
python -m venv venv
```

### Step 3: 
Activate the virtual environment based on your operating system:


```bash
# On Unix/macOS:
source venv/bin/activate
```


```bash
# On Windows:
venv\Scripts\activate
```
You'll see the virtual environment name appear in your command prompt, indicating that it's now active.

### Get Hugging Face Access Token
Save your Access Token inside the `.env` file:

```bash
HF_KEY=<your_access_token>
```
If you don't have access token, follow [this](HuggingFace.md) guide to learn how to obtain your Hugging Face API Access Token

### Install Project Dependencies
Now that you have your virtual environment set up, install the project dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```
### Download PDF
Assuming you have a PDF document named "example.pdf" that you want to download into the "/home/ubuntu/pdfs" directory, you can use the wget command in the Linux terminal.
```bash
wget wget -O /home/ubuntu/pdfs/example.pdf https://example.com/path/to/example.pdf
```
This command will download the PDF file from the specified URL and save it as "example.pdf" in the "/home/ubuntu/pdfs" directory.


### Run project
```bash
python run.py
```

### Deactivate Virtual Environment
After you're done working on your project, you can deactivate the virtual environment:

```bash
deactivate
```