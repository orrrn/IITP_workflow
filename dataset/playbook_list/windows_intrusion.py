# Windows Intrusion - unauthorised access to the operating and/or file systems of electronic devices running on windows
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
    goto file_on_a_secure_place_describing_the_usual_port_activity
    goto ask_a_Windows_expert_for_their_assistance

def identification():
    goto monitor_unusual_accounts
    goto monitor_unusual_files
    goto monitor_unusual_registry_entries
    goto monitor_unusual_process_and_services
    goto monitor_look_for_unusual_and_unexpected_network_services_installed_and_started
    goto monitor_unusual_network_activity
    goto monitor_unusual_automated_tasks
    goto monitor_unusual_log_entires
    goto monitor_unusual_rootkit_check
    goto monitor_unusual_malware_check
    
def containment():
    if machine is considered ciritical_for_your_companys_businesses_activity & cannot be disconnected :
        goto backup_all_information_data
    
    goto make_a_copy_of_the_systems_memory_for_further_analysis

    if machine is not onsidered ciritical_for_your_companys_businesses_activity & can be disconnected :
        goto shut_the_machine_down_the_hard_way
    
    goto make_a_physical_copy
    goto find_all_files_used_by_the_attacker
    goto check_all_files_assssed_recently
    goto check_log_files
    goto find_how_the_attacker_got_into_the_system
    goto apply_fixes_when_applicable

def remediation():
    goto temporary_remove_all_accesses
    goto remove_all_malicious_files

def recovery():
    goto reinstall_the_system_fully_from_original_media
    goto apply_all_fixes_to_the_newly_installed_system

    if the solution cannot be applied:
        goto change_all_the_systems_accounts_passwords
        goto restore_all_files

def lessons_learnt():
    goto report
    goto capitalize

