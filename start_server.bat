@echo off

rem Change the directory to the location of the Minecraft server
cd "C:\Path\to\minecraft_server_directory"

rem Start the Minecraft server with 8GB ram in a separate Command Prompt window
start cmd /k java -Xmx8G -Xms8G -jar server.jar nogui

rem Change the directory to the location of the minecraft_server_tunnel.py script
cd "C:\Path\to\minecraft_tunnel_script_directory"

rem Run the minecraft_server_tunnel.py script in a separate Command Prompt window
start cmd /k python minecraft_server_tunnel.py
