# Employee Bonus Management

This Odoo module enables organizations to manage employee bonuses with a transparent approval workflow, role-based access, and audit trail.

## Features

- **Bonus Request Creation:** HR can Create the Request and Employees manager can Approve and the Employee Can only view
- **Approval Workflow:** Bonuses move through Draft, Submitted, Approved, and Rejected states.
- **Role-Based Actions:** Managers can approve or reject submitted bonuses; employees can submit requests.
- **Rejection Reason:** When rejecting a bonus, managers must provide a reason via a wizard.
- **Security & Access Control:** Employees see only their own bonuses or those of their direct reports (except drafts); HR managers see all bonuses.
- **Audit Trail:** All actions are tracked via Odoo's chatter.
- **Bonus Overview:** Employees' total approved bonus amount is displayed on their profile.

## Installation

1. Copy the `employee_bonus_management` folder to your Odoo `addons` directory.
2. Update the app list in Odoo.
3. Install the **Employee Bonus Management** module from the Apps menu.

## Usage

- Go to **Employees** and open the "Bonuses" tab to view and manage bonuses.
- Create a new bonus request from the employee profile or the "Employee Bonus" menu.
- Submit the request for approval.
- HR managers can approve or reject submitted requests.
- If rejected, a wizard will prompt for the rejection reason.
- The status and rejection reason are visible in the bonus record.

## Security & Access

- **Employee Rule:** Employees see only their own bonuses or those of their direct reports, except for drafts.
  - See [`security/bonus_record_rule.xml`](security/bonus_record_rule.xml)
- **HR Manager Rule:** HR managers see all bonus records.
- Access rights are defined in [`security/ir.model.access.csv`](security/ir.model.access.csv).

## Configuration

- Ensure the `hr` and `mail` modules are installed.
- No additional configuration is required.

## File Structure
employee_bonus_management/   
├── models/   
│   └── employee_bonus.py   
├── views/   
│   └── employee_bonus_views.xml   
├── wizards/   
│   ├── bonus_rejection_wizard.py   
│   └── bonus_rejection_wizard_view.xml   
├── security/   
│   ├── ir.model.access.csv   
│   └── bonus_record_rule.xml   
├── static/   
│   └── module requirement/   
│       └── 4_5792034776164603656.docx   
├── __init__.py   
└── __manifesst__.py   

 


## Author

Chala Olani

## License

See Odoo licensing terms.
