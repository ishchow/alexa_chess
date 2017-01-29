pa = [
    'Alpha 1', 'Alpha 2', 'Alpha 3', 'Alpha 4', 'Alpha 5', 'Alpha 6',
    'Alpha 7', 'Alpha 8', 'Bravo 1', 'Bravo 2', 'Bravo 3', 'Bravo 4',
    'Bravo 5', 'Bravo 6', 'Bravo 7', 'Bravo 8', 'Charlie 1', 'Charlie 2',
    'Charlie 3', 'Charlie 4', 'Charlie 5', 'Charlie 6', 'Charlie 7',
    'Charlie 8', 'Delta 1', 'Delta 2', 'Delta 3', 'Delta 4', 'Delta 5',
    'Delta 6', 'Delta 7', 'Delta 8', 'Echo 1', 'Echo 2', 'Echo 3',
    'Echo 4', 'Echo 5', 'Echo 6', 'Echo 7', 'Echo 8', 'Foxtrot 1',
    'Foxtrot 2', 'Foxtrot 3', 'Foxtrot 4', 'Foxtrot 5', 'Foxtrot 6',
    'Foxtrot 7', 'Foxtrot 8', 'Golf 1', 'Golf 2', 'Golf 3', 'Golf 4',
    'Golf 5', 'Golf 6', 'Golf 7', 'Golf 8', 'Hotel 1', 'Hotel 2',
    'Hotel 3', 'Hotel 4', 'Hotel 5', 'Hotel 6', 'Hotel 7', 'Hotel 8']

count = 1
for ch in pa:
    if count % 5 == 0:
        print()
    print(repr(ch.lower()), end=", ")
    count += 1
