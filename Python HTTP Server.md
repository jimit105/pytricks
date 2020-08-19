# Python HTTP Server

To create a simple Python HTTP Server simply navigate to the desired folder and type the following in command prompt:
`python -m http.server 8000`  
This command will create an HTTP Server hosted on port `8000`.

You can use this server for file sharing purposes.  
To see the contents of the folder, enter the following URL in any web browser:  
`localhost:8000` or `127.0.0.1:8000`

You can use this server to share files between the devices on the LAN.  
First, find the local IP address of the device on which the server is hosted using the command `ipconfig` (For Windows) or `ifconfig` (For Linux).  
Then, enter the URL `<ip-address>:8000` in any web browser of the devices connected to the LAN.

```{tip}
You can host a website using this server by placing the `index.html` file in the root folder.
```
