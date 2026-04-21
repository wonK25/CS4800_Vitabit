# Vitabit

## Local setup
1. Copy `.env.example` to `.env`.
2. Set `MONGODB_URI` in `.env`.
3. Set `FLASK_SECRET_KEY` for session-based login.
4. Optional for AI features: set `OPENAI_API_KEY`.
5. Optional for welcome emails: set `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, and `SMTP_FROM_EMAIL`.
6. Optional for Google Analytics 4: set `GA_MEASUREMENT_ID` (example: `G-XXXXXXXXXX`).
7. Install dependencies: `pip install -r requirements.txt`
8. Seed the supplement catalog: `python mongo-test.py`
9. Run app: `python vitabit_main.py`

## Vercel Web Analytics
If you enable Web Analytics in the Vercel dashboard, Vitabit automatically loads the Vercel analytics script on Vercel deployments. This provides visitor and page view tracking without additional environment variables.

## Included MVP features
- Supplement catalog search across vitamins, minerals, multivitamins, probiotics, fish oil, and store-style supplement formulas
- Browser-based daily supplement reminder planner
- Session-based sign up / log in with household profiles (up to 4)
- One-page onboarding after sign up with sex, age, height, and weight fields plus skip support
- Profile-aware supplement and medication tracking
- DB-backed daily completion state for tracked routines
- Profile-specific recent meal analysis history
- Optional Google Analytics 4 page and interaction tracking for coursework demos
- Optional Vercel Web Analytics page-view tracking on Vercel deployments
- AI coach chat endpoint at `/assistant/chat`
- Meal photo analysis endpoint at `/assistant/analyze-meal`

## Vercel deployment
This repo includes `app.py` and `vercel.json` so Vercel can deploy the Flask app directly.

1. Push this repo to GitHub.
2. Import the repo into Vercel.
3. Set these environment variables in the Vercel project:
   - `MONGODB_URI`
   - `FLASK_SECRET_KEY`
   - `OPENAI_API_KEY`
   - `OPENAI_CHAT_MODEL` (optional)
   - `OPENAI_VISION_MODEL` (optional)
   - `GA_MEASUREMENT_ID` (optional)
   - `SMTP_HOST` (optional)
   - `SMTP_PORT` (optional)
   - `SMTP_USERNAME` (optional)
   - `SMTP_PASSWORD` (optional)
   - `SMTP_FROM_EMAIL` (optional)
4. Deploy.

## Notes
- `mongo-test.py` should be run against your MongoDB instance before production use so the supplement catalog exists.
- Vitabit estimates wellness coverage from meal photos, tracked items, and official intake references such as NIH Office of Dietary Supplements guidance.
