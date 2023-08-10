import os

def truncate_log(log_path, num_lines=100):
    try:
        with open(log_path, 'r') as log_file:
            lines = log_file.readlines()
        
        if len(lines) > num_lines:
            truncated_lines = lines[-num_lines:]
            
            with open(log_path, 'w') as log_file:
                log_file.writelines(truncated_lines)
            
            print(f"Truncated {log_path} to {num_lines} lines.")
        else:
            print(f"{log_path} has less than {num_lines} lines, not truncated.")
    except FileNotFoundError:
        print(f"{log_path} not found.")

def find_largest_log(directory):
    largest_size = 0
    largest_log = None

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'x.log':
                log_path = os.path.join(root, file)
                size = os.path.getsize(log_path)
                if size > largest_size:
                    largest_size = size
                    largest_log = log_path

    return largest_log

log_directory = '/path/to/log/directory'
largest_log = find_largest_log(log_directory)

if largest_log:
    truncate_log(largest_log)
