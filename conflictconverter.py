import re

def convert_to_real_time(input_time, speed_multiplier=4):
    # Extract days, hours, and minutes
    pattern = re.compile(r'(?:(\d+)\s*d)?\s*(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?')
    match = pattern.fullmatch(input_time.strip())
    if not match:
        return "Invalid format. Use format like '2d 3h 15m', '5h', or '3d 2h'."

    days = int(match.group(1)) if match.group(1) else 0
    hours = int(match.group(2)) if match.group(2) else 0
    minutes = int(match.group(3)) if match.group(3) else 0

    # Convert everything to minutes
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes
    real_minutes = total_minutes / speed_multiplier

    # Convert real minutes back to days, hours, and minutes
    real_days = int(real_minutes // (24 * 60))
    real_minutes = real_minutes % (24 * 60)
    real_hours = int(real_minutes // 60)
    real_minutes = int(real_minutes % 60)

    return f"{real_days}d {real_hours}h {real_minutes}m (real time)"

# Example usage:
user_input = input("Enter game time (e.g., 2d 3h 15m): ")
print(convert_to_real_time(user_input))
