{
    'name': 'Employee Bonus',
    'version': '1.0',
    'depends': ['hr','mail'],
    'author': 'Chala Olani',
    'category': 'Human Resources',
    'summary': 'Manage Employee Bonuses with Approval Workflow',
    'data': [
        'security/ir.model.access.csv',
        'security/bonus_record_rule.xml',
        'views/employee_bonus_views.xml',
        'wizards/bonus_rejection_wizard_view.xml',
    ],
    'installable': True,
    'application': False,
}
