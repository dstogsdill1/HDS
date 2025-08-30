# HDS Configuration & Knowledge Base Repository

This repository holds the static configuration and documentation for the **Homeland Development Services** platform. Its purpose is to provide version‑controlled, auditable storage for platform metadata, seed data, and documentation. Runtime data (work orders, customer records, vendor contacts, etc.) continue to live in the primary Excel workbooks stored in OneDrive/SharePoint and are referenced by the service desk tools (e.g., JotForm) to capture live requests.

## Repository structure

```
HDS/
├─ .github/workflows/        # Automation pipelines (e.g., GitHub Pages deploy, validation)
├─ README.md                 # This file
├─ config/                   # Version‑controlled platform configuration
│   ├─ csv/                  # Seed data exported from Excel (e.g. service codes, priority levels)
│   ├─ schemas/              # JSON schemas describing expected structure of CSV files
│   └─ tenants/              # Optional per‑customer/package configuration files
├─ docs/                     # Documentation and how‑to guides
│   ├─ knowledge_base.md     # Explains how to refresh the master knowledge base
│   ├─ workflow_overview.md  # High‑level overview of intake, triage, dispatch & escalation workflows
│   └─ data_flow.md          # Diagrams/data flow between OneDrive, JotForm, Power Automate and GitHub
└─ backups/                  # Optional backups of key workbooks (e.g. HDS_IT_Master_Updated_v2.xlsx)
```

## Current state

- The **IT master knowledge base** and supporting worksheets (Technical Config, Recurring Costs, Resource Links, AI Systems) are stored in OneDrive/SharePoint and referenced by JotForm and other automations. A read‑only backup of the latest versions can be found in the [HDS‑Knowledge‑Base](https://github.com/dstogsdill1/HDS-Knowledge-Base) repository. Maintaining the live copies in OneDrive ensures JotForm and existing workflows continue to function without interruption.
- The `config/` folder is ready to receive CSV exports of seed data from the Excel workbooks. For example:
  - `priority_levels.csv` could list Emergency, Urgent and Routine codes along with associated SLA minutes.
  - `service_categories.csv` could enumerate allowed values for work‑order categories.
- The `.github/workflows/static.yml` file is a placeholder for future automation. A suggested first automation is to validate CSV seed data against JSON schemas on each commit.

## Updating the live workbooks

1. **Edit in OneDrive**: For any changes to customer lists, vendor contacts, call flows, or service instructions, edit the respective workbook in its OneDrive/SharePoint location. JotForm and Power Automate flows reference these live sheets.
2. **Export for version control** (optional): To capture a snapshot of static tables for code‑driven configuration, export individual tabs from Excel as CSV files and place them under `config/csv/`. Use consistent names and update corresponding JSON schemas as necessary.
3. **Commit to GitHub**: Add the new CSV files to this repository. Open a pull request or commit directly to `main`. Describe the purpose of the change and reference any related JotForm or automation updates.
4. **Backups**: When major changes are made to the Excel workbooks, upload a copy of the entire workbook into the `backups/` directory with a timestamp in its filename. Do **not** rely on GitHub as the primary working location for these spreadsheets; treat these backups as safety snapshots.

## Future enhancements

- **Automated sync**: Consider using Power Automate or another integration tool to regularly export specific tabs (e.g. service codes, vendor matrix) from the OneDrive workbooks into CSV and commit them here. This would provide history without interrupting JotForm.
- **Template conversion**: Over time, migrate configuration that rarely changes (e.g. status codes, escalation rules) from Excel into YAML or JSON files in this repository. This makes the platform more portable and avoids hard‑coding business logic inside spreadsheets.
- **Documentation**: Add detailed guides in the `docs/` folder for onboarding, daily operations, and troubleshooting. Include diagrams of the current automation flows and any new workflows introduced.

## Notes on JotForm integration

- JotForm currently reads and writes directly to specific sheets in your OneDrive/SharePoint workbooks (customer list, work‑order log, vendor matrix). As long as the file names and tab names remain unchanged, this integration should continue to function.
- If you decide to rename or restructure a workbook, create a copy with the new structure rather than overwriting the original. Update your JotForm forms and Power Automate flows to point to the new file/tab. Keep the old file in the `backups/` folder for reference.
- Should JotForm eventually support GitHub as a data source, you may revisit where the canonical data lives. For now, maintain OneDrive as the live data store and use GitHub for version control and documentation.

---

**Last updated:** August 30, 2025
