# In responding to a ransomware
# In Incident Reponse Playbook from FRESCURE
# Written in Sudocode


def main():
    #preparation
    goto determine_the_memebers_of_the_CSIRT
    goto determine_the_extended_CSIRT_members
    goto define_escalation_paths
    goto evaluate_and_secure_critical_system_backups

    #identification
    goto isolate_infected_systems
    goto investigate_malware_to_determine
    goto analyze_the_malware_to_determine_characteristics
    goto use_all_information_and_IoCs
    if ransomware_variant is identified:
        goto perform_research_to_determine_tactics_techniques_and_procedures
    
    #Containment
    goto use_the_information_about_the_initial_point
    if IoCs discoverd:
        goto isolate_these_device
    goto add_IoCs_to_endpoint_protection
    goto submit_hash_value_to_community_sources
    goto implement_any_temporary_network_rules
    if additional_accounts have been discoverd:
        goto disable_those_accounts
    
    #Eradication
    goto preserve_artifacts_systems_and_relevant_backups
    goto preserve_any_volatile_data
    if all_relevant_data_and_equipment have been preserved:
        goto replace_or_rebuild_systems

    #recoveory
    goto restore_impacted_systems
    goto rebuild_the_machine_from_a_known_good_images
    goto remediate_any_vulnerabilities_and_gaps_identified
    goto reset_passwords_for_all_impacted_accounts
    goto continue_to_monitor
    if data_exfiltration_and_extortion were determined:
        goto work_with_legal_counsel
    
    #lessons learnd
    goto conduct_a_meeting_after_the_incident
    goto create_and_distribute_an_incident_report