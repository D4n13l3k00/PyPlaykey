#!/bin/bash

RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
MAGENTA="\033[0;35m"
CYAN="\033[0;36m"

BOLD="\033[1m"
LIGHT="\033[2m"

RESET="\033[0m"

echo -e "${CYAN}${BOLD}PyPlaykey by @D4n13l3k00${RESET}"

function is_installed() {
    if [ -z "$(command -v $1)" ]; then
        echo -e "${RED}${BOLD}[-] $1 is not installed${RESET}"
        exit 1
    else
        echo -e "${GREEN}${BOLD}[+] $1 is installed${RESET}"
    fi
}

function delete_temp_dirs() {
    echo -e "${YELLOW}${BOLD}Removing temp dirs...${RESET}"
    rm -rf temp
    rm -rf client
}

echo -e "${BLUE}${BOLD}Running $0${RESET}"