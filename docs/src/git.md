# Git/Github Short Notes

Basic commands to get start working with git and github and pulling or pishing changes.

## Configuring Git and Github

**Step 1**: **Setup Git**

For Git to work properly, we need to let it know who we are so that it can link a local Git user (you) to GitHub. When working on a team, this allows people to see what you have committed and who committed each line of code.

The commands below will configure Git. Be sure to enter your own information inside the quotes (but include the quotation marks)!

```git
git config --global user.name "Your Name"
git config --global user.email "yourname@example.com"
```

GitHub recently changed the default branch on new repositories from *master* to *main*. Change the default branch for Git using this command:

```git
git config --global init.defaultBranch main
```

To enable colorful output with `git`, type:

```git
git config --global color.ui auto
```

To verify that things are working properly, enter these commands and verify whether the output matches your name and email address.

```git
git config --get user.name
git config --get user.email
```

**Step 2: Create a Github Account or sign-in**

Go to [GitHub](https://github.com) and create an account! If you already have an account, sign in. You do not need to use the same email address you used before, but it might be a good idea to use the same one to keep things simple.

**Step 3: Create a SSH Key**

An SSH key is a cryptographically secure identifier. It’s like a really long password used to identify your machine. GitHub uses SSH keys to allow you to upload to your repository without having to type in your username and password every time.

First, we need to see if you have an Ed25519 algorithm SSH key already installed. Type this into the terminal and check the output with the information below:

```bash
ls ~/.ssh/id_ed25519.pub
```

If a message appears in the console containing the text “No such file or directory”, then you do not yet have an Ed25519 SSH key, and you will need to create one. If no such message has appeared in the console output, you can proceed to *Step 4*.

To create a new SSH key, run the following command inside your terminal. The -C flag followed by your email address ensures that GitHub knows who you are.

**Note:** The angle brackets (`< >`) in the code snippet below indicate that you should replace that part of the command with the appropriate information. Do not include the brackets themselves in your command. For example, if your email address is `johndoe@gmail.com`, then you would type `ssh-keygen -t ed25519 -C johndoe@gmail.com`.

```bash
ssh-keygen -t ed25519 -C <youremail>
```

- When it prompts you for a location to save the generated key, just push `Enter`.
- Next, it will ask you for a password; enter one if you wish, but it’s not required.

**Step 4: Link your SSH key with GitHub**

Now, you need to tell GitHub what your SSH key is so that you can push your code without typing in a password every time.

First, you’ll navigate to where GitHub receives our SSH key. Log into GitHub and click on your profile picture in the top right corner. Then, click on `Settings` in the drop-down menu.

Next, on the left-hand side, click `SSH and GPG keys`. Then, click the green button in the top right corner that says `New SSH Key`. Name your key something that is descriptive enough for you to remember where it came from. Leave this window open while you do the next steps.


Now you need to copy your public SSH key. To do this, we’re going to use a command called *cat* to read the file to the console. (Note that the `.pub` file extension is important in this case.)

```bash
cat ~/.ssh/id_ed25519.pub
```

Highlight and copy the output, which starts with `ssh-ed25519` and ends with your email address.

Now, go back to GitHub in your browser window and paste the key you copied into the key field. Then, click `Add SSH key`. You’re done! You’ve successfully added your SSH key!

**Step 5: Testing your key**

Follow the directions in [this article from GitHub](https://help.github.com/en/articles/testing-your-ssh-connection) to verify your SSH connection *(Don’t forget to omit the `$` when you copy and paste the code!).* You should see this response in your terminal: Hi username! You’ve successfully authenticated, but GitHub does not provide shell access. Don’t let GitHub’s lack of providing shell access trouble you. If you see this message, you’ve successfully added your SSH key and you can move on.

Done, you have setted up `git` and `github`. Congratulations!!

___


# Git/Github Basic Commands

**Initialiasing a repo**

```git
git init
```

**Add files/folders to repo**

```git
git add . #for all files and folders
git add <file> #for a specific file
```

**Commit**

```git
git commit -m "Commit message"
```

**Push changes to remote repo**

## Using HTTP

1. Add remote repo location

```git
git remote add origin https://github.com/<username>/<repo_name>
```
2. Push changes

```git
git push origin <branch_name>

Username: xxxxxx
Password: xxxxxx
```

**Pull changes/updates**

```git
git pull origin <branch_name>
```

> Using passwords for pushing changes is depreciated use a PAT i.e Personal Access Token in place of password.


## Using SSH

1. Clone repo

```git
git clone git@github.com:USERNAME/REPO_NAME
```

1. Add changes

```git
git add .
git commit -m "Updated repo"
```

1. Push Changes

```git
git push
```

> It'll only work if you have setted up your SSH key.
