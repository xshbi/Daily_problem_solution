#!/bin/bash

# Ask the user for the number of tabs to open
read -p "Enter the number of tabs you want to open: " num_tabs

# Loop to open the specified number of tabs
for ((i=1; i<=num_tabs; i++))
do
    xdg-open about:newtab
done

echo "Opened $num_tabs tabs."
