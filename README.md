# systemd exporter for [Honcho](https://github.com/nickstenning/honcho)
##Installation
```bash
$ pip install honcho-export-systemd
```
##Usage
Assuming you have a `Procfile` with the following contents:
```
web: python app.py
```

```bash
$ honcho export -a app -d /home/app -u app systemd /usr/lib/systemd/system
```

produces the following systemd service files:

```
# app.target
[Unit]
StopWhenUnneeded=true
Wants=app-web.target

[Install]
```

```
# app-web.target
[Unit]
StopWhenUnneeded=true
Wants=app-web-1.service
```

```
# app-web-1.service
[Unit]
StopWhenUnneeded=true

[Service]
User=app
WorkingDirectory=/home/app
Environment=PORT=5000
ExecStart=/bin/sh -c 'python app.py'
Restart=always
StandardInput=null
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=%n
```

