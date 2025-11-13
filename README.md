# Scopus Interactive Search Script

This project contains a Python script that allows you to perform advanced, interactive searches on the Scopus (Elsevier) search API. It is designed to automate bibliographic research, allowing the user to dynamically define search parameters and filter out unwanted results before they are displayed.

## 🤖 Features

* **Interactive Search:** The script prompts the user for search terms, the field (Title, Abstract, etc.), and the start year.
* **Default Values:** The script suggests default search terms, making it fast to run repetitive searches.
* **Result Count:** Allows the user to define how many results they want to see.
* **Exclusion Filter:** Automatically removes articles from a predefined list of titles in the code.
* **Keyword Filter:** Automatically removes articles that contain unwanted keywords (e.g., "egg").

---

## 📋 Prerequisites

To use this script, you will need:

1.  **Python 3** installed on your machine.
2.  An **Elsevier Developer Account** (Scopus).
3.  A valid Scopus **API Key**.

---

## 🛠️ Installation and Setup Guide

Follow these steps to set up and run the project on your local machine.

### Step 1: Install Python

If you don't already have Python, you'll need to install it.

1.  Go to the official website: [python.org/downloads](https://www.python.org/downloads/)
2.  Download the latest installer for your operating system (Windows, macOS, Linux).
3.  Run the installer.
    * **Important (For Windows):** On the first screen of the installation, check the box that says **"Add Python 3.x to PATH"**. This is essential so you can use the `python` and `pip` commands in your terminal (CMD).

### Step 2: Get the Project Code

1.  Clone this repository (if you have Git):
    ```bash
    git clone [https://github.com/your-user/your-repository.git](https://github.com/your-user/your-repository.git)
    ```
    *(Remember to change the URL to your actual repository!)*

2.  Or, simply download the ZIP file and extract it to a folder on your computer.

### Step 3: Install Dependencies (`requests` library)

This script needs the `requests` library to communicate with the API.

1.  Open **Command Prompt (CMD)** in Windows (or "Terminal" on macOS/Linux).
2.  Navigate to the folder where you saved the project using the `cd` command:
    ```bash
    cd C:\path\to\your\project\folder
    ```
3.  Run `pip` (Python's package manager) to install the library:
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
>
> Your API key is like a password. Never publish it on GitHub, send it in an email, or show it in screenshots. Treat it with the utmost confidentiality.

### Step 5: Configure the Script

**(Note: This step is only if you are *not* using the `.gitignore` method. The recommended method is to use a `config.py` file as we discussed.)**

If you *are* using the `config.py` and `.gitignore` method,
