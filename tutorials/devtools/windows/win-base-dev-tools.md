# Windows Developer tools for seamless developing on different OS.

Sometime we are required to work on different OS.
However when Mac OS and Linux have a lot similarities,
not all the things are compatible (brew vs apt).

In case of windows there are much more different things, then *nix.

We will pick the robust ones that will provide enough level of abstration
to treat windows differently in very small amount of places
and provide general way to develop cross platform.

## Minimal Toolbox

Basic Linux Style development on Windows. PATH, cmderr, conda, vscode

### Package Manager
First thing we need to to be able to install basic things
without need to click on link and download and run installers.
Windows have it's own package manager called [choco](https://chocolatey.org/).

> Installation

```powershell
# Run in Administrator mode in powershell. Details: https://chocolatey.org/install
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

> Usage

We will obviously need wget, so lets install it:
```cmd
; Run in Administrator mode in cmd
choco install wget
```

> Install output: [install-wget-with-choco-win.md](./install-wget-with-choco-win.md)


### Console Emulator
When we want to work on windows in similar way as *nix,
we first of all meaning cli based approach.
When we can use same `ls -1 | grep _build_ | xargs -n 1 -P4 -I {} xargs czvf _pack/{}.tar.gz {}`
one liners as we use to in bash(zsh).

There are couple solutions for that on windows.
Such as cygwin, migwin, git tools, conemu, cmder.
We would like to propose using of cmder for such porpuse,
since it's build on top other tools and provide very solid linux cli experience,
while still running on real windows (not vm/docker/wsl).

> Installation

**just use choco**

```batch
; In Admin CMD
choco install cmder
```

Also, you can install it manually from site https://cmder.net/ 
or `wget https://github.com/cmderdev/cmder/releases/download/v1.3.14/cmder.zip`,
unpack to $HOME/Apps, create shortcut to cmderr app.

### Python Version and Venv Managment System
When windows involved in devopment cycle the best solution for 
management of python versions and virtual environments is conda.
it can be installed usig choco

**just use choco**

```batch
; In Admin CMD
choco install miniconda3
```

Or download from site: https://docs.conda.io/en/latest/miniconda.html 
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe`

> After Installation

Currently I prefer to setup python 3.6 as default interpreter

```
conda install python=3.6
```

### Editor
VS Code is the best cross platform multi build chain editor,
which supports a lot of languages and remote development:
```batch
choco install vscode
```

## My Basic Crossplatform tools:
To be able to create multi os build pipelines we need level
of file system abstraction and shell abstraction (executor).
To overcome path issues and absence of bash in windows,
we propose to create automations and binary artifacts management
with next tools:

> (task)[https://taskfile.dev/#/installation]

download from https://github.com/go-task/task/releases
unarchive and to to C:\Windows\system32

> (minio)[https://min.io/download]

```batch
choco install minio-server
choco install minio-client
```

## Advanced Windows Isolation tools
- WSL
- Migwin
- docker win(Win Pro)
- docker win(Home VirtualBox + docker machine)
- microk8s (pro, native k8s on vm)

### Develop in docker on windows HOME

> Requiremetns

- VirtualBox
- DockerToolbox-19.03.1

Pros: No need for pro
Cons: Too much stuff to install, Slow and Terrible sharing

### Develop in WSL

> Requrments

- WSL

Pros: Fast, real linux
Cons: dockers only in wsl2 on Pro.