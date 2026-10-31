# Yash Data Shield

### Automated Backup and File Monitoring System

**Author:** Yash Chavan
**Project Date:** 15/10/2026
**Project Type:** Python Automation

---

## 📌 Project Description

Yash Data Shield is a Python-based automation project designed to automate file backups and monitor file changes.

The system scans files in a source directory, calculates MD5 checksums, and compares source files with their corresponding backup copies. If a file is new or has been modified, the system copies it to the backup directory and verifies the copied file.

The project also generates log files containing backup activities, file statuses, errors, and execution statistics.

After the initial backup, the system automatically runs another backup every five minutes.

## 🎯 Project Objectives

* Automate file backup operations.
* Detect new and modified files using checksums.
* Avoid copying files that have not changed.
* Verify copied files using checksum comparison.
* Maintain logs of backup operations.
* Generate backup execution reports.
* Schedule automatic backups at regular intervals.

## ✨ Features

* **Automated Backup:** Copies new and modified files from the source directory.
* **File Monitoring:** Scans files to identify changes.
* **Checksum Verification:** Uses MD5 checksums to compare files.
* **Incremental Backup:** Skips files whose contents have not changed.
* **Metadata Preservation:** Uses `shutil.copy2()` to preserve supported file metadata.
* **Automatic Logging:** Records backup activities with timestamps.
* **Error Handling:** Handles certain file access and operating system errors.
* **Execution Report:** Displays scanned files, copied files, unchanged files, errors, and execution time.
* **Scheduled Backup:** Repeats the backup process every five minutes.
* **Command-Line Arguments:** Accepts source and backup directory paths.

## 🛠️ Technologies Used

* Python
* `os`
* `shutil`
* `hashlib`
* `time`
* `sys`
* `schedule`
* `datetime`

## 📂 Project Structure

```text
Yash_Data_Shield_Automated_Backup_And_File_Monitoring/
│
├── YashDataShield.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── TestData/
│   ├── file1.txt
│   ├── file2.txt
│   └── Documents/
│       └── sample.txt
│
├── YashBackup/
│   ├── file1.txt
│   ├── file2.txt
│   └── Documents/
│       └── sample.txt
│
├── Logs/
│   └── Yash_Data_Shield_YYYYMMDD_HHMMSS.log
│
└── Yash_Env/
```

**Note:** `TestData/`, `YashBackup/`, and `Logs/` are example directory names. The backup directory should be outside the source directory. The log directory is used if you configure your Python script to save logs there.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

Clone the project repository to your computer:

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd Yash_Data_Shield_Automated_Backup_And_File_Monitoring
```

### Step 2: Create a Virtual Environment

```bash
python -m venv Yash_Env
```

### Step 3: Activate the Virtual Environment

For Windows Command Prompt:

```cmd
Yash_Env\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

## 📦 Requirements

The `requirements.txt` file contains:

```text
schedule
```

The other imported modules are part of Python's standard library.

## ▶️ How to Run the Project

Run the following command from the project directory:

```bash
python YashDataShield.py TestData YashBackup
```

### Command Explanation

* `YashDataShield.py`: Main Python program.
* `TestData`: Source directory containing the files to back up.
* `YashBackup`: Destination directory for backup copies.

**Important:** Replace `TestData` and `YashBackup` with your actual directory paths if you use different folder names.

The program performs the first backup immediately. It then schedules subsequent backups every five minutes.

To stop the program, press `Ctrl + C` in the terminal.

## 🔍 How the Project Works

1. Accepts the source and backup directory paths.
2. Checks whether the source directory exists.
3. Validates that the backup directory is outside the source directory.
4. Creates the backup directory if necessary.
5. Scans files and subdirectories in the source directory.
6. Calculates the MD5 checksum of each source file.
7. Compares the source checksum with the backup file's checksum.
8. Copies new or modified files to the backup directory.
9. Verifies the copied files by calculating their checksums again.
10. Records file statuses and errors in a log file.
11. Generates a summary report.
12. Repeats the backup process every five minutes.

## 📊 Sample Output

```text
____________________________________________________________
Yash Data Shield
Author : Yash Chavan
Date   : 15/10/2026
Step 7 : Main Function and Scheduling
____________________________________________________________

Source Directory : TestData
Backup Directory : YashBackup

[2026-10-15 10:00:00] Backup Started: TestData
[2026-10-15 10:00:01] Backup Successful: file1.txt
[2026-10-15 10:00:01] Backup Successful: file2.txt
[2026-10-15 10:00:02] Total Files Scanned: 2
[2026-10-15 10:00:02] Total Files Backed Up: 2
[2026-10-15 10:00:02] Unchanged Files: 0
[2026-10-15 10:00:02] Total Errors: 0
[2026-10-15 10:00:02] Total Time: 2.00 Seconds

____________________________________________________________
Automatic Scheduling Started
Backup Interval : 5 Minutes
____________________________________________________________
```

*The output above is illustrative. Actual timestamps, file counts, and execution times depend on the files and computer.*

## 📈 Backup Report

| Metric                | Description                                               |
| --------------------- | --------------------------------------------------------- |
| Total Files Scanned   | Number of source files examined                           |
| Total Files Backed Up | Number of new or modified files copied and verified       |
| Unchanged Files       | Number of files whose contents match the existing backups |
| Total Errors          | Number of errors recorded during file processing          |
| Total Time            | Time taken to complete the backup operation               |

## 🔐 Important Notes

* Keep the backup direc
