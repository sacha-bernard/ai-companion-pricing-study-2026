# Findings: pricing and subscription transparency of 20 AI companion apps (observed 2026-11-01)

All figures below are computed by `scripts/findings.py` from `data/dataset.csv`. Prices are as displayed, in the currency the site showed from Belgium without a VPN. Monthly equivalents divide annual totals by 12.

## Aggregate statistics

| Indicator | Value |
|---|---|
| Apps whose prices are not visible before creating an account | 8 of 20 (40%) |
| Apps using a hybrid model (subscription plus credits or tokens) | 17 of 20 (85%) |
| Apps using a pure subscription model | 3 of 20 (15%) |
| Apps with a free tier | 20 of 20 (100%) |
| Apps offering a free trial of a paid plan | 2 of 20 (10%) |
| Median cheapest paid plan, monthly equivalent, all currencies pooled | 5.83 (USD rows median 5.83 USD, EUR rows median 6.62 EUR) |
| Range of cheapest monthly equivalent | 3.33 to 14.92 |
| Median annual discount versus monthly billing | 52.1% (range 16.0% to 77.6%) |
| Automatic renewal stated on the checkout screen | yes 9 of 20 (45%); no 4 of 20 (20%); checkout states no renewal 1 of 20 (5%); not observable 6 of 20 (30%) |
| Automatic renewal stated on checkout among the 14 observable checkouts | 9 of 14 (64%) |
| Age gate: simple checkbox or button | 12 of 20 (60%) |
| Age gate: date of birth or age bracket | 4 of 20 (20%) |
| Age gate: none (text statement only) | 4 of 20 (20%) |
| Tax treatment unclear on price pages | 16 of 20 (80%) |
| Prices explicitly shown before tax | 4 of 20 (20%) |
| Cancellation possible through an in-app control | 18 of 20 (90%) |
| Cancellation only by email or through the biller | 1 of 20 (5%) |
| Terms state a non-refundable or final-sale rule | 15 of 20 (75%) |
| Terms mention a 14-day EU withdrawal right | 6 of 20 (30%) |
| Payment processor identifiable at checkout | 11 of 20 (55%) |
| Payment processor not observable (checkout unreachable) | 6 of 20 (30%) |
| Crypto accepted at checkout | 6 of 20 (30%) |
| Weekly billing offered | 4 of 20 (20%) |
| Lifetime or one-time plans offered | 1 of 20 (5%) |
| Adult content is the core offer | 13 of 20 (65%) |
| Prices displayed in USD | 16 of 20 (80%); in EUR 4 of 20 (20%) |

## Operator countries (as stated on legal pages)

- United States: 8
- Cyprus: 4
- Romania: 2
- Malta: 1
- not stated: 1
- not stated on observed pages: 1
- Finland: 1
- Canada: 1
- Singapore: 1

## Cheapest paid plan per app (monthly equivalent, as displayed)

| App | Cheapest monthly equivalent | Annual discount |
|---|---|---|
| Anima | 3.33 USD | 66.6% |
| DreamGF | 3.69 USD | 71.6% |
| Candy.ai | 3.99 EUR | 71.5% |
| Joi | 4.00 USD | 71.4% |
| CrushOn | 4.90 USD | 18.1% |
| Character.AI | 4.99 USD | 20.8% |
| Nectar AI | 4.99 USD | 50.0% |
| SpicyChat | 5.00 EUR | 16.0% |
| FantasyGF | 5.83 USD | 77.6% |
| Muah.ai | 5.83 USD | 70.8% |
| Replika | 5.83 USD | 70.8% |
| Romantic AI | 5.83 USD | 76.7% |
| Luvr | 5.99 USD | 33.4% |
| Talkie | 8.00 USD | 19.9% |
| PolyBuzz | 8.25 EUR | 16.7% |
| Janitor AI | 8.25 USD | 36.5% |
| Secrets.ai | 9.17 USD | 54.2% |
| OurDream | 9.99 USD | 50.0% |
| Kindroid | 11.67 USD | 16.6% |
| Kupid AI | 14.92 EUR | 73.5% |

## Factual observations

1. 8 of the 20 apps show no price until an account exists: Anima, FantasyGF, Joi, Kindroid, Muah.ai, Nectar AI, Replika, Romantic AI.
2. 17 apps combine a subscription with a credit or token currency; only 3 sell a plain subscription and none sell credits alone.
3. Across the 20 apps the cheapest paid plan ranges from 3.33 to 14.92 per month in displayed currency, with a pooled median of 5.83.
4. The median annual discount is 52.1% and 12 apps advertise 50% or more off for annual billing; the extremes are 16.0% and 77.6%.
5. Of the 14 checkouts that could be reached, 9 state automatic renewal on the payment screen, 4 do not (DreamGF, Luvr, Nectar AI, Replika) and 1 states that the purchase does not renew (Kupid AI).
6. 12 apps gate age with a checkbox or button, 4 ask for a date of birth or age bracket, and 4 rely on a sentence next to the sign-up button; Talkie offers brackets below 18 and Character.AI states a minimum age of 13.
7. Only 4 apps state whether displayed prices include tax; Character.AI and Janitor AI added 21% Belgian VAT at the Stripe checkout and Joi added 10.08 USD of taxes to a 47.99 USD plan.
8. 15 apps state in their terms that payments are non-refundable or final, while 6 mention a 14-day withdrawal right for EU consumers; Romantic AI states that the EU right does not apply and Luvr advertises a 30-day money-back guarantee in its FAQ only.
9. 6 apps accept cryptocurrency and Kupid AI accepted only crypto or Alipay on the observation day because card payments were suspended; 4 apps sell weekly plans and 1 sell lifetime or one-time access.
10. Card checkouts were unreachable for 6 apps because registration was rejected, blocked by a bot check, or the verification email arrived after the link expired; their rows keep the public pricing and terms with the reason recorded in each cell.
