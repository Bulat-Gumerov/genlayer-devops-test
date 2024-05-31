#!/usr/bin/env python3
def simple_hash(input_string):
    prime = 31
    hash_value = 0
    
    for i, char in enumerate(input_string):
        hash_value = hash_value * prime + (ord(char) + i)
    
    return hash_value

def verify_fragments(fragments):
    expected_keys = sorted(fragments.keys())
    for key in range(1, max(expected_keys) + 1):
        if key not in fragments:
            return False, f"Missing fragment {key}"
    
    for key in expected_keys:
        fragment = fragments[key]
        if 'data' not in fragment or 'hash' not in fragment:
            return False, f"Incomplete fragment {key}"
        if simple_hash(fragment['data']) != fragment['hash']:
            return False, f"Hash mismatch in fragment {key}"
    
    return True, "All fragments verified successfully"

def reconstruct_data(fragments):
    # Verify the integrity of each fragment
    integrity_check, message = verify_fragments(fragments)
    if not integrity_check:
        return None, message

    # Reconstruct the original data by concatenating the data from each fragment
    sorted_keys = sorted(fragments.keys())
    original_data = ''.join(fragments[key]['data'] for key in sorted_keys)
    
    return original_data, "Data reconstructed successfully"

# Test data
fragments1 = {
    1: {'data': 'Hello', 'hash': simple_hash('Hello')},
    2: {'data': 'World', 'hash': simple_hash('World')},
    3: {'data': '!', 'hash': simple_hash('!')}
}

fragments2 = {
    1: {'data': 'Hellofff', 'hash': simple_hash('Hellofff')},
    2: {'data': 'World\n222', 'hash': simple_hash('World\n222')},
    3: {'data': '!', 'hash': simple_hash('!')}
}

# Reconstruct data
print(reconstruct_data(fragments1))  # Should print ("HelloWorld!", "Data reconstructed successfully")
print(reconstruct_data(fragments2))  # Should print ("HellofffWorld\n222!", "Data reconstructed successfully")

# Introduce an error for testing
print('Introduce an error for testing:')

fragments2[2]['data'] = 'World'
print(reconstruct_data(fragments2))  # Should print (None, "Hash mismatch in fragment 2")
