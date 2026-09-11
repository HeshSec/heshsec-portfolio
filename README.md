# Heshan / Security & Infrastructure Portfolio

Original responsive static website for Heshan Kodippilyge. GitHub profile: https://github.com/HeshSec. No framework, package installation, database or secrets required.

## Preview
Run `python -m http.server 8080` in this folder; open http://localhost:8080. Opening index.html directly also works.

## Structure
index.html (home), about.html (experience), projectx.html (case study), notes.html (field notes), outlook.html (research/roadmap), resume.html (printable summary), privacy.html and 404.html. Shared styles.css and app.js. Public research and project brief in assets/.

## Validate
Run `python scripts/check_site.py`. A GitHub Actions workflow runs this audit on pushes and pull requests. It checks local assets and fragments, duplicate IDs, page titles, a single H1, unsafe inline handlers, scripts and local-path leaks. Browser layout and keyboard testing should also accompany significant changes.

## GitHub and Vercel deployment
Create your chosen repository in HeshSec (suggested: heshsec-portfolio). Upload only this directory’s contents, including hidden .github files, with index.html at the repository root. In Vercel import the repository, select Other, leave Build Command empty and use the root as output directory (`.` if requested). No environment variables are required. See https://vercel.com/docs/deployments/overview.

vercel.json applies security headers and prevents HTTP access to development/documentation directories. After deployment, verify headers and the 404 route on the real URL. Add canonical metadata and a sitemap only after choosing the final public domain. GitHub/Vercel account access is not included in this package, and no live deployment is claimed.

## Content maintenance
Keep current study and planned credentials distinct from completed certifications. ProjectX is independent lab work, not client production experience. Use the original CV and internal report as private sources, not public downloads. Employment facts come from the supplied CV; the GPA and ticket percentage are not highlighted because their scale/context needs clarification. Change contact information only to owner-approved values.

## Privacy and scope
No analytics, cookies, browser storage, live lab connections or contact backend. Email opens the visitor’s mail client. Hosting and external sites have their own data policies. The original CV PDF, phone, certification identifier, private screenshots, VM exports and raw evidence reports are excluded. Review assets/research-and-design.md for research sources and editorial decisions.

## Security model
Local CSS/JS only; a restrictive CSP; no runtime dependencies. These choices reduce unnecessary surface area but do not constitute an enterprise security certification. Headers must be validated after deployment. Report issues privately via the email on the site; do not include secrets in issues.

## Final edition
Capabilities page, original HeshSec mark and local SVG icons added. Technical identifiers retain their punctuation; ordinary visible prose avoids decorative dashes and unnecessary hyphens. projectx-public-report.html is a downloadable public reading edition, not the full internal report. It contains no original screenshots. The source INTERNAL DOCX has not been copied into this package.
