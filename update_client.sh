#!/bin/bash

source "./dependencies.sh"

echo -e "${BLUE}${BOLD}Checking dependencies...${RESET}"
is_installed "aria2c"
is_installed "7z"

echo -e "${BLUE}${BOLD}Downloading latest client...${RESET}"
aria2c -q "https://github.com/D4n13l3k00/PyPlaykey/releases/download/latest/client.7z" -o client.7z

echo -e "${BLUE}${BOLD}Removing old client...${RESET}"
rm -rf client

echo -e "${BLUE}${BOLD}Extracting client...${RESET}"
7z x -y client.7z  > /dev/null 2>&1
rm -rf client.7z

echo -e "${BLUE}${BOLD}Done!${RESET}"

