# Minecraft Server Tunnel with ngrok and No-IP v2

This script allows you to create a tunnel for your Minecraft server using ngrok and update the corresponding No-IP domain with the tunnel's address.
It simplifies the process of making your Minecraft server accessible to your friends by automatically setting up the ngrok tunnel and updating the No-IP domain with the tunnel's address.

## Prerequisites

Before running the script, ensure that you have the following:

- Operating System: Ensure that your system is running Windows 10.
- Minecraft Server running on the specified port (default: 25565)
- Latest Java Version: Make sure you have the latest version of Java installed on your system.
- Python 3.10.6: Make sure you have Python 3.10.6 installed on your system.
	- Run the `install_java_notepad++_python.bat` to install or update notepad++, java and python 
- `ngrok` executable added to the system's path
- An ngrok account and an authtoken
- A No-IP account with a registered domain

## Getting Started

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Create a configuration file named `config.ini` based on the provided `config.ini.example` file and fill in the required information (ngrok authtoken, No-IP account details).
	- Edit with notepad++ and save as `config.ini`.
4. Run the script using the command `python minecraft_server_tunnel.py`.
	- Edit the `start_server.bat` with notepad++ to update the directory paths
	- Replace "C:\Path\to\minecraft_server_directory" with the actual path to your Minecraft server directory (where server.jar is located).
	- Replace "C:\Path\to\minecraft_tunnel_script_directory" with the actual path to your minecraft_server_tunnel.py script directory.
	- Save and Run: Save the .bat file and double-click to run it. This will start the Minecraft server and the minecraft_server_tunnel.py script in separate Command Prompt windows.

## Configuration

The script uses a configuration file named `config.ini` to store sensitive information. Open the `config.ini` file and replace the placeholder values with your ngrok auth token, No-IP account details, and Minecraft server port.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.