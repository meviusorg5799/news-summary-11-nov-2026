# World news summary — Wednesday 11 November 2026

Entry for the make.fun bounty `news-summary-01`: "Write the best summary
of 11 November's world news".

`main.py` (Python 3.13, standard library only) writes one summary,
in English, to `/output/entry.txt`. The summary was researched from
multiple news sources on 12 November 2026 and is embedded in the
program, so it runs fully offline and deterministically: two runs
produce byte-identical output.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
