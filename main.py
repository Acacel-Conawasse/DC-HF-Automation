import pyautogui
import time
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

                # Modify the JavaScript file
                js_content[6] = f"const targetCell = document.querySelector('.ui-grid-cell-contents[title=\"{hyperfind_name}\"]');\n"
                with open(js_modified_file, 'w') as modified_js:
                    modified_js.writelines(js_content)

                # Execute the GUI automation sequence
                automate_sequence(schedule_groups)

def automate_sequence(schedule_groups):
    # Open console
    pyautogui.click(5866, 248)
    time.sleep(1)

    # Copy JS content to clipboard and paste it into the console
    subprocess.run(['clip.exe'], input=open('js_modified.txt', 'r').read().encode('utf-16'), check=True)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(10)

    # Close General Information
    pyautogui.click(3418, -671)
    time.sleep(.5)

    # Open Scheduling and Schedule Group
    pyautogui.click(3413, -506)
    time.sleep(.5)
    pyautogui.click(3488, -459)
    time.sleep(.5)

    # Process each schedule group
    for group in schedule_groups:
        pyautogui.click(3768, -575)
        time.sleep(.5)
        pyautogui.write(group)
        time.sleep(.5)
        pyautogui.press('tab')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(.5)

        # Select and move selected
        pyautogui.click(3803, -538)
        time.sleep(.5)
        pyautogui.click(4708, -532)
        time.sleep(.5)

        # Reset search bar
        pyautogui.click(3768, -575)
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.5)
        pyautogui.press('backspace')
        time.sleep(.5)
        pyautogui.write('*')
        time.sleep(.5)

    # Apply and save
    pyautogui.click(5701, 418)
    time.sleep(.5)
    pyautogui.click(5615, 427)
    time.sleep(2)

    # Validate the process
    pyautogui.click(3421, -705, clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # wait for clipboard
    result = pyautogui.paste()
    if result == "HYPERFINDS":
        print("Processed successfully")
    else:
        print("Terminate program")
        exit()

# Run the automation
read_and_process_file('Input.txt', 'js.txt', 'js_modified.txt')
