import argparse


print('''
  ____          _       ___  _     _____       _                          
 / ___|___   __| | ___ / _ \| |   | ____|_ __ | |__   __ _ _ __   ___ ___ 
| |   / _ \ / _` |/ _ \ | | | |   |  _| | '_ \| '_ \ / _` | '_ \ / __/ _ \
| |__| (_) | (_| |  __/ |_| | |___| |___| | | | | | | (_| | | | | (_|  __/
 \____\___/ \__,_|\___|\__\_\_____|_____|_| |_|_| |_|\__,_|_| |_|\___\___|
                                                                          ''')



if __name__ == "__main__":
    args=argparse.ArgumentParser()
    args.add_argument('-d','--database',type=str,required=True,help="generate database")
    args.add_argument('-v','--version',type=str,required=True,help="choose jdk version")
    
    parse_args=args.parse_args()
    print(parse_args)