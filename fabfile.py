from fabric.api import *
filename = input("Enter the File Path: ")
for line in open(filename,'r').readlines():
    host,pasw = line.split()
    env.host.append(host)
    env.passwords[host] =passw

def run_command(command):
    try:
        with hide('running','stdout','stderr'):
            if command.strip()[0:5] == "sudo":
                results = sudo(command)
            else:
                results = run(command)
    except:
        results = 'Error'
    return results

def check_host():
    for host,results in execute(run_command,"uptime",host=env.host).iteritems():
        running_hosts[host] = results if result.succeded else "HOST DOWN"

def get_hosts():
    selected_hosts = []
    for host in input("Hosts (eg: 0,1): ").split():
        selected_hosts.append(env.hosts[int(host)])
    return selected_hosts

def menu():
    for num,desc in enumerate(["List Hosts","Run Command","Open Shell","Exit"]):
        print("["+ str(num)+"]"+desc)
        choice = int(input('\n'+PROMPT))
        while (choice !=3):
            list_hosts()
            if choice==1:
                cmd = input("Command: ")
                for host,result in execute(run_command,cmd,hosts = get_host()).iteritems():
                    print("["+host+"]:"+ cmd)
                    print('-'*80+'\n'+result+'\n')
            elif choice==2:
                host = int(input("Host:"))
                execute(open_shell,host = env.hosts[host])
            for num,desc in enumerate(["List Hosts","Run Command","Open Shell","exit"]):
                print("["+str(num)+"] "+desc)
            choice = int(input('\n'+PROMPT))

if __name__ =="__main__":
    fill_host()
    check_host()
    menu()
                
