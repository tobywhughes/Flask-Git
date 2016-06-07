# Flask-Git [Work in Progress [<img src="https://icons.duckduckgo.com/ip2/waffle.io.ico">](https://waffle.io/NixonInnes/Flask-Git)]
A simple site to manage git repositories.  




## Problem
I frequently switch between machines during the production of software, which can lead to me pushing commits before theyre mature simply so I can grab the updates on another machine. I'd like a solution to where I can push commits to an intermediatary repository, where I can "squash" all the half-commits into a sensible one before committing to a public repository.  
This could also be useful when developing in a team where you don't want to make code public until it is fully baked, but need versioning on the interim period.  

## Goals
Create a lightweight site to use locally (i.e. to run on a local network Raspberry Pi) to manage several git repositories.  
* List current projects  
* Show recent commits
* "squash" commits (rebase)
* Push to GitHub 
* Pull from GitHub (or maybe highlight it's out of sync?)

## Getting Involved
This project is part of the June '16 [DevHack](https://github.com/devolio-devchat/devhack) competition. Please check it out!  
If you would like to get involved, please check the [DevHack website](https://github.com/devolio-devchat/devhack). You can find me in the [Slack](http://devchat.devolio.net/) under `@nixoninnes`, usually skulking around `#python` or `#devhack`.  
If you are already a part of the [DevHack](https://github.com/devolio-devchat/devhack) then please see the [Waffle Board](https://waffle.io/NixonInnes/Flask-Git) to see where you can help out.  
Please feel free to get in touch on [Slack](http://devchat.devolio.net/) or [drop me a line](mailto://nixoninnes@echonet.com).

## References
A list of handy libraries...
* [GitPython](http://gitpython.readthedocs.io/en/stable/)
* [GitHub-Flask](https://github-flask.readthedocs.io/en/latest/)
