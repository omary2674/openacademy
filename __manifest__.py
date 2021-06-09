{
    'name': "Open Academy",
    'version': '14.0.01',
    'depends': ['base', 'mail', 'sale', 'report_xlsx'],
    'author': "Mohammad Omari",
    'website': "adawliah.com",
    'category': 'Category',
    'description': """
        Open Academy module for managing traning:
        - training courses
        - training session
        - attendees registration 
    """,
    'installable': True,
    # data files always loaded at installation
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/res_partner.xml',
        'reports/custom_header_footer.xml',
        'reports/paperformat.xml',
        'reports/reports.xml',
        'data/email_template.xml',
        'data/ir_cron.xml',
        'data/ir_sequence.xml',
        'reports/sale_qweb_template.xml',
        'views/res_config_settings.xml',
        'wizard/report_wizard_view.xml',
        'reports/openacademy_pdf_report.xml',
        'reports/openacademy_xlsx_report.xml',
        'views/product_sale_analysis.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}
