# Portfolio research & design rationale
Reviewed 6 September 2026. This is a qualitative review of selected public portfolios and primary security guidance, not a hiring-outcome study or exhaustive ranking.

## Portfolio references
- [Michael Maben](https://michaelmaben.com/): clear professional positioning, a dedicated work area, and technical writing. Adopted the separation of experience, work and notes, without copying design, credentials or professional claims.
- [tdt1114 detection engineering portfolio](https://github.com/tdt1114/detection-engineering-portfolio): presents telemetry, ingestion, detection and investigation as a progression. Adopted a source-to-alert narrative and explicit context around demonstrated capabilities.
- [Adrian Tanasse SOC portfolio](https://github.com/adriantanasse/SOC-Portfolio): organizes work by security discipline. Adopted concise capability groupings, but avoided filters implying multiple completed projects when ProjectX is the current flagship.

These examples are authors’ self-presentations. They are not independently verified candidate rankings or evidence that a specific layout produces job offers.

## 2026 priorities and application
1. [WEF Global Cybersecurity Outlook 2026](https://www.weforum.org/publications/global-cybersecurity-outlook-2026/), published 12 January 2026: highlights AI adoption, geopolitical fragmentation and cyber capability gaps. Design implication: demonstrate practical capability through focused projects; do not substitute a trend list for evidence.
2. [NIST IR 8596 preliminary Cyber AI Profile](https://csrc.nist.gov/pubs/ir/8596/iprd), published 16 December 2025 with 2026 working-session updates: distinguishes securing AI, AI-enabled defense and countering AI-enabled attacks. Used to scope a controlled AI-security project. This source is a draft, not a final standard or certification.
3. [Microsoft Cloud and AI Security Engineer Associate](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/): connects identity, cloud controls and AI workloads. Used to check the CV’s SC-500 direction; the portfolio marks it planned.
4. [Splunk CI/CD detection engineering](https://www.splunk.com/en_us/blog/security/ci-cd-detection-engineering-splunk-security-content-part-1.html): established engineering practice, not a newly invented 2026 trend. Informs testing and versioning as explicit deliverables.
5. [Google Web Vitals](https://web.dev/articles/vitals): loading, interaction and visual stability inform implementation. Field performance needs real deployed traffic; local checks do not establish field Core Web Vitals compliance.
6. [Reduced motion guidance](https://web.dev/articles/prefers-reduced-motion): motion is optional and disabled when requested by the visitor’s system preferences.

## Design decisions
An original dark/lime system takes broad visual inspiration from the supplied Varonis reference. Large typography, generous space and a conceptual network illustration create a recognizable identity. No vendor logos, testimonials or enterprise customer claims were borrowed. The site offers two reading depths: a quick recruiter summary and a detailed engineering case study.

Professional experience is separate from lab validation. The CV supports two dated roles, CEH certification and a cybersecurity degree. AZ-104 remains in progress and SC-500 planned. The supplied 4.88 GPA has no stated scale; it is omitted rather than converted. The ticket-resolution percentage lacks workload context and is not promoted as a headline performance metric. No relocation or work-authorization claims are inferred.

## Credibility and publication boundaries
Only one FSRM detection path is described as fully correlated. Six rules being configuration-valid does not establish six validated detections. Same-subnet bypass, broad SERVER permissions and passive-monitoring limits are retained. The public bundle contains no raw internal evidence, phone number, credential identifier or original CV PDF. Email and LinkedIn are sourced from the CV; GitHub was supplied directly by Heshan.

## Deliverables and future improvements
The implemented site includes home, experience, ProjectX, engineering notes, research roadmap, printable recruiter summary, privacy notes and a 404 page. A static audit and GitHub workflow check links and unsafe HTML patterns. After deployment: review headers, run PageSpeed on the live URL, and add a canonical URL and sitemap for the actual domain. Future content should add fresh reproducible investigations; avoid empty project cards presented as finished work.
