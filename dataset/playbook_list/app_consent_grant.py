# App Consent Grant in Incident Response Playbook from Microsoft
# Written in Sudocode

def main():
    goto signs_of_an_applcation_consent_grant_attack
    goto inventory_apps_with_access_using_Azure_AD_poral
    goto inventory_apps_with_access_using_Powershell
    goto inventory_apps_with_access_using_Users_enumerate_their_app_access

    if AzureADPSPermissions.ps1_script_output_file is not null:
        goto run_AzureADPSPermissions_script
        goto filter_the_results_on_ConsentType
        if search_for_value_admin_consent_tenant_wide("All principals") is not null:
            goto look_in_column_F
            goto review_permissions_for_each_delegated_application
            goto llok_for_review_permissions
        else:
            stop()
        endif
        
        if search_for_value_user_consent_only_appkicable_to_the_user_who_consented("All principals") is not null:
            goto look_in_column_F
            goto review_permissions_for_each_delegated_application
            goto llok_for_review_permissions
        else:
            stop()
        endif

        goto review_users_that_have_consent_granted

        if check_clientDisplayName_for_apps_that_seem_suspicious is true:
            if confirmed_attack is false:
                stop()
            else:
                revoke_applicatinos_permissions()
                if completed investigation:
                    stop()
            endif
        else:
            goto apps_with_misspelled_names_bland_names_or_hacker_sounding_names
        endif

def revoke_applications_permission():
    goto naviagate_to_the_affected_user_in_the_Azure_AD_portal
    goto use_PowerShell_to_revocke_Oauth_consent_grant
    goto use_PowerShell_to_revoke_AppRole_assignment
    goto disable_sign_in_for_the_account
    goto disable_integrated_applictions_for_your_tenancy # not recommended
