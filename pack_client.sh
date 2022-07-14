#!/bin/bash

source "./dependencies.sh"


echo -e "${BLUE}${BOLD}Checking dependencies...${RESET}"
is_installed "aria2c"
is_installed "innoextract"
is_installed "7z"

if [ -n "$CI" ]; then
    echo -e "${BLUE}${BOLD}CI/CD detected!${RESET}"
fi

delete_temp_dirs

echo -e "${BLUE}${BOLD}Downloading Playkey...${RESET}"
aria2c -q "https://static.playkey.net/clientdownload.aspx?file=windows-desktop/Release/PlaykeySetup.exe&name=pk.exe" -o temp/pk.exe

echo -e "${BLUE}${BOLD}Extracting client from installer...${RESET}"
innoextract -q -s -p1 -c1 temp/pk.exe
mv app client

echo -e "${BLUE}${BOLD}Packing client...${RESET}"
rm -rf client.7z
7z a -mx9 -r client.7z client/*  > /dev/null 2>&1

delete_temp_dirs

echo -e "${GREEN}${BOLD}Done!${RESET}"