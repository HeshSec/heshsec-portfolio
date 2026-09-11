# ProjectX — Personal Security Engineering Project

Designed and implemented by Heshan as an independent learning project.

## Scope
Seven VirtualBox VMs, three internal networks and four Wazuh agents. Active Directory, Group Policy, Windows LAPS, pfSense, SMB/NTFS, FSRM, Wazuh and passive Security Onion monitoring form the lab.

## Verified case: Finance file protection
An inert executable-named file was blocked by FSRM. Windows emitted SRMSVC event 8215. After diagnosing the event path and correcting the custom rule parent to 60601, Wazuh rule 100201 generated a level-10 alert. Event record 1312 was correlated across the source and central alert.

FSRM performed the block; Wazuh provided detection and central alerting. Six custom rules were recovered and configuration-validated; this does not mean all six have been independently tested.

## Engineering decisions
- Separate CORP, SERVER and DMZ networks with explicit routed exceptions.
- Use directory groups for departmental access and LAPS for local credential management.
- Collect native Windows and endpoint events for central investigation.
- Preserve failed results, configuration changes and verification evidence.

## Boundaries
This is a lab, not a production deployment or certification. SERVER interface rules retained broad permissions in the reviewed configuration. Same-subnet traffic normally bypasses pfSense. Passive monitoring does not establish inline prevention or visibility into every flow. Credentials, raw machine exports and internal evidence reports are intentionally excluded from this public website package.

## Proposed next work
Identity and access evaluation, a secure delivery pipeline, and controlled AI-security testing. These are planned directions, not completed projects.
