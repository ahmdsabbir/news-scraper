import os

def create_dir_if_not_exists(dir_name):
  """
  Creates a directory with the given name if it does not already exist.

  Args:
    dir_name: The name of the directory to create.
  """
  if not dir_exists(dir_name):
    os.makedirs(dir_name)
  else:
    pass

def dir_exists(dir_name):
  if os.path.exists(dir_name):
    return True
  
  return False