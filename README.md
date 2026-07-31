# Stoke Creator Campaign, funnel analysis

A cold outreach campaign that recruited TikTok creators to promote a subscription app on commission only. Recruitment worked. Activation was zero. This repo holds the data and the analysis behind that result.

## The question

Stoke is a subscription app for married men. Paying creators for UGC at market rate would have cost roughly £6,000 for 10 to 20 partnerships. I had £400.

TikTok Shop has already trained a large population of creators to work without guaranteed pay, taking a cut only when something sells. The question was whether that same tolerance would extend to a different performance-only offer: $15 flat per signup, nothing to buy, nothing to ship, no payout hold.

The primary metric was set before the run: creators who publish content. Not replies, not signups.

## The data

Three CSV exports from Instantly.ai, one per email variant, daily granularity across the send window.

| File | Variant | Sent | Replied |
|---|---|---|---|
| `Instantly Analytics - Stoke Campaign 1.csv` | A | 2,334 | 55 |
| `Instantly Analytics - Stoke Campaign 2.csv` | B | 977 | 33 |
| `Instantly Analytics - Stoke Campaign 3.csv` | C | 979 | 14 |

Columns: date, sent, opened, unique opened, replied, link clicks, unique link clicks.

Open and click columns are all zero by design. Tracking pixels and link tracking were disabled to protect deliverability on cold sending domains. That was a deliberate trade, not a gap in the export. Those four columns are dropped in the script.

Lead counts, pre-scale windows and opportunity counts are not in the exports. They are hardcoded as dictionaries in the script and come from the sending platform and from a manual read of the reply inbox.

## The approach

`stoke_funnel_analysis.py` does the following:

1. Loads the three exports and normalises column names, stripping whitespace and replacing spaces with underscores
2. Drops the four zeroed tracking columns
3. Tags each frame with its variant label and concatenates them
4. Aggregates sent and replied by variant
5. Joins in lead counts, pre-scale lead counts, and opportunity counts
6. Derives three rates and writes `stoke_campaign_summary.csv`

Requires pandas. Run from the directory containing the CSVs.

**On the rate definitions.** `Leads_Reply_Rate` is replies divided by reachable leads, not replies divided by emails sent. A lead usually receives more than one email in the sequence, so the two denominators give different numbers for the same-sounding metric. Per lead: 6.88%, 9.88%, 4.20% for A, B and C. Per send: 2.36%, 3.38%, 1.43%. Both appear in write-ups of this campaign, so the denominator is worth checking before comparing.

## What happened

| Stage | Count |
|---|---|
| Emails sent | 4,290 |
| Reachable leads | 1,466 |
| Replies | 102 |
| Real conversations | ~41 |
| Signed up | 5 |
| Posted content | 0 |

Roughly 60% of the 102 replies were canned rate cards. A rate card in response to a commission-only pitch is a polite decline, not a negotiation. Any metric counting those as engagement ranks the variant that attracts the most polite noes, which is why raw reply rate was not used to pick a winner.

Variant A was scaled on day 8 on the basis of the pre-scale window: 10 opportunities against 8 and 4, on roughly 330 leads each. 10 against 8 is not statistically distinguishable at that sample size. That was known at the time, which is why the decision rested on a case by case read of the flagged replies rather than the count alone. It was a judgment call the numbers supported, not a result the numbers proved.

Cost per signup: £80. Cost per activated creator is undefined. The denominator is zero.

## What I would do differently

I built infrastructure to recruit creators and nothing to activate them. No onboarding, no check-in, no reason for anyone to move from signed up to filming. Because of that, weak interest and weak follow-up are indistinguishable in this data.

The list was deliberately unfiltered for creator quality. Screening on top of already low cold email conversion would have left too small a sample to observe posting behaviour at all. I stand by that call. It does mean the 5 signups are not a quality-controlled cohort.

## Open measurement tasks

- Exact intrigued versus rate card count per variant. The metric argument currently rests on a hand read.
- Whether any of the 5 signups stalled at the 48 hour approval gate, or whether all five cleared and still did not post.

## Stack

Sourcing FastMoss, cleaned with NeverBounce. Sending Instantly.ai, 15 mailboxes across 5 domains. Landing page A/B tested, tracked via PostHog. Analysis in Python and pandas. Dashboard in Looker Studio.
