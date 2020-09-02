import pysftp

# Accept any host key (still wrong see below)
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
# And authenticate with private key
with pysftp.Connection(host='webdev.bentley.edu', username='hudsonthom', password='6547', private_key=".ppk", cnopts=cnopts) as sftp:

    sftp.put('./index.html')

sftp.close()