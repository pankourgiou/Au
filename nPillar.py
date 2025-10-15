#!/usr/bin/env python3

import subprocess
import os

# Remove existing nanopillar files
for filename in os.listdir('.'):
    if filename.startswith('nanopillar'):
        os.remove(filename)

# Build the command as a list of arguments
atomsk_command = [
    "atomsk",
    "--create", "fcc", "4.08", "Au",
    "-duplicate", "40", "40", "40",
    "-select", "out", "cylinder", "z", "box/2", "box/2", "50.0",
    "-cut", "above", "10.0", "z",
    "nanopillar.xsf", "cfg"
]

# Execute the command
try:
    subprocess.run(atomsk_command, check=True)
    print("Nanopillar generated successfully!")
except subprocess.CalledProcessError as e:
    print("Error while generating nanopillar:", e)
#!/usr/bin/env python3

import subprocess
import os

# Remove existing nanopillar files
for filename in os.listdir('.'):
    if filename.startswith('nanopillar'):
        os.remove(filename)

# Build the command as a list of arguments
atomsk_command = [
    "atomsk",
    "--create", "fcc", "4.08", "Au",
    "-duplicate", "40", "40", "40",
    "-select", "out", "cylinder", "z", "box/2", "box/2", "50.0",
    "-cut", "above", "10.0", "z",
    "nanopillar.xsf", "cfg"
]

# Execute the command
try:
    subprocess.run(atomsk_command, check=True)
    print("Nanopillar generated successfully!")
except subprocess.CalledProcessError as e:
    print("Error while generating nanopillar:", e)
#!/usr/bin/env python3

import subprocess
import os

# Remove existing nanopillar files
for filename in os.listdir('.'):
    if filename.startswith('nanopillar'):
        os.remove(filename)

# Build the command as a list of arguments
atomsk_command = [
    "atomsk",
    "--create", "fcc", "4.08", "Au",
    "-duplicate", "40", "40", "40",
    "-select", "out", "cylinder", "z", "box/2", "box/2", "50.0",
    "-cut", "above", "10.0", "z",
    "nanopillar.xsf", "cfg"
]

# Execute the command
try:
    subprocess.run(atomsk_command, check=True)
    print("Nanopillar generated successfully!")
except subprocess.CalledProcessError as e:
    print("Error while generating nanopillar:", e)
#!/usr/bin/env python3

import subprocess
import os

# Remove existing nanopillar files
for filename in os.listdir('.'):
    if filename.startswith('nanopillar'):
        os.remove(filename)

# Build the command as a list of arguments
atomsk_command = [
    "atomsk",
    "--create", "fcc", "4.08", "Au",
    "-duplicate", "40", "40", "40",
    "-select", "out", "cylinder", "z", "box/2", "box/2", "50.0",
    "-cut", "above", "10.0", "z",
    "nanopillar.xsf", "cfg"
]

# Execute the command
try:
    subprocess.run(atomsk_command, check=True)
    print("Nanopillar generated successfully!")
except subprocess.CalledProcessError as e:
    print("Error while generating nanopillar:", e)
#!/usr/bin/env python3

import subprocess
import os

# Remove existing nanopillar files
for filename in os.listdir('.'):
    if filename.startswith('nanopillar'):
        os.remove(filename)

# Build the command as a list of arguments
atomsk_command = [
    "atomsk",
    "--create", "fcc", "4.08", "Au",
    "-duplicate", "40", "40", "40",
    "-select", "out", "cylinder", "z", "box/2", "box/2", "50.0",
    "-cut", "above", "10.0", "z",
    "nanopillar.xsf", "cfg"
]

# Execute the command
try:
    subprocess.run(atomsk_command, check=True)
    print("Nanopillar generated successfully!")
except subprocess.CalledProcessError as e:
    print("Error while generating nanopillar:", e)
#!/usr/bin/env python3

import subprocess
import os

# Remove existing nanopillar files
for filename in os.listdir('.'):
    if filename.startswith('nanopillar'):
        os.remove(filename)

# Build the command as a list of arguments
atomsk_command = [
    "atomsk",
    "--create", "fcc", "4.08", "Au",
    "-duplicate", "40", "40", "40",
    "-select", "out", "cylinder", "z", "box/2", "box/2", "50.0",
    "-cut", "above", "10.0", "z",
    "nanopillar.xsf", "cfg"
]

# Execute the command
try:
    subprocess.run(atomsk_command, check=True)
    print("Nanopillar generated successfully!")
except subprocess.CalledProcessError as e:
    print("Error while generating nanopillar:", e)
