# Keylogger & Detection Script

<div align="center">

<img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Keylogger-and-Detection-Script
">

<img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Keylogger-and-Detection-Script
">

<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Keylogger-and-Detection-Script
">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Keylogger-and-Detection-Script
">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Keylogger-and-Detection-Script
">

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Keylogger-and-Detection-Script
">

</div>

## Project Description

### Objective

The goal of this project is to create an **ethical hacking demonstration** by building a keylogger and an accompanying detection script, showcasing both **red team (offensive)** and **blue team (defensive)** skills.


### Technology and Tools Used

- **Programming Language:** Python  
- **Libraries/Frameworks:** `os`, `requests`, `pynput`, `dotenv`, `psutil`  
- **Tools:** Git, VS Code, ChatGPT (for brainstorming, debugging, and guidance)  

### Challenges Faced

1. **Keylogging Functionality:**  
   - Initially, the keylogger correctly detected key presses but did not store them in the variable.  
   - Solved by defining `keys_logged` as a **global variable** to persist key data.

2. **Detection Script Development:**  
   - Detecting the running keylogger was challenging.  
   - Initial attempts using `psutil` from online tutorials were unsuccessful.  
   - ChatGPT was used to understand how to **identify active processes** and implement a working detection script.

3. **Environment Variables:**  
   - Environment variables were not loading as expected.  
   - Solved by installing and using the `dotenv` package, allowing smooth access to variables from a `.env` file.  

### Notes & Takeaways

- This project provided hands-on experience with **ethical hacking techniques**, process monitoring, and environment management in Python.  
- It strengthened understanding of **offensive (keylogger)** and **defensive (detection)** methods in a controlled, ethical environment.  
- Debugging unfamiliar modules or concepts like can be efficiently accelerated using guided assistance from AI tools.

### Outcome

I successfully implemented a working **keylogger** that records keystrokes in a controlled, ethical environment.Developed a **detection script** capable of identifying the running keylogger, demonstrating basic blue team defensive skills. Gained practical experience with Python libraries such as `pynput`, `psutil`, and `dotenv`. Demonstrated a full **red team vs. blue team workflow**, highlighting the importance of both offensive and defensive cybersecurity techniques.Strengthened understanding of ethical hacking principles and safe experimentation within a controlled environment.  

## How to Use the Project

### Keylogger

### 1. Clone the repository

```
git clone <repository-url>
cd <repository-folder>
```
### 2. Install dependencies

```
pip install pynput requests python-dotenv psutil
```
### 3. Set up your Discord webhook

* Create a .env file in the project root.
* Add your webhook URL:
```
WEBHOOK_URL=your_discord_webhook_url_here
```

### 4. Run the keylogger
```
python keylogger.py
```
* The script logs all key presses.
* Press Esc to stop the keylogger and send the log to Discord.

### 5. View logs
* Logs are stored locally at:
* /Keylogger-and-Detection-Script/key_presses.txt
* A copy is also sent to your Discord channel when the script stops.

### Keylogger Detection Script

### 1. Run the detection script
```
python keylogger_detection.py
```

### 2. Functionality
* Detects if the keylogger script is running.
* Checks if the log file exists.
* Terminates the keylogger process and deletes the log if found.

### 3.Logs

* The detection script prints status messages in the terminal to indicate what was found and removed.

## Licenses
License can be found in the root of the repository.
