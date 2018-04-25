"""
Screen saver module for Linux
"""


import subprocess


def idle_check():
    """Check how long the machine has been idle for. """
    pass


def running_programs():
    """Return a list of the running programs,
       False if there is none.
    """
    # Call pacmd and parse the output, looking for programs, playing sound.
    output = subprocess.check_output(["pacmd", "list-sink-inputs"])
    if output.startswith(b"0"):
        return False
    else:
        running_apps = []
        found = False
        for line in output.decode().splitlines():
            if not found:
                if "state: RUNNING" in line:
                    found = True
            else:
                if "application.name" in line:
                    running_apps.append(line.split()[-1])
                    found = False
        if not running_apps:
            return False
        else:
            return running_apps


def log():
    """Write logs."""
    pass


def run():
    """Run program."""
    pass
