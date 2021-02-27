## XKCD Desktop BASH Script

This script grabs the most recent comic posted by XKCD and imposes it on 
another background image which it then makes your desktop background. Enjoy
the newest XKCD comic on your desktop whenever you turn on your ocmputer 
without any extra effort!

### Requirements

Both opencv and python are needed and can be dowloaded through the linux repo.

```
sudo apt-get install python3
sudo apt-get install python-opencv
```

### Linux Setup

The program will need to run on startup everytime. To get this to happen add 
xkcd_launch.sh to your systems start up applications. 

How:
 * Launch 'Startup Applications Preferences'
 * Click 'Add'
 * For 'Command:' put the full path to xkcd_launch.sh

### Detailed Breakdown

The launch script will get the html file for XKCD's comic archive and then 
launch the python code. Python then searched the html for the most recent 
comic's title which is listed next to the current date. With the title,
the image URL can be known and Downloaded into the local directory.

Then opencv is used to double the size of the comic and sharpen it. It is
then given borders (for aesthetic) and imposed on a nice background. The
background can be changed freely.

Back in the launch script. The desktop background is changed using
gsettings.

### Author

Calvin Stahoviak

UNM School Of Engineering | Computer Science

e: cjstahoviak@gmail.com
