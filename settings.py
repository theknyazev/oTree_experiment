SECRET_KEY = 'morgenstern42' 
ADMIN_PASSWORD = 'password' 

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",                
)


SESSION_CONFIGS = [
    dict(
        name='wealth_tax',
        display_name="Wealth Tax Experiment",
        num_demo_participants=1,
        app_sequence=['wealth_tax'],
    ),
]

LANGUAGE_CODE = 'ru'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
