# [Minecraft](https://www.minecraft.net/en-us) Server Tunnel with [ngrok](https://ngrok.com) and [No-IP](https://www.noip.com) v2

This python script allows you to create a free tcp tunnel for your Minecraft Server using ngrok and update a free dynamic DNS of No-IP with the tunnel's ip address.
It simplifies the process of making your Minecraft server accessible to your friends by automatically setting up the ngrok tunnel and updating the No-IP dynamic DNS with the tunnel's address.

## Prerequisites

Before running the script, ensure that you have the following:

- Operating System: Windows 10
- Python 3.10.6 installed
- Latest Java Runtime Environment installed
- [Download Minecraft Server 1.19.2](https://piston-data.mojang.com/v1/objects/f69c284232d7c7580bd89a5a4931c3581eae1378/server.jar)
- [Minecraft Server](https://www.minecraft.net/en-us/download/server) running on a specified port
- An [ngrok](https://ngrok.com) account and an authtoken
- [ngrok](https://ngrok.com) executable added to the system's path
- [No-IP](https://www.noip.com) account with a set up free dynamic DNS hostname to a ipv4 type A

## Installation

1. Clone or download this repository to your local machine.
2. Extract the contents of the zip file to a directory of your choice.
4. Run the `install_java_notepad++_python.bat` file, only if you don't have installed it already.
5. Install the required Python packages by running `pip install -r requirements.txt` in your console.

## Configuration

The script uses a configuration file named `config.ini` to store sensitive information.

1. Open the `config.ini.example` file in a text editor.
2. Replace the placeholder values with your ngrok authtoken, No-IP account details, and Minecraft server port.
5. Save the file as `config.ini`.
6. Open the `start_server.bat` file in a text editor.
7. Replace "C:\Path\to\minecraft_server_directory" with the actual path to your Minecraft server directory (where server.jar is located).
8. Replace "C:\Path\to\minecraft_tunnel_script_directory" with the actual path to your minecraft_server_tunnel.py script directory.
9. Save the `start_server.bat` file.

## Usage

1. Run the `start_server.bat` file.
2. The Minecraft Server will start, make sure you have set it up right.
3. The script will start ngrok, create a secure tunnel for your Minecraft server, and update the corresponding No-IP dynamic DNS with the tunnel's ip address.
4. The Server Address will be displayed and copied to your clipboard
5. Now you can share the link with your friends so they can connect to your Minecraft Server.
6. Have fun playing together!

Note: Make sure to complete all steps mentioned in the "Shutdown and Exit Procedure" section before running the `start_server.bat` again.

Shutdown and Exit Procedure:
1. Write "stop" (without the quotes) in the console of the running Minecraft Server and press Enter to shutdown the server.
2. Wait until the server has completely finished shutting down.
3. Write "exit" (without the quotes) and press Enter to close the console.
4. Press Enter in the console of the running ngrok tcp tunnel to stop the tunnel.
5. Wait until the tunnel has stopped successfully.
6. Write "exit" (without the quotes) and press Enter to to close the console.

Note: After following the "Shutdown and Exit Procedure", you can safely run the `start_server.bat` again.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
