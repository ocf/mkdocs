---
title: How to Edit BoD Notes
---

If you have something you want to talk about at BoD, you should note it down on the BoD Notes before the meeting! Here's how to do it:

## Github Web Editor

1. Log into github and go to [github.com/ocf/mkdocs](https://github.com/ocf/mkdocs).
2. Under the name of the repository, open the branches dropdown (under the title of the repository) and then click "View All Branches.
    - If a branch containing the date of the upcoming bod does not yet exist, click "New Branch" and name the new branch "YYYY-MM-DD-bod-notes", then click "Create new branch".
    - If there is already a branch, select it in the dropdown.
3. Navigate to docs/bod/current_year/current_season.
    - If you created a new branch, click "Add file" -> "Create new file" in the top right corner.
        - Name the file YYYY-MM-DD.md
        - Copy the contents from docs/bod/template into the new file.
    - If you're editing the BoD notes on an existing branch, there should already be a file named YYYY-MM-DD.md for you to select. Then, click the pencil icon in the top right corner.
4. Make your additions to the file, then click "Commit changes...", add a short commit message ("add topic to bod notes" is fine), and click "Commit changes".
5. Create a pull request and get it merged!

## CLI

1. `git clone git@github.com:ocf/mkdocs.git`
2. `git checkout -b YYYY-MM-DD-bod-notes` for a new branch or `git switch YYYY-MM-DD` for an existing one
3. `nvim mkdocs/docs/current_year/current_season/YYYY-MM-DD.md`, edit and save
4. `git add --all`
5. `git commit -m "update bod notes"`
6. `git push`
7. Go create a PR for the branch on github, either using GitHub Cli or on the website.

## FAQ
### My branch is out-of-sync with the main branch!

Do steps 1-2 of the CLI guide, then run `git pull`, `git rebase origin/main`, and `git push --force`.
