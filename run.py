from func_network_adapters import *

if is_adapter_enabled():
    print("At least one adapter is enabled")
else:
    print("No adapter is enabled")

adapters = get_enabled_adapters()
for adapter in adapters:
    print(f"Index: {adapter[0]}, Name: {adapter[1]}")

disabled_indexes = disable_adapters()
print(f"{len(disabled_indexes)} adapters disabled: {disabled_indexes}")

enable_adapters(disabled_indexes)
print(f"{len(disabled_indexes)} adapters enabled")


