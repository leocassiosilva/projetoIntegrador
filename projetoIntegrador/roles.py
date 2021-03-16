from rolepermissions.roles import AbstractUserRole


class Vendedor(AbstractUserRole):
    available_permissions = {
        'create_vendedor': True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'create_cliente': True,
    }