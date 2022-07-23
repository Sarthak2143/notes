# Basic Linux commands

## ls

```bash
# list all files
ls

# list all hidden files and perms
ls -la

# list files with perms
ll

# list hidden files with perms
ll -a
```

## grep

```bash
# pattern matching in a file with a string(caps matters)
cat file.txt | grep password

Output:
password1234
hard_password
password

# same case for only "password"
cat file.txt | grep "password"

Output: 
password

# same case but with no caps matters
cat file.txt | grep -i password

Output:
Password
password
pASSword

# exclude multiple strings
cat file.txt | grep -Ev 'string1 | string2'

```

## curl

```bash
# make http, http2 and http3 requests with curl
curl -vv http://10.10.10.10
curl --http2 http://10.10.10.10
curl --http3 http://10.10.10.10

# obtain only the response header
curl --head http://10.10.10.10

# upload files with curl
curl --user "{user}:{creds}" --upload-file=<file_path> "http://10.10.10.10/upload_location"

#save the output
curl http://10.10.10.10 -o index.html
```

## wget

```bash
# download file with wget
wget http://10.10.10.10/xxx.xxx

# run files without downloading
wget -O - http://10.10.10.11:<port_no>:lin(peas\|enum).sh
```
**Important Note**

While, downloading a file `wget` provides metadata but `curl` does not.

## sed

```bash
# search and replace strings
cat username.txt | sed s/{stringToBeChanged}/{replacementString}/g

# replace the last ',' with a null character
cat usernames.txt | sed s/,$//

# add \x after every two characters, the .. denotes the two characters, \x&, adds \x and & doesnt delete the characters that were before
cat hexpayload.txt | sed 's/../\\x&/g'

# replace something in a file, replace the last occurance of , in the intel_update.log file ( in each line)
sed -i 's/,$/\]/' intel_update.log

# replace only the last occurance of , at the end of the line in the end of the file ( make changes only in the last line)
# the $ before s/,$/\]/ metions the last line of the file
sed -i '$ s/,$/\]/' intel_update.log

# delete empty lines in a file
cat test.txt | sed -r '/^\s*$/d'

# use -i when a modification needs to be done on the file
# use -r when the modification has to be done on the output alone
```

## find

```bash
# find with file names
find . -name user.txt 

# find and execute
find . -name '*.txt' -exec cat "{}" \;

# {} is used as the place holder and tells the follwing to as an argument
# find directories with the specified name and execute the command
find . -type d -name uploads -exec rm -rf "{}" ';'

# find and copy files 
find -name 'file.ext' -exec cp "{}" <copy_path>  \;

# find the recently modified files
# maxdepth - sub directories, newermt - timestamp
find . -maxdepth 1 -newermt "2016-02-28"

# find files with specific string in it
find . -type f -print0 | xargs -0 -e grep -niH -e "your common word to search"
```

## Compressing and Decompressing

```bash
# zip a folder with its contents
zip -r -9 html.zip /var/www/html

# unzip a zip file
unzip html.zip

# tar a file
tar cvf html.tar html/

# extract a .tar file
tar -xvf html.tar 

# tar.gz a folder
tar cvfz html.tar.gz html/

# unzip a *.tar.gz file
tar -xzvf html.tar.gz

# unzip rar file
unrar x html.rar
```
