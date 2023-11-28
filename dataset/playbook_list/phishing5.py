# Phishing in Incident Response Playbook from Microsoft
# Written in Sudocode

def main():
    goto initial_phishng_email_and_subject_and_email_address
    goto get_the_list_of_users_identities_who_got_the_email
    goto who_else_got_or_read_the_same_email

    if delegated_access_to_the_mailbox is true:
        goto to_which_users_is_it_delegated_or_forwarded
        goto list_of_users_and_identities
    endif

    if forwarding_rule_for_the_mailbox is true:
        goto to_which_users_is_it_delegated_or_forwarded
        goto list_of_users_and_identities
    endif

    goto list_of_users_and_identities
    goto get_timstamp_when_user_identity_had_access_to_mailbox
    goto investigate_sign_in_evnets_for_the_identity

    if the_user_read_the_email is true:
        if the_email_contain_an_attachment is true:
            if was_there_payload_in_the_attachment is true:
                goto record_hash_or_IOC
            else:
                check_email_header()
            endif
        else:
            goto check_email_header()
        endif
    else: 
        goto stop or remove_the_user or identity_off_the_potential_list
    endif
   
def check_email_header():
    goto check_email_header_for_the_true_source_of_the_sender
    goto record_the_source_IP_address
    goto verify_IP_addresss_to_attackers_or_campaigns

    if the_user_click_the_link_in_the_email is true:
        goto record_destination_IP_address or record_destination_URL
    else:
        goto on_what_endpoints_was_the_email_opended
        for each endpoint:
            goto get_deivce_ID
        if get_device_ID is not null:
            goto get_device_investigate_package
        endif
        if attachment_was_executed is true:
            if process_creation_event is true:
                goto get_device_investigate_package
            endif
        else:
            if was_the_dest_IP_or_URL_touched_or_opended is true:
                if was_code_downloaded_or_executed is ture:
                    goto get_device_investigate_package
                endif
            else:
                goto investigate_sign_in_events_for_the_identity
                goto record_time_stamps
                goto record_devices
                goto record_source_IP_addressses
                goto record_app_IDs
                goto record_user_agent_string
                if investigate_source_IP_address is not null:
                    goto identify_device
                    goto get_device_investigate_package
                endif
                if investigate_each_app_id is not null:
                    goto app_investigation_flow
                endif
            endif
        endif
    endif
        