# Website Defacement - an unauthorised change to the visual appearance of a website or a web page
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
    goto have_up_to_date_schemes
    goto build_a_backup_website_up_and_ready
    goto define_a_procedure_to_redirect_every_visitor
    goto deploy_monitoring_tools
    goto export_the_web_servers_log_files
    goto reference_external_contents
    goto create_a_list_for_each_of_them
    goto be_sure_your_hosting_provider_enforces_policies
    goto make_sure_you_have_an_up-to-date_network_map

def identification():
    goto unusual_channels_of_detecion_are_webpage_monitoring
    goto unusual_channels_of_detecion_are_user
    goto unusual_channels_of_detecion_are_checking_security_with_tools
    goto verify_defacement_and_detect

def containment():
    goto backup_all_data
    goto check_your_network_architecture_map
    goto find_out_how_the_attacker_got_into_the_system
    goto deploy_a_temporary_web_server

def remediation():
    goto remove_all_altered_content
    goto replace_it_with_the_legitimate_content

def recovery():
    goto change_all_user_passwords
    if backup_servers has been used:
        goto restore_the_primary_web_server_component_as_nominal

def lessons_learnt():
    goto communication
    goto report
    goto capitalize

