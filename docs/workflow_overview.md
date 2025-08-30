# HDS Workflow Overview (Simplified)

This guide explains the basic way that Homeland Development Services (HDS) manages its **live data**, **configuration files**, and **documentation**. It is meant for anyone who needs to understand how the system is organised.

## 1. Where data lives

**Live data – OneDrive/SharePoint**

- Service requests, customer lists, vendor lists, work‑order logs and call‑flow guides are stored as Excel workbooks in OneDrive/SharePoint.
- These spreadsheets are used by JotForm and Power Automate.  **Do not rename or restructure them** unless instructed to do so, because automations depend on their names and columns.
- If you need to change a live workbook (e.g., add a new column), **make a copy** first, adjust the flows to use the new file, and then archive the old version.

**Configuration & documentation – GitHub**

- A separate GitHub repository (`dstogsdill1/HDS`) holds static configuration and documentation.  This repo contains:
  - CSV versions of tables (status codes, vendor categories, etc.) under `config/csv/`.
  - Scripts (e.g., `scripts/convert_excel_to_csv.py`) to convert Excel sheets into CSV files.
  - Markdown documents in `docs/` that describe how things work and how to update them.
  - A backup copy of important Excel workbooks in another repo (`dstogsdill1/HDS‑Knowledge‑Base`).
- You should update and commit files in GitHub whenever configuration changes.  This gives you a history of who changed what and why.

## 2. How to fetch and store information

- Use the **SharePoint connector** to search for files (e.g., "customer list"), fetch workbooks and check for new or updated files.  If a workbook is updated, export any non‑changing tables to CSV and commit them to GitHub.
- Use the **Teams connector** to search chats for workflow discussions and decisions.  Document any important information in the `docs/` folder.
- Use **GitHub** to store CSV files, scripts and documentation.  You cannot upload files via the API, so you will use the browser (via the computer tool) to create or edit files in the repository.
- Use the **Google Drive connector** only when specifically told to fetch marketing assets or other static documents.

## 3. Typical workflow for updates

1. **Identify a change** – For example, a new vendor category needs to be added or a status code is changed.
2. **Download the workbook** – Fetch the relevant Excel file from SharePoint.
3. **Update and test** – Make changes in a copy of the live workbook.  Test that JotForm and Power Automate flows still work.
4. **Export static data to CSV** – Use `convert_excel_to_csv.py` to export any updated tables to CSV files under `config/csv/`.
5. **Commit to GitHub** – In the GitHub repository, create or update the corresponding CSV and documentation files.  Include a clear commit message describing the change.
6. **Document the change** – Add a note to the `docs/` folder describing what changed, why, and any follow‑up actions.

## 4. What not to do

- **Do not** modify JotForm forms or Power Automate flows unless the user explicitly asks you to.  Focus on the data and configuration they depend on.
- **Do not** rename or delete files that are currently used by automations.
- **Do not** expose passwords or personal data from the spreadsheets or emails.

Following this pattern ensures that the live system continues to run smoothly while changes are properly tracked.  For more detailed procedures, see the individual documents in the `docs/` folder.
