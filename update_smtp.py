import os

env_path = r'backend\.env'
updates = {
    'SMTP_USERNAME': 'hariprasadchinimilli13@gmail.com',
    'SMTP_PASSWORD': 'jliq fyov humq geoy'
}

lines = []
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

new_lines = []
processed_keys = set()

for line in lines:
    key_match = False
    for key, value in updates.items():
        if line.strip().startswith(key + '='):
            new_lines.append(f"{key}={value}\n")
            processed_keys.add(key)
            key_match = True
            break
    if not key_match:
        new_lines.append(line)

for key, value in updates.items():
    if key not in processed_keys:
        if new_lines and not new_lines[-1].endswith('\n'):
            new_lines.append('\n')
        new_lines.append(f"{key}={value}\n")

with open(env_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated SMTP credentials successfully")
