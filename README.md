# Scopus Interactive Search Script

This project contains a Python script that allows you to perform advanced, interactive searches on the Scopus (Elsevier) search API. It is designed to automate bibliographic research, allowing the user to dynamically define search parameters and filter out unwanted results before they are displayed.

## 🤖 Features

* **Interactive Search:** The script prompts the user for search terms, the field (Title, Abstract, etc.), and the start year.
* **Default Values:** The script suggests default search terms, making it fast to run repetitive searches.
* **Result Count:** Allows the user to define how many results they want to see.
* **Exclusion Filter:** Automatically removes articles from a predefined list of titles in the code.

---

## 📋 Prerequisites

To use this script, you will need:

1.  **Python 3** installed on your machine.
2.  An **Elsevier Developer Account** (Scopus).
3.  A valid Scopus **API Key**.

---

## 🛠️ Installation and Setup Guide

Follow these steps to set up and run the project.

### Step 1: Install Python

### Step 2: Get the Project Code

1.  Clone this repository:

2.  Or download the ZIP file and extract it to a folder.

### Step 3: Install Dependencies (`requests` library)

This script needs the `requests` library to communicate with the API.

1.  Open **Command Prompt (CMD)** in Windows.
2.  Navigate to the folder where you saved the project:
    ```bash
    cd C:\path\to\your\project\folder
    ```
3.  Run `pip` to install the library:
    ```bash
    pip install requests
    ```

### Step 4: Get Your Scopus API Key

This is the most important part. The script needs a key to authenticate with Scopus.

1.  Go to the [Elsevier Developer Portal](https://dev.elsevier.com/) and create an account (or log in).
2.  After logging in, navigate to the "My API Keys" section.
3.  Create a new API Key. Give it a "label" (name), for example, "MySearchScript".
4.  The site will generate your API Key. Copy this value (a long string of letters and numbers).

> ⚠️ **VERY IMPORTANT: DO NOT SHARE YOUR API KEY** ⚠️

### Step 5: Configure the Script

**(Note: This step is only if you are *not* using the `.gitignore` method. The recommended method is to use a `config.py`. Just paste your API Key inside `config.py`.
Or just put your API Key at the line 6 of the code `##API_KEY = "PASTE KEY HERE"` and don't forget to uncomment this line!)**
