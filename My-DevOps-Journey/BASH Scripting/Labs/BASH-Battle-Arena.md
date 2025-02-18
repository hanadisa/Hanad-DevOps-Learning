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
