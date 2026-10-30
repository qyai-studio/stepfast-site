"""Single place to edit facts that appear across the site.
Anything marked VERIFY must be checked against the current app build before publishing."""

SITE_URL = "https://stepfast.app"          # VERIFY: final production domain (no trailing slash)
SITE_NAME = "StepFast"
PUBLISHER = "QYAI Tech Limited"
APP_ID = "6818072132"
APP_STORE_URL = f"https://apps.apple.com/us/app/stepfast-walk-fasting-timer/id{APP_ID}"
GA_MEASUREMENT_ID = "G-LWVPFNRKPV"            # StepFast.app GA4 web stream
PROVIDER_TOKEN = ""                         # optional: App Store Connect provider token (pt=) for campaign analytics
LEGAL_PRIVACY = "https://legal.qyaitech.com/privacy/"
LEGAL_TERMS = "https://legal.qyaitech.com/terms/"
CONTACT_EMAIL = ""                          # VERIFY: real support address; footer shows it only when set
PUBLISHED = "2026-10-26"                    # Original publication date for existing articles
UPDATED = "2026-10-30"                      # ISO date used for lastmod / dateModified
REVIEWER = None                             # e.g. "Reviewed by Jane Doe, RD" ONLY when a real reviewer signed off

# --- StepFast rules quoted on the site. VERIFY against the current app build. ---
DEFAULT_GOAL = 5000                         # "starting estimate" shown in the app
WALK_STEPS_PER_MIN = 100                    # step gap -> walking minutes
LATER_BREAKFAST_MIN_PER_1000 = 45           # step gap -> minutes later first meal, per 1,000 steps
FAST_CAP_HOURS = 18                         # total fasting hours StepFast will not exceed in a day
MIN_AGE = 18
MIN_IOS = "17"

def app_link(slug: str) -> str:
    """App Store link tagged with the page slug so downloads can be attributed per page."""
    ct = slug.strip("/").replace("/", "-") or "home"
    pt = f"pt={PROVIDER_TOKEN}&" if PROVIDER_TOKEN else ""
    return f"{APP_STORE_URL}?{pt}ct={ct}"

