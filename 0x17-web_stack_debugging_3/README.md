# Alx System Engineering (Devops)

## Projects
### [0x00-shell_basics](./0x00-shell_basics)
| Filename | Description | Command |
| -------- |:-----------:| -------:|
| 0-current_working_directory prints the current path |
| 1-listit | Prints the content of the curremt working directory | ls |
| 2-bring_me_home | Send the user to home | cd ~ |
| 3-listfiles | Prints pwd files in long format | ls -l |
| 4-listmorefiles | Lists files in the long format, including hidden ones | ls -a |
| 5-listfilesdigitonly | Lists the files with group id displayed numerically | ls -an |
| 6-firstdirectory | Creates a directory in the specified folder | mkdir |
| 7-movethatfile | Moves betty like a gentleman | mv |
| 8-firstdelete | Deletes a file from a location | rm |
| 9-firstdirdeletion | Deletes a folder | rmdir |
| 10-back | Goes to the previous directory | cd .. |
| 11-lists | Gives files in root and /boot | ls -al |
| 12-filetype | Checks the kind of file iamafile is | file |
| 13-symbolic_link | Directs to another file at specified location | ln -s |
| 14-copy_html | Copies html files using wildcards | * |

---------------------------------------------------------------

### [0x01-shell_permissions](./0x01-shell_permissions)
Using shell executeables to perform commands
| Filename | Command |
| -------- | -------:|
| 0-iam_betty | su |
| 100-change_owner_and_group | chown -R |
| 101-symbolic_link_permissions | chown -h |
| 102-if_only | chown |
| 103-Star_Wars | telnet |
| 10-mirror_permissions | chmod |
| 11-directories_permissions | chmod -R |
| 12-directory_permissions | chmod - R |
| 13-change_group | chgrp |
| 1-who_am_i | whoami |
| 2-groups | groups |
| 3-new_owner | chown |
| 4-empty | touch |
| 5-execute | chmod |
| 6-multiple_permissions | chmod nnn |
| 7-everybody | chmod ugo+x |
| 8-James_Bond | chmod 007 |
| 9-John_Doe | chmod 753 |

-------------------------------------------------------------

### [0x02-shell_redirections](./0x02-shell_redirections)
Using shell commands to display and manipulate files
##### Related COmmands
- echo "Hello, World"
- find . -empty|rev|cut -d "/" -f 1|rev
- find . -type f -name "*.gif"  -printf '%f\n' | rev | cut --complement -d . -f 1 | rev | LC_ALL=C sort -f
- echo $(cut -c 1 |tr -d '\n')
- tail -n +2 | cut -f 1 | sort | uniq -c | sort -nrk 1 | rev | cut -d " " -f 1 | rev | head -n 11
- find -mindepth 0 -type f -name "*.js"  -delete
- find . -mindepth 1 -type d | wc -l
- ls -1t | head
- sort | uniq -u
- grep root /etc/passwd
- grep bin /etc/passwd | wc -l
- grep -A 3 root /etc/passwd
- grep -v bin /etc/passwd
- grep -i ^[[:alpha:]] /etc/ssh/sshd_config
- tr A Z|tr c e
- echo "\"(Ôo)'"
- tr -d c|tr -d C
- rev
- cut -d ":" -f 1,6 /etc/passwd |sort -d
- cat /etc/passwd
- cat /etc/passwd /etc/hosts
- tail /etc/passwd
- head /etc/passwd
- cat iacta | head -3 | tail -1
- echo "Best School" > \\\*\\\\\'\"Best\ School\"\\\'\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)
- ls -la > ls_cwd_content
- tail -1 iacta>> iacta

-------------------------------------------------------------------------------

### [0x03-shell_variables_expansions](./0x03-shell_variables_expansions)
Using global and local variables
##### Related Commands
- alias ls="rm *"
- echo $(printf "%x" $DECIMAL)
- tr 'a-zA-Z' 'n-za-mN-ZA-N'
- paste -d, - - | cut -d, -f1
- echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol')
- echo $((($BREATH)**($LOVE)))
- echo $((2#$BINARY))
- echo {a..z}{a..z}|tr " " "\n"|grep -v "oo"
- echo $(printf "%.2f" $NUM)
- echo hello $USER
- PATH="$PATH:/action"
- echo $PATH|tr ':' '\n'|wc -l
- printenv
- set
- BEST="School"
- export BEST="School"
- echo $((($TRUEKNOWLEDGE)+128))
- echo $((($POWER)/($DIVIDE)))
