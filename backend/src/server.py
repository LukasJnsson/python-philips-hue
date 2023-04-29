
import os
from dotenv import load_dotenv
from phue import Bridge
load_dotenv()


# Bridge
bridge = Bridge(os.environ.get('BRIDGE_IP_ADRESS'))
bridge.connect()


def get_all_lights():
    """
    Function that fetch all the lights connected to the bridge
    """
    lights = []
    get_lights = bridge.lights

    for light in get_lights:
        lights.append(light.name)
    return lights


def get_all_groups():
    """
    Function that fetch all the light groups connected to the bridge
    """
    get_groups = bridge.get_group()
    groups = []
    for group in get_groups.items():
        groups.append(group[1])
    group_names = []
    for group in groups:
        group_names.append(group['name'])
    return group_names


def get_name_of_lamp():
    """
    Function that fetch the name of a specific light
    """
    get_lights = bridge.lights
    lights = []
    for light in get_lights:
        lights.append(light)
    return lights


def get_name_of_group():
    """
    Function that fetch the name of a specific light group
    """
    get_groups = bridge.get_group()
    groups = []
    for group in get_groups.items():
        groups.append(group[1])
    group_names = []
    for group in groups:
        group_names.append(group['name'])
    return group_names


def turn_on_lamp(lamp_name):
    """
    Function that turn on lamp
    """
    bridge.set_light(lamp_name, 'on', True)


def turn_off_lamp(lamp_name):
    """
    Function that turn off lamp
    """
    bridge.set_light(lamp_name, 'on', False)


def set_brightness_lamp(lamp_name, lamp_brightness):
    """
    Function that set the brightness for a specific light
    """
    bridge.set_light(lamp_name, 'bri', lamp_brightness)


def turn_on_group(group):
    """
    Function that turn on group
    """
    bridge.set_group(group, 'on', True)


def turn_off_group(group):
    """
    Function that turn on off
    """
    bridge.set_group(group, 'on', False)


def set_brightness_group(group, group_brightness):
    """
    Function that set the brightness for a specific room
    """
    bridge.set_group(group, 'bri', group_brightness)


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

    bridge = Bridge(os.environ.get('BRIDGE_IP_ADRESS'))
    bridge.connect()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            get_all_lights()

        elif choice == "2":
            get_all_groups()
            
        elif choice == "3":
            get_name_of_lamp()

        elif choice == "4":
            get_name_of_group()
        
        elif choice == "5":
            turn_on_lamp()
        
        elif choice == "6":
            turn_off_lamp()

        elif choice == "7":
            set_brightness_lamp()

        elif choice == "8":
            turn_on_group()

        elif choice == "9":
            turn_off_group()

        elif choice == "10":
            set_brightness_group()

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