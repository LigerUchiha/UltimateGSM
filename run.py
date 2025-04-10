import argparse
from core.sim_exploit import run as sim_exploit
from core.a5_cracker import run as a5_crack
from core.geo_spoofer import run as geo_spoof
from core.osint_engine import run as osint_engine

def main():
    parser = argparse.ArgumentParser(description="GSM Cracker and OSINT Tools")
    parser.add_argument('--sim-exploit', action='store_true', help="Run SIM Exploit")
    parser.add_argument('--a5-crack', action='store_true', help="Run A5/1 Cracking")
    parser.add_argument('--geo-spoof', action='store_true', help="Run Geo Spoofing")
    parser.add_argument('--osint-engine', type=str, help="Run OSINT Engine with target (email, phone, ip)")

    args = parser.parse_args()

    if args.sim_exploit:
        sim_exploit()
    elif args.a5_crack:
        a5_crack()
    elif args.geo_spoof:
        geo_spoof()
    elif args.osint_engine:
        osint_engine(args.osint_engine)
    else:
        print("[!] No valid options provided.")

if __name__ == '__main__':
    main()
