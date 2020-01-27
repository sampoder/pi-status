import os
import re
import sys
import tkinter as tk

import psutil
from flask import Flask
from flask import render_template


def main():

    if len(sys.argv) == 1:

        hostname = re.sub("\n", "", os.popen("hostname").read())

        ip = re.sub(
            "\n", "",
            os.popen("ip addr show wlan0 | grep -Po 'inet \K[\d.]+'").read())

        memory = psutil.virtual_memory()

        cpuusage = psutil.cpu_percent(interval=1)

        cputemp = re.sub(
            "temp=", "",
            re.sub("\n", "",
                   os.popen("vcgencmd measure_temp").read()))

        disk = psutil.disk_usage("/")

        print("\n" + "Hostname: " + hostname)

        print("IP Address: " + ip + "\n")

        print("Physical Memory: " + str(round(memory.total / 1000000)) + " MB")

        print("Available Memory: " + str(round(memory.available / 1000000)) +
              " MB\n")

        print("CPU Usage: " + str(cpuusage) + "%")

        print("CPU Temperature: " + cputemp + "\n")

        print("Disk Total Storage: " + str(round(disk.total / 1000000000, 2)) +
              " GB")

        print("Disk Available Storage: " +
              str(round(disk.free / 1000000000, 2)) + " GB \n" + "\n")

        print(
            "No Command Line Arguments Specified. Use -g to launch GUI app. Use -w to launch Web Server"
        )

    elif sys.argv[1] == "-g":

        # Create the main window
        root = tk.Tk()
        root.title("Pi Status")
        root.geometry("250x300+50+90")

        # Create label
        label = tk.Label(root, text="Loading")
        # Lay out label
        label.pack()

        def setText():

            hostname = re.sub("\n", "", os.popen("hostname").read())

            ip = re.sub(
                "\n",
                "",
                os.popen(
                    "ip addr show wlan0 | grep -Po 'inet \K[\d.]+'").read(),
            )

            memory = psutil.virtual_memory()

            cpuusage = psutil.cpu_percent(interval=1)

            cputemp = re.sub(
                "temp=", "",
                re.sub("\n", "",
                       os.popen("vcgencmd measure_temp").read()))

            disk = psutil.disk_usage("/")

            label.configure(
                text="\n" + "Hostname: " + hostname + "\n" + "IP Address: " +
                ip + "\n" + "\n" + "Physical Memory: " +
                str(round(memory.total / 1000000)) + " MB" + "\n" +
                "Available Memory: " + str(round(memory.available / 1000000)) +
                " MB" + "\n" + "\n" + "CPU Usage: " + str(cpuusage) + "%" +
                "\n" + "CPU Temperature: " + cputemp + "\n" + "\n" +
                "Disk Total Storage: " +
                str(round(disk.total / 1000000000, 2)) + " GB" + "\n" +
                "Disk Available Storage: " +
                str(round(disk.free / 1000000000, 2)) + " GB \n")

            root.after(10000, setText)

        setText()

        # Run forever!
        root.mainloop()

    elif sys.argv[1] == "-w":

        app = Flask(
            __name__,
            template_folder=os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "templates"),
        )

        @app.route("/")
        @app.route("/index")
        def index():

            hostname = re.sub("\n", "", os.popen("hostname").read())

            ip = re.sub(
                "\n",
                "",
                os.popen(
                    "ip addr show wlan0 | grep -Po 'inet \K[\d.]+'").read(),
            )

            memory = psutil.virtual_memory()

            cpuusage = psutil.cpu_percent(interval=1)

            cputemp = re.sub(
                "temp=", "",
                re.sub("\n", "",
                       os.popen("vcgencmd measure_temp").read()))

            disk = psutil.disk_usage("/")

            return render_template(
                "index.html",
                Title=hostname,
                ip=ip,
                pmemory=str(round(memory.total / 1000000)),
                amemory=str(round(memory.available / 1000000)),
                cpuusage=str(cpuusage),
                cputemp=cputemp,
                tdisk=str(round(disk.total / 1000000000)),
                adisk=str(round(disk.free / 1000000000, 2)),
            )

        ip = re.sub(
            "\n", "",
            os.popen("ip addr show wlan0 | grep -Po 'inet \K[\d.]+'").read())
        app.run(host=ip)
