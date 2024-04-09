ROLES = ['intern', 'barista', 'manager', 'supervisor', 'hr_manager']

ROLE_CHOICES = (
    ('intern', 'Стажер'),
    ('barista', 'Бариста'),
    ('manager', 'Менеджер'),
    ('supervisor', 'Управляющий'),
    ('hr_manager', 'Менеджер по персоналу'),
)

ROLE_HIERARCHY = {
    'intern': ['intern', 'barista', 'manager', 'supervisor', 'hr_manager'],
    'barista': ['barista', 'manager', 'supervisor', 'hr_manager'],
    'manager': ['manager', 'supervisor', 'hr_manager'],
    'supervisor': ['supervisor', 'hr_manager'],
    'hr_manager': ['hr_manager'],
}

ROLE_HIERARCHY_ACCESS = {
    'intern': ['intern'],
    'barista': ['barista'],
    'manager': ['intern', 'barista'],
    'supervisor': ['intern', 'barista', 'manager'],
    'hr_manager': ['intern', 'barista', 'manager', 'supervisor', 'hr_manager'],
}