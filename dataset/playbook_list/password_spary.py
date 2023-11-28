# Passwrod Spary in Incident Response Playbook from Microsoft
# Written in Sudocode

def main():
    while(true):
        if incident_trigger is true:
            start()

def start():
    if you_are_federated is true:
        goto check_ADFS_for_an_increase_in_failed_password_attempts_and_or_extranet_lockouts
        goto collect_any_successful_sign_IP_0addresses_and_authentication_protocols_used_during_the_attack_time
    endif

    goto check_azure_AD_sign_in_for_failed_password_attempts_extranet_lockout_authentication_protocol_and_identity_protection_for_password_spary_alert

    if password_spary_attack_confirmed is true:
        goto collect_any_successful_sigin_ins_during_this_time_and_attacker_IP_addresss
    else:
        if the_IP_address_a_known_address_or_another_explanation_for_the_alert is true:
            goto troubleshoot_as_per_operational_process
        else:
            goto collect_any_successful_sigin_ins_during_this_time_and_attacker_IP_addresss
        endif

    if the_compromised_password_or_account_identified is true:
        goto change_user_password_and_mark_as_compromised_in_identity_protection
        if the_attacker_successfully_accessed_data:
            goto follow_procedure_for_data_loss
        endif
    else:
        goto block_IP_address_of_attacker_on_firwall_azure_AD_and_ADFS
        if lagacy_authentication_blocked is true:
            if MFA is enabled:
                if IP_policies is enabled:
                    if extranet_lockout is enablied:
                        goto enable_logner_term_protections
                    else:
                        goto enable_extranet_lockout
                    endif
                else:
                    goto enable_IP_polilces_and_risk-based_CA
                endif
            else:
                goto enable_MFA
            endif
        else:
            goto block_lagacy_authentication
        endif
    endif

