from i3pystatus import Status
from i3pystatus.weather import wunderground

status = Status()

status.register("clock",
    format="%a %-d %b %H:%M",
    hints = {'markup': 'pango'},
    )

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
#status.register("load")

#Caps lock module
status.register("keyboard_locks",
    format="{caps}",
    caps_off = "",
    color = "#dc5e86",
        )

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

status.register("battery",
    format="[{glyph} ]{percentage_design:.0f}%[{status}]",
    alert=True,
    alert_percentage=10,
    status={
        "DIS": "",
        "CHR": "↑",
        "FULL": "",
        },
    full_color = '#9edc60',
    charging_color = '#9edc60',
    critical_color = '#dc5e86',
    hints = {"markup": "pango"},
    glyphs = [
        "<span color=\"#dc5e86\"></span>",
        "<span color=\"#dc5e86\"></span>",
        "<span color=\"#dcb65e\"></span>",
        "<span color=\"#dcb65e\"></span>",
        "<span color=\"#9edc60\"></span>",
        ],
    )

status.register("network",
    interface="wlp3s0",
    format_up="{essid} {quality}",
    on_leftclick="/usr/bin/networkmanager_dmenu",
#    on_leftclick="ip addr show dev {interface} | xmessage -file -",
    color_up = "#9edc60",
    color_down = "#f81141",
    ) 
status.register(
    "pulseaudio",
    color_unmuted = "#9edc60",
    color_muted = "#f81141",
    format_muted="",
    format="{volume_bar}",
    vertical_bar_width=1,
    vertical_bar_glyphs=["  ", " ", ""],
)

status.register("shell",
    format="{output}",
    hints = {"markup": "pango"},
    command="/home/andromeda/.config/i3pystatus/ice-status.py",
    ignore_empty_stdout=True,
    interval=2)

status.register(
    'weather',
    format='{city}:[ {icon}] {condition} {current_temp}{temp_unit}[ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
    colorize=True,
    hints={'markup': 'pango'},
    backend=wunderground.Wunderground(
        location_code='$localweatherstation',
        update_error='<span color="#ff0000">!</span>',
    ),
)

status.run()
