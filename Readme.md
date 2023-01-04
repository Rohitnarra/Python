This folder consists of Python scripts pushed to a repo named Python in Git, the Python repository has 2 branches : main and Feature branch. the changes made in main branch is merged in Feature branch and is shown in this exercise.
This project is about creating a repository, pushing an existing folder into that git repository, creating a new branch, making changes in the folder, and committing those changes in the new branch feature created previously, the next step would be to merge the feature branch with the main defualt branch, by doing so all the changes done in the feature branch will be synced with main branch, and by pushing all changes from main branch there will be sucessful push of all new changes committed in Feature.
Using git merge, several commit sequences will be integrated into a single, unified history. Git merge is most commonly used to join two branches. In the examples that follow, this article will stress the branch merging pattern. Git merge will seek for a common base commit between two commit points, often the branch tips, in these instances. When Git identifies a shared base commit, it will create a new "merge commit" that combines the modifications of each pending merge commit sequence.
![IAC_assignment2_pushed_readme_changes_to_main_branch](https://user-images.githubusercontent.com/121063728/210657260-bf53d679-8b2e-4ee4-aca3-f1273c55783c.png)
In their git repository, the programmer generally keeps a pristine master branch. They then create a copy of the master branch where they may retain their most current code modifications, fix any mistakes, commit the changes, and do a variety of additional tasks. This strategy includes just branching in the git structure. Users can use the git Branch command to create, remove, list, and rename branches. Branching is one of git's newest features for managing code version control. It shows the most recent version of your code without making any changes to the master branch.
In this project, we constructed a python repository and incorporated the exercise folders from weeks 1-9. We need to build one git repository entitled Python, and this python repo will only have one default branch named main. Commit the folders and all files included within them; we use the command git init to initialize git in the folder where the project is to be pushed. After git init, we can use git add to add the contents of the folder to the git repo, git commit to commit all the files to the git repository, and lastly push the folder contents to the git repository, which will automatically push the folder to the main branch. The picture below depicts the pushed Python repository.
![IAC_assignment2_Python_repo_created_and_pushed](https://user-images.githubusercontent.com/121063728/210655658-467e7f35-ad43-4f58-aad9-91b57212f114.png)
Branch Feature must be formed, and to change the branch, we use the git checkout command, which changes the branch to whatever branch is created and supplied. Branch creation may be accomplished with git branch -b branch name (Feature). After creating the branch, use the checkout command to change it from the default main branch, and then add and commit the modifications made in the folder repo. To merge the changes made in the Feature branch, use the command git merge -b Feature. This will combine the changes made in the Feature branch with the main branch, and the main branch will be synchronized with the Feature branch. Finally, we may push it. The graphic below depicts the construction of the Feature branch.
