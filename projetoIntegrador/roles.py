from rolepermissions.roles import AbstractUserRole


class Produtor(AbstractUserRole):
    available_permissions = {
        'create_produtos': True,
    }
