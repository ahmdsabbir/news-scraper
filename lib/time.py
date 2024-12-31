from datetime import datetime, timedelta, timezone

def generate_published_date():
  """Generates a published_date string in the format "YYYY-MM-DDTHH:MM:SS.000-08:00"."""

  # Get current UTC time
  utc_now = datetime.now(timezone.utc)

  # Calculate PST time (UTC-8)
  pst_now = utc_now - timedelta(hours=8)

  # Format the PST time as the desired string
  date_str = pst_now.strftime("%Y-%m-%dT%H:%M:%S.%f%z") 
  readable = pst_now.strftime('%A-%B-%d-%Y')

  return {"date_str": date_str, "readable": readable}