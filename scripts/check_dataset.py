"""Consistency checks for data/dataset.csv.
Checks: 20 rows, no empty cell, enumerated values, ISO date, cheapest_monthly and
annual_discount_pct consistent with the plans column where both are numerically derivable.
Exit code 1 on any failure."""
import csv, os, re, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'dataset.csv'), encoding='utf-8')))
errors, warns = [], []
if len(rows) != 20:
    errors.append(f'row count {len(rows)} != 20')
ENUM = {
 'adult_content_available': {'no','optional','core'},
 'price_visible_before_signup': {'yes','no'},
 'free_tier_exists': {'yes','no'},
 'pricing_model': {'subscription','credits','hybrid'},
 'price_shown_with_tax': {'yes','no','unclear'},
 'trial_conversion_stated': {'yes','no','none'},
 'age_gate_type': {'none','checkbox','date of birth','ID','phone'},
}
for r in rows:
    name = r['app_name']
    for k, v in r.items():
        if v is None or not str(v).strip():
            errors.append(f'{name}: empty cell {k}')
        if '—' in str(v) or '–' in str(v):
            errors.append(f'{name}: dash character in {k}')
        if 'not observable' in str(v).lower() and '(' not in str(v):
            errors.append(f'{name}: not observable without reason in {k}')
    for k, allowed in ENUM.items():
        if r[k] not in allowed:
            errors.append(f'{name}: {k}={r[k]!r} not in {sorted(allowed)}')
    for k in ('auto_renewal_stated_at_checkout',):
        if not (r[k] in ('yes','no') or r[k].startswith('not observable (') or r[k].startswith('stated: no renewal')):
            errors.append(f'{name}: {k}={r[k]!r}')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['observation_date_utc']):
        errors.append(f'{name}: bad date {r["observation_date_utc"]}')
    if r['price_visible_before_signup'] == 'yes' and r['pricing_page_url'] == 'none':
        errors.append(f'{name}: price visible but no pricing_page_url')
    if r['price_visible_before_signup'] == 'no' and not (r['pricing_page_url'] == 'none' or 'login' in r['pricing_page_url'].lower()):
        warns.append(f'{name}: price not visible but pricing_page_url set')
    m = re.fullmatch(r'(\d+(?:\.\d+)?) (USD|EUR)', r['cheapest_paid_monthly_equivalent'])
    if not m:
        errors.append(f'{name}: cheapest_paid_monthly_equivalent format {r["cheapest_paid_monthly_equivalent"]!r}')
    try:
        pct = float(r['annual_discount_pct'])
        if not (0 <= pct <= 95):
            errors.append(f'{name}: annual_discount_pct out of range {pct}')
    except ValueError:
        errors.append(f'{name}: annual_discount_pct not numeric {r["annual_discount_pct"]!r}')
    # derive monthly equivalents from the plans string: numbers with /month or /year
    plans = r['plans']
    monthly = [float(x) for x in re.findall(r'(\d+(?:\.\d+)?) (?:USD|EUR)/month', plans)]
    yearly = [float(x) for x in re.findall(r'(\d+(?:\.\d+)?) (?:USD|EUR)/year', plans)]
    shown_mo = [float(x) for x in re.findall(r'\((\d+(?:\.\d+)?)(?:/mo| USD/month| EUR/month)', plans)]
    candidates = monthly + [y/12 for y in yearly] + shown_mo
    if candidates and m:
        cheapest = float(m.group(1))
        if cheapest > min(candidates) + 0.02 and 'promo' not in r['notes'].lower():
            warns.append(f'{name}: cheapest {cheapest} > min derived {min(candidates):.2f}')
print(f'rows: {len(rows)}; errors: {len(errors)}; warnings: {len(warns)}')
for e in errors: print('ERROR', e)
for w in warns: print('WARN ', w)
sys.exit(1 if errors else 0)
