import os, platform

def install_linkfinder():
    if os.geteuid() != 0:
        print("Please run this script with root privileges.")
        exit(1)

    directory = "/usr/share/ihaahi"
    if not os.path.exists(directory):
        os.system("mkdir {}".format(directory))
    
    os.system("mkdir /usr/share/ihaahi/LinkFinder")
    os.system("mv linkfinder /usr/share/ihaahi/LinkFinder")

    with open("/usr/local/bin/linkfinder", "w") as wrt:
        wrt.write("#!/bin/bash\n")
        wrt.write('all=""\n')
        wrt.write('for arg in "$@"; do\n')
        wrt.write('     all=$all$arg" "\n')
        wrt.write('done')
    
    os.system("chmod +x /usr/local/bin/linkfinder")

    print("linkfinder installed successfully.")
    print("type 'linkfinder' to use this tool")

def Main():
    os_system = platform.system()

    if os_system == "Linux":
        install_linkfinder()
    else:
        print("type 'python3 linkfinder' to use this tool")