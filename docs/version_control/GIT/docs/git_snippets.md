# Git Snippets

## Multiple Git Repositories Download

```GHUSER=ronakr14; curl "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | xargs -L1 git clone```

** change GHUSER to user from where you want to download the repositories.

## Set VSCode as Git Default editor

```git config --global core.editor "code --wait"```

## Set your file compatible for windows and linux.(for windows user)

```git config --global core.autocrlf true```
```git config --global core.autocrlf input```