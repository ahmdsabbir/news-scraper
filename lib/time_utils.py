from datetime import datetime, timedelta, timezone


def generate_published_date():
    """Generates a published_date string in the format "YYYY-MM-DDTHH:MM:SS.000-08:00"."""

    # Get current UTC time
    utc_now = datetime.now(timezone.utc)

    # Calculate PST time (UTC-8)
    pst_now = utc_now - timedelta(hours=8)

    # Format the PST time as the desired string
    date_str = pst_now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    readable = pst_now.strftime("%A-%B-%d-%Y")

    return {"date_str": date_str, "readable": readable}

def generate_blogger_timestamp():
    """
    Generate the current date and time in the format used for Blogger timestamps.

    Format: YYYY-DD-MMTHH:MM:SS.sss±HH:MM
    """
    now = datetime.now()
    # Format datetime object into the desired string format
    formatted_time = now.strftime("%Y-%d-%mT%H:%M:%S.%f")[:-3] + "-08:00"  # Adjust timezone as needed
    return formatted_time

# Example usage
print(generate_blogger_timestamp())