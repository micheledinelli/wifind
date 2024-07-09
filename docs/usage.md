# Usage

```
# learn current location labelling it as kitchen
wifind learn -r kitchen

# print saved locations
wifind rooms
# ['kitchen', 'bedroom']

# predicts current location
wifind predict
# kitchen

# predicts returning probabilities
wifind predict -p
# {'kitchen': 0.68, 'bedroom': 0.32}

# watch for location changes
wifind --watch
# 2024-07-10 00:58:16 - kitchen
# 2024-07-10 00:58:18 - bedroom

# clears data
wifind clear
```