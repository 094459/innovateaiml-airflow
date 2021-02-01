import requests
import boto3
import base64
import argparse


def parse_args():
    """Parse argument values from command-line"""

    parser = argparse.ArgumentParser(description='Arguments required for script.')
    parser.add_argument('-e', '--env', required=True, help='The name of your Mwaa environment')
    parser.add_argument('-c', '--command', required=True, help='The name of the Apache Airflow command you want to run.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    print("Connecting to MWaa environment" + ": " + args.env)
    client = boto3.client('mwaa')
    response = client.create_cli_token(Name=str(args.env))
    
    print("Using this command" + ": " + args.command)

    auth_token=response.get('CliToken')
    hed = {'Content-Type': 'text/plain', 'Authorization': 'Bearer ' + auth_token}
    data = str(args.command)
    url = 'https://{web_server}/aws_mwaa/cli'.format(web_server=response.get('WebServerHostname'))
    r = requests.post(url, data=data, headers=hed)
    print_output(r)


def print_output(r):
    output = base64.b64decode(r.json()['stdout']).decode('utf8')
    print(output)

if __name__ == '__main__':
    main()