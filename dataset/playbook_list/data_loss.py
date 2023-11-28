# The purpose of the Cyber Incident Response: Data Loss Playbook is to define activities that should be considered when detecting, analysing and remediating a Data Loss incident. The playbook also identifies the key stakeholders that may be required to undertake these specific activities.
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
    goto detect_dos_attack
    goto mobilise_the_CIRT_and_verify_it_is_a_DoS_attack
    goto collate_inital_incident_data_and_classify_cyber_incident
    goto escalate_in_accordance_with_the_CIRP
    goto consider_mobilising_forensic_readiness_capability
    
    #analyze
    goto engage_technical_staff
    goto cofirm_systems_and_or_applications_being_targeted
    goto collate_a_timeline_of_events_from_when_the_attack_was_first_detected
    goto collate_details_on_the_type_of_DoS_attack_if_known_at_this_stage
    if personal_data is at_risk:
        goto consider_engaging_the_DPO_and_reporting_to_the_ICO

    #remediation
    goto implement_immediate_steps
    goto consider_wheter_the_bussiness_continuity_plan
    goto consider_filtering_traffic_at_the_border
    goto consdier_placing_IP_restrictions_on_sensitive_and_critical_systems_and_applications
    goto patch_systems_applications_to_protect_against_vulnerabilities
    goto restore_serviced_to_BAU

    #post incident
    goto draft_post_incident_report
    goto complete_formal_lessons_learnt_process_defined_in_CIRP
    goto publish_internal_communications
    goto updates_to_cyber_incident_documentation

    end()
