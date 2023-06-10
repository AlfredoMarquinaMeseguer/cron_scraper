import datetime

from  classes import mongo_conn
if __name__ == "__main__":
    import requests


    def get_public_ip():
        try:
            response = requests.get('https://api.ipify.org?format=json')
            if response.status_code == 200:
                data = response.json()
                print(data)
                return data
            else:
                print('Error: Failed to retrieve IP address.')
        except requests.exceptions.RequestException as e:
            print('Error: {}'.format(e))


    # Call the function to get the public IP address
    public_ip = get_public_ip()
    if public_ip:
        print('Your public IP address is: {}'.format(public_ip))

