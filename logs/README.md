# Logs
A simple logging program is running here that logs the classes or methods called.

Logs format is:\
`%(asctime)s::%(name)s::%(levelname)s::[%(processName)s::%(process)d]::[%(threadName)s::%(thread)d]::%(message)s`

Every time the application is run, log records are deleted and new logs begin to be written.

You can find the details in the `log.ini` file.