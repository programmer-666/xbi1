![xbi1_banner](https://github.com/programmer-666/xbi1/assets/34501436/56fe6b34-4f68-4178-99cb-4d37cca1ca6d)

[![Flake8 Linting](https://github.com/programmer-666/xbi1/actions/workflows/flake8py.yml/badge.svg)](https://github.com/programmer-666/xbi1/actions/workflows/flake8py.yml)
[![CodeQL](https://github.com/programmer-666/xbi1/actions/workflows/codeql.yml/badge.svg)](https://github.com/programmer-666/xbi1/actions/workflows/codeql.yml)

# XBI1 - A Proxmox Notification Bot 🤖
xBi_1 is a discord bot that allows you to quickly access various information about your Proxmox Nodes and get reports. It's personal, private and basic.

## About Discord Bot
Firstly you need a private discord bot. If you want to share your server information with everyone, you will not need to turn off this option.
 
<img width="1102" alt="dc_appliaction_setting" src="https://github.com/programmer-666/xbi1/assets/34501436/86df32af-86dc-4ee6-ac8b-d3bc4774d219">

## Installation
Clone this repo, create a virtual environment or directly install modules needed.

```
git clone https://github.com/programmer-666/xbi1.git
pip install -r requirements.txt
```
Fill the `ini.conf` file.
```
[DISCORD]
bot_token= <discord_bot_token>

[PROXMOX]
host= <proxmox_node_ip>
user= <proxmox_user_and_site>
password= <proxmox_user_password>
```
