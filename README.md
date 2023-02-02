# Hi Fellow TA's :D

This is a script that you **MUST** put in your grading environment folder and it's pretty self explanatory to use. What I recommend doing is making a separate subfolder and just calling it in the root directory like this:

```
python3 <SUBDIRECTORY>/<ScriptName> .......
```

that way it's separate from all the grading and whatnot.

## Usage:
```
.work-env/main.py <import|edit|remove|compile|distribute> <OPTIONS>
```

### FOR TEXT FILE USAGE
You can just copy and paste the values from the spreadsheet into a txt file, essentially separate the names by a new line, and that'll also yield the same results as listing the ids.

example text file:
```
id1
id2
id3
id3
```

example input:
```
python3 SCRIPT/bringFiles.py students.txt 1
```

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

## Options
Not yet included :)