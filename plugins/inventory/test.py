#!/usr/bin/env python3
class InventoryModule(BaseInventoryPlugin):
    NAME = 'test'

    def verify_file(self, path):
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith('yaml') or path.endswith('yml'):
                valid = True
        return valid

    def parse(self, inventory, loader, path, cache=True):
       super(InventoryModule, self).parse(inventory, loader, path, cache)
       '''Return dynamic inventory from source '''
       self._read_config_data(path)
       self.inventory.add_group("test_hosts")
       self.inventory.add_host(host="192.168.3.61", group="test_hosts")
