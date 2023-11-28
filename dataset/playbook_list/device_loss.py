# In responding to a lost or stolen device incident
# In Incident Reponse Playbook from FRESCURE
# Written in Sudocode



def main():
    #preparation
    goto determine_the_memebers_of_the_CSIRT
    goto determine_the_extended_CSIRT_members
    goto define_escalation_paths
    goto determine_controls_for_lost_or_stolen_devices

    #identification
    goto identify_the_nature_of_the_device
    goto assess_the_criticality_of_data_or_accounts
    goto interview_the_user_to_understand
    goto contact_local_authorities

    #containment and eradication
    goto disable_or_reset_password
    goto perform_remote_wipe_capabilities
    if device is laptop | other_computer:
        goto disable_any_directories
        goto create_alerts
        goto disable_any_remote_access
        goto remind_user_to_disable_or_reset_the_password
    else:
         goto disable_any_directories
         goto disable_any_remote_access
         goto contact_the_cellular_provider
         goto create_alerts
         goto remind_user_to_disable_or_reset_the_password
    
    #recovery
    goto restore_user_work
    goto create_alerts_for_any_abnormal_activity

        
    #lessons learnd
    goto conduct_a_meeting_after_the_incident
    goto create_and_distribute_an_incident_report