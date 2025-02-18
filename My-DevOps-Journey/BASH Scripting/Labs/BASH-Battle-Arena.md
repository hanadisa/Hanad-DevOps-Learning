## ⚔️ Bash Battle Arena - Challenge Log  

The **Bash Battle Arena** is a set of scripting challenges designed to test and apply key Bash concepts in a hands-on way. As I wrap up the **Bash Scripting Module**, I'm documenting my solutions from **Level 1 to Level 15**, showcasing my progress in:  

- Using **loops, conditionals, and functions** 🔄  
- Handling **user input and variables** 📝  
- Improving **script efficiency and logic** ⚙️  

These challenges reinforce my understanding of **Bash scripting fundamentals**, preparing me for more advanced automation tasks in my DevOps journey. 🚀  


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
