import subprocess
import pandas as pd

# List of files and cryptographic algorithms to be tested
files = ["10kb.txt", "10mb.txt", "100kb.jpg", "100mb.jpg", "10mb.mp4", "1gb.mp4"]
algorithms_to_test = [
    ('AES', 256),
    ('Blowfish', 128),
    ('ChaCha20', 256),
    ('Camellia', 256)
]

# Execute encryption tests
results = []
for file in files:
    for algo, key_size in algorithms_to_test:
        result = subprocess.run(['python', 'run_task.py', 'files/' + file, algo, str(key_size)],
                                capture_output=True, text=True)
        results.append(result.stdout.strip().split(','))

# The results list can then be processed further or saved to a file.
df = pd.DataFrame(results, columns=['File Path', 'File Size (bytes)', 'Algorithm', 'CPU Usage (sec)', 'Memory Usage (bytes)'])
with pd.ExcelWriter('results.xlsx', engine='openpyxl', mode='a') as writer:
    df.to_excel(writer, sheet_name='Sheet3', index=False)
