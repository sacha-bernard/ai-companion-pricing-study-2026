# Codebook: Pricing and subscription transparency of AI companion apps (2026)

File: `dataset.csv` (UTF-8, comma separated, 20 rows, 36 columns). One row per app. Every cell is an observation made on 2026-11-01 from Belgium without a VPN, in a Chrome browser driven by Playwright, logged out first and then with a free test account where one could be created. "not observable (reason)" is a valid value: it means the screen could not be reached and gives the reason.

## Identity

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| app_name | Short name of the app | text | as branded on the site |
| official_url | Official website | URL | homepage reached directly |
| operator_name | Legal entity operating the service, with address when published | text | Terms of Service, legal notice, footer, or merchant name shown at checkout; the source is named in the cell |
| operator_country | Country of the operator | text | same sources; where only governing law or a court is named, the cell says so |
| platforms | Where the product is offered | web, ios, android separated by a pipe | links to app stores on the site; web means a usable web app |
| adult_content_available | Whether adult content is offered | no, optional, core | no: prohibited or filtered; optional: available behind a toggle or verification; core: the marketing of the service is adult oriented |
| observation_date_utc | Date of observation | ISO date | system clock, UTC |
| site_language_observed | Language the site served | text | html lang attribute and visible text |
| currency_observed | Currency displayed on pricing or checkout | text | pricing page and checkout; both are given when they differ |
| observer_country_note | Observer location | text | fixed: Belgium, no VPN |

## Transparency before registration

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| price_visible_before_signup | Whether any plan price can be read without an account | yes, no | pricing link or modal opened in a logged-out session |
| pricing_page_url | URL of the public pricing page | URL or none | the page or modal where the prices were read; when a URL redirects to login it is given with that note |
| free_tier_exists | Whether a free plan or free use exists | yes, no | pricing page, FAQ or terms |
| free_tier_limits | Limits of the free tier | short text | comparison table, FAQ or terms; "not quantified" when the site gives no number |
| free_trial | Trial of a paid plan | none, number of days with conditions | pricing or checkout screen |

## Model and plans

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| pricing_model | Monetisation model | subscription, credits, hybrid | hybrid when a subscription coexists with a purchasable currency (tokens, coins, gems, credits, hearts, neurons, moments, dreamcoins, charms) |
| plans | Every plan with its displayed price and period | list separated by a pipe: name: price currency/period | pricing page, modal or checkout; struck list prices and promotional prices are described as displayed |
| cheapest_paid_monthly_equivalent | Lowest monthly equivalent of any paid plan | number and currency | monthly price, or annual or multi-month total divided by the number of months, or the per-month figure displayed by the site; regular displayed prices are used; a promotional first-term price is reported in notes, not in this column |
| most_expensive_plan | Highest single charge plan | text | plans column |
| annual_discount_pct | Discount of annual billing versus twelve monthly payments | number, percent | computed as 100 x (1 - annual total / (12 x monthly price)) on the same tier; the tier used is named in notes when it is not the only one; weekly plans are converted with 52 weeks |
| credits_pack_prices | Prices of credit packs | text | shop or checkout add-on; "not applicable" for pure subscriptions |
| cost_per_message_or_image_in_credits | Credit cost of a message, image, video or minute | text | FAQ, pricing page or in-app popup; "not shown" when the site gives none |
| price_shown_with_tax | Whether prices are stated as including tax | yes, no, unclear | yes or no only when the site says it; unclear when nothing is said; tax lines added at checkout are reported in notes |

## Renewal and cancellation

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| auto_renewal_stated_at_checkout | Whether the payment screen itself states that the subscription renews automatically | yes, no, stated: no renewal, not observable (reason) | text on the screen that collects the payment method; a link to the terms does not count; "stated: no renewal" when the screen itself says that the purchase does not renew (Kupid AI) |
| where_auto_renewal_is_stated | Where automatic renewal is stated | checkout, terms, both, nowhere, not observable (reason) | checkout screen and terms |
| cancellation_path | How a subscriber cancels | in-app button, email, app store, contact form, or combinations | terms, FAQ or settings page; the source is named |
| notice_period | Notice required before renewal | text | terms; "None stated" when the terms only say to cancel before the renewal date |
| refund_policy_stated | Refund rule | short text with source | terms, refund policy or FAQ |
| trial_conversion_stated | Whether the site states that a trial converts to a paid plan | yes, no, none | none when there is no trial |

## Age and identity

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| age_gate_type | Mechanism used at entry or signup | none, checkbox, date of birth, ID, phone | none: a sentence only; checkbox: a box, a button or an interest selector whose click confirms 18+; date of birth: a date or an age bracket; ID or phone: documents or number required to use the service |
| minimum_age_stated | Minimum age in the terms | number or text | terms |

## Payment

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| payment_methods_shown | Payment methods offered at checkout | list | checkout screen; when unreachable the terms or FAQ statement is quoted with the reason |
| payment_processor_visible | Processor or merchant of record visible | name, not visible, not observable (reason) | checkout domain, iframe source, mandate text or API response |

## Evidence

| Column | Definition | Possible values | How observed |
|---|---|---|---|
| source_urls | Pages consulted | URLs separated by a pipe | browser history |
| evidence_files | Private screenshots and dumps kept by the author | file names separated by a pipe | stored outside the dataset |
| notes | Factual remarks, at most 300 characters | text | observation |

## Conventions

- No cell is empty. "not observable (reason)" records why a screen could not be reached. "not shown" records that the site gives no figure. "not applicable" records that the column does not apply to the model.
- Prices are copied as displayed, decimal point, no thousands separator, currency after the number. Prices in the plans column that were displayed with a struck list price are described as such.
- Dates are ISO 8601. Times in the journal are UTC.
- No dash characters other than the hyphen are used.
