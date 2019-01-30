import requests
import click
import json

app_url = 'http://localhost:5000/message'


@click.command()
@click.argument('get-msg')
@click.option('--id',
              help='id of the Message to retrieve',
              default=None)
def restcli(get_msg,id=None):
    """
    This CLI can be used to send and receive messages
    from the Rest_app

    Retrieving individual messages will also show
    whether the message received is a palindrome
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


if __name__ == '__main__':
    restcli()


