import os, ctypes, sys

def main():
  if is_admin():
    disable_enable_eth()
  else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    disable_enable_eth()

def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False

def disable_enable_eth():
  os.system("netsh interface set interface Ethernet disable")

  os.system("netsh interface set interface Ethernet enable")

main()