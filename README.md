# RAG-based QA system from PDF documents using Gemma

## Project Setup Guide
This guide is written and tested on a linux (Ubuntu) virtual machine.

**Prerequisites:** Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/). 

## Installation

### Step 1: Install `pip`

If you don't have `pip` installed, follow these steps:
- On Unix/macOS
```bash
sudo apt-get install python3-pip
```
- On Windows
```bash
python -m ensurepip --default-pip
```

### Step 2: Install `venv`
Now, let's install venv and create a virtual environment for your project:
- Install venv
```bash
sudo apt install python3.10-venv
```

#### Create virtual environment named `venv`
- On Unix/macOS/Windows
```bash
python3 -m venv venv
```

### Step 3: 
Activate the virtual environment based on your operating system:

- On Unix/macOS:
```bash
source venv/bin/activate
```

- On Windows:
```bash
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

- If encountering out-of-memory issues, consider utilizing the following command for resolution.

```bash
pip install -r requirements.txt --no-cache-dir
```
### Download PDF
Assuming you have a PDF document named "example.pdf" that you want to download into the "/home/ubuntu/pdfs" directory, you can use the wget command in the Linux terminal.
```bash
wget -O /home/ubuntu/pdfs/example.pdf https://example.com/path/to/example.pdf
```
This command will download the PDF file from the specified URL and save it as "example.pdf" in the "/home/ubuntu/Gemma-RAG/pdfs" directory.


### Run project
```bash
python run.py
```

### Deactivate Virtual Environment
After you're done working on your project, you can deactivate the virtual environment:

```bash
deactivate
```