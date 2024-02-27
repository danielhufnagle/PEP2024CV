# Guide to Setting Up Your Anaconda Environment
### What and Why
Trust me when I say you want this. Anaconda environments allow you to have a separate isolated environment for each and every project.
Hopefully this is convincing enough. Idk.
### Installing Anaconda
[Installation Guide](https://docs.anaconda.com/free/anaconda/install/index.html)
- *Hopefully this will make the installation process a little less painful*
### Creating Our Environment
I'm actually cheating when I do this. Sorry.
to create your environment, open a terminal and copy this command
```
conda create -n pep python=3.8
```
this will create a new conda environment called pep that is using python 3.8
now, let's activate this environment:
```
conda activate pep
```
so we should now be in the pep environmemnt
To actually install all of our packages, we are going to have to go into the `PEP2024CV` directory and type in the following command:
```
pip install -r packagelist.txt
```
this should install all of the packages in packagelist.txt
### If you install any new packages
when you next commit make sure to update the packagelist.txt file by typing in
```
pip freeze > packagelist.txt
```
this will updtae the packagelist.txt file that we use to install all of our packages
### Getting the hell out of here
to leave this environment (and go back to the base environment)
```
conda deactivate
```

