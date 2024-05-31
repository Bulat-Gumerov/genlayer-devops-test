#!/usr/bin/env python3

def distribute_fragments(data_centers, fragments):
    # Ensure all data centers are integers
    data_centers = [dc for dc in data_centers if isinstance(dc, int)]
    
    def can_distribute(max_risk):
        # This function checks if it's possible to distribute all fragments
        # such that no data center's total risk exceeds `max_risk`
        count = 1  # start with the first data center
        current_sum = 0

        for risk in data_centers:
            if current_sum + risk > max_risk:
                count += 1  # need to use a new data center
                current_sum = risk  # start a new sum for the new data center
                if count > fragments:  # if more fragments than allowed
                    return False
            else:
                current_sum += risk

        return True

    low, high = max(data_centers), sum(data_centers)

    while low < high:
        mid = (low + high) // 2
        if can_distribute(mid):
            high = mid
        else:
            low = mid + 1

    return low

# Example usage 30
print('Example usage 30 risk:')
data_centers = [10, 20, 30]
fragments = 5
min_risk30 = distribute_fragments(data_centers, fragments)
print(f"Minimized maximum risk: {min_risk30}")

# Example usage 40
print('Example usage 40 risk:')
data_centers = [40, 30, 38, 1,]
fragments = 5
min_risk40 = distribute_fragments(data_centers, fragments)
print(f"Minimized maximum risk: {min_risk40}")
