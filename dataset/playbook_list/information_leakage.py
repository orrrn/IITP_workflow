# Information Leakage - unintended loss of information from an organization. This usually  occurs as a result of employees passing information to others  sometimes unwittingly sometimes wittingly
# In IRM Playbook
# Written in Sudocode

def main():
    preparation()
    identification()
    containment()
    remediation()
    recovery()
    lessons_learnt()

def preparation():
    goto contacts
    goto securtiy_policy

def identification():
    #step1: detect the issue
    goto incident_notification_process
    goto public_monitoring_tool
    goto DLP_tool

    #step2: confirm the issue
    goto e_mail
    goto browsing
    goto external_storage_devices
    goto local_files
    goto network_transfer
    goto printer
    goto malware



def containment():
    goto notify_the_management
    goto block_the_access_to_the_disclosure_URI
    goto suspend_the_logical_and_physical_credentials_of_the_insider
    goto isolate_the_computing_system

def remediation():
    if data has been sent to public_servers:
        goto ask_the_owner_to_remove_the_disclosed_data
    
    if not possilbe to remove_the_disclosed_data:
        goto provide_a_complete_analysis_to_the_PR_team_and_management
    
    goto monitor_leaked_documents_spread_on_websites_and_social_networks
    goto provide_the_elements_to_HR_team

def recovery():
    if systesm has been compromised:
        goto restore_it
    goto warn_your_employee_or_some_local_teams
    if situation comes basck to normal:
        goto remove_the_official_communication

def lessons_learnt():
    goto report
    goto capitalize