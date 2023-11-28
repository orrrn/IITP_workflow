# Ransomware - a type of malicious software designed to block access to a computer system until a sum of money is paid
# In IRM Playbook
# Written in Sudocode

from typing import Collection


def main():
    preparation()
    identification()
    containment()
    remediation()
    recovery()
    lessons_learnt()

def preparation():
    goto ensure_that_the_endpoint_and_perimetric_security_products_are_up_to_date_and_their_logs_are_enabled
    goto raise_your_IT_support_awareness
    goto make_sure_to_have_exhaustive_and_recent_and_reliable_backups_of_local_and_network_users_data

def identification():
    goto monitor_odd_professioonal_emails
    goto monitor_ransom_message
    goto monitor_people_are_complaining_about_thier_files
    goto monitor_numerous_files_are_being_modified
    goto monitor_systems_and_or_applications_become_unavailable

    #host_bsaed identification
    goto look_for_the_aforementioned_extensions
    goto capture_a_memory_image_of_the_computer
    goto look_for_unusual_executable_binaries
    goto look_for_unusual_program
    goto look_for_unusual_services_running
    goto look_for_unusual_process
    goto look_for_unusual_email_attachment_patterns
    goto look_for_unusual_network_or_web_browsing_activities

    #network based identification
    goto look_for_unusual_VPN_activities
    goto look_for_unusual_network_or_web_browsing_activities
    goto look_for_connection_patterns_to_exploit_kits
    goto look_for_connection_patterns_to_ransomware_C&C
    goto look_for_unusual_email_attachment_patterns

def containment():
    goto disconnect_all_computer
    if cannot isolate computer:
        goto disconnect_and_cancle_the_shared_drives
    goto block_traffic_to_identified_ransomware_C&C
    goto send_the_undetected_samples_to_endpoint_security_provider
    goto send_the_uncategorized_malicious_URL_domain_names_and_IP

def remediation():
    goto remove_the_binaries_and_the_related_registry_entires
    goto remove_the_services_related_to_the_ransomware
    if current_anti_virus did not detect the_malware_and_ransomware:
        goto try_running_a_different_one_from_a_USB_stick
    else not possible:
        goto reimage_the_computer_with_a_clean_install

def recovery():
    goto update_antivirus_signatures
    goto ensure_that_no_malicious_binaries
    goto ensure_that_the_network_traffic_is_back_to_normal
    goto restore_users_documents_from_backups
    goto ensure_the_backups_used_are_from_before_the_incident_first_happened

def lessons_learnt():
    goto report
    goto capitalize


