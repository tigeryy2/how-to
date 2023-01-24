# GIT References

General info and references for git.

## Move local repo to a fork after cloning

Steps for changing local repo from clone of remote repo to fork of repo.

1. Fork repo on github
2. In local, rename origin remote to upstream
    1. `git remote rename origin upstream`
3. Add a new origin, your fork on github
    1. `git remote add origin <github_clone_link>`
4. Fetch & push
    1. `git fetch origin`
    2. `git push origin`

See https://gist.github.com/jagregory/710671