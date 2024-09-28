#!/bin/bash

# Funtio for the first menu
# Take_a_look        ->  Join without log_in
# Log_in Info        ->  Put the info
# Exit               ->  Left App
function main_menu() {
    echo -e "\nWelcome to the App Storage\n"
    PS3="Select an option: "
    select option in "Take_a_look" "Log_in" "Exit" "test"; do
        case $REPLY in
        1)
            menu_Only_look
            break
            ;;
        2)
            menu_Clients
            break
            ;;
        3)
            echo "Exit..."
            exit 0
            ;;
        4)
            test
            break
            ;;
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
        1)
            echo "Status has been selected"
            break
            ;;
        2)
            echo "General_Info has been selected"
            break
            ;;
        3)
            main_menu
            break
            ;;
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
        1)
            echo "Start has been selected"
            break
            ;;
        2)
            echo "Status has been selected"
            break
            ;;
        3)
            echo "Perfils has been selected"
            break
            ;;
        4)
            echo "Storages has been selected"
            break
            ;;
        5)
            echo "Instructions has been selected"
            break
            ;;
        6)
            main_menu
            break
            ;;
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
        1)
            echo "Start has been selected"
            break
            ;;
        2)
            echo "Status has been selected"
            break
            ;;
        3)
            echo "Perfils has been selected"
            break
            ;;
        4)
            echo "Storages has been selected"
            break
            ;;
        5)
            echo "Instructions has been selected"
            break
            ;;
        6)
            main_menu
            break
            ;;
        *) echo "Invalid Option. Try again." ;;
        esac
    done
}

# Map_2D
function test() {
    # Dimentions
    rows=10
    cols=100

    declare -A storage_Array

    for ((i = 0; i < rows; i++)); do
        for ((j = 0; j < cols; j++)); do
            storage_Array[$i, $j]=-
        done
    done

    # Change
    storage_Array[1, 0]=A
    storage_Array[5, 5]=B
    storage_Array[9, 9]=C
    storage_Array[2, 0]=D
    storage_Array[2, 10]=E
    storage_Array[0, 0]=F
    storage_Array[3, 2]=G
    storage_Array[7, 8]=H
    storage_Array[1, 9]=I
    storage_Array[0, 5]=J
    storage_Array[5, 2]=KK
    storage_Array[5, 2]=■

    storage_Array[1, 0]=■
    storage_Array[5, 5]=■
    storage_Array[9, 9]=■
    storage_Array[2, 0]=■
    storage_Array[2, 10]=■
    storage_Array[0, 0]=■
    storage_Array[3, 2]=■
    storage_Array[7, 8]=■
    storage_Array[1, 9]=■
    storage_Array[0, 5]=■
    storage_Array[5, 2]=■

    # ASCII generator
    for ((i = -1; i < $rows + 1; i++)); do
        if [[ $i -eq -1 ]]; then
            printf "█▀"
            printf "▀%.0s" $(seq 1 $((cols)))
            printf "▀█\n"
            printf "█ "
            printf " %.0s" $(seq 1 $((cols)))
            printf " █\n"

        elif [[ $i -eq $((rows)) ]]; then
            printf "█ "
            printf " %.0s" $(seq 1 $((cols)))
            printf " █\n"
            printf "█▄"
            printf "▄%.0s" $(seq 1 $((cols)))
            printf "▄█\n"
        else
            printf "█ "
            for ((j = 0; j < $((cols)); j++)); do
                printf "${storage_Array[$i, $j]}"
            done
            printf " █\n"
        fi
    done
}
# Map_1D
function Map_1D() {
    # Dimentions
    rows=1
    cols=10

    declare -A storage_Array

    for ((i = 0; i < rows; i++)); do
        for ((j = 0; j < cols; j++)); do
            storage_Array[$i, $j]=-
        done
    done

    # ASCII generator
    for ((i = -1; i < $rows + 1; i++)); do
        if [[ $i -eq -1 ]]; then
            printf "█▀"
            printf "▀%.0s" $(seq 1 $((cols)))
            printf "▀█\n"
            printf "█ "
            printf " %.0s" $(seq 1 $((cols)))
            printf " █\n"

        elif [[ $i -eq $((rows)) ]]; then
            printf "█ "
            printf " %.0s" $(seq 1 $((cols)))
            printf " █\n"
            printf "█▄"
            printf "▄%.0s" $(seq 1 $((cols)))
            printf "▄█\n"
        else
            printf "█ "
            for ((j = 0; j < $((cols)); j++)); do
                printf "${storage_Array[$i, $j]}"
            done
            printf " █\n"
        fi
    done
}

# Start main menu ▄■▀ █ ░ ▒ ▓
main_menu
