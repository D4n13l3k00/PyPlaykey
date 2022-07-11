#!/bin/bash

source "./dependencies.sh"


delete_temp_dirs

echo -e "${BLUE}${BOLD}Downloading Playkey...${RESET}"
aria2c -q "https://static.playkey.net/clientdownload.aspx?file=windows-desktop/Release/PlaykeySetup.exe&name=pk.exe" -o temp/pk.exe

echo -e "${BLUE}${BOLD}Extracting client from installer...${RESET}"
innoextract -q -s -p1 -c1 temp/pk.exe
mv app client

echo -e "${BLUE}${BOLD}Packing client...${RESET}"
rm -rf client.7z
7z a -mx9 -r client.7z client/*

delete_temp_dirs

if [ -n "$CI" ]; then
    echo -e "${BLUE}${BOLD}CI/CD detected! Running ./actions_uploader.sh${RESET}"
    source "./actions_uploader.sh"
else
    echo -e "${GREEN}${BOLD}Done!${RESET}"
fi