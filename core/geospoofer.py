import geocoder
import random
import time

# Fake coordinates (in case of spoofing)
def generate_fake_coords():
    lat = random.uniform(37.0, 42.0)  # Random lat within range
    lon = random.uniform(-80.0, -75.0)  # Random lon within range
    return lat, lon

def send_fake_gps(lat, lon):
    # Placeholder: send GPS spoofed coordinates to a system or service
    print(f"[+] Fake GPS Coordinates: LAT={lat}, LON={lon}")
    # Here, you could send the GPS coordinates to an app, for example

def geo_lookup():
    print("[*] Attempting to retrieve current real location...")
    g = geocoder.ip('me')
    print(f"[+] Real Location: {g.latlng}")

def run(location=None):
    if location:
        lat, lon = map(float, location.split(','))
        send_fake_gps(lat, lon)
    else:
        print("[*] Generating random fake location...")
        lat, lon = generate_fake_coords()
        send_fake_gps(lat, lon)
        geo_lookup()

    time.sleep(1)
    print("[*] GPS spoofing complete.")
