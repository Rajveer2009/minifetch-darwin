import os
import sys
import time

R = "\033[0m"
MAC = sys.platform == "darwin"
if MAC:
    from ctypes import CDLL, byref, c_size_t, c_uint32, c_uint64, create_string_buffer
    L = CDLL(None)

    def sysctl(name, size=16):
        b, n = create_string_buffer(size), c_size_t(size)
        L.sysctlbyname(name.encode(), b, byref(n), None, 0)
        return b.raw[: n.value]

    def num(name):
        return int.from_bytes(sysctl(name)[:8], "little")

    def info():
        v = (c_uint32 * 38)()
        L.host_statistics64(L.mach_host_self(), 4, v, byref(c_uint32(38)))
        used = (v[1] + v[3] + v[32]) * num("hw.pagesize")
        cask = "/opt/homebrew/Caskroom"
        pk = len(os.listdir("/opt/homebrew/Cellar")) + (len(os.listdir(cask)) if os.path.isdir(cask) else 0)
        return (
            "macOS " + sysctl("kern.osproductversion", 32).rstrip(b"\0").decode(),
            pk,
            used,
            num("hw.memsize"),
            int(time.time()) - num("kern.boottime"),
        )

    LOGO = (
        ("92", "        .:'"),
        ("92", "    __ :'__"),
        ("93", " .'`__`-'__``."),
        ("38;5;208", ":__________.-'"),
        ("91", ":_________:"),
        ("95", " :_________`-;"),
        ("94", "  `.__.-.__.'"),
    )
else:
    def info():
        m = {k: int(v.split()[0]) * 1024 for k, v in (l.split(":") for l in open("/proc/meminfo"))}
        name = next((l.split("=", 1)[1].strip('"\n') for l in open("/etc/os-release") if l.startswith("PRETTY_NAME=")), "Linux")
        try:
            pk = len(os.listdir("/var/lib/pacman/local")) - 1
        except OSError:
            try:
                pk = sum(l == "Status: install ok installed\n" for l in open("/var/lib/dpkg/status"))
            except OSError:
                pk = 0
        return name, pk, m["MemTotal"] - m["MemAvailable"], m["MemTotal"], int(float(open("/proc/uptime").read().split()[0]))

    LOGO = (
        ("97", "    .--."),
        ("97", "   |o_o |"),
        ("93", "   |:_/ |"),
        ("97", "  //   \\ \\"),
        ("97", " (|     | )"),
        ("93", "/'\\_   _/`\\"),
        ("93", "\\___)=(___/"),
    )


def main():
    name, pk, used, total, up = info()
    d, h, m = up // 86400, up % 86400 // 3600, up % 3600 // 60
    rows = (
        "╭────────────",
        f"│ {{}}OS{R}› {name}",
        f"│ {{}}Kernel{R}› {os.uname().release}",
        f"│ {{}}Packages{R}› {pk}",
        f"│ {{}}Memory{R}› {used / 2**30:.1f}G/{total / 2**30:.1f}G",
        f"│ {{}}Uptime{R}› {f'{d}d ' * (d > 0)}{f'{h}h ' * (h > 0)}{m}m",
        "╰────────────",
    )
    print()
    for (c, art), row in zip(LOGO, rows):
        c = f"\033[{c}m"
        i = 1 if row[0] == "│" else len(row)
        print(f"{c}{art:<17}{row[:i]}{R}{row[i:].format(c)}")
    print()


if __name__ == "__main__":
    main()
