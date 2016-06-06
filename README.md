# Flask-Git [Work in Progress]
A simple site to manage git repositories.  

## Problem
I frequently switch between machines during the production of software, which can lead to me pushing commits before theyre mature simply so I can grab the updates on another machine. I'd like a solution to where I can push commits to an intermediatary repository, where I can "squash" all the half-commits into a sensible one before committing to a public repository.  
This could also be useful when developing in a team where you don't want to make public code until it is fully baked, but need versioning on the interim period.  

## Goals
Create a lightweight site to use locally (i.e. to run on a local network Raspberry Pi) to manage several git repositories.  
* List current projects  
* Show recent commits
* "squash" commits
* Push to GitHub
* Pull from GitHub (or maybe highlight it's out of sync?)

## References
A list of handy libraries...
* [GitPython](http://gitpython.readthedocs.io/en/stable/)
* [GitHub-Flask](https://github-flask.readthedocs.io/en/latest/)
