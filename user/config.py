from django.core.validators import RegexValidator

gender_type = [
    ('man','مرد'),
    ('female','زن')
]
phone_regex = RegexValidator(regex=r'^9\d{9}$',
                                 message="شماره تماس باید با فرمت ۹۱۲۷۸۹۳۴۵۶ وارد شود")