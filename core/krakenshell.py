#!/usr/bin/env python3
import argparse
from core import sdr_sniffer, sim_exploit, a5_cracker, geo_spoofer, base_mapper, osint_engine

def banner():
    print(r"""
   ____ ____  __  __ _  __  __  _  __ ____  _____  ______ __ __
  / ___/ ___||  \/  | ||  \/  || |/ // ___||  _ \ \/ / __ \\ V /
 | |  | |__  | |\/| | || |\/| || ' /\___ \| | | \  /| |  | |> < 
 | |__|___ \ | |  | | || |  | || . \ ___) | |_| /  \| |__| / . \
  \____|___/ |_|  |_|_||_|  |_||_|\_\____/|____/_/\_\\____/_/ \_\
        Advanced GSM Cracking, OSINT, SIM Exploit Toolset
    """)

def main():
    banner()
    parser = argparse.ArgumentParser(description="GSMKRAKEN - Full Stack GSM Security Framework")

    parser.add_argument('--sniff', action='store_true', help='Start SDR sniffer')
    parser.add_argument('--sim', action='store_true', help='SIM card hacking mode')
    parser.add_argument('--a5', action='store_true', help='Start A5/1 cracking module')
    parser.add_argument('--osint', type=str, help='Run OSINT on phone number/email/IP')
    parser.add_argument('--map', type=str, help='Map BTS or IMSI catch logs from file')
    parser.add_argument('--spoof', type=str, help='Fake GPS location: LAT,LON')

    args = parser.parse_args()

    if args.sniff:
        sdr_sniffer.run()
    elif args.sim:
        sim_exploit.run()
    elif args.a5:
        a5_cracker.run()
    elif args.osint:
        osint_engine.run(args.osint)
    elif args.map:
        base_mapper.run(args.map)
    elif args.spoof:
        geo_spoofer.run(args.spoof)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
