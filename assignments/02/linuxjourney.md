# The Command Line Interface

1. Visit [https://linuxjourney.com/the-shell](https://linuxjourney.com/lesson/the-shell). Read each of the 19 lessons carefully, answer the quizzes (lower right), and also do the exercises (upper right). Please document the questions and your answers, as well as the command line outputs of the exercises in a Markdown-formatted file `linuxjourney.md` and add it to this subfolder. Please remember that you can also document your command line outputs with verbatim code.
2. Visit [https://gitlab.com/slackermedia/bashcrawl](https://gitlab.com/slackermedia/bashcrawl) and learn Linux commands by playing a simple text adventure. Please follow the instructions provided in the README of the `bashcrawl` repository. Once you finish the game, create a file with your command history and add it to this subfolder - for instance, with the help of `history -100 >> bashcrawl.log`. You can also upload a Markdown file that documents your history with verbatim code. Please pay attention that you upload the full history beginning with `cd ./bashcrawl/entrance/` or similar.

## Solutions

### Task 1
### Quiz 1
- **Question**: What should be outputted to the display when you type `echo Hello World`?
- **Answer**: `Hello World`

### Exercises
- **Command**: `date`
  - **Output**: `Mi 23 Okt 2024 17:05:23 CEST`

- **Command**: `whoami`
  - **Output**: `tolgaipek`
 
---

### Quiz 2
- **Question**: How do I find what directory you are currently in?
- **Answer**: `pwd`

---

### Quiz 3
- **Question**: If you are in `/home/pete/Pictures` and wanted to go to `/home/pete`, what’s a good shortcut to use?
- **Answer**: `cd ..`

### Exercises
- **Command**: `cd`
  - **Output**: Takes you to your home directory, e.g., `/Users/tolgaipek`

---
 
### Quiz 4
- **Question**: What command would you use to see hidden files?
- **Answer**: `ls -a`

### Exercises
- **Command**: `ls -R`
  - **Output**: Recursively lists all directory contents from the current directory.

- **Command**: `ls -r`
  - **Output**: Lists files and directories in reverse alphabetical order.

- **Command**: `ls -t`
  - **Output**: Lists files sorted by modification time, with the newest first.

---
 
### Quiz 5
- **Question**: How do you create a file called `myfile`?
- **Answer**: `touch myfile`

### Exercises
- **Step 1**: Create a new file
  - **Command**: `touch mysuperduperfile`
  - **Output**: Creates an empty file named `mysuperduperfile`.

- **Step 2**: Note the timestamp
  - **Command**: `ls -l mysuperduperfile`
  - **Output**: Displays file details, including the timestamp of the file creation.

- **Step 3**: Touch the file to update the timestamp
  - **Command**: `touch mysuperduperfile`
  - **Output**: Updates the file's timestamp.

- **Step 4**: Check the updated timestamp
  - **Command**: `ls -l mysuperduperfile`
  - **Output**: The timestamp will be updated to the current time.

---

 ### Quiz 6
- **Quiz**: What command can you use to find the file type of a file?
  - **Answer**: `file`

- **Exercises**: Run the file command on a few different directories and files and note the output.
  - **Command**: `file filename_or_directory`
  - **Output**: Displays the file type of the specified file or directory.

---

### Quiz 7
- **Quiz**: What's a good way to see the contents of a file?
  - **Answer**: `cat`

- **Exercises**: Run `cat` on different files and directories. Then try to `cat` multiple files.
  - **Command**: `cat file1 file2`
  - **Output**: Displays the contents of both files.

### Quiz 8
- **Quiz**: How do you quit out of a less command?
  - **Answer**: `q`

- **Exercises**: Run `less` on a file, navigate with arrow keys, and search for a word using `/search_term`.
  - **Command**: `less filename`
  - **Navigation**: Use the arrow keys or `Page Up`/`Page Down` to navigate. Use `/search_term` to search.

---

### Quiz 9
- **Quiz**: What is the command to clear the terminal?
  - **Answer**: `clear`

- **Exercises**: Navigate through your previous command history with the Up and Down keys, and try out `ctrl-R` for reverse search.
  - **Command**: `history` to see command history and use Up/Down keys or `ctrl-R` for reverse search.

---

### Quiz 10
- **Quiz**: What flag do you need to specify to copy over a directory?
  - **Answer**: `-r`

- **Exercises**: Copy over a couple of files without overwriting anything.
  - **Command**: `cp -r source_directory destination_directory`

---

### Quiz 11
- **Quiz**: How do you rename a file called cat to dog?
  - **Answer**: `mv cat dog`

- **Exercises**: Rename a file, then move that file to a different directory.
  - **Command**: `mv oldfile newfile` to rename and `mv file /destination_directory` to move.

---

### Quiz 12
- **Quiz**: What command is used to make a directory?
  - **Answer**: `mkdir`

- **Exercises**: Make a couple of directories and move some files into that directory.
  - **Command**: `mkdir new_directory`

---

### Quiz 13
- **Quiz**: How do you remove a file called myfile?
  - **Answer**: `rm myfile`

- **Exercises**: Create and remove a file with a dash in the name.
  - **Command**: `rm ./-file`

---

### Quiz 14
- **Quiz**: What option should I specify for find if I want to search by name?
  - **Answer**: `-name`

- **Exercises**: Find a file from the root directory that has the word "net" in it.
  - **Command**: `find / -name "*net*"`

---

### Quiz 15
- **Quiz**: How do you get quick command line help for built-in bash commands?
  - **Answer**: `help`

- **Exercises**: Run help on the `echo`, `logout`, and `pwd` commands.
  - **Command**: `help echo`, `help logout`, `help pwd`

---

### Quiz 16
- **Quiz**: How do you see the manuals for a command?
  - **Answer**: `man`

- **Exercises**: Run the man command on the `ls` command.
  - **Command**: `man ls`

---

### Quiz 17
- **Quiz**: What command can you use to see a small description of a command?
  - **Answer**: `whatis`

- **Exercises**: Run the `whatis` command on the `less` command.
  - **Command**: `whatis less`

---

### Quiz 18
- **Quiz**: What command is used to make an alias?
  - **Answer**: `alias`

- **Exercises**: Create a couple of aliases then remove them.
  - **Command**: `alias myalias='ls -la'`
  - **Remove alias**: `unalias myalias`

---

### Quiz 19
- **Quiz**: How can you exit from the shell?
  - **Answer**: `exit`

- **Exercises**: Exit out of the shell and see what happens.
  - **Command**: `exit` or `logout`

### Task 2
cd /Users/tolgaipek/Downloads/bashcrawl/entrance
cat scroll
