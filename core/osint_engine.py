import requests
import json
from bs4 import BeautifulSoup

# Reverse Email Lookup (Example using Hunter.io API)
def reverse_email_lookup(email):
    print(f"[*] Looking up email: {email}")
    api_key = 'your_hunter_io_api_key'
    url = f"https://api.hunter.io/v2/email-finder?email={email}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['data']:
        name = data['data'].get('first_name', 'Unknown')
        company = data['data'].get('organization', 'Unknown')
        print(f"[+] Name: {name}")
        print(f"[+] Company: {company}")
        print(f"[+] Email: {email}")
    else:
        print("[!] No data found.")

# Reverse Phone Lookup (Example using TrueCaller API)
def reverse_phone_lookup(phone):
    print(f"[*] Looking up phone number: {phone}")
    url = f"https://www.truecaller.com/search/{phone}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('span', {'class': 'name'})
    if name:
        print(f"[+] Name: {name.text}")
    else:
        print("[!] No results found.")

# Reverse IP Lookup (Using IPinfo API)
def reverse_ip_lookup(ip):
    print(f"[*] Looking up IP address: {ip}")
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    if 'city' in data:
        print(f"[+] Location: {data['city']}, {data['region']}, {data['country']}")
        print(f"[+] Organization: {data.get('org', 'Unknown')}")
        print(f"[+] IP: {ip}")
    else:
        print("[!] No data found.")

# Main OSINT function to handle reverse lookups based on input type
def run(target):
    print(f"[*] Running OSINT on {target}...")
    if '@' in target:  # Email Lookup
        reverse_email_lookup(target)
    elif target.isdigit():  # Phone Lookup (assuming it's a valid phone number)
        reverse_phone_lookup(target)
    else:  # IP Lookup (fallback if it's not a valid email or phone)
        reverse_ip_lookup(target)
