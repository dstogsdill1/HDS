# HDS CMMS Onboarding and Workflow Index

## Vendor Categories
The `VendorCategories` sheet lists each vendor with a category (specialty) and a **code** for easier reference.  These codes follow the format **X#**, where the letter represents the trade and the number distinguishes sub‑categories.  Categories are derived from the vendor’s **Specialty** column and the mapping is stored in `vendor_categories.csv`.

Example mapping:

| CategoryCode | CategoryName |
|-------------|-------------|
| **E1** | Electrical – General |
| **E2** | Electrical – Lighting |
| **E3** | Electrical – Controls/EMS |
| **H1** | HVAC – General |
| **H2** | HVAC – RTUs/Splits |
| **H3** | Heating – Gas/Electric |
| **R1** | Refrigeration – Rack/Compressor |
| **R2** | Refrigeration – Cases/Walk‑ins |
| **R3** | Refrigeration – Ice Machines |
| **P1** | Plumbing – General |
| **D1** | Doors/Docks/Overhead |
| **G1** | General Building/Handyman |
| **S1** | Signage/Glass |
| **C1** | Cleaning/Janitorial |
| **X9** | Other / Uncoded |


## Call Flow Steps
These steps summarise the call triage and dispatch process extracted from the HDS Call Flow Guide.

| StepCode | Description |
|---------|-------------|
| S001 | Greeting – answer with "HDS Service Desk—how may I help you?" |
| S002 | Determine caller type – service request vs general inquiry |
| S003 | Verify customer – existing or new; ask for store number or full address |
| S004 | Gather core details – caller name, callback number, store number, trade/equipment, issue description, priority (Emergency, Urgent, Routine), overtime authorization, PO/billing |
| S005 | Confirm & summarise – read back details and provide ticket ID and response time |
| S006 | Dispatch & escalation – based on priority; follow escalation chain |
| S007 | Triage questions – trade-specific questions (e.g., for refrigeration: running warm? products? wait 24 hrs? breaker checked? leakage?) |
| S008 | Emergency failsafe – instruct caller to call 911 first if life-safety emergency, then call HDS emergency line |
| S009 | Closing – thank caller and remind them of follow-up or status update |


## Onboarding Checklist
1. **Template copy:** For each new customer, duplicate `base_template_restructured_v2.xlsx` into a separate folder on SharePoint (e.g., `HDS_Work_Orders/CustomerXYZ/`).
2. **Form & flow setup:** Point JotForm/Power Automate to the duplicated workbook for that customer. The `WorkOrders` and `PurchaseOrders` sheets have `Customer ID` and `Vendor Number` fields for linking.
3. **Vendor and customer lists:** Use the `Vendors` and `Customers` sheets as master lists.  Add new entries here, ensuring each vendor has a `Vendor Number` and a `CategoryCode` matching the mapping table.
4. **Call flows:** Copy the `CallFlows` sheet (or `call_flows.csv`) into each customer’s workbook if you need customer-specific variations.  Otherwise, use the global call-flow index.
5. **Documentation:** Keep static configuration (CSV files, this guide, and any Python scripts) in the GitHub repo (`HDS`).  Commit changes there to maintain version history.

By following this structure, you can onboard new clients quickly while maintaining a single source of truth for categories and call flows.
