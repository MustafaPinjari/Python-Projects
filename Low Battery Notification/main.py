import psutil
from plyer import notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 80 and plugged != True:
    notification.notify(
        title="Battery Low",
        message=str(percent) + "% Battery Remain!!",
        timeout=5
    )
