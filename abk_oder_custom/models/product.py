from odoo import models, fields, api


class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    abk_uom_class_id = fields.Char('UOM Class')
    abk_ium = fields.Char('Inventory UM')
    abk_sales_um = fields.Char('Sales UM')
    abk_purchase_UM = fields.Char('Purchase UM')
    abk_prod_code = fields.Char('Group')
    abk_class_id = fields.Char('Class')
    abk_commodity_code = fields.Char('HS Commodity Code')
    abk_on_hold = fields.Char('Hold')
    abk_on_hold_date = fields.Char('Hold Date')
    abk_on_hold_reason_code = fields.Char('Hold Reason Code')
    abk_track_lots = fields.Char('Track Lots')
    abk_track_dimension = fields.Char('Track Dimension UOMs')
    abk_non_stock = fields.Char('Non-Stock Item')
    abk_inactive = fields.Char('Inactive')
    abk_mfg_comment = fields.Char('Manufacturing Comment')
    abk_pur_comment = fields.Char('Purchase Comment')
    abk_brand = fields.Char('Brand')
    abk_sub_brand = fields.Char('Sub-Brand')
    abk_co_warehouse = fields.Char('CO Warehouse')
    abk_grs_weight = fields.Char('GRS Weight(g)')
    abk_fsc_paper_weight = fields.Char('FSC Paper Weight (kg)')
    abk_fsc_claim = fields.Char('FSC Claim')
    abk_agent = fields.Char('Agent')
    abk_fk_lookup = fields.Char('F/K Lookup')
    abk_wo_salesman = fields.Char('WO-Salesman')
    abk_plant = fields.Char('Site')
    abk_prim_whse = fields.Char('Primary Warehouse')
    abk_minimum_qty = fields.Integer('Min On-Hand')
    abk_maximum_qty = fields.Integer('Max On-Hand')
    abk_safety_qty = fields.Char('Safety Stock')
    abk_reorder_level = fields.Integer('Re-Order to Max')
    abk_minorder_qty = fields.Integer('Min Order Qty')
    abk_lead_time = fields.Datetime('Lead Time')
    abk_production_lead_time = fields.Datetime('Production Lead Time')
    abk_generate_sugg = fields.Char('Generate PO Suggestions')
    abk_backflush = fields.Char('BackFlush')
    abk_prim_bin_num = fields.Char('Bin')

    abk_part_length = fields.Float('Part Length')
    abk_part_height = fields.Float('Part Height')
    abk_part_width = fields.Float('Part Width')

    # existing
    abk_part_num = fields.Char('Part')
    abk_part_description = fields.Text('Description')
    abk_type_code = fields.Char('Type')

