---
title: "NameAura"
description: "AI-powered brand and domain name generator"
date: 2025-11-06
link: "https://github.com/fl-sean03/nameaura"
---

Naming things is one of the two hard problems in computer science and also in startups. Every founder spends a weekend with a thesaurus and a domain lookup tool, comes up with something like "Zendrix" or "Flowlet," registers it, and moves on. The process is slow and the output is usually worse than asking a language model.

**The thesis:** A good naming tool is a language model that understands positioning, checks domain availability in real time, and generates names that sound like real companies.

**What was built:** Working app with a gradient title, a business-concept textarea, filters for TLDs and name style, and a shortlist drawer. Calls Claude Sonnet to produce name candidates with rationales, then runs a DNS check for availability on each selected TLD. Source at [github.com/fl-sean03/nameaura](https://github.com/fl-sean03/nameaura).

**Note:** The original app was deployed at nameaura.co and deleted in a Vercel cleanup. The version above is a rebuild from a screenshot, published as open source.

**Why it's parked:** The category is crowded (Namelix, Shopify name generator, Namecheap beast mode) and the product is a feature. Fine utility, small moat. Fork it if you want to use or extend it.
