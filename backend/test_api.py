import requests
import json
from pprint import pprint

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("\n--- Testing /health ---")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    pprint(response.json())

def test_current_time():
    print("\n--- Testing /api/current-time ---")
    response = requests.get(f"{BASE_URL}/api/current-time")
    print(f"Status Code: {response.status_code}")
    pprint(response.json())

def test_menstrual_health():
    print("\n--- Testing /api/menstrual-health ---")
    response = requests.get(f"{BASE_URL}/api/menstrual-health", params={"section": "foods_to_eat"})
    print(f"Status Code: {response.status_code}")
    pprint(response.json())

def test_hospitals():
    print("\n--- Testing /api/hospitals-doctors ---")
    # Coordinates for Kolkata as a test point
    params = {
        "lat": 22.57,
        "lon": 88.36,
        "radius": 5000
    }
    response = requests.get(f"{BASE_URL}/api/hospitals-doctors", params=params)
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Total Hospitals Found: {data.get('count')}")
    print(f"Total Available Doctors: {data.get('doctors_available_now')}")
    print("Pre-view of first hospital:")
    if data.get('hospitals'):
        pprint(data['hospitals'][0])

def test_doctor_availability():
    print("\n--- Testing /api/doctor-availability ---")
    params = {
        "lat": 22.57,
        "lon": 88.36,
        "radius": 5000
    }
    response = requests.get(f"{BASE_URL}/api/doctor-availability", params=params)
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Total Available Doctors: {data.get('total_doctors_available')}")
    if data.get('hospitals'):
        print(f"Sample Hospital with Available Doctors ({data['hospitals'][0]['name']}):")
        pprint(data['hospitals'][0]['available_doctors'])

if __name__ == "__main__":
    print("Testing Blood Health Advisor APIs...")
    print("Make sure the Uvicorn server is running before executing this script!")
    test_health()
    test_current_time()
    test_menstrual_health()
    test_hospitals()
    test_doctor_availability()
    print("\n✅ All Tests Completed Successfully!")
