import subprocess
import requests
import socket
import time
import pyperclip
import base64
import sys
import configparser
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename='minecraft_server_tunnel.log',
    filemode='w'
)

# Create a stream handler to log messages to the console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
console_handler.setFormatter(console_formatter)

# Add the stream handler to the root logger
root_logger = logging.getLogger()
root_logger.addHandler(console_handler)

# Load configuration from a file
config = configparser.ConfigParser()
config.read('config.ini')

# Port of the Minecraft Server
port = config.get('Minecraft', 'Port')

# Ngrok auth token
ngrok_authtoken = config.get('Ngrok', 'AuthToken')

# NO-IP account information
noip_username = config.get('NoIP', 'Username')
noip_password = config.get('NoIP', 'Password')
noip_domain = config.get('NoIP', 'Domain')

# Concatenate the username and password with a colon
credentials = f"{noip_username}:{noip_password}"

# Encode the credentials using base64
base64_encoded_auth_string = base64.b64encode(credentials.encode()).decode()

# Start ngrok and return the process object
def start_ngrok():
    try:
        ngrok_process = subprocess.Popen(['ngrok', 'tcp', '--authtoken', ngrok_authtoken, port],
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                         creationflags=subprocess.CREATE_NO_WINDOW)
        logging.info('Starting ngrok tunnel...')
        return ngrok_process
    except FileNotFoundError:
        logging.error('ngrok executable not found. Make sure ngrok is installed and added to the system path.')
        sys.exit(1)
    except Exception as e:
        logging.error(f'Failed to start ngrok: {str(e)}')
        sys.exit(1)

# Stop ngrok tunnel if it is running
def stop_ngrok(ngrok_process):
    if ngrok_process is not None:
        ngrok_process.terminate()
        logging.info('The ngrok tunnel was stopped successfully.')
    else:
        logging.info('No ngrok tunnel is running.')

# Get the ngrok tunnel address
def get_ngrok_address():
    try:
        tunnels_response = requests.get('http://localhost:4040/api/tunnels')
        tunnels_data = tunnels_response.json()

        for tunnel in tunnels_data['tunnels']:
            if tunnel['proto'] == 'tcp':
                forwarding_address = tunnel['public_url'].replace('tcp://', '').split(':')[0]
                forwarding_port = ':' + tunnel['public_url'].replace('tcp://', '').split(':')[1]
                return forwarding_address, forwarding_port

        logging.error('Error: Forwarding Address not found.')
        return None, None
    except requests.exceptions.RequestException as e:
        logging.error(f'Error occurred while retrieving ngrok tunnels: {str(e)}')
        return None, None

# Update No-IP domain with the ngrok address
def update_noip_domain(forwarding_address, forwarding_port):
    try:
        ip_address = socket.gethostbyname(forwarding_address)
        logging.info(f"The IP address of '{forwarding_address}' is: {ip_address}")

        # Update the No-IP target domain
        noip_api_url = f'https://dynupdate.no-ip.com/nic/update?hostname={noip_domain}&myip={ip_address}'
        headers = {
            "Authorization": f"Basic {base64_encoded_auth_string}"
        }

        response = requests.get(noip_api_url, headers=headers)
        response.raise_for_status()

        if response.text.startswith('good'):
            logging.info('No-IP API response: Success! IP address updated.')
        elif response.text.startswith('nochg'):
            logging.info('No-IP API response: Success! IP address unchanged.')
        else:
            logging.error('No-IP API response:', response.text)
            logging.error('Please refer to the No-IP API documentation for more information about the error.')
            logging.error('API documentation: https://www.noip.com/integrate/response')
            sys.exit(1)

        noip_domain_with_port = noip_domain + forwarding_port
        logging.info('Your Server Address: %s', noip_domain_with_port)

        pyperclip.copy(noip_domain_with_port)
        logging.info("The Server Address has been copied to the clipboard.")
        logging.info("Share it with your friends.")
        logging.info('And have fun!')
    except socket.gaierror:
        logging.error(f"Failed to perform DNS lookup for '{forwarding_address}'")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        logging.error('An error occurred during the No-IP API call: %s', str(e))
        sys.exit(1)

# Main script
def main():
    logging.info('Minecraft Server Tunnel with ngrok and No-IP')
    logging.info('---------------------------------------------')
    logging.info('This script allows you to create a tunnel for your Minecraft server using ngrok and update the corresponding No-IP domain with the tunnel\'s address.\n')

    ngrok_process = start_ngrok()
    time.sleep(5)

    forwarding_address, forwarding_port = get_ngrok_address()

    if forwarding_address and forwarding_port:
        logging.info('Ngrok tunnel address: %s', forwarding_address)
        update_noip_domain(forwarding_address, forwarding_port)

        # Wait for user input to stop the ngrok tunnel
        input('Press Enter to stop the ngrok tunnel: ')
        stop_ngrok(ngrok_process)
    else:
        stop_ngrok(ngrok_process)
        sys.exit(1)

    # Keep the script running until ngrok process is terminated
    ngrok_process.wait()

if __name__ == '__main__':
    main()
