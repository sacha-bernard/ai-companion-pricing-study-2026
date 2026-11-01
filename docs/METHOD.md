# Method

## Scope

Twenty consumer "AI companion" apps, ten general public and ten adult oriented, selected by visibility. Each app was observed once on 2026-11-01 (UTC) from Belgium, without a VPN, in Google Chrome driven through the Playwright MCP server, cookies accepted, site language left as served. One observer, one session per app.

## Protocol per app

1. Official URL verified from the homepage and its legal links. Mobile-only apps were checked on the App Store and Google Play web listings.
2. Logged-out pass: homepage, pricing page or pricing modal, terms of service, refund policy, FAQ. Every price, plan name, period, currency and renewal sentence was copied from the page text as displayed.
3. Account pass: one free account per app with an address on a private catch-all domain, a neutral female persona (first name, last name, adult date of birth) and a generated password. No Google, Apple, Discord or Microsoft sign-in was used. Verification codes and links were read from the mailbox with a script.
4. Path to the payment screen: the cheapest or default paid plan was selected and the flow was followed until the screen that collects a card or wallet. No card number was entered and no payment, trial or order was ever submitted. The payment screen was read for plan, total, taxes, renewal wording, payment methods, processor domain and billing descriptor.
5. Evidence: a screenshot per criterion, stored privately outside the dataset, plus text dumps of long terms. Screenshots that would show nudity or sexual text were not kept; two captures were deleted for that reason and the deletion is logged.
6. Each cell of the grid was filled with the observed value. When a screen could not be reached, the cell says "not observable" followed by the reason.

## Replacement rule

An app was replaced by the next app of the reserve list when the payment screen was unreachable under the rules above. Replacements and the reasons are listed in `apps.md` and `RAPPORT.md`. The reserve list was exhausted during the run; after that, apps whose checkout stayed unreachable were kept as rows with the reason written in each affected cell, so that the dataset keeps 20 rows and every cell has a value.

## Derived values

- Monthly equivalent of an annual or multi-month plan: total divided by the number of months; of a weekly plan: price multiplied by 52 and divided by 12.
- Annual discount: 100 x (1 - annual total / (12 x monthly price)) on the same tier, computed from displayed prices. When a site shows only a promotional monthly figure for the annual plan, the regular monthly price is used and the notes say which tier was used.
- All derived values were recomputed by `work/check_dataset.py`, which also verifies the row count, the absence of empty cells, the enumerated values and the date format. `work/findings.py` computes every number in `findings.md` from the CSV.

## Limits

- Single day, single country, single browser. Prices, promotions and checkout wording change often; localized prices and taxes differ by country.
- Several sites detect automation. One registration API rejected the catch-all email domain, one Cloudflare Turnstile check failed in the automated browser, and three sites sent verification emails that either never arrived or arrived after their 10-minute validity. These cases are documented and their checkout cells are marked not observable.
- App-store prices for mobile-only apps could not be read because the store web listings no longer show in-app purchase prices; those apps were replaced.
- The observer did not pay, so post-payment screens (receipts, cancellation flows, renewal notices) are outside the dataset; cancellation paths come from terms, FAQ and settings pages.
- Operator identity is taken from the published legal pages and checkout mandates; it was not verified in company registers.
