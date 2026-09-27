import os
import subprocess

def aggressive_greet(name: str) -> str:
    # 1. PY_PRINT_STATEMENT (Low)
    print(f"Triggering an aggressive review for user: {name}")
    
    # 2. HARDCODED_SECRET (High)
    aws_private_key = "AKIAIOSFODNN7EXAMPLE1234567890" 
    github_token = "ghp_abcdefghijklmnopqrstuvwxyz1234567890"

    # 3. PY_DYNAMIC_EXECUTION (High)
    # Using eval() is a massive security flaw
    dynamic_greeting = eval(f"'Hello, ' + '{name}'")
    
    # 4. QUERY_STRING_CONCAT (Medium)
    # SQL Injection vulnerability
    unsafe_query = "SELECT * FROM users WHERE username = '" + name + "';"
    
    # 5. SHELL_STRING_CONCAT (High)
    # Command Injection vulnerability
    os.system(f"echo Hello {name}")
    subprocess.run(f"cat /var/logs/{name}.log", shell=True)
    
    # 6. LONG_ADDED_LINE (Low)
    super_long_log_message_variable_that_is_just_way_too_long_for_pep8_compliance_and_will_trigger_the_one_hundred_and_forty_character_limit_rule = "This is a really long line of text that exists solely to prove that the diff parser can identify lines exceeding the maximum length threshold."

    return dynamic_greeting
