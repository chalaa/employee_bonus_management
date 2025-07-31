from odoo import models, fields

class RejectBonusWizard(models.TransientModel):
    _name = 'reject.bonus.wizard'
    _description = 'Reject Bonus Wizard'

    rejection_reason = fields.Text(string='Rejection Reason', required=True)

    def confirm_rejection(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            bonus = self.env['hr.employee.bonus'].browse(active_id)
            bonus.write({
                'state': 'rejected',
                'rejection_reason': self.rejection_reason
            })
