# Building a Full-Stack Application with React and Django
A guide to building a full-stack application using the popular JavaScript library React and the Python web framework Django. Through hands-on practice and expert guidance, participants will learn the fundamentals of both technologies and gain the skills necessary to create modern, dynamic web applications.

## Setting up the developer environment
Since we will be using the Linux platform, anyone who wants to code along needs to install either WSL or GitBash if they are using Windows OS. Otherwise, if you are using MacOS or any Unix base OS you are set.

### GitBash
Installing GitBash is quick and fast, below is the download link and instructions on how to install
Visit [this link](https://code.visualstudio.com/download) and download the one for Windows 

### WSL
This installation needs more time to set up because it might require you to change some bios settings of your machine. 
Use [this link](https://github.com/nvm-sh/nvm#:~:text=windows%20WSL.-,Installing%20and%20Updating,-Install%20%26%20Update%20Script) to do the installation.

> Note: You only need to install one of the above and only if you are using Windows OS

Setting up IDE
We recommend using Visual Studio Code as your IDE.
Download and install it from [here](https://code.visualstudio.com/download).


## Frontend Development Environment
To prepare for the frontend Dev Environment you need to install the following
Node Version Manager(nvm)
Download and installation instructions from [here](https://github.com/nvm-sh/nvm) 
Once that is installed, use it to install NodeJs version 16.20.2 or v18.19.0 using the following command
``` 
nvm install v18.19.0
```
	
##Backend Development Environment
We will be  using Python Django Framework for our backend development so, we need to install python3.10.8
Before installing, first confirm if it is already installed using this command

```
python3 –version

// Outputs
// Python 3.10.x
```

If you do not see the output outlined in the code block above, it means you do not have Python installed and so,you need to install it.
```
Installing Python

sudo apt update -y \
sudo apt install software-properties-common \
sudo add-apt-repository ppa:deadsnakes/ppa \
sudo apt update \
sudo apt install python3.10.2

//confirm if it is installed
python3 --version

// Outputs
// Python 3.10.x 
```

Installing PIP for managing Python packages
Python uses pip to manage packages like Django, Django Rest which we will be using for our backend.

```
sudo apt install python3-pip
```


