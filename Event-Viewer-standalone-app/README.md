# Windows Event Log Viewer

This application provides a graphical interface for querying and reviewing Windows Event Logs.  
It supports filtering by date range, event type, and event ID, and can display events from the following logs:

## Features

### Log Sources
- Application
- System
- Security
- Setup

### Event Filtering
- By Date and Time Range
- By Event Types:
  - Error
  - Warning
  - Information
  - Success Audit
  - Failure Audit
- By Specific Event IDs  
  (comma-separated list for precise filtering)

### Displayed Event Details
- Event ID
- Source
- Level:
  - Error
  - Warning
  - Information
  - Success Audit
  - Failure Audit
- Timestamp
- User
- Message

### Export to CSV
- Export filtered event results for further analysis


## Requirements
- All Python package dependencies are listed in the `requirements.txt` file
