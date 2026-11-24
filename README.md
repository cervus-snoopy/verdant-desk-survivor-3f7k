# The Houseplant Out-of-Office

[![Bounty](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/cervus-snoopy/verdant-desk-survivor-3f7k/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/cervus-snoopy/verdant-desk-survivor-3f7k/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

A one-line out-of-office auto-reply written in the voice of the office's longest-serving resident, a snake plant that thrives on neglect and keeps outlasting everyone who manages it.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Writes `entry.txt` into the output directory (default `/output`).

## Verify

The program validates the line itself before writing (1–120 characters, not only whitespace, a single line), writes it as UTF-8 with no trailing newline and mode `0644`, then reads the file back and checks it matches byte for byte.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/houseplant-check python3 main.py
wc -m /tmp/houseplant-check/entry.txt
python3 -c "print(len(open('/tmp/houseplant-check/entry.txt', encoding='utf-8').read()))"
```

## License

MIT — see [LICENSE](LICENSE).
