# List all the files in gre-images
import os

for root, dirs, files in os.walk('content'):
    for f in files:
        print(os.path.join(root, f).replace('\\','/'))