# Nk_code
# ATM Simulation in Python

This repository contains a simple ATM simulation program written in Python. The program allows users to create a PIN, deposit money, withdraw money, and check their balance. It simulates basic ATM functionalities through a console-based interface.

## Features

- **Create PIN**: Users can set up a new PIN for their account.
- **Deposit Money**: Users can deposit a specified amount into their account.
- **Withdraw Money**: Users can withdraw a specified amount from their account, provided they have sufficient balance.
- **Check Balance**: Users can check their current account balance.
- **Exit**: Users can exit the program.

## Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nk0126/atm-simulation.git
    cd atm-simulation
    ```

2. **Run the program**:
    ```bash
    python atm.py
    ```

3. **Follow the on-screen instructions**:
    - Enter `1` to create a PIN.
    - Enter `2` to deposit money.
    - Enter `3` to withdraw money.
    - Enter `4` to check your balance.
    - Enter `5` to exit the program.

## Code Overview

The main functionality is encapsulated in the `Atm` class:

- **Initialization**:
    - The `__init__` method initializes the PIN and balance, and calls the `menu` method.

- **Menu**:
    - The `menu` method displays the main menu and handles user input.

- **Create PIN**:
    - The `create_pin` method allows users to set a new PIN.

- **Deposit**:
    - The `deposit` method allows users to deposit money into their account.

- **Withdraw**:
    - The `withdraw` method allows users to withdraw money from their account.

- **Check Balance**:
    - The `check_balance` method displays the current balance.
