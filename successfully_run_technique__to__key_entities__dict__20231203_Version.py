# Successfully executed techniques:


sucessfully_run_technique__to__key_entities__dict = \
{
"atomic__t1547_004__multiple__boot_or_logon_autostart_execution-_winlogon_helper_dll__92578413245a3418c9dc21dc5db784ff__trial_1"  # done for now
:["HKLM:\\Software\\Microsoft\\Windows", "NT\\CurrentVersion\\Winlogon\\", "Userinit", "Userinit.exe", "C:\\Windows\\System32\\cmd.exe"],
 
"atomic__t1053_005__multiple__scheduled_task,job-_scheduled_task__920a251237fac2b70fe4d647aa16bfdd__trial_1" # Requires looking into Invoke-MalDoc.ps1 content, and further.
:["Invoke-MalDoc.ps1", "notepad.exe", "T1053.005-macrocode.txt", "word", "scheduler"],

"atomic__t1059_005__execution__command_and_scripting_interpreter-_visual_basic__42302f7d89c15f8070f83e743771d567__trial_1" # Requires looking into Invoke-MalDoc.ps1 content, and further.
[],

"atomic__t1070_003__defense-evasion__indicator_removal_on_host-_clear_command_history__18d69a8fd988d6b63f5307ce857723c9__trial_1" # difficult
:[], 

"atomic__t1087_002__discovery__account_discovery-_domain_account__613dc87cebac339d20973268e0bb1c0b__trial_1"   # difficult 
:[],

"atomic__t1070_004__defense-evasion__indicator_removal_on_host-_file_deletion__b0026f9a57639c049490a43d623d7695__trial_1" # done for now
:["TeamViewer_54.log"],

"atomic__t1547_001__multiple__boot_or_logon_autostart_execution-_registry_run_keys_,_startup_folder__3c0760559a620aad7664cdf98f486127__trial_1" # done for now
:["HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce", "powershell.exe"],

"atomic__t1546_013__multiple__event_triggered_execution-_powershell_profile__49a7502f9c667aa3af9c87f6ab1e68b3__trial_1" # Requires more knowledge --
:["calc.exe"],

"atomic__t1547_004__multiple__boot_or_logon_autostart_execution-_winlogon_helper_dll__7cd5d1852fb4a534fa9b735288ca158f__trial_1"
:["HKCU:\\Software\\Microsoft\\Windows", "NT\\CurrentVersion\\Winlogon\\", "Shell", "explorer.exe", "C:\\Windows\\System32\\cmd.exe"],

"atomic__t1055_003__multiple__thread_execution_hijacking__6a64ea6e29cdb83d468a27d6f69960cb__trial_1"   # done for now
:["notepad.exe", "InjectContext.exe"],

"atomic__t1036__defense-evasion__masquerading__7575d3d5ae97ee568d49afbd0f878fe2__trial_1" # Needs more investigation -- https://github.com/jgwak1/meeting-txtfiles/blob/b1127706f0e2f49b3fedec9f42fe5c79736ccdc8/parsed_operations__reports_20231203.txt#L6200 -- Need to look into more detail
:["ExternalPayloads\\T1036.zip", "Downloads\\T1036", "T1036\\README.cmd"],

"atomic__t1562_004__defense-evasion__impair_defenses-_disable_or_modify_system_firewall__9378f5d52c7f94cd08f407f8c0a5fbd7__trial_1"
:["3389", "netsh", "firewall", "advfirewall"],
# local port

"atomic__t1027_004__defense-evasion__obfuscated_files_or_information-_compile_after_delivery__55b2c04e70a5711957e264b04e645e91__trial_1"
:["893687_T1027.004_DynamicCompile.exe"],

"atomic__t1219__command-and-control__remote_access_software__f1b3fca18d7465cd10e5a7477a3bf97d__trial_1"
:[],

"atomic__t1059_003__execution__command_and_scripting_interpreter-_windows_command_shell__942d94dff3cc494bacf5517e775321a7__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__34952e2eefd3066c5f574744e1734ca6__trial_1"
:[],

"atomic__t1003_001__credential-access__os_credential_dumping-_lsass_memory__35d92515122effdd73801c6ac3021da7__trial_1"
:[],

"atomic__t1074_001__collection__data_staged-_local_data_staging__4382d53f0f53399e72c728d019fffd77__trial_1"
:[],

"atomic__t1055_002__multiple__process_injection-_portable_executable_injection__ca6a3f579181ea47b7d95779e8d8a79b__trial_1"
:[],

"atomic__t1113__collection__screen_capture__64569d9eb87191fc3cbf365a656e31ab__trial_1"
:[],

"atomic__t1555_003__credential-access__credentials_from_password_stores-_credentials_from_web_browsers__5610bf38f44ad2da2ecb846ba776ecdc__trial_1"
:[],

"atomic__t1204_002__execution__user_execution-_malicious_file__ab1b50880382b06d48d3d23ad1786239__trial_1"
:[],

"atomic__t1482__discovery__domain_trust_discovery__feb9647c55185e3b6045293fd26f6a5b__trial_1"
:[],

"atomic__t1090_001__command-and-control__proxy-_internal_proxy__b0eb5108debf92ed5707a964b2bf3481__trial_1"
:[],

"atomic__t1112__defense-evasion__modify_registry__0424ccb447bfa66b94162266f55ecd52__trial_1"
:[],

"atomic__t1555__credential-access__credentials_from_password_stores__935e8026584b85192519c57d7080b048__trial_1"
:[],

"atomic__t1027_006__defense-evasion__html_smuggling__a96a64caf38bca14cef902e999bb6b98__trial_1"
:[],

"atomic__t1572__command-and-control__protocol_tunneling__f49909057fa568660a6f268b7261e446__trial_1"
:[],

"atomic__t1547_005__multiple__boot_or_logon_autostart_execution-_security_support_provider__bd9f08eb7c3215b8a6a7dd1af9ea406a__trial_1"
:[],

"atomic__t1055__multiple__process_injection__9999b5c073203122cbe5f1f5438cf637__trial_1"
:[],

"atomic__t1059_005__execution__command_and_scripting_interpreter-_visual_basic__9c955a373154a7090d4b4396b561f5da__trial_1"
:[],

"atomic__t1033__discovery__system_owner,user_discovery__2bf75f949823305d3ea815c8e94e9ee3__trial_1"
:[],

"atomic__t1217__discovery__browser_bookmark_discovery__abc25aecd2ed0524af31e79add29cc43__trial_1"
:[],

"atomic__t1204_002__execution__user_execution-_malicious_file__cde814c61dcd8b0fbeeb14f005c2432f__trial_1"
:[],

"atomic__t1564_003__defense-evasion__hide_artifacts-_hidden_window__f1222384fe40cc71e7dea9d182014eaf__trial_1"
:[],

"atomic__t1070_004__defense-evasion__indicator_removal_on_host-_file_deletion__2413b013bc82d152765e2ac34601a327__trial_1"
:[],

"atomic__t1070_003__defense-evasion__indicator_removal_on_host-_clear_command_history__df94858e92a23d274ac1d70133d9150f__trial_1"
:[],

"atomic__t1490__impact__inhibit_system_recovery__e90756bb6dcd21462dc4cc452661df91__trial_1"
:[],

"atomic__t1119__collection__automated_collection__344e7eaf650763e0d3e9f02e62c1cf4b__trial_1"
:[],

"atomic__t1112__defense-evasion__modify_registry__1296157a99b29c9a81fb1ce4eaf24cbd__trial_1"
:[],

"atomic__t1547_004__multiple__boot_or_logon_autostart_execution-_winlogon_helper_dll__dc74af5b90b9cbb4dcfbcaaa3e412a5e__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__32047c4f30d4e65ebc9b22b9b8368bca__trial_1"
:[],

"atomic__t1059_005__execution__command_and_scripting_interpreter-_visual_basic__f2131e45dbd95e3057bd3494b5aeed41__trial_1"
:[],

"atomic__t1204_002__execution__user_execution-_malicious_file__98adc43648b0e4ea6e90a88ad5ae4b3d__trial_1"
:[],

"atomic__t1033__discovery__system_owner,user_discovery__221d4ebcb41e708b6ee90c1c0369a969__trial_1"
:[],

"atomic__t1106__execution__native_api__b262964145fa55e27265e7caa89b1169__trial_1"
:[],

"atomic__t1112__defense-evasion__modify_registry__f4d3c5648b8d2fab9b061016eb91f478__trial_1"
:[],

"atomic__t1036_003__defense-evasion__masquerading-_rename_system_utilities__4bb550aacec4efb190c72389677b7f4e__trial_1"
:[],

"atomic__t1547_004__multiple__boot_or_logon_autostart_execution-_winlogon_helper_dll__5c23188ed301af9f1b6b55d4f3f60b46__trial_1"
:[],

"atomic__t1548_002__multiple__abuse_elevation_control_mechanism-_bypass_user_account_control__e7d20e7f0087f8a4234c1d1b7a228bb0__trial_1"
:[],

"atomic__t1003__credential-access__os_credential_dumping__18f31c311ac208802e88ab8d5af8603e__trial_1"
:[],

"atomic__t1546__multiple__event_triggered_execution__2fc2b9c9b48990938653dbe8966d487d__trial_1"
:[],

"atomic__t1120__discovery__peripheral_device_discovery__7b9c7afaefa59aab759b49af0d699ac1__trial_1"
:[],

"atomic__t1548_002__multiple__abuse_elevation_control_mechanism-_bypass_user_account_control__64430e7597668877a832b9d1e379c9f2__trial_1"
:[],

"atomic__t1566_001__initial-access__phishing-_spearphishing_attachment__1afaec09315ab71fdfb167175e8a019a__trial_1"
:[],

"atomic__t1546_015__multiple__event_triggered_execution-_component_object_model_hijacking__d94bcdfc9d0f769b062e1960f7af6804__trial_1"
:[],

"atomic__t1547_014__multiple__active_setup__7ad5840a79f3259965fa28835dda93c4__trial_1"
:[],

"atomic__t1548_002__multiple__abuse_elevation_control_mechanism-_bypass_user_account_control__b473176c321f31824c909c73807caf92__trial_1"
:[],

"atomic__t1036__defense-evasion__masquerading__bc456ce28da22e33b96257b6ae020391__trial_1"
:[],

"atomic__t1070_001__defense-evasion__indicator_removal_on_host-_clear_windows_event_logs__05f8b752dbccff102ef530103bd8e550__trial_1"
:[],

"atomic__t1070_003__defense-evasion__indicator_removal_on_host-_clear_command_history__adce11c81bb77ae74660c6c743a0442d__trial_1"
:[],

"atomic__t1119__collection__automated_collection__0c7c18db582bff4d0da4b4f8fdb2be49__trial_1"
:[],

"atomic__t1204_002__execution__user_execution-_malicious_file__705c4b9714ce06223e7d7038cd332808__trial_1"
:[],

"atomic__t1055_012__multiple__process_injection-_process_hollowing__557321faaf98c77b2b452cecd7b1de37__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__e0946bc3b8b888d6c4cdf3f023fe3c0b__trial_1"
:[],

"atomic__t1491_001__impact__defacement-_internal_defacement__2fc2e45dde68ab78a97a22ca138652e1__trial_1"
:[],

"atomic__t1105__command-and-control__ingress_tool_transfer__b0e28215c59037cc6cdb61b38615c32d__trial_1"
:[],

"atomic__t1087_002__discovery__account_discovery-_domain_account__9ccef9b46ce26850bb709a83d8e538ae__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__392e12d6a466407e28d1bb51cf0729bb__trial_1"
:[],

"atomic__t1219__command-and-control__remote_access_software__aada5380e7d0a4c7b71f2a324d9d5327__trial_1"
:[],

"atomic__t1204_002__execution__user_execution-_malicious_file__431121fe12b6fd82938a9a52526b3423__trial_1"
:[],

"atomic__t1547_001__multiple__boot_or_logon_autostart_execution-_registry_run_keys_,_startup_folder__9b74d10b3164f13d357830d1a6ee334a__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__c407315583b3a00d9a2e0c3c510f2c96__trial_1"
:[],

"atomic__t1562_004__defense-evasion__impair_defenses-_disable_or_modify_system_firewall__34f398de2b04b96158b3bd25abaea5a7__trial_1"
:[],

"atomic__t1134_001__multiple__access_token_manipulation-_token_impersonation,theft__81289b3d78d06c14b816f7644b1d9f8b__trial_1"
:[],

"atomic__t1547_009__multiple__boot_or_logon_autostart_execution-_shortcut_modification__501af516bd8b24fee0c7c650ae5cc861__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__43e3334362b140924f001b256b229ee5__trial_1"
:[],

"atomic__t1003_002__credential-access__os_credential_dumping-_security_account_manager__69219b448ba0a75bae573d58d8b6cf40__trial_1"
:[],

"atomic__t1548_002__multiple__abuse_elevation_control_mechanism-_bypass_user_account_control__c4c471259798dd6c7b0b56f716e12113__trial_1"
:[],

"atomic__t1547_001__multiple__boot_or_logon_autostart_execution-_registry_run_keys_,_startup_folder__1f15ab22c39a9b6bb2bb0d77276dfcb3__trial_1"
:[],

"atomic__t1006__defense-evasion__direct_volume_access__80e752c5fc69a56ccb86bc90efc5eff6__trial_1"
:[],

"atomic__t1197__multiple__bits_jobs__5a9be3b1696cc0cce8557f9596547e13__trial_1"
:[],

"atomic__t1592_001__reconnaissance__gather_victim_host_information-_hardware__53861bc51eb67cb9775c95b9e02ad141__trial_1"
:[],

"atomic__t1556_002__multiple__modify_authentication_process-_password_filter_dll__cc7f0eb8b9115b271eaaa42c9b6f3dca__trial_1"
:[],

"atomic__t1136_002__persistence__create_account-_domain_account__8a95e17c084e9a8bf41c69c73beeb0af__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__5c4ea84c2b050f1f8b6f880755ccbc62__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__2e9acde621e7768a73c1b9a1157c444d__trial_1"
:[],

"atomic__t1566_001__initial-access__phishing-_spearphishing_attachment__0a69420bec84b02bd47464f6835653b1__trial_1"
:[],

"atomic__t1574_012__multiple__hijack_execution_flow-_cor_profiler__7179bb4957f1f7f3004ea70c714a8fb9__trial_1"
:[],

"atomic__t1219__command-and-control__remote_access_software__b6ebae300e5ff115e965cc9179d4f831__trial_1"
:[],

"atomic__t1115__collection__clipboard_data__abd5327a47c4994e2824f833eefe4250__trial_1"
:[],

"atomic__t1547_006__multiple__boot_or_logon_autostart_execution-_kernel_modules_and_extensions__bdd0be771e2462e572e2ecfbe5bf2eb7__trial_1"
:[],

"atomic__t1547_001__multiple__boot_or_logon_autostart_execution-_registry_run_keys_,_startup_folder__acf646b22c5d2c2b1058feb7da1f3bdc__trial_1"
:[],

"atomic__t1021_003__lateral-movement__remote_services-_distributed_component_object_model__68df771632fd6216858edd20458ee5bb__trial_1"
:[],

"atomic__t1105__command-and-control__ingress_tool_transfer__a88b5c13a1d5d6bdf02b66bc73411f41__trial_1"
:[],

"atomic__t1562_001__defense-evasion__impair_defenses-_disable_or_modify_tools__f0fde90a3d59061b226197974e7dcbaa__trial_1"
:[],
}