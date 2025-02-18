## ⚔️ Bash Battle Arena - Challenge Log  

The **Bash Battle Arena** is a set of scripting challenges designed to test and apply key Bash concepts in a hands-on way. As I wrap up the **Bash Scripting Module**, I'm documenting my solutions from **Level 1 to Level 15**, showcasing my progress in:  

- Using **loops, conditionals, and functions** 🔄  
- Handling **user input and variables** 📝  
- Improving **script efficiency and logic** ⚙️  

These challenges reinforce my understanding of **Bash scripting fundamentals**, preparing me for more advanced automation tasks in my DevOps journey. 🚀  

## 📜 Table of Contents

- [Level 1: The Basics](#level-1-the-basics)
- [Level 2: Variables and Loops](#level-2-variables-and-loops)
- [Level 3: Conditional Statements](#level-3-conditional-statements)
- [Level 4: File Manipulation](#level-4-file-manipulation)
- [Level 5: The Boss Battle - Combining Basics](#level-5-the-boss-battle---combining-basics)
- [Level 6: Argument Parsing](#level-6-argument-parsing)
- [Level 7: File Sorting Script](#level-7-file-sorting-script)
- [Level 8: Multi-File Searcher](#level-8-multi-file-searcher)
- [Level 9: Script to Monitor Directory Changes](#level-9-script-to-monitor-directory-changes)
- [Level 10: Boss Battle 2 - Intermediate Scripting](#level-10-boss-battle-2---intermediate-scripting)
- [Level 11: Automated Disk Space Report](#level-11-automated-disk-space-report)
- [Level 12: Simple Configuration File Parser](#level-12-simple-configuration-file-parser)
- [Level 13: Backup Script with Rotation](#level-13-backup-script-with-rotation)
- [Level 14: User-Friendly Menu Script](#level-14-user-friendly-menu-script)
- [Level 15: Boss Battle 3 - Advanced Scripting](#level-15-boss-battle-3---advanced-scripting)



---

## Level 1: The Basics
---

### 🎯 The Mission
Create a directory named **Arena** and then inside it, create three files: **warrior.txt**, **mage.txt**, and **archer.txt**. List the contents of the **Arena** directory.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:  
```bash
mkdir Arena  # Create the Arena directory
cd Arena  # Move into the Arena directory
touch warrior.txt mage.txt archer.txt  # Create three empty text files
ls  # List the contents of Arena
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%201.gif?raw=true" alt="Level 1 GIF" width="100%" />
  </div>
</div>

---

## Level 2: Variables and Loops
---

### 🎯 The Mission
Create a script that outputs the numbers 1 to 10, one number per line.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

while ((num <= 10)); do # Start a loop that runs while while 'num' is less than or equal to 10
  echo "$num" # Prints the current value of 'num'
  ((num++)) # Increment 'num' by 1
done # End of while loop
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://raw.githubusercontent.com/hanadisa/Hanad-DevOps-Learning/4bc729bfac70e30c248504aec7a9e93df1431fed/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%202.gif" alt="Level 2 GIF" width="100%" />
  </div>
</div>

---

## Level 3: Conditional Statements
---

### 🎯 The Mission
Write a script that checks if a file named **hero.txt** exists in the **Arena** directory. If it does, print **Hero found!**; otherwise, print **Hero missing!**.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

if [ -f Arena/hero.txt ]; then # Check if 'hero.txt exists inside the 'Arena' directory
  echo "Hero found!" # If the file exists, print this message
else
  echo "Hero missing!" # If the file does not exist, print this message
fi # End of if statement
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%203.gif?raw=true" alt="Level 3 GIF" width="100%" />
  </div>
</div>

---

## Level 4: File Manipulation
---

### 🎯 The Mission
Create a script that copies all **.txt** files from the **Arena** directory to a new sirectory called **Backup**.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

mkdir Backup # Create a directory named 'Backup'
cp Arena/*.txt Backup/ # Copy all .txt files from 'Arena' directory to 'Backup'
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%204.gif?raw=true" alt="Level 4 GIF" width="100%" />
  </div>
</div>

---

## Level 5: The Boss Battle - Combining Basics
---

### 🎯 The Mission
Combine what you've learnt! Write a script that: 

1) Creates a directory named **Battlefield**.
2) Inside **Battlefield**, create files named **knight.txt**, **sorcerer.txt**, and **rogue.txt**.
3) Check if **knight.txt** exists; if it does, move it to a new directory called **Archive**.
4) List the contents of both **Battlefield** and **Archive**.

---

### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

mkdir Battlefield # Create a directory named 'Battlefield'
touch Battlefield/knight.txt Battlefield/sorcerer.txt Battlefield/rogue.txt # Create three text files inside 'Battlefield'

if [ -f Battlefield/knight.txt ]; then # Check if 'knight.txt' exists inside 'Battlefield'
    mkdir Archive # Create a directory named 'Archive'
    mv Battlefield/knight.txt Archive/ # Move 'knight.txt' from 'Battlefield' to 'Archive'
else    
    echo "The file knight.txt cannot be found" # Print message if 'knight.txt' does not exist
fi # End of if statement

ls Battlefield # List all files inside 'Battlefield' directory
ls Archive # List all files inside 'Archive' directory
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%205.gif?raw=true" alt="Level 5 GIF" width="100%" />
  </div>
</div>

---

## Level 6: Argument Parsing
---

### 🎯 The Mission
Write a script that accepts a filename as an argument and prints the number of lines in that file. If no filename is provided, display a message saying 'No file provided'.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

if [ $# == 0]; then
  echo "No file provided."
elif  [ ! -f $1 ]; then
  echo "$1 doesn't exist."
else
  line_count=$(wc -l < $1)
  echo "There are $line_count lines in the file called £1!"
fi
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%206.gif?raw=true" alt="Level 6 GIF" width="100%" />
  </div>
</div>

---

## Level 7: File Sorting Script
---

### 🎯 The Mission
Write a script that sorts all .txt files in a directory by their size, from smallest to largest, and displays the sorted list.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

echo "What is the name of the directory?" # Prompt the user for a directory name
read directory_name # Store the user input in the variable 'directory_name'

if [ ! -d "$directory_name" ]; then # Check if the directory does NOT exist ('-d' checks for a directory, '!' negates the condition)
    echo "Sorry. The directory you provided doesn't exist." # Print an error message if the directory doesn't exist
else # If the directory exists, proceed with the next steps
    sizes=$(ls -l "$directory_name" | sort -k 5 -h | awk '{print $9, $5}')
    # 1. 'ls -l "$directory_name"' → List files with details
    # 2. 'sort -k 5 -h' → Sort by the 5th column (file size), in human-readable format
    # 3. 'awk '{print $9, $5}'' → Extract and display only the filename (9th column) and size (5th column)
    echo "Here are the sizes of all the files within the '$directory_name' directory, sorted from smallest to largest: $sizes" # Display the sorted file sizes
fi # End of if-else statement
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%207.gif?raw=true" alt="Level 7 GIF" width="100%" />
  </div>
</div>

---

## Level 8: Multi-File Searcher
---

### 🎯 The Mission
Create a script that searches for a specific word or phrase across all .log files in a directory and outputs the names of the files that contain the word or phrase.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

echo "What is the name of the directory?" # Ask user for a directory name
read directory_name # Store user input in 'directory_name'
echo "What is the keyword you're looking for?" # Ask user for a keyword to search
read key_word # Store user input in 'key_word'

if [ ! -d "$directory_name" ]; then # Check if the directory does NOT exist
    echo "Sorry. The directory you provided doesn't exist." # Print an error message if directory is missing
else
    search=$(grep -l "$key_word" "$directory_name"/*.log) # Search for the keyword inside '.log' files in the given directory
    echo "Here are the filenames within the $directory_name directory that contain the keyword '$key_word':$search" # Display matching files
fi  # End of if statement
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%208.gif?raw=true" alt="Level 8 GIF" width="100%" />
  </div>
</div>

---

## Level 9: Script to Monitor Directory Changes
---

### 🎯 The Mission
Write a script that monitors a directory for any changes (file creation, modification, or deletion) and logs the changes with a timestamp.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

dir="Level9_Directory" # Define the directory to monitor
logs="logs.txt" # Define the log file to store detected changes

if [ ! -d "$dir" ]; then # Check if the directory does NOT exist
    echo "The "$dir" directory does not exist." # Print error message
    exit 1 # Exit the script with an error code
fi

fswatch -r "$dir" | while read event; do # Monitor the directory for changes
    if [ -e "$event" ]; then # Check if the detected file still exists
        echo "$(date) File modified: $event" >> "$logs" # Append event details to the log file
    else
        echo "No log events detected." # Print message if no events occur
    fi
done # End of while loop
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%209.gif?raw=true" alt="Level 9 GIF" width="100%" />
  </div>
</div>

---

## Level 10: Boss Battle 2 - Intermediate Scripting
---

### 🎯 The Mission
Write a script that:

1) Creates a directory called **Arena_Boss**.
2) Creates 5 text files inside the directory, named **file1.txt** to **file5.txt**.
3) Generates a random number of lines (between 10 and 20) in each file.
4) Sorts these files by their size and displays the list.
5) Checks if any of the files contain the word "Victory", and if found, moves the file to a directory called **Victory_Archive**.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash 

mkdir Arena_Boss  # Create a directory named 'Arena_Boss'

for i in {1..5}; do  # Loop to create 5 files
    touch "Arena_Boss/file$i.txt"  # Create empty file (file1.txt, file2.txt, etc.)

    num_lines=$((RANDOM % 11 + 10))  # Generate a random number of lines (between 10 and 20)

    for j in $(seq 1 $num_lines); do  # Loop to add lines to each file
        echo "Random line $j in file$i" >> "Arena_Boss/file$i.txt"  # Append a line with text to the file
    done
done  # End of file creation loop

echo "Here's the list of all files within the Arena_Boss directory, sorted by size from smallest to largest:"  
ls -l "Arena_Boss" | sort -k 5 -h | awk '{print $9, $5}'  # List files, sort by size, and display filename + size

mkdir Victory_Archive  # Create a directory named 'Victory_Archive'

for file in Arena_Boss/*.txt; do  # Loop through all .txt files in 'Arena_Boss'
    if grep -q "Victory" "$file"; then  # Check if the file contains the keyword "Victory"
        mv "$file" Victory_Archive/  # Move the file to 'Victory_Archive'
        echo "The file $file contains the keyword 'Victory'. This file has now been moved to the 'Victory_Archive' directory."
    else
        echo "The file $file does not contain the keyword."  # Message if the file does not contain "Victory"
    fi
done  # End of loop
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%2010.gif?raw=true" alt="Level 10 GIF" width="100%" />
  </div>
</div>

---

## Level 11: Automated Disk Space Report
---

### 🎯 The Mission
Create a script that checks the disk space usage of a specified directory and sends an alert if the usage exceeds a given threshold.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

size=10  # Set the size threshold to 10MB

echo "What is the name of the directory?"  # Ask user for a directory name
read directory_name  # Store user input in 'directory_name'

dir_size=$(du -sm "$directory_name" | cut -f1)  # Get the directory size in MB (du -sm), then extract the size using 'cut'

if [ "$dir_size" -ge "$size" ]; then  # Check if the directory size is greater than or equal to 10MB
    echo "The $directory_name directory is taking up too much disk space. Please remove any unnecessary files within it or delete the directory."  # Warn if the directory is too large
else
    echo "There is plenty of disk space remaining."  # Print a message if the directory size is within the limit
fi  # End of if-else statement
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%2011.gif?raw=true" alt="Level 11 GIF" width="100%" />
  </div>
</div>

---

## Level 12: Simple Configuration File Parser
---

### 🎯 The Mission
Write a script that reads a configuration file in the format KEY=VALUE and prints each key-value pair.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

echo "What is the name of the config file?"  # Ask user for a config file name
read conf_file  # Store user input in 'conf_file'

if [ ! -f "$conf_file" ]; then  # Check if the file does NOT exist
    echo "The file '$conf_file' doesn't exist."  # Print an error message if the file is missing
    exit 1  # Exit the script with an error code
fi

while IFS='=' read -r KEY VALUE; do  # Read each line of the file, splitting by '='
    echo "Key: $KEY, Value: $VALUE"  # Print the extracted key and value
done < "$conf_file"  # Redirect the file input to the while loop
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%2012.gif?raw=true" alt="Level 12 GIF" width="100%" />
  </div>
</div>

---

## Level 13: Backup Script with Rotation
---

### 🎯 The Mission
Create a script that backs up a directory to a specified location and keeps only the last 5 backups.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

dir=Level13  # Set the directory to be backed up

mkdir -p Backups  # Ensure the 'Backups' directory exists (create it if it doesn't)

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")  # Generate a timestamp for the backup name
BACKUP_NAME="backup_$TIMESTAMP.tar.gz"  # Create a unique backup filename

tar -czf "Backups/$BACKUP_NAME" "$dir"  # Create a compressed backup of 'Level13' inside 'Backups'
echo "Backup file created: $BACKUP_NAME"  # Print confirmation message

cd Backups  # Navigate to the 'Backups' directory

backup_count=$(ls -1 | wc -l)  # Count the number of backup files

if [ "$backup_count" -gt 5 ]; then  # Check if there are more than 5 backups
    ls -t | tail -n +6 | while IFS= read -r file; do  # List backups in order, keeping the 5 newest
        rm -f "$file"  # Delete old backup files
        echo "Deleted old backup: $file"  # Print message confirming deletion
    done
else
    echo "There are fewer than 5 backups, no files will be deleted."  # Print message if deletion is not needed
fi
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%2013.gif?raw=true" alt="Level 13 GIF" width="100%" />
  </div>
</div>

---

## Level 14: User-Friendly Menu Script
---

### 🎯 The Mission
Create an interactive script that presents a menu with options for different system tasks (e.g., check disk space, show system uptime, list users), and executes the chosen task.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

echo "Choose an option:"  # Display menu options
echo "1. Check disk space"  
echo "2. List running processes"  
echo "3. Check current shell"  

read -p "Enter your choice [1-3]: " choice  # Prompt user for input and store it in 'choice'

case $choice in  # Start case statement to handle user choices
    1) df -h ;;  # If user selects 1, show disk space usage in human-readable format
    2) ps aux ;;  # If user selects 2, list all running processes
    3) echo $SHELL ;;  # If user selects 3, print the current shell being used
    *) echo "Invalid option" ;;  # If input is not 1, 2, or 3, print an error message
esac  # End of case statement
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%2014.gif?raw=true" alt="Level 14 GIF" width="100%" />
  </div>
</div>

---

## Level 15: Boss Battle 3 - Advanced Scripting
---

### 🎯 The Mission
Combine the skills you've gained! Write a script that:

1) Presents a menu to the user with the following options:
2) Check disk space
3) Show system uptime
4) Backup the **Arena** directory and keep the last 3 backups
5) Parse a configuration file settings.conf and display the values
6) Execute the chosen task.

---
### 🛠 **Solution:**  
Steps I followed to complete the challenge:
```bash
#!/bin/bash

conf="settings.conf"  # Define the configuration file

echo "Choose an option:"  # Display menu options
echo "1. Check disk space"
echo "2. Show system uptime"
echo "3. Backup the Arena directory and keep the last 3 backups"
echo "4. Parse a configuration file (settings.conf) and display the values"

read -p "Enter your choice [1-4]: " choice  # Prompt user for input

case $choice in  # Start case statement to handle user choices
    1)  df -h ;;  # If user selects 1, show disk space usage
    2)  uptime ;;  # If user selects 2, display system uptime
    3)  dir="Arena"  # Define the directory to back up
        mkdir -p Backups  # Ensure the 'Backups' directory exists

        TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")  # Generate a timestamp for the backup filename
        BACKUP_NAME="backup_$TIMESTAMP.tar.gz"  # Create a unique backup filename

        tar -czf "Backups/$BACKUP_NAME" "$dir"  # Create a compressed backup of 'Arena' inside 'Backups'
        echo "Backup file created: $BACKUP_NAME"  # Confirm backup creation

        cd Backups  # Navigate to the 'Backups' directory

        backup_count=$(ls -1 | wc -l)  # Count the number of backup files

        if [ "$backup_count" -gt 3 ]; then  # If there are more than 3 backups
            ls -t | tail -n +4 | while IFS= read -r file; do  # Keep the 3 newest, delete older ones
                rm -f "$file"  # Delete the old backup
                echo "Deleted old backup: $file"  # Print confirmation
            done
        else
            echo "There are fewer than 3 backups, no files will be deleted."  # No deletion needed
        fi ;;
    4)  if [ ! -f "$conf" ]; then  # Check if the config file exists
            echo "Configuration file does not exist."  # Print error message
            exit 1  # Exit the script with an error code
        fi
        while IFS='=' read -r KEY VALUE; do  # Read each line of the file, splitting by '='
            echo "Key: $KEY, Value: $VALUE"  # Print the extracted key-value pairs
        done < "$conf" ;;  # Redirect the file input to the while loop
    *)  echo "Invalid option" ;;  # Handle invalid choices
esac  # End of case statement
```
<div style="text-align: center; margin: 20px 0;">
  <h2 style="font-family: 'Arial', sans-serif; color: #FF5722; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎥Live Demonstration</h2>
  <div style="width: 400px; margin: 0 auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <img src="https://github.com/hanadisa/Hanad-DevOps-Learning/blob/main/My-DevOps-Journey/BASH%20Scripting/Labs/Images/Level%2015.gif?raw=true" alt="Level 15 GIF" width="100%" />
  </div>
</div>
