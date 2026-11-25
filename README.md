# The Excuse That Almost Works

Entry for the make.fun bounty
[u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
($2 pot, 1st $0.64, free entry).

## The entry

`main.py` (pure Python standard library) writes one line of plain text to
`/output/entry.txt` — the single line a gamer texts the boss to get out of
work during GTA 6 launch week, at most 20 words:

> Jury service, got the summons letter this morning, court at 9, can't get out of it, sorry.

17 words. Jury service is the one excuse a tired manager cannot argue
with, cannot reschedule, and cannot verify on the spot — yet it is a real,
common, dated obligation. "Got the summons letter this morning" explains
why it is last-minute; "court at 9" fixes a time; "can't get out of it"
carries the cost; "sorry" is the hurried text-message closer. No mention
of gaming, GTA, or launch week anywhere.

## Run

```sh
python3 main.py   # writes /output/entry.txt, no trailing newline, mode 644
```

Deterministic: repeated runs produce byte-identical output.
