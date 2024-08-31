#!/bin/bash

# Función para el primer menú
# Take_a_look        ->  Join without log_in
# Log_in Info        ->  Put the info
# Exit        ->  Left App
function main_menu() {
    echo -e "\nWelcome to the App Storage\n"
    PS3="Select an option: "
    select option in "Take_a_look" "Log_in" "Exit"; do
        case $REPLY in
            1) menu_Only_look; break ;;
            2) menu_Clients; break ;;
            3) echo "Exit..."; exit 0 ;;
            *) echo "Invalid Option. Try again." ;;
        esac
    done
}

# Funtion for guets
# Status            ->  Info storage(s) with his packages
# General Info      ->  App Info 
# Return            ->  return to main menu
function menu_Only_look() {
    echo -e "\nGuest Menu:\n"
    PS3="Select an option: "
    select subopcion in "Status" "General_Info" "Return"; do
        case $REPLY in
            1) echo "Status has been selected"; break ;;
            2) echo "General_Info has been selected"; break ;;
            3) main_menu; break ;;
            *) echo "Invalid Option. Try again." ;;
        esac
    done
}

# Funtion for clients
# Start         ->  CRUD packages or select storages
# Status        ->  Info storage(s) with his packages
# Perfils       ->  Own info
# Storages      ->  Own Storages
# Instructions  ->  Option's specifics
# Log_out
function menu_Clients() {
    echo -e "\nClients Menu:\n"
    select subopcion in "Start" "Status" "Perfils" "Storages" "Instructions" "Log_out"; do
        case $REPLY in
            1) echo "Start has been selected"; break ;;
            2) echo "Status has been selected"; break ;;
            3) echo "Perfils has been selected"; break ;;
            4) echo "Storages has been selected"; break ;;
            5) echo "Instructions has been selected"; break ;;
            6) main_menu; break ;;
            *) echo "Invalid Option. Try again." ;;
        esac
    done
}

# Funtion for administrators
# Start         ->  CRUD packages or select storages
# Status        ->  general info (just for show)
# Perfils       ->  CRUD users
# Storages      ->  CRUD Storages
# Instructions  ->  Option's specifics
# Log out
function menu_admin() {
    echo -e "\nAdmin Menu:\n"
    select subopcion in "Start" "Status" "Perfils" "Storages" "Instructions" "Log out"; do
        case $REPLY in
            1) echo "Start has been selected"; break ;;
            2) echo "Status has been selected"; break ;;
            3) echo "Perfils has been selected"; break ;;
            4) echo "Storages has been selected"; break ;;
            5) echo "Instructions has been selected"; break ;;
            6) main_menu; break ;;
            *) echo "Invalid Option. Try again." ;;
        esac
    done
}

# Start main menu
main_menu
