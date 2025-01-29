# log
My custom logging library

# Usage
The setup function is used to setup logging, although it is optional. You just have to provide it with the location to the log file. If you do not configure a log file, a fatal message will appear. To supress this, do `lf_supress = True` and the warning will be gone. to log, use the log() function. Usage:

```
log(mesage, type)
```
Message: Can be anything as the function will convert it to a string before printing.

Type: The type of message. Optinons: None = debug, 0 = info, 1 = success, 2 = warning, 3 = error, 4 = fatal
