# Simple Counter

A minimal CLI counter utility that persists your count between sessions.

## Usage

```bash
# Show current count
python counter.py

# Increase count
python counter.py up
python counter.py up -n 5

# Decrease count
python counter.py down
python counter.py down -n 3

# Reset to zero
python counter.py reset
```

## Data Storage

Counts are stored in `~/.counter.json` in your home directory.

## License

MIT
