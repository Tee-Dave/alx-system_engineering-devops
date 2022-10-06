#Various scripts in shell basics task:
'pwd' prints the absolute path name of the current working directory.

'ls' displays the contents list of your current directory.

'cd ~' changes the working directory to the user’s home directory.

'ls -l' displays current directory contents in a long format.

'ls -la' displays current directory contents, including hidden files (starting with .) using the long format. 

'ls -l -la' displays current directory contents in Long formatwith user and group IDs displayed numerically

and hidden files (starting with .) .

'mkdir /tmp/my_first_directory' creates a directory named my_first_directory in the /tmp/ directory.

'mv /tmp/betty /tmp/my_first_directory' moves the file betty from /tmp/ to /tmp/my_first_directory.

'rm -rf /tmp/my_first_directory/betty' deletes the file betty in /tmp/my_first_directory. 

'rm -rf /tmp/my_first_directory' deletes the directory my_first_directory that is in the /tmp directory.

'cd -' changes the working directory to the previous one.

'ls -la . .. /boot' lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

'file /tmp/iamafile' prints the type of the file named iamafile in the /tmp directory.

'ln -s /bon/ls __ls__' create a symbolic link to /bin/ls, named __ls__ in the current working directory.

'cp -u *.html ..' copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

'mv [{:upper:}]* /tmp/u' moves all files beginning with an uppercase letter to the directory /tmp/u.

'rm *~'  deletes all files in the current working directory that end with the character ~.

'mkdir -p welcome/to/school' creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

'ls -map | sort -d' lists all the files and directories of the current directory, separated by commas (,) with directory names ending with a slash (/), files and directories starting with a dot (.) listed the listing is alpha ordered, except for the directories . and .. which are listed at the very beginning, only digits and letters are used to sort; digits come first.

'file -C -m school.mgc' detects School data files.  
