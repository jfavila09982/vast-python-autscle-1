#!/usr/bin/env python3

import subprocess
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('VAST_API_KEY')
#print(f'API Key: {api_key}')

def show_instances(api_key):
    command = ['../vast_cli/vast.py', 'show', 'instances', '--api-key', api_key, '--raw']
    
    try:
        command_output = subprocess.run(command, capture_output=True, text=True)

        

        return command_output.stdout
    except Exception as e:
        return f"An error occured {e}"
    

def show_machines(api_key):
    command = ['../vast_cli/vast.py', 'show', 'machines', '--api-key', api_key, '--raw']
    
    try:
        command_output = subprocess.run(command, capture_output=True, text=True)
        return command_output.stdout
    except Exception as e:
        return f"An error occured {e}"
        
print_instances = show_instances(api_key)
print_machines = show_machines(api_key)

print(print_instances)
#print(print_machines)