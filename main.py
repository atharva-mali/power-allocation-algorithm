# Power Allocation Algorithm
# ==========
#
# Initialize
# MAX_CAPACITY = 92
# Initialize
# devices = [] // List
# to
# store
# active
# devices(FIFO
# queue)
# Initialize
# total_power_consumed = 0
#
# Function
# connect_device(device_id, requested_power):
# If
# requested_power > 40:
# requested_power = 40 // Maximum
# device
# capacity is 40
# units
#
# available_power = MAX_CAPACITY - total_power_consumed
#
# If
# requested_power <= available_power:
# allocate_power = requested_power
# Else:
# allocate_power = available_power
#
# Add
# {device_id, allocate_power, requested_power}
# to
# devices
# total_power_consumed += allocate_power
#
# Return
# allocate_power
#
# Function
# disconnect_device(device_id):
# For
# device in devices:
# If
# device.id == device_id:
# total_power_consumed -= device.allocated_power
# Remove
# device
# from devices
#
# redistribute_power()
# Break
#
# Function
# change_consumption(device_id, new_requested_power):
# If
# new_requested_power > 40:
# new_requested_power = 40
#
# For
# device in devices:
# If
# device.id == device_id:
# delta_power = new_requested_power - device.allocated_power
# If
# total_power_consumed + delta_power <= MAX_CAPACITY:
# device.allocated_power = new_requested_power
# total_power_consumed += delta_power
# Else:
# redistribute_power()
# Break
#
# Function
# redistribute_power():
# available_power = MAX_CAPACITY - total_power_consumed
# For
# device in devices:
# If
# device.requested_power > device.allocated_power:
# extra_power = min(available_power, device.requested_power - device.allocated_power)
# device.allocated_power += extra_power
# available_power -= extra_power
# If
# available_power == 0:
# Break
#
# Function
# print_status():
# For
# device in devices:
# Print
# "Device", device.id, "Allocated Power:", device.allocated_power, "Requested Power:", device.requested_power


# Implementation
# ==========


MAX_CAPACITY = 92
devices = []  # List to store active devices in FIFO order
total_power_consumed = 0


def connect_device(device_id, requested_power):
    global total_power_consumed
    requested_power = min(requested_power, 40)  # Max device capacity is 40
    available_power = MAX_CAPACITY - total_power_consumed

    allocate_power = min(requested_power, available_power)
    devices.append({"id": device_id, "allocated_power": allocate_power, "requested_power": requested_power})
    total_power_consumed += allocate_power

    return allocate_power


def disconnect_device(device_id):
    global total_power_consumed
    for device in devices:
        if device["id"] == device_id:
            total_power_consumed -= device["allocated_power"]
            devices.remove(device)
            redistribute_power()
            break


def change_consumption(device_id, new_requested_power):
    global total_power_consumed
    new_requested_power = min(new_requested_power, 40)

    for device in devices:
        if device["id"] == device_id:
            delta_power = new_requested_power - device["allocated_power"]
            if total_power_consumed + delta_power <= MAX_CAPACITY:
                device["allocated_power"] = new_requested_power
                total_power_consumed += delta_power
            else:
                device["requested_power"] = new_requested_power
                redistribute_power()
            break


def redistribute_power():
    global total_power_consumed
    available_power = MAX_CAPACITY - total_power_consumed

    for device in devices:
        if device["requested_power"] > device["allocated_power"]:
            extra_power = min(available_power, device["requested_power"] - device["allocated_power"])
            device["allocated_power"] += extra_power
            available_power -= extra_power
            if available_power == 0:
                break


def print_status():
    for device in devices:
        print(f"Device {device['id']} | Allocated: {device['allocated_power']} | Requested: {device['requested_power']}")


# Example usage
connect_device("A", 40)
connect_device("B", 40)
connect_device("C", 40)
print_status()
change_consumption("A", 20)
disconnect_device("B")
print_status()