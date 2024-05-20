import pyautogui
import pyperclip
import time
import re
import subprocess
import os

def read_and_process_file(input_file, js_template_file, js_modified_file):
    with open(input_file, 'r') as file, open(js_template_file, 'r') as template:
        lines = file.readlines()
        js_content = template.readlines()

    for line in lines:
        if line.strip():
            parts = line.split('|')
            if len(parts) > 1:
                hyperfind_name = parts[0].strip()
                schedule_groups = parts[1].strip().split('#')
                escaped_hyperfind_name = hyperfind_name.replace("'", "\\'") 

                # Modify the JavaScript file
                js_content[6] = f"const targetCell = document.querySelector('.ui-grid-cell-contents[title=\"{escaped_hyperfind_name}\"]');\n" 
                    # Write the modified JavaScript content to the file
                with open(js_modified_file, 'w') as modified_js:
                    modified_js.writelines(js_content)

                # Execute the GUI automation sequence
                automate_sequence(schedule_groups)
                print(f"{hyperfind_name} has been susccessfully created\n")
                with open('log.txt','a') as log_file:
                    log_file.write(f"{hyperfind_name} has been susccessfully created\n")

def automate_sequence(schedule_groups):
    # Open console
    pyautogui.click(1570, 1752)
    time.sleep(1)
    


    # Copy JS content to clipboard and paste it into the console
    subprocess.run(['clip.exe'], input=open('js_modified.txt', 'r').read().encode('utf-16'), check=True)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.rightClick(1703,1397)
    time.sleep(.25)
    pyautogui.click(1750,1431)

    # Close General Information
    pyautogui.click(79, 389)
    time.sleep(.5)

    # Open Scheduling and Schedule Group
    pyautogui.click(74, 633)
    time.sleep(.5)
    pyautogui.click(126, 693)
    time.sleep(.5)

    # Process each schedule group
    for group in schedule_groups:
        pyautogui.click(532, 537)
        time.sleep(.5)
        pyautogui.write(group)
        time.sleep(.5)
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(.5)

        # Select and move selected
        pyautogui.click(638, 581)
        time.sleep(1)
        pyautogui.click(935, 591)
        time.sleep(1)
        #Add
        pyautogui.click(727, 1377)
        time.sleep(1)
        #Remove Selected
        pyautogui.click(944, 729)
        time.sleep(1)     


        # Reset search bar
        pyautogui.click(532, 537)
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.5)
        pyautogui.press('backspace')
        time.sleep(.5)
        pyautogui.write('*')
        time.sleep(.5)

    # Apply and save
    pyautogui.click(1367,1787)
    time.sleep(.5)
    pyautogui.click(1235, 1787)
    time.sleep(2)

    # Validate the process
    pyautogui.click(87, 328, clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # wait for clipboard
    result = pyperclip.paste()
    if result == "HYPERFINDS":
        print("Processed successfully")
        
    else:
        print("Terminate program")
        exit()

# Run the automation
read_and_process_file('Input.txt', 'js.txt', 'js_modified.txt')
