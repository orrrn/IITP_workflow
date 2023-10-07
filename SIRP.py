import SOA

playbook_list = ['Initial Access - Drive-by Compromise', 'Initial Access - Exploit Public-Facing Application',
               'Initial Access - Exploitation of Remote Services', 'Initial Access - External Remote Services',
               'Initial Access - Internet Accessible Device', 'Initial Access - Remote Services',
               'Initial Access - Replication Through Removable Media', 'Initial Access - Rogue Mastser',
               'Initial Access - Spearphishing Attachment', 'Initial Access - Supply Chain Compromise',
               'Initial Access - Transient Cyber Asset', 'Initial Access - Wireless Compromise',
               'Execution - Change Operating Mode', 'Execution - Command-Line Interface',
               'Execution - Execution through API', 'Execution - Graphical User Interface', 'Execution - Hooking',
                'Execution - Modify Controller Tasking',
               'Execution - Native API', 'Execution - Scripting',
               'Execution - User Execution', 'Persistence - Hardcoded Credentials', 'Persistence - Modify Program',
               'Persistence - Module Firmware'
               'Persistence - Project File Infection', 'Persistence - System Firmware', 'Persistence - Valid Accounts',
               'Privilege Escalation - Exploitation for Privilege Escalation',
               'Privilege Escalation - Hooking', 'Evasion - Change Operating Mode',
               'Evasion - Exploitation for Evasion', 'Evasion - Indicator Removal on Host',
               'Evasion - Masquerading', 'Evasion - Rootkit', 'Evasion - Spoof Reporting Message',
               'Discovery - Network Connection Enumeration',
               'Discovery - Network Sniffing', 'Discovery - Remote System Discovery',
               'Discovery - Remote System Information Discovery', 'Discovery - Wireless Sniffing',
               'Lateral Movement - Default Credentials', 'Lateral Movement - Exploitation of Remote Services',
               'Lateral Movement - Hardcoded Credentials',
               'Lateral Movement - Lateral Tool Transfer', 'Lateral Movement - Program Download',
               'Lateral Movement - Remote Services', 'Lateral Movement - Valid Accounts',
               'Collection - Adversary-in-the-Middle', 'Collection - Automated Collection',
               'Collection - Data from Information Repositories', 'Collection - Detect Operating Mode',
               'Collection - I/O Image', 'Collection - Monitor Process State', 'Collection - Point&Tag Identification',
               'Collection - Program Upload',
               'Collection - Screen Capture', 'Collection - Wireless Sniffing',
               'Command and Control - Commonly Used Port', 'Command and Control - Connection Proxy',
               'Command and Control - Standard Application Layer Protocol',
               'Inhibit Response Function - Activate Firmware Update Mode',
               'Inhibit Response Function - Alarm Suppression', 'Inhibit Response Function - Block Command Message',
               'Inhibit Response Function - Block Reporting Message', 'Inhibit Response Function - Block Serial COM',
               'Inhibit Response Function - Data Destruction', 'Inhibit Response Function - Denial of Service',
               'Inhibit Response Function - Device Restart/Shutdown',
               'Inhibit Response Function - Manipulate I/O Image', 'Inhibit Response Function - Modify Alarm Settings',
               'Inhibit Response Function - Rootkit',
               'Inhibit Response Function - Service Stop', 'Inhibit Response Function - System Firmware',
               'Impair Process Control - Brute Force I/O', 'Impair Process Control - Modify Parameter',
               'Impair Process Control - Module Firmware', 'Impair Process Control - Spoof Reporting Message',
               'Impair Process Control - Unauthorized Command Message', 'Impact - Damage to Property',
               'Impact - Denial of Control', 'Impact - Denial of View', 'Impact - Loss of Availability',
               'Impact - Loss of Control'
               'Impact - Loss of Productivity and Revenue', 'Impact - Loss of Protection', 'Impact - Loss of Safety',
               'Impact - Loss of View',
               'Impact - Manipulation of Control', 'Impact - Manipulation of View',
               'Impact - Theft of Operational Information']

def sirp_generate_playbook():
    print("generate_playbook")
    sirp_add_playbook()


def sirp_add_playbook():
    print("add new playbook at playbook list")
    # add new playbook at playbook[] list


def sirp_match_playbook(case):
    print("maching playbooks...")

    # maching playbook lists using for(iterate)

    for i in playbook_list:
        if case[1] == i:
            case[3] = 1 # playbook exists and set classification available
            break
        else:
            case[3] = 0 # playbook does not exists and set classification unavailable

    # maching playbook lists

    return case

def sirp_play_playbook(case):
    print("play this playbook..")
    # finding playbook
    playbook = None
    isworked = 1 # if isworked is 1 means response using playbook is worked, or not is 0

    result = [case, playbook, isworked]

    return result[case, playbook]



def sirp_check_isplaybook_can_improve(case): #check is playbook can be improve for response accident
    result = SOA.soa_analyzing_more_AV(case)