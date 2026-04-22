import platform
import subprocess
import sys

GATEWAYS = {
    "TRUSTED": "10.10.10.1",
    "IOT": "10.10.20.1",
    "GUEST": "10.10.30.1",
}


def ping(host):
    count_flag = "-n" if platform.system() == "Windows" else "-c"
    result = subprocess.run(
        ["ping", count_flag, "2", host],
        capture_output=True,
        timeout=10,
    )
    return result.returncode == 0


def main():
    failed = []
    for name, ip in GATEWAYS.items():
        ok = ping(ip)
        status = "OK" if ok else "FAIL"
        print(f"{name:8} {ip:14} {status}")
        if not ok:
            failed.append(name)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
