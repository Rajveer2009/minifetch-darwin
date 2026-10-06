# minifetch-darwin

A tiny, fast system fetch script for macOS, written in Python with no dependencies.

A macOS port of [RohanKP1/minifetch](https://github.com/RohanKP1/minifetch), which is Arch Linux only.

## What it shows

OS version, kernel, Homebrew package count, memory usage and uptime, next to a small logo.

## Installation

```shell
git clone https://github.com/Rajveer2009/minifetch-darwin.git
cd minifetch-darwin
mkdir -p ~/.local/bin && cp minifetch ~/.local/bin/
```

Make sure `~/.local/bin` is on your `PATH`. In fish:

```fish
fish_add_path ~/.local/bin
```

Then run `minifetch`.

## Requirements

- macOS
- Python 3 (the one bundled with the Xcode command line tools works)
- Homebrew (optional, used for the package count)

## License

MIT. See [LICENSE](LICENSE).
