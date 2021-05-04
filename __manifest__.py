{
    'name': 'PFA Advice in excel',
    'version': '1.0',
    'category': 'payroll',
    'sequence': 61,
    'summary': 'shows PFA Remittance  Advice in xlsx format',
    'description': "It shows PFA Remittance Advice in excel for given month",
    'author':'aswathy-modified by Adeniyi',
    'depends': ['base','hr', 'hr_payroll'],
    'data': ['wizard/pfa_report_wiz.xml'
      ],
    'installable': True,
    'auto_install': False,
    'application': False,
}