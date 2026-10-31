# ------------------------------------------------------------
# Project Name : Data Shield - Automated Backup and File Monitoring System
# Description  : Python-based automated file backup and monitoring system.
# Author Name  : Yash Chavan
# Date         : 15/10/2026
# ------------------------------------------------------------

import os
import shutil
import hashlib
import time
import sys
import schedule
from datetime import datetime


# ------------------------------------------------------------
# Step 1 : Calculate Checksum
# ------------------------------------------------------------

def CalculateChecksum(FileName):

    hobj = hashlib.md5()

    with open(FileName, "rb") as fobj:
        Buffer = fobj.read(4096)

        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(4096)

    return hobj.hexdigest()


# ------------------------------------------------------------
# Step 2 : Write Log
# ------------------------------------------------------------

def WriteLog(Message, LogFileName):

    Timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(LogFileName, "a", encoding="utf-8") as fobj:
        fobj.write("[%s] %s\n" % (Timestamp, Message))

    print(Message)


# ------------------------------------------------------------
# Step 3 : Create Automated Backup
# ------------------------------------------------------------

def CreateBackup(SourceDirectory, BackupDirectory):

    Border = "_" * 60
    StartTime = time.time()

    Timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    LogFileName = "Yash_Data_Shield_%s.log" % Timestamp

    TotalFiles = 0
    TotalCopied = 0
    TotalUnchanged = 0
    TotalErrors = 0

    print("\n" + Border)
    print("Yash Data Shield")
    print("Automated Backup and File Monitoring System")
    print("Author Name : Yash Chavan")
    print("Date        : 15/10/2026")
    print(Border)

    if not os.path.isdir(SourceDirectory):
        print("Invalid Source Directory")
        return

    SourceAbsolute = os.path.abspath(SourceDirectory)
    BackupAbsolute = os.path.abspath(BackupDirectory)

    # Backup directory must be outside source directory
    if os.path.commonpath(
        [SourceAbsolute, BackupAbsolute]
    ) == SourceAbsolute:
        print("Error: Backup directory must be outside source directory")
        return

    os.makedirs(BackupDirectory, exist_ok=True)

    WriteLog(
        "Backup Started: %s" % SourceDirectory,
        LogFileName
    )

    # --------------------------------------------------------
    # Step 4 : Scan Files and Monitor Changes
    # --------------------------------------------------------

    print("\n" + Border)
    print("Step 4 : File Scanning and Monitoring")
    print(Border)

    for FolderName, SubFolders, FileNames in os.walk(
        SourceDirectory
    ):

        for FileName in FileNames:

            SourceFile = os.path.join(FolderName, FileName)

            RelativePath = os.path.relpath(
                SourceFile, SourceDirectory
            )

            BackupFile = os.path.join(
                BackupDirectory, RelativePath
            )

            TotalFiles += 1

            try:
                os.makedirs(
                    os.path.dirname(BackupFile),
                    exist_ok=True
                )

                SourceHash = CalculateChecksum(SourceFile)

                if os.path.exists(BackupFile):
                    BackupHash = CalculateChecksum(BackupFile)
                else:
                    BackupHash = None

                # ------------------------------------------------
                # Step 5 : Backup New or Modified Files
                # ------------------------------------------------

                if SourceHash != BackupHash:

                    shutil.copy2(SourceFile, BackupFile)

                    NewHash = CalculateChecksum(BackupFile)

                    if SourceHash == NewHash:
                        TotalCopied += 1

                        WriteLog(
                            "Backup Successful: %s" % RelativePath,
                            LogFileName
                        )

                    else:
                        TotalErrors += 1

                        WriteLog(
                            "Verification Failed: %s" % RelativePath,
                            LogFileName
                        )

                else:
                    TotalUnchanged += 1

                    WriteLog(
                        "No Changes: %s" % RelativePath,
                        LogFileName
                    )

            except OSError as Error:
                TotalErrors += 1

                WriteLog(
                    "Error: %s - %s" % (RelativePath, Error),
                    LogFileName
                )

    # --------------------------------------------------------
    # Step 6 : Generate Automation Report
    # --------------------------------------------------------

    TotalTime = time.time() - StartTime

    print("\n" + Border)
    print("Step 6 : Automation Report")
    print(Border)

    WriteLog(
        "Total Files Scanned: %d" % TotalFiles,
        LogFileName
    )

    WriteLog(
        "Total Files Backed Up: %d" % TotalCopied,
        LogFileName
    )

    WriteLog(
        "Unchanged Files: %d" % TotalUnchanged,
        LogFileName
    )

    WriteLog(
        "Total Errors: %d" % TotalErrors,
        LogFileName
    )

    WriteLog(
        "Total Time: %.2f Seconds" % TotalTime,
        LogFileName
    )

    WriteLog(Border, LogFileName)


# ------------------------------------------------------------
# Step 7 : Main Function and Scheduling
# ------------------------------------------------------------

def main():

    Border = "_" * 60

    print(Border)
    print("Yash Data Shield")
    print("Author : Yash Chavan")
    print("Date   : 15/10/2026")
    print("Step 7 : Main Function and Scheduling")
    print(Border)

    if len(sys.argv) == 2 and sys.argv[1] in (
        "--h", "--H", "--help"
    ):
        print(
            "Usage: python YashDataShield.py "
            "SourceDirectory BackupDirectory"
        )
        return

    if len(sys.argv) != 3:
        print("Invalid Number Of Arguments")
        print(
            "Usage: python YashDataShield.py "
            "SourceDirectory BackupDirectory"
        )
        return

    SourceDirectory = sys.argv[1]
    BackupDirectory = sys.argv[2]

    print("Source Directory :", SourceDirectory)
    print("Backup Directory :", BackupDirectory)

    # Run backup immediately
    CreateBackup(SourceDirectory, BackupDirectory)

    # Schedule backup every 5 minutes
    schedule.every(5).minutes.do(
        CreateBackup,
        SourceDirectory,
        BackupDirectory
    )

    print(Border)
    print("Automatic Scheduling Started")
    print("Backup Interval : 5 Minutes")
    print(Border)

    while True:
        schedule.run_pending()
        time.sleep(1)


# ------------------------------------------------------------
# Step 8 : Program Execution
# ------------------------------------------------------------

if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# End Of Yash Data Shield
# Developed By : Yash Chavan
# ------------------------------------------------------------