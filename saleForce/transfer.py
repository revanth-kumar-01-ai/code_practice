
{
  "name": "saleforce_Routine_Transfer",
  "description": "Delta + Compliance validation for Transfer",
  "properties": {
    "input_path": "G:\\Prithviraj",
    "input_files": {
      "saleforce_curr_week_report": "benefact_security_prod_700_20260602_050058.csv",
      "saleforce_next_week_report": "benefact_security_prod_700_20260608_050113.csv",
      "identity_active_report": "IAM OPS & NASCO_Termination 06-01.xlsx",
      "transfer_report" : "BCBSMA_Job_Profile_Changes_CIS_2026-05-25-2026-06-01.csv",
      "sharepoint_compaign_file": "RC20260602135712_CampaignRecords 5-25 to 6-01.xlsx"
    },
    "output_path": "G:\\Prithviraj\\output\\output_saleforce_transfer.xlsx",
    "save_delta": false
  },
  "delta": "saleforce_transfer_delta.py",
  "validator": null,
  "notify": {
    "email": {
      "to": [
        "admin@company.com"
      ]
    }
  },
  "log_cloudwatch": true
}
