# Automation and Integration Plan

## Purpose
This document outlines how to maintain the HDS knowledge base, integrate data sources, and automate key processes while keeping live operational data in OneDrive/SharePoint.

## JotForm & Service Request Integration
- Service requests are captured via JotForm forms.
- Use Power Automate to monitor JotForm submissions and append new rows to the *Work Order* Excel file in SharePoint.
- Avoid renaming or moving the original workbook used by JotForm; if changes are necessary, duplicate the workbook, update your flows to point to the new file, test thoroughly, then deprecate the old workbook.

## Static Configuration Export
- Non-changing tables (status codes, vendor categories, default priorities) should be exported from Excel to CSV and stored in the `/config/csv/` folder of this repository.
- Use the `scripts/convert_excel_to_csv.py` script to export worksheets to CSV. Example usage:
  ```
  python scripts/convert_excel_to_csv.py --input path/to/workbook.xlsx --sheet "Sheet Name" --output config/csv/sheet_name.csv
  ```
- Review and commit the generated CSV files to version control.

## GitHub Backup & Versioning
- For each update to a workbook that contains configuration data, commit the updated CSV and increment the version tag or commit message.
- Use release tags to package seed data and configuration for deployment or for onboarding new customers.

## Monitoring & Maintenance
- Regularly review new documents added to SharePoint. If a file is part of your static configuration, back it up into the `backups/` folder or export it to CSV as appropriate.
- Keep documentation up to date in the `/docs/` folder with explanations of flows, integration points, and changes.
