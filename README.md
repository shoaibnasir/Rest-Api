# Rest-Api
This is a simple python Flask based Rest Application which allows the users to achieve the following objectives
1. Submit / Post messages
2. List all the received messages
3. Retrieve a specific message on demand, and determine whether is it a palindrome
4. Delete specific messaged
5. Update a specific message

The Api service uses the python Flask framework and uses Flask-Sqlalchemy plugin to create a lightweight database
to save the received messages

## Additional Features
This application can also be strapped into a docker container which exposes the Rest-Api. A requirements.txt file 
details the required dependencies for this application

A Command Line tool has also been provided to make calls the Rest application which can either be run 
on a host or from inside the docker container

# Deployment Guidelines

Docker needs to be installed in order to perform the following operations

1 - Clone this repository
```bash
https://github.com/shoaibnasir/Rest-Api.git
```

2 - Build a docker image
  
```bash
cd Rest-Api/
docker build --tag <tag>

Example:
  docker build --tag snasir/rest_app:latest .
``` 

3 - Boot up a docker container

```bash
docker run --name rest_app -d -p 5000:5000 snasir/rest_app:latest
```

4 - Verify that the container is running and the port 5000 is exposed

```bash
docker ps -a | grep rest_app

Example:
[snasir:~/Rest-Api] docker ps -a | grep rest
5021f8557bc6        snasir/rest_app:latest   "./entrypoint.sh"        12 minutes ago      Up 12 minutes   0.0.0.0:5000->5000/tcp   rest_app

```

5 - Login to the rest_app container to execute the cli commands

```bash
[snasir:~/Rest-Api] docker exec -it -u 0 rest_app /bin/bash
root@5021f8557bc6:/Rest_app# 

root@5021f8557bc6:/Rest_app# python Msgcli.py --help
Usage: Msgcli.py [OPTIONS] COMMAND [ARGS]...

```
## Command Line Tool

The Msgcli tool uses the Rest-app to make use of the above-mentioned features
The Msgcli.py can be found in the /Rest_app directory

#### Usage Instructions:

```bash
Msgcli --help
Usage: Msgcli.py [OPTIONS] COMMAND [ARGS]...

  This CLI can be used to send and receive messages from the Rest_app

  Retrieving individual messages will also show whether the message received
  is a palindrome

Options:
  --help  Show this message and exit.

Commands:
  delete-msg  Delete a Message with a specific id :param id:
  get-msgs    Get all messages or a specific message from the app
  send-msg    Send a Message with a "Property" and "Message" header

```
#### send-msg option
```bash

Msgcli send-msg --help
Usage: Msgcli.py send-msg [OPTIONS]

  Send a Message with a "Property" and "Message" header

Options:
  --property TEXT  property attribute of the message (optional)
  --message TEXT   Actual message to send
  --help           Show this message and exit.
  
Example:
   Msgcli send-msg --message SampleMessage
   Msgcli send-msg --property SampleProperty --message SampleMsg
```

#### get-msgs option
```bash
Msgcli get-msgs --help
Usage: Msgcli.py get-msgs [OPTIONS]

  Get all messages or a specific message from the app

Options:
  --id INTEGER  id of the Message to retrieve
  --help        Show this message and exit.
 
 Example:
   Msgcli get-msgs --all
   Msgcli get-msgs --id <id>
```

#### delete-msg option
```bash
Msgcli delete-msg --help
Usage: Msgcli.py delete-msg [OPTIONS]

  Delete a Message with a specific id :param id:

Options:
  --id INTEGER  id of the Message to retrieve
  --help        Show this message and exit.
  
Example:
  Msgcli delete-msg --id <id>
```

```note
To use the CLI tool from inside a docker container, use the following format

python Msgcli.py [OPTIONS]
```



