# This script updates the version number in all Python files from "Version: Beta 0.1" to "Version: Beta 0.2"

#!/bin/bash
for file in *.py; do
  sed -i '' 's/Version: Beta 0.1/Version: Beta 0.2/g' "$file"
done