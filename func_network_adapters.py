import wmi

# Create a WMI object for the network adapter class
wmi_config = wmi.WMI().Win32_NetworkAdapterConfiguration()

# Check if at least one network adapter is enabled
def is_adapter_enabled():
    for c in wmi_config:
        if c.IPEnabled:
            return True
    return False

# Return the index and name of all enabled adapters
def get_enabled_adapters():
    adapters = []
    for n in wmi_config:
        if n.IPEnabled:
            adapters.append((n.Index, n.Caption))
    return adapters

# Disable all enabled adapters and keep a list of their indexes
def disable_adapters():
    disabled_indexes = []
    for n in wmi_config:
        if n.IPEnabled:
            disabled_indexes.append(n.Index)
            n.Disable()
    return disabled_indexes

# Enable all adapters with the given indexes
def enable_adapters(indexes):
    for n in wmi_config:
        if n.Index in indexes:
            n.Enable()
