# Git/Github Short Notes

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
