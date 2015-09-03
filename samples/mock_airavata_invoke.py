#!/usr/bin/python
# Mock example script to illustarte Workbench Wrapper

import sys, argparse

parser = argparse.ArgumentParser(description='Mock example script to illustarte Workbench Wrapper')
parser.add_argument("-i", help="SSH Key location to run as NSG User")
parser.add_argument("sshlogin", help="SSH Login command")
parser.add_argument("id", default='ind123', help="Compute Resource Allocation")
parser.add_argument("url", help="Monitoring URL to be called back by application upon execution")
parser.add_argument("commandline", help="Command line arguments to be passed to remote submit.py")
parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose logging")

args = parser.parse_args()

sys.stdout.write('URL passed ' + args.url + ' command line is ' + args.commandline)
sys.stderr.write('There is a undetermined error -- good luck debugging ')
sys.exit(0)
