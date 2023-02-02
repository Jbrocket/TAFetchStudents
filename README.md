# Hi Fellow TA's :D

This is a script that you **MUST** put in your grading environment folder and it's pretty self explanatory to use. What I recommend doing is making a separate subfolder and just calling it in the root directory like this:

```
python3 <SUBDIRECTORY>/<ScriptName> .......
```

that way it's separate from all the grading and whatnot.

## Usage:
```
python3 <ScriptName> <ListofIds|TextFile> <CHALLENGE_NUMBER> <FLAGS>
```
What this basically means is put in your list of NDId's you want to grade for this week, separated by commas **(NOT SPACES)**, into the program and **COPIES**  of your students' directories will be put into your current working directory for you to grade.

### FOR TEXT FILE USAGE
You can just copy and paste the values from the spreadsheet into a txt file, essentially separate the names by a new line, and that'll also yield the same results as listing the ids.

## IMPORTANT NOTICE:
Since we are copying files, obviously
```
ls -al
```
won't work since we're creating new copies, so just 
```
cat LSOUTPUTS.txt
```
within the directory to get the correct outputs for dates submitted

## Flags
Not yet included :)