# sbuClassEnsurer
a python script for checking class availbility

<h3>this program will check availbilites of classes by class number you put on classes.txt file every 5 min(it can be modified by changing the number in time.sleep() in the very last part of classEnsurer.py) and send you a email reminder if any of them are available.</h3>

this script is developed under python3.7.2, any python version newer than 3.2 should be working

<h3>you will need to install beautifulsoup for running this script
<code>pip3 install beautifulsoup4<code>   </h3>

<h4>check this page https://myaccount.google.com/security to turn on the less secure app access for gmail(otherwise you may experience a hard time to get the server connected)</h4>


put the classes number you want to check on <h5>classes.txt</h5> <br>
spliting them by new line<br>
(you can find class number on our school's official class finder page
http://classfind.stonybrook.edu/vufind/ )


hard code your gmail address,password and receivers' email address on the <h5>classEnsurer.py </h5>file





I coded this script in a rush, 4 sure there'll be many unexpecting bugs. It will get more features such as gui, email support other than gmail and packed executable file if ppl find this is useful.
