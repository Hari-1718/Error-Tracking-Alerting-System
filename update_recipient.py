import os

env_path = r'backend\.env'
new_line = 'ALERT_RECIPIENT=hariprasadchinimilli18@gmail.com'
key = 'ALERT_RECIPIENT'

lines = []
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

processed_lines = []
found = False
for line in lines:
    if line.strip().startswith(key + '='):
        processed_lines.append(new_line + '\n')
        found = True
    else:
        processed_lines.append(line)

if not found:
    if processed_lines and not processed_lines[-1].endswith('\n'):
        processed_lines.append('\n')
    processed_lines.append(new_line + '\n')

with open(env_path, 'w', encoding='utf-8') as f:
    f.writelines(processed_lines)

print("Updated ALERT_RECIPIENT successfully")
