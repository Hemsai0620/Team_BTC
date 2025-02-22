import socket
import threading

def get_local_ip():
    """Returns the actual LAN IP address of this machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


peer_table = set()

peer_team_names = {}

default_peers = [("10.206.5.228", 6555)]

def handle_client(conn, addr):
    """Handles incoming connections and processes messages."""
    try:
        data = conn.recv(1024).decode()
        if not data:
            return
        parts = data.split()
        if len(parts) < 3:
            print("Invalid message format received.")
            return

        sender_info = parts[0]  
        team_name = parts[1]
        message_content = " ".join(parts[2:]).strip()

        
        if message_content.lower() == "exit":
            if sender_info in peer_table:
                peer_table.remove(sender_info)
                peer_team_names.pop(sender_info, None)
                print(f"{sender_info} ({team_name}) disconnected.")
            else:
                print(f"Exit message from unknown peer: {sender_info}.")
            return

        print(f"{sender_info} {team_name} {message_content}")

        
        if sender_info not in peer_table:
            peer_table.add(sender_info)
            peer_team_names[sender_info] = team_name

    except Exception as e:
        print("Error handling client:", e)
    finally:
        conn.close()

def server_thread(my_port):
    """Server thread that listens for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(("0.0.0.0", my_port))
        server_socket.listen(5)
        print(f"Server listening on all interfaces (port {my_port})")
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except Exception as e:
        print("Server error:", e)
    finally:
        server_socket.close()

def send_message(my_ip, my_port, team_name):
    """Prompts the user for recipient details and sends a formatted message."""
    recipient_ip = input("Enter recipient's IP address: ").strip()
    try:
        recipient_port = int(input("Enter recipient's port number: ").strip())
    except ValueError:
        print("Invalid port number.")
        return

    message = input("Enter your message (type 'exit' to disconnect): ").strip()
    full_message = f"{my_ip}:{my_port} {team_name} {message}"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((recipient_ip, recipient_port))
        s.sendall(full_message.encode())
        s.close()
    except Exception as e:
        print("Error sending message:", e)

def send_mandatory_messages(my_ip, my_port, team_name):
    """Sends a message to the mandatory default peers."""
    message = input("Enter mandatory message: ").strip()
    for ip, port in default_peers:
        full_message = f"{my_ip}:{my_port} {team_name} {message}"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendall(full_message.encode())
            s.close()
            print(f"Sent mandatory message to {ip}:{port}")
        except Exception as e:
            print(f"Error sending to {ip}:{port}: {e}")

def query_peers():
    """Displays active peers and their associated team names."""
    if peer_table:
        print("Connected Peers:")
        for peer in peer_table:
            print(f"{peer} - {peer_team_names.get(peer, 'Unknown Team')}")
    else:
        print("No connected peers.")

def connect_to_peers(my_ip, my_port, team_name):
    """Connects to a chosen active peer from the peer table."""
    if not peer_table:
        print("No active peers to connect to.")
        return

    peer_list = list(peer_table)
    print("Active Peers:")
    for idx, peer in enumerate(peer_list, start=1):
        team = peer_team_names.get(peer, "Unknown Team")
        print(f"{idx}. {peer} - {team}")

    try:
        choice = int(input("Select peer number: "))
        if choice < 1 or choice > len(peer_list):
            print("Invalid selection.")
            return
        selected_peer = peer_list[choice - 1]
    except ValueError:
        print("Invalid input. Enter a number.")
        return

    try:
        ip, port_str = selected_peer.split(":")
        port = int(port_str)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        connect_message = f"{my_ip}:{my_port} {team_name} CONNECT"
        s.sendall(connect_message.encode())
        s.close()
        print(f"Connected to {selected_peer}")
    except Exception as e:
        print(f"Could not connect to {selected_peer}: {e}")

def main():
    """Main function to initialize user details and start the server."""
    team_name = input("Enter your team name: ").strip()
    try:
        my_port = int(input("Enter your port number: ").strip())
    except ValueError:
        print("Invalid port number. Exiting.")
        return

    my_ip = get_local_ip()
    print(f"Your detected IP address: {my_ip}")

    threading.Thread(target=server_thread, args=(my_port,), daemon=True).start()

    while True:
        print("\n***** Menu *****")
        print("1. Send message")
        print("2. Query active peers")
        print("3. Connect to active peers")
        print("4. Send mandatory message to default peers")
        print("0. Quit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            send_message(my_ip, my_port, team_name)
        elif choice == "2":
            query_peers()
        elif choice == "3":
            connect_to_peers(my_ip, my_port, team_name)
        elif choice == "4":
            send_mandatory_messages(my_ip, my_port, team_name)
        elif choice == "0":
            print("Exiting")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
