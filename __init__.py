import argparse
import configparser
from prtg import prtg

arguments = argparse.ArgumentParser()
arguments.add_argument("ConfFile",help="Path to conf.ini file")
args = arguments.parse_args()


config = configparser.ConfigParser()
config.read(args.ConfFile)
prtg_connection = prtg(config['prtg']['prtg_address'],config['prtg']['prtg_user'],config['prtg']['prtg_password'],config['DEFAULT']['prtg_port'],config['prtg']['prtg_protocol'])
if(config['DEFAULT']['test'] == 'True'):
    print("PRTG Test Result: [{}]".format(prtg_connection.test_connection(prtg_connection.http_address)))
else:
    prtg_connection.get_current_alerts(prtg_connection.http_address,bool(config['prtg']['ignore_ack']))