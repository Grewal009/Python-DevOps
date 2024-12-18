# WAP to update a MAX_CONNECTIONS in server.conf file when 200 connections are met and update to 500

def update_server_config(file_path, key, value):
    with open(file_path,"r") as file:
        lines = file.readlines()
    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key+"="+value+"\n")
            else:
                file.write(line)


update_server_config("server.conf", "MAX_CONNECTIONS", "500")