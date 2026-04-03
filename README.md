# ACEest Fitness – Assignment‑1 (v1.1.2)

## Description
Web‑based Flask implementation of Aceestver‑1.1.2 with CI/CD automation.

## Run Locally
```bash
pip install -r requirements.txt
python run.py
```

## Testing
```bash
pytest
```

## Docker
```bash
docker build -t aceest-fitness:1.1.2 .
docker run -p 5000:5000 aceest-fitness:1.1.2
```

## CI/CD
- GitHub Actions: automated test + build
- Jenkins: venv → pytest → docker build
