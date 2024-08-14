import os
import argparse


icon_names = ["original","candy", "hologram", "neon", "flutedGlass", "schoolbook", "colorful"]


def change_icon(icon_name: str):
    '''
    The changes the current icon used by the Arc Browser to the one specified 
    '''
    if icon_name not in icon_names:
        print(f"Error: '{icon_name}' is not a valid icon name. Choose from {', '.join(icon_names)}.")
        return
    
    cmd = f"defaults write company.thebrowser.Browser currentAppIconName {icon_name}"
    
    try:
        os.system(cmd)
        print(f"Icon changed to {icon_name}, restart arc next")
    except Exception as exc:
        print(type(exc), exc.args)


def main():
    parser = argparse.ArgumentParser(description="Change the Arc browser's icon.")
    parser.add_argument('action', choices=['set'], help="Action to perform.")
    parser.add_argument('iconName', choices=icon_names, help="Name of the icon to set.")
    
    args = parser.parse_args()

    if args.action == 'set':
        change_icon(args.iconName)

if __name__ == "__main__":
    main()