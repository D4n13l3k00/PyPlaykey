#!/bin/bash

if [ -n "$(git status --porcelain)" ]; then
    echo -e "${RED}${BOLD}[-] Repo has changes! Commiting...${RESET}"
    git config --global user.name 'Daniel'
    git config --global user.email 'D4n13l3k00@users.noreply.github.com'
    git commit -am "[CI/CD] Update client"
    git push
fi