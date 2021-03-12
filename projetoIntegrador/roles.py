from rolepermissions.roles import AbstractUserRole


class Produtor(AbstractUserRole):
    available_permissions = {
        'create_produtos': True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'create_produtos': True,
    }