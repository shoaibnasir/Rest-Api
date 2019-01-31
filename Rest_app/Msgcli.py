import requests
import click
import json

app_url = 'http://localhost:5000/message'


@click.group()
def main():
    """
    This CLI can be used to send and receive messages
    from the Rest_app

    Retrieving individual messages will also show
    whether the message received is a palindrome
    """
    pass


@main.command(name='get-msgs')
@click.option('--id',
              help='id of the Message to retrieve',
              default=None,
              type=int)
def get_msgs(id=None):
    """
    Get all messages or a specific message from the app
    """
    response = []
    uri = app_url
    if id:
        uri = "".join([app_url, '/', str(id)])
        print(uri)
    try:
        response = requests.get(uri)
        if response.status_code == 200:
            click.echo(response.json())
        else:
            msg = "Error code '%s'\n Response-Content: %s" \
                  % (response.status_code, response.content)
            print(msg)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


@main.command()
@click.option('--property',
              help='property attribute of the message',
              default="")
@click.option('--message',
              help='Actual message to send',
              default="")
def send_msg(property, message):
    """
    Send a Message with a "Property" and "Message" header
    """
    try:
        headers = {'Content-type': 'application/json'}
        payload = {
                    'property': property,
                    'message': message
                  }
        response = requests.post(app_url, headers=headers,
                                 data=json.dumps(payload))

        if response.status_code == 200:
            click.echo(response.json())
        else:
            msg = "Error code '%s'\n Response-Content: %s" \
                  % (response.status_code, response.content)
            print(msg)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


@main.command()
@click.option('--id',
              help='id of the Message to retrieve',
              default=None,
              type=int)
def delete_msg(id):
    """
    Delete a Message with a specific id
    :param id:
    """
    response = []
    uri = app_url
    if id:
        uri = "".join([app_url, '/', str(id)])
        print(uri)
    try:
        response = requests.delete(uri)
        if response.status_code == 200:
            click.echo(response.json())
        else:
            msg = "Error code '%s'\n Response-Content: %s" \
                  % (response.status_code, response.content)
            print(msg)
    except requests.exceptions.RequestException as err:
        print("Error deleting message", err)


if __name__ == '__main__':
    main()
