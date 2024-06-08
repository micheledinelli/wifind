from access_points import get_scanner


def scan(room=None):
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