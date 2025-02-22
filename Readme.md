# Peer-to-Peer Chat Program (BONUS)

## Team Information

**Team Name:** BTC

### Team Members

| Name              | Roll No     |
|-------------------|-------------|
| Ayush Kumar       | 230001012   |
| Hemsai            | 230001079   |
| Shubham Prajapati | 230005047   |

---

## Problem Statement

This project implements a peer-to-peer chat program in Python that supports simultaneous sending and receiving of messages. Each instance acts as both a server (listening for incoming connections) and a client (sending messages) using multi-threading. The application maintains a list of active peers from which messages have been received and allows users to query and connect to these peers.

---

## Project Overview

- **Concurrent Communication:**  
  Uses multi-threading to allow each instance to send and receive messages simultaneously.

- **Peer Management:**  
  Maintains a set of active peers (IP:PORT) and their corresponding team names. Duplicate entries are automatically avoided.

- **Standardized Message Format:**  
  Every message is formatted as:  
  `<Your_IP:Your_Port> <Team_Name> <Your_Message>`  
  This ensures consistent message parsing across the network.

- **Static IP Connections:**  
  The program is configured to mandatorily connect to the following static IP addresses and ports (only when connected to the IIT internal network):
  - **IP:** 10.206.5.228, **PORT:** 6555

- **Bonus Feature – Connect to Active Peers:**  
  Provides functionality to send a "CONNECT" message to selected active peers to verify connectivity and update the peer list.

---

## Requirements

- **Python 3.x:**  
  Ensure that Python 3 is installed on your system.

- **Network Setup:**  
  - All devices (or terminal instances) should be on the same network (e.g., same WiFi).  
  - The chosen ports must be available and permitted through any firewall/antivirus.  
  - Use your local network IP (e.g., 10.x.x.x, 172.x.x.x, or 192.168.x.x) instead of 127.0.0.1 when connecting between different machines.

---

## Instructions to Run the Program

1. **Clone or Download the Repository:**  
   Ensure you have the Python source file (e.g., `p2p_chat.py`) available locally.
2. **Clone the Repository:**  
   Clone or download the repository from GitHub. In your terminal, run:
   ```bash
   git clone https://github.com/Hemsai0620/Team_BTC.git
   cd Team_BTC
   ```

3. **Run the Program:**  
   - On Linux/macOS:
     ```bash
     python3 p2p_chat.py
     ```
   - On Windows:
     ```bash
     py p2p_chat.py
     ```

4. **Provide Required Details:**  
   When prompted, enter:
   - Your team name (e.g., BTC)
   - A free port number for your server

5. **Simulate Multiple Peers:**  
   Open multiple terminal windows or run the program on different devices to simulate various peers.

## Menu Options & Usage

When the program starts, the following menu is displayed:

**Server Status:**  
_Server listening on all interfaces (port 8080)_

**Menu:**  
1. **Send Message:**  
   Sends a message to a specified peer. You will be prompted for the recipient's IP address, port number, and your message.  
   **Message Format:** `<Your_IP:Your_Port> <Team_Name> <Your_Message>`
   
2. **Query Active Peers:**  
   Displays the list of active peers (with their team names) from which messages have been received.

3. **Connect to Active Peers:**  
   Allows you to select an active peer from the list and sends a "CONNECT" message to verify connectivity and update the peer list.

4. **Send Mandatory Message to Default Peers:**  
   Automatically sends a message to the predefined static IP addresses:  
   - **IP:** 10.206.5.228, **PORT:** 6555  
   *Note: This option works only when connected to the IIT internal network.*

0. **Quit:**  
   Exits the program.

 ---
# SAMPLE RUN
    
     Enter your team name: Team_BTC
     Enter your port number: 5000
     Your detected IP address: 10.18.x.xxx

     **** Menu ****
     1. Send message
     2. Query active peers
     3. Connect to active peers
     4. Send mandatory message to default peers
     0. Quit
    Server listening on all interfaces (port 5000)
    Enter choice: 1
    Enter recipient's IP address: 10.18.x.xxx
    Enter recipient's port number: 6000
    Enter your message (type 'exit' to disconnect): Hi
    


## Additional Notes

- **Correct IP Addresses:**  
Always enter your network-assigned local IP (e.g., 10.x.x.x) rather than 127.0.0.1 when connecting between different machines.

- **Port Selection:**  
Ensure the port number you choose is not used by another service and is allowed through your firewall.

- Verify that the recipient peer is running the program and listening on the correct port.

- **Network Connectivity:**  
*If your WiFi connection fails, try using a personal hotspot.*

---

## Acknowledgement  
- Prof. Subhra Mazumdar, for the project idea and concepts of peer-to-peer networks.  
- A helpful documentation of socket programming at [GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/).

