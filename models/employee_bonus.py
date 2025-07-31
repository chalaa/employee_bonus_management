from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    employee_bonus_ids = fields.One2many('hr.employee.bonus', 'employee_id', string='Employee Bonuses')
    total_bonus_amount = fields.Float(string='Total Bonus', compute='_compute_total_bonus')

    @api.depends('employee_bonus_ids.amount', 'employee_bonus_ids.state')
    def _compute_total_bonus(self):
        for emp in self:
            emp.total_bonus_amount = sum(
                b.amount for b in emp.employee_bonus_ids if b.state == 'approved'
            )
    
class EmployeeBonus(models.Model):
    _name = 'hr.employee.bonus'
    _description = 'Employee Bonus'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_id'
    _order = 'create_date desc'    
    
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    bonus_type = fields.Selection([
        ('performance', 'Performance'),
        ('holiday', 'Holiday'),
        ('other', 'Other')
    ], string='Bonus Type', required=True)
    amount = fields.Float(string='Amount', required=True)
    date_awarded = fields.Date(string='Date Awarded', default=fields.Date.today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'), 
        ('rejected', 'Rejected')
    ], default='draft', string='Status')    
    manager_id = fields.Many2one('hr.employee', string='Manager', compute='_compute_manager', store=True)
    
    is_manager = fields.Boolean(compute='_compute_is_manager', store=False)
    
    rejection_reason = fields.Text(string='Rejection Reason', readonly=True)

    @api.depends('employee_id')
    def _compute_manager(self):
        for record in self:
            record.manager_id = record.employee_id.parent_id
            
    @api.onchange('amount')
    def _check_amount(self):
        for record in self:
            if record.amount <= 0:
                raise ValidationError(_('Bonus amount must be greater than zero.'))
    
    
    
    @api.depends('employee_id')
    def _compute_is_manager(self):
        for record in self:
            record.is_manager = self.env.user.employee_id == record.employee_id.parent_id

    def action_submit(self):
        self.ensure_one()
        self.write({'state': 'submitted'})
        
    def action_approve(self):
        self.ensure_one()
        self.write({'state': 'approved'})

    def action_reject(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'reject.bonus.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_id': self.id
            }
        }


    

    @api.model
    def create(self, vals):
        return super().create(vals)