import sys
import argparse
if sys.version_info[0] < 3:
    from StringIO import StringIO
    import commands as command_runner
else:
    from io import StringIO
    import subprocess as command_runner

import pandas as pd
import requests

def run(interval, hook_url=None):
    CMD = "sadf -dh -- -p"
    header = "# hostname;interval;timestamp;CPU;%user;%nice;%system;%iowait;%steal;%idle[...]"

    output = command_runner.getoutput(CMD)
    output = output[output.index(header): ]

    df = pd.read_csv(StringIO(output), sep=";")
    average_usage = df.tail(int(interval))['%user'].mean()
    if hook_url:
        requests.post(hook_url, json={
            "average_usage": average_usage,
            "data": df.tail(10).to_dict()
        })

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interval', required=True)
    parser.add_argument('-ho', '--hook')
    args = parser.parse_args()
    run(args.interval, args.hook)

if __name__ == '__main__':
    main()
