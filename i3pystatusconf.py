from i3pystatus import Status
from i3pystatus.weather import wunderground

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
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

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
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

# This would look like this:
# Discharging 6h:51m
#status.register("battery",
#    format="{status} {remaining:%E%hh:%Mm}",
#    alert=True,
#    alert_percentage=5,
#    status={
#        "DIS":  "Discharging",
#        "CHR":  "Charging",
#        "FULL": "Bat full",
#    },
#    )

# Displays whether a DHCP client is running
#status.register("runwatch",
#    name="DHCP",
#    path="/var/run/dhclient*.pid",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
#status.register("network",
#    interface="eth0",
#    format_up="{v4cidr}",)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlp3s0",
    format_up="{essid} {quality}",
    on_leftclick="/usr/bin/networkmanager_dmenu",
#    on_leftclick="ip addr show dev {interface} | xmessage -file -",
    color_up = "#9edc60",
    color_down = "#f81141",
    ) 

# Shows disk usage of /
# Format:
# 42/128G [86G]
#status.register("disk",
#    path="/",
#    format="{used}/{total}G [{avail}G]",)

status.register(
    "pulseaudio",
    color_unmuted = "#9edc60",
    color_muted = "#f81141",
    format_muted="",
    format="{volume_bar}",
    vertical_bar_width=1,
    vertical_bar_glyphs=["  ", " ", ""],
)


# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },)

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
