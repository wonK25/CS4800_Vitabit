# Vitabit

## Local setup
1. Copy `.env.example` to `.env`.
2. Set `MONGODB_URI` in `.env`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run app: `python vitabit_main.py`

## Deployment secrets
Set these GitHub repository secrets:
- `EC2_HOST`
- `EC2_USER`
- `EC2_SSH_KEY`
- `MONGODB_URI`
