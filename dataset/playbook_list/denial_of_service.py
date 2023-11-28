# Denial of Service in Incident Response Playbook from Incident Response Consortium
# Written in Sudocode

def main(step):
    prepare()
    detect()
    analyze()
    contain()
    eradicate()
    recover()
    post_incident_handling()

def prepare():
    if vulnerability_manager | threat_manager | risk_manager : # Determine Core Ops Team & Define Roles
        goto review_and_maintain_timeline
    endif

    goto dispute_resolution

    interview = interviews(user,manager,physical_security,key_stakeholders)

    if interview is internal_path:
        goto document(internal_path)
    else interview is external_path:
        goto document(external_path)
    endif

def detect():
    if define_threat_indicators is is_custom:
        goto custom_indicators
        threat_indicators is custom

    else define_threat_indicators is is_standard:
        goto detection_of_unknown_or_unidentified_packets_from_unknown_senders
        goto peaked_amount_of_inbound_data
        goto unknown_or_unexpected_incoming_internet_traffic
        goto alerting_from_firewall_and_intrusion_detection_systems
        goto notification_from_outside_organizations
        threat_indicators is standard
    endif

    goto categorize_incident
    goto request_packet_capture
    goto conduct_scans

def analyze():
    if define_risk_factors is is_custom:
        goto custom_indicators
        risk_factors is custom
    else define_risk_factors is is_standard:
        goto products_goods_services_are_affected_by_this_attack
        goto customers_are_affected_by_this_incident
        goto public_or_personnel_safety_affected
        goto ability_to_control_record_measure_track_any_significant_amounts_of_inventory_products_cash_revenue_has_been_lost
        goto this_act_is_being_launched_by_known_entities
        goto there_is_internal_knowledge_of_this_incident
        goto there_is_external_knowledge_of_this_incident
        goto worst_case_business_impact_if_unable_to_mitigate_this_attack
        risk_factors is standard
    endif

    goto determine_path_methods
    goto log_collection
    goto evidence_collection
    goto data_capture
    goto analysis

def contain():
    goto identify_the_systems_that_have_been_affected(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_systems_that_have_suffered_outage_or_degradation_of_services(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_the_IT_services_being_impacted(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_critical_systems_that_are_at_risk_from_dos_and_ddos(servers, desktop, laptop, mobile, VM, LDAP_directory)
    goto identify_type_of_packets_being_utilized
    goto identify_critical_choke_points_or_bottlenecks_on_network_that_could_increases_that_effect
    goto identify_the_source_and_if_their_networks_can_be_blackholed(select_database, incident_database, vulnerability_logs, threat_database, system_logs, query_databases, generate_report)
    goto identify_additional_traffic_rerouting_or_egress_filtering_to_block_more_traffic(view_report,view_record_details, select_records, copy_record_details)
    goto identify_the_tools_used_to_detect_the_attack(SIEM, IDS, firewall, scanners, antivirus, network_monitoring_tools)

def eradicate():
    if triage_and_confirm_incident_report is true:
        goto request_system_patch
        goto request_network_segment_or_other_configuration_change
        goto add_chagne_remove_affected_system_site_network
    endif

    if communications is true:
        goto direct_phone_call
        goto conference_call
        goto intranet_meeting
        goto internet_meeting
        goto in_person_meeting
        goto mobile_messaging
    endif

    if mitigate_malware is true:
        goto identify_any_alternate_course_for_business_operations_that_will_be_effected
        goto create_whitelist_of_sourceIP_and_services_that_must_be_allowed_into_network
        goto coordinate_with_business_continuity_on_rolling_over_services_to_any_alternate_sites
        goto coordinate_with_ISP_to_determine_best_courses_of_action
    endif

def recover():
    if recover_systems is true:
        goto reimage
        goto IDS_and_IPS_and_firewall_updates
        goto determine_alternate_network_ingress_and_egress_solutions_if_malware_causes_DoS
    endif

    goto incident_remediation
    
def post_incident_handling():
    if incident_review is true:
        goto is_electronic_personal_health_information_compromised
        goto is_sensitive_government_information_compromised
    endif

    if lessons_uncoverd is true:
        goto discovery_meeting
        goto policy_updates_defined
        goto process_updates_defined
        goto configuration_updates_defined
    endif

    if lessons_applied is true:
        goto policies_implemented
        goto process_changes_implemented
        goto configurations_applied
    endif
