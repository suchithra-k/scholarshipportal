class UserConstant:

    # Roles
    ROLE_ADMIN = 1
    ROLE_ORGANISATION_ADMIN = 2
    ROLE_STUDENT = 3

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    YEAR_CHOICES = (
        (0, '---'),
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
    )

    CASTE_CHOICES = (
        ('', '---'),
        ('OC', 'OC'),
        ('BC', 'BC'),
        ('MBC', 'MBC'),
        ('BCM', 'BCM'),
        ('SC', 'SC'),
        ('ST', 'ST')
    )
