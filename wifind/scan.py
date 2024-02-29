from access_points import get_scanner

def scan(room=None):
    """
    Scans for WiFi access points and returns a list of dictionaries containing the BSSID, SSID, signal quality, and room.

    Parameters:
    room (str): Optional; a string representing the room in which the scan is performed. Defaults to None.

    Returns: a list
    """
    wifi_scanner = get_scanner()
    aps = wifi_scanner.get_access_points()
    
    samples = {}
    for ap in aps:
        id = ap.get("bssid") + "-" + ap.get("ssid")    
        quality = ap.get("quality")
        samples[id] = quality 

    results = {room: samples}
    return results