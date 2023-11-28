# Unix Intrusion - unauthorised access to the operating and/or file systems of electronic devices running on a Unix based systems
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
    goto updated_list_of_all_critical_files
    goto have_a_map_of_your_usual_port_activity

def identification():
    goto monitor_unusual_accounts
    goto monitor_unusual_files
    goto monitor_unusual_services
    goto monitor_unusual_network_activity
    goto monitor_unusual_automated_tasks
    goto monitor_unusual_log_entries
    goto monitor_unusual_kernel_log_entries
    goto monitor_file_hashes

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
    goto inspect_network_shared_to_see
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
        goto check_the_integrity_of_the_whole_data_stored_on_the_system

def lessons_learnt():
    goto report
    goto capitalize

