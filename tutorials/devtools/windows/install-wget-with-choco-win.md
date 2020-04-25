```batch
Microsoft Windows [Version 10.0.18363.778]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Windows\system32>choco install wget
Chocolatey v0.10.15
Installing the following packages:
wget
By installing you accept licenses for the packages.
Progress: Downloading Wget 1.20.3.20190531... 100%

Wget v1.20.3.20190531 [Approved]
wget package files install completed. Performing other installation steps.
The package Wget wants to run 'chocolateyinstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): y

Getting x64 bit zip
Extracting C:\ProgramData\chocolatey\lib\Wget\tools\wget-1.20.3-win64_x64.zip to C:\ProgramData\chocolatey\lib\Wget\tools...
C:\ProgramData\chocolatey\lib\Wget\tools
 ShimGen has successfully created a shim for wget.exe
 The install of wget was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\Wget\tools'

Chocolatey installed 1/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

Did you know the proceeds of Pro (and some proceeds from other
 licensed editions) go into bettering the community infrastructure?
 Your support ensures an active community, keeps Chocolatey tip top,
 plus it nets you some awesome features!
 https://chocolatey.org/compare

C:\Windows\system32>wget
wget: missing URL
Usage: wget [OPTION]... [URL]...

Try `wget --help' for more options.

C:\Windows\system32>
```