# The purpose of the Cyber Incident Response: Denial of Service Playbook.
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
    goto reports_of_data_breach_or_compromise_to_service_desk
    goto mobilise_the_CIRT
    goto collate_inital_incident_data_and_classify_cyber_incident
    goto escalate_in_accordance_with_the_CIRP
    goto consider_mobilising_forensic_readiness_capability
    
    #analyze
    goto engage_technical_staff
    goto confirm_data_involved
    goto analyze_the_data_types_and_quantities_to_determine
    goto consider_engaging_the_DPO_and_reporing_to_the_ICO

    #remediation
    goto contain_systems_that_have_been_affected
    goto consider_disconnecting_infected_systems
    goto deploy_latest_malware_definitions_to_anti_malware_solutions
    goto contain_business_effects_of_the_cyber_security_incident
    goto re_image_systems_and_scan_for_malware
    goto restore_serviced_to_BAU

    #post incident
    goto draft_post_incident_report
    goto complete_formal_lessons_learnt_process_defined_in_CIRP
    goto publish_internal_communications
    goto updates_to_cyber_incident_documentation

    end()