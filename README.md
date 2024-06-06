![xbi1_banner](https://github.com/programmer-666/xbi1/assets/34501436/56fe6b34-4f68-4178-99cb-4d37cca1ca6d)

[![Flake8 Linting](https://github.com/programmer-666/xbi1/actions/workflows/flake8py.yml/badge.svg)](https://github.com/programmer-666/xbi1/actions/workflows/flake8py.yml)
[![CodeQL](https://github.com/programmer-666/xbi1/actions/workflows/codeql.yml/badge.svg)](https://github.com/programmer-666/xbi1/actions/workflows/codeql.yml)

# XBI1 - A Proxmox Notification Bot 🤖

xBi_1 is a discord bot that allows you to quickly access various information about your Proxmox Nodes and get reports. It's personal, private and basic.

## About Discord Bot

Firstly you need a private discord bot.

<img width="1102" alt="dc_appliaction_setting" src="https://github.com/programmer-666/xbi1/assets/34501436/86df32af-86dc-4ee6-ac8b-d3bc4774d219">
If you want to share your server information with everyone, you will not need to turn off this option.

## Installation & Before Running

Clone this repo, create a virtual environment or directly install modules needed.

```sh
git clone https://github.com/programmer-666/xbi1.git &&
cd xbi1 &&
virtualenv .venv &&
source .venv/bin/activate &&
pip install -r requirements.txt
```

Fill the `ini.conf` file.

```ini
[DISCORD]
bot_token= <discord_bot_token>

[PROXMOX]
host= <proxmox_node_ip>
user= <proxmox_user_and_site>
password= <proxmox_user_password>
```

The `timed_tasks.json` file is the important. With the edits you make in this file, the bot will transmit the data to the channels you want.

```json
{
  "minutely": {
    "commands": [],
    "channels": []
  },
  "hourly": {
    "commands": [],
    "channels": []
  },
  "monthly": {
    "commands": [],
    "channels": []
  },
  "yearly": {
    "commands": [],
    "channels": []
  }
}
```

You can find detailed information about the commands here [commands](https://github.com/programmer-666/xbi1/blob/master/commands.md). You need to copy the ID of the channel to which notifications will be sent and paste it into "channels".

![image](https://github.com/programmer-666/xbi1/assets/34501436/98e0f838-b64c-4e69-8392-ad44e6bafb14)

All you have to do is write this code to run the bot.

```
python3 dc_app.py
```

# Logs

A simple logging program is running here that logs the classes or methods called. Logs saved `/tmp` location.

Logs format is:\
`%(asctime)s::%(name)s::%(levelname)s::[%(processName)s::%(process)d]::[%(threadName)s::%(thread)d]::%(message)s`

Every time the application is run, log records are deleted and new logs begin to be written.

You can find the details in the `log.ini` file.
