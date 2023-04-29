
from backend.src.server import *


def display_all_lights():
    """
    Function that displays all the lights connected to the bridge
    """
    lights = get_all_lights()

    if len(lights) == 0:
        print("-"*60)
        print("Could not find any rooms!")
        print("-"*60)

    else:
        print("-"*60)
        print("Found the following lights...")
        print("-"*60)
        
        for light in lights:
            print(light)
        
        print("-"*60)
        print(f"Displays {len(lights)} of total {len(lights)} lights in system")
        print("-"*60)


def display_all_groups():
    """
    Function that displays all the light groups connected to the bridge
    """
    groups = get_all_groups()

    if len(groups) == 0:
        print("-"*60)
        print("Could not find any group!")
        print("-"*60)

    else:
        print("-"*60)
        print("Found the following groups...")
        print("-"*60)
        
        for group in groups:
            print(group)
        
        print("-"*60)
        print(f"Displays {len(groups)} of total {len(groups)} groups in system")
        print("-"*60)


def display_name_of_lamp():
    """
    Function that displays the name of a light
    """
    lights = get_name_of_lamp()

    lamp_id = int(input("Enter lamp-ID: "))

    if lamp_id > len(lights):
        print("-"*60)
        print(f"Could not find the lamp with ID: '{lamp_id}' in the system")
        print("-"*60)

    else:
        get_lamp_name = bridge.get_light(lamp_id, 'name')
        print("-"*60)
        print(f"| LampID: {lamp_id} | Name: {get_lamp_name} |")
        print("-"*60)


def display_name_of_group():
    """
    Function that displays the name of a group
    """
    group_names = get_name_of_group()

    group_id = int(input("Enter group-ID: "))

    if group_id > len(group_names):
        print("-"*60)
        print(f"Could not find the group with ID: '{group_id}' in the system")
        print("-"*60)

    else:
        get_group_name = bridge.get_group(group_id, 'name')
        print("-"*60)
        print(f"| GroupID: {group_id} | Name: {get_group_name} |")
        print("-"*60)


def display_turn_on_lamp():
    """
    Function that turn on lamp
    """
    lights = get_all_lights()

    lamp_name = input("Enter name of lamp: ")

    if lamp_name not in lights:
        print("-"*60)
        print(f"'Could not find the lamp '{lamp_name}' in the system")
        print("-"*60)

    else:
        turn_on = turn_on_lamp(lamp_name)
        print("-"*60)
        print(f"Successfully turned on '{lamp_name}'!")
        print("-"*60)


def display_turn_off_lamp():
    """
    Function that turn off lamp
    """
    lights = get_all_lights()

    lamp_name = input("Enter name of lamp: ")

    if lamp_name not in lights:
        print("-"*60)
        print(f"'Could not find the lamp '{lamp_name}' in the system")
        print("-"*60)

    else:
        turn_off = turn_off_lamp(lamp_name)
        print("-"*60)
        print(f"Successfully turned off '{lamp_name}'!")
        print("-"*60)


def display_set_brightness_lamp():
    """
    Function that set brightness for lamp
    """
    lights = get_all_lights()

    lamp_name = input("Enter name of lamp: ")

    if lamp_name not in lights:
        print("-"*60)
        print(f"'Could not find the lamp '{lamp_name}' in the system")
        print("-"*60)

    else:
        print("-"*60)
        print("Maximum brightness (100%) = 254")
        print("Medium brightness (50%) = 127")
        print("Minimum brightness (0%) = 0")
        print("-"*60)
        lamp_brightness = int(input("Enter brightness of lamp: "))
        set_brightness = set_brightness_lamp(lamp_name, lamp_brightness)
        print("-"*60)
        print(f"Successfully set brightness to {lamp_brightness}!")
        print("-"*60)


def display_turn_on_group():
    """
    Function that turn on group
    """
    groups = get_all_groups()

    group = input("Enter name of group: ")

    if group not in groups:
        print("-"*60)
        print(f"'Could not find the group '{group}' in the system")
        print("-"*60)

    else:
        turn_on = turn_on_group(group)
        print("-"*60)
        print(f"Successfully turned on '{group}'!")
        print("-"*60)


def display_turn_off_group():
    """
    Function that turn off group
    """
    groups = get_all_groups()

    group = input("Enter name of group: ")

    if group not in groups:
        print("-"*60)
        print(f"'Could not find the group '{group}' in the system")
        print("-"*60)

    else:
        turn_on = turn_off_group(group)
        print("-"*60)
        print(f"Successfully turned off '{group}'!")
        print("-"*60)


def display_set_brightness_group():
    """
    Function that set brightness for group
    """
    groups = get_all_groups()

    group = input("Enter name of group: ")

    if group not in groups:
        print("-"*60)
        print(f"'Could not find the group '{group}' in the system")
        print("-"*60)

    else:
        print("-"*60)
        print("Maximum brightness (100%) = 254")
        print("Medium brightness (50%) = 127")
        print("Minimum brightness (0%) = 0")
        print("-"*60)
        group_brightness = int(input("Enter brightness of group: "))
        set_brightness = set_brightness_group(group, group_brightness)
        print("-"*60)
        print(f"Successfully set brightness to {group_brightness}!")
        print("-"*60)


def display_menu():
    """
    Function displays menu options 
    """
    options = [
        'List all lights connected to bridge',
        'List all light groups connected to bridge',
        'Get the name of a specific lamp',
        'Get the name of a specific group',
        'Turn on specific lamp',
        'Turn off specific lamp',
        'Set brightness of specific lamp',
        'Turn on specific room',
        'Turn off specific room',
        'Set brightness of specific room',
        'Quit'
    ]
    print("-"*60)
    for index, option in enumerate(options, start=1):
        print(f'{index}. {option}')
    print("-"*60)


def display_error():
    """
    Function that displays error message
    """
    print("-"*60)
    print("Please enter a valid choice!")
    print("-"*60)


def display_quit():
    """
    Function that displays quit message
    """
    print("-"*60)
    print("Logging out...")
    print("-"*60)


def menu():
    """
    Function that contains the application
    """
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            display_all_lights()

        elif choice == "2":
            display_all_groups()
            
        elif choice == "3":
            display_name_of_lamp()

        elif choice == "4":
            display_name_of_group()
        
        elif choice == "5":
            display_turn_on_lamp()
        
        elif choice == "6":
            display_turn_off_lamp()

        elif choice == "7":
            display_set_brightness_lamp()

        elif choice == "8":
            display_turn_on_group()

        elif choice == "9":
            display_turn_off_group()

        elif choice == "10":
            display_set_brightness_group()

        elif choice == "11":
            display_quit()
            break
        
        else:
            display_error()


def app():
    """
    Function executes the application
    """
    menu()