import os;
import requests;

current_version = "Version 1.5.0"
r = requests.get('https://github.com/MattPlayGamez/shutdown/blob/main/version.txt', allow_redirects=True)
insertversion = open('version.txt', 'wb').write(r.content)
version = open('version.txt', 'r').read()
print('You\'re version: ' + current_version )
print('Latest version: ' + version)
if current_version == version:
     os.system('del version.txt')
     os.system('shutdown /p')
     os._exit(1)
    
os.system("PowerShell -Command \"Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'PLEASE UPDATE TO THE LATEST VERSION OF SHUTDOWN\', 'update Shutdown')\"")
ok = os.system("PowerShell -Command \"Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show(\'go to https://github.com/MattPlayGamez/shutdown/ to find the latest release\', 'URL for updating')\"")
os.system('del version.txt')
