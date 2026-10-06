# minifetch-darwin

A tiny, fast system fetch for macOS and Linux, written in Python with no dependencies.

A port of [RohanKP1/minifetch](https://github.com/RohanKP1/minifetch), which is Arch Linux only.

- **macOS:** rainbow Apple logo. Values come straight from `sysctl` and the Mach API through `ctypes`, with no subprocesses.
- **Linux:** penguin logo. Values come from `/proc` and `/etc/os-release`.
- Shows OS, kernel, package count, memory and uptime. Runs in about 25 ms.

## Installation

With [uv](https://docs.astral.sh/uv/):

```shell
uv tool install git+https://github.com/Rajveer2009/minifetch-darwin
```

Then run `minifetch`. Update with `uv tool upgrade minifetch`, remove with `uv tool uninstall minifetch`.

## Notes

- Package count on macOS is Homebrew formulae plus casks. On Linux it supports pacman and dpkg, and shows 0 otherwise.
- The Linux path is untested on real hardware.

## License

MIT. See [LICENSE](LICENSE).
