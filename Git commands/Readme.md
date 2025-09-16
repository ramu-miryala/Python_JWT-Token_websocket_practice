## Git Commands

## Initialize a Git Repository
Command:
git init


**When to Use:**

At the start of a new project to create a local Git repository.

**Why:**

To start tracking changes in your project files.

**Check Status**
Command:
git status


**When to Use:**

To view changes that have been staged, modified, or are untracked.

**Why:**

To know which files are ready to be committed and which aren’t.

 ## Add Files to Staging 
Command:
git add <file-name>


Or add all files:

git add .


**When to Use:**

Before committing changes, add files to the staging area.

**Why:**

To prepare specific files or all modified files for commit.

 **Commit Changes**
Command:
git commit -m "Your commit message"


**When to Use:**

After staging files, commit the changes to the local repository.

**Why:**

To record snapshots of your project history with descriptive messages.

### Set Remote Repository
Command:
git remote add origin <repository-url>


▶️ When to Use:

To link your local repository to a remote repository (e.g., GitHub).

▶️ Why:

To push your local changes to a remote server.

## Push Changes to Remote
Command:
git push origin <branch-name>


▶️ When to Use:

After committing locally, push changes to the remote repository.

▶️ Why:

To share code with others and keep the remote repo updated.

## Clone a Repository
Command:
git clone <repository-url>


▶️ When to Use:

To copy an existing remote repository to your local machine.

▶️ Why:

To start working on an existing project.

## Pull Latest Changes
Command:
git pull origin <branch-name>


▶️ When to Use:

To fetch and merge changes from the remote repository.

▶️ Why:

To keep your local repository up to date with the latest code from others.

## Create a New Branch
Command:
git branch <branch-name>


▶️ When to Use:

To work on new features or experiments without affecting the main code.

▶️ Why:

For better organization and safe parallel development.

## Switch Branches
Command:
git checkout <branch-name>


▶️ When to Use:

To move between branches.

▶️ Why:

To work on different features or fixes.

## Merge Branches
Command:
git merge <branch-name>


▶️ When to Use:

After finishing work on a branch, merge it into the main branch.

▶️ Why:

To integrate feature work into the main project.

## View Commit History
Command:
git log


▶️ When to Use:

To see the history of commits with details like author, date, and message.

▶️ Why:

To track changes and debug when needed.

## Revert Changes (Unstaged)
Command:
git checkout -- <file-name>


▶️ When to Use:

To discard local changes in a file before committing.

▶️ Why:

To restore the file to its last committed state.

## Delete a Branch
Command:
git branch -d <branch-name>


▶️ When to Use:

After merging, delete feature branches to keep the repo clean.

▶️ Why:

To remove unnecessary branches.

## Stash Changes
Command:
git stash


▶️ When to Use:

To temporarily save changes without committing.

▶️ Why:

To switch branches without committing incomplete work.

### Typical Workflow Example

git init → Start repo

Edit files → git add . → git commit -m "Initial commit"

git remote add origin <URL> → Link to remote

git push origin master → Upload code

git pull origin master → Sync changes

Create branch → git checkout -b feature → Work → git commit → git checkout master → git merge feature → git push