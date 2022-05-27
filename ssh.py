import os
import paramiko
from paramiko import BadHostKeyException, SSHException


def ssh_connect(command):
    try:
        host = os.getenv('SERVER_IP')
        user = os.getenv('USER_SSH')
        password = os.getenv('PASSWORD_SSH')
        port = int(os.getenv('PORT_SSH'))

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password, port=port)
        stdin, stdout, stderr = client.exec_command(command)
        data = stdout.read() + stderr.read()
        client.close()
        return data.decode('UTF-8')
    except (TimeoutError, BadHostKeyException, SSHException):
        return 'Не удается подключиться по SSH'
