# The purpose of the Cyber Incident Response: Phishing Playbook.
# In Incident Respone Playbook Malware From Scottish Government
# Written in SudoCode
def main():
    prepare()
    
    #preparation
    goto review_and_rehearse_CIRP
    goto review_recent_cyber_incidents_and_outputs
    goto review_threat_intelligence_feeds_latest_vulnerabilities_and_risks
    goto ensure_access_to_CIRP_and_data_flow_diagrams_and_appropriate_documentation
    goto maintain_awareness_with_employees_through_security_awareness_training

     
    #detect
    goto report_of_phishing_emails_to_service_desk
    goto mobilise_the_CIRT
    goto collate_inital_incident_data_and_classify_cyber_incident
    goto escalate_in_accordance_with_the_CIRP
    goto consider_mobilising_forensic_readiness_capability

    
    #analyze
    goto engage_technical_staff
    goto identify_and_research
    goto identify_how_widespread_the_attack_is
    goto identify_impacted_data_and_systems
    goto consider_engaging_the_DPO_and_reporing_to_the_ICO

    
    #remediation
    goto quarantine_affected_systems_and_monitor_infrastructure
    goto suspend_login_credentials_for_compromised_accounts
    goto remove_malware_from_affected_systems
    goto conduct_restoration_of_affected_network_systems_from_trusted_back_up
    goto re_image_systems_and_scan_for_malware
    goto restore_serviced_to_BAU
        
    #post incident
    goto draft_post_incident_report
    goto complete_formal_lessons_learnt_process_defined_in_CIRP
    goto publish_internal_communications
    goto updates_to_cyber_incident_documentation

    end()
    