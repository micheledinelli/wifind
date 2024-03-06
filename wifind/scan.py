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
    
    sample = {}
    for ap in aps:
        id = ap.get("bssid") + "-" + ap.get("ssid")    
        quality = ap.get("quality")
        sample[id] = quality
        if room:
            sample["room"] = room  

    return sample